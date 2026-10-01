"""Manage assignments, subtasks, and work logs; adapted from catalog/form."""
from datetime import date

import models
import storage

TITLE = "จัดการงาน"


def build():
    context = models.overview(storage.load(), models.load_daily_hours())
    context["items"] = context["all_items"]
    context["count"] = len(context["items"])
    context["members"] = models.team_data()["members"]
    context["today"] = date.today().isoformat()
    history, actual_total = models.work_history(context["items"])
    context["history"] = history
    context["actual_total"] = actual_total
    context["daily_history"] = models.daily_history(history)
    return context


def read_hours(text):
    return models.read_number(text)


def check(form, previous=None):
    title = str(form.get("title", "") or "").strip()
    course = str(form.get("course", "") or "").strip()
    due_text = str(form.get("due_date", "") or "")
    due = models.read_date(due_text)
    estimate = read_hours(form.get("estimated_hours", ""))
    done = read_hours(form.get("done_hours", "0"))
    priority = form.get("priority", "normal")
    owner = form.get("owner", "")
    if title == "" or course == "":
        return None, "กรุณากรอกชื่องานและวิชา"
    if len(title) > 80 or len(course) > 40:
        return None, "ชื่องานไม่เกิน 80 และวิชาไม่เกิน 40 ตัวอักษร"
    if due is None:
        return None, "กรุณาเลือกวันส่งที่ถูกต้อง"
    if estimate is None or estimate < 0.1 or estimate > 200:
        return None, "เวลาที่คาดว่าจะใช้ทั้งหมดต้องตั้งแต่ 0.1 ถึง 200 ชั่วโมง"
    if done is None or done < 0 or done > estimate:
        return None, "เวลาที่ทำแล้วต้องตั้งแต่ 0 ถึงเวลาทั้งหมด"
    if priority not in models.PRIORITIES:
        return None, "กรุณาเลือกระดับความสำคัญที่มีในรายการ"
    valid_owner = owner == ""
    for member in models.team_data()["members"]:
        if member["id"] == owner:
            valid_owner = True
    if not valid_owner:
        return None, "ไม่พบสมาชิกที่รับผิดชอบ"
    same_past_date = previous is not None and previous["due_date"] == due_text
    if due < date.today() and not same_past_date and form.get("acknowledge_past") != "yes":
        return None, "วันส่งผ่านไปแล้ว หากต้องการติดตามงานค้าง ให้ยืนยันบันทึกงานเกินกำหนด"
    details = {"owner": owner, "started": done > 0, "subtasks": [],
               "history": [], "created_on": date.today().isoformat(),
               "progress_on": ""}
    if previous is not None:
        details = models.details_of(previous)
        details["owner"] = owner
    else:
        lines = str(form.get("subtasks", "") or "").splitlines()
        for line in lines:
            name = line.strip()
            if name:
                if len(name) > 100 or len(details["subtasks"]) >= 30:
                    return None, "งานย่อยไม่เกิน 30 รายการ ชื่อแต่ละรายการไม่เกิน 100 ตัวอักษร"
                details["subtasks"].append({"title": name, "done": False})
    return {"title": title, "course": course, "due_date": due_text,
            "estimated_hours": round(estimate, 2), "done_hours": round(done, 2),
            "priority": priority, "details": details}, ""


def save_assignment(form, rows, index=None):
    previous = None
    if index is not None:
        previous = rows[index]
    task, error = check(form, previous)
    if error:
        return "✗ " + error
    old_done = 0
    if previous is not None:
        old_done = previous["done_hours"]
    delta = task["done_hours"] - old_done
    if abs(delta) > 0.000000001:
        models.record_history(task, delta, "adjustment", date.today().isoformat(),
                              "ปรับยอดชั่วโมงที่ทำแล้ว ไม่ใช่รายการบันทึกเวลารายวัน")
    if task["done_hours"] < task["estimated_hours"]:
        task["details"].pop("completed_on", None)
        task["details"].pop("before_complete", None)
        task["details"].pop("subtasks_before_complete", None)
    if index is None:
        rows.append(task)
        message = "✓ เพิ่มงานแล้ว"
    else:
        rows[index] = task
        message = "✓ บันทึกการแก้ไขแล้ว"
    storage.save(rows)
    if task["due_date"] < date.today().isoformat():
        message = message + " · งานนี้เกินกำหนด ควรตรวจแผนและติดต่อผู้สอน"
    return message


def log_time(form, row):
    hours = read_hours(form.get("hours", ""))
    on_date = models.read_date(form.get("work_date", ""))
    note = str(form.get("note", "") or "").strip()
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
    if hours is None or hours < 0.1 or hours > remaining:
        return "✗ ชั่วโมงที่บันทึกต้องตั้งแต่ 0.1 และไม่เกินชั่วโมงที่เหลือ"
    if on_date is None or on_date > date.today():
        return "✗ วันที่ทำงานต้องเป็นวันที่ถูกต้องและไม่ใช่อนาคต"
    if len(note) > 120:
        return "✗ หมายเหตุไม่เกิน 120 ตัวอักษร"
    row["done_hours"] = round(row["done_hours"] + hours, 2)
    models.record_history(row, hours, "work", on_date.isoformat(), note)
    return "✓ บันทึกเวลาทำงานจริงแล้ว"


def change_subtask(form, row):
    details = models.details_of(row)
    if row["done_hours"] >= row["estimated_hours"]:
        return "✗ เปิดงานกลับมาทำต่อก่อนแก้ไขงานย่อย"
    if form.get("action", "") == "add_subtask":
        name = str(form.get("subtask_title", "") or "").strip()
        if name == "" or len(name) > 100:
            return "✗ ชื่องานย่อยต้องมี 1 ถึง 100 ตัวอักษร"
        if len(details["subtasks"]) >= 30:
            return "✗ งานย่อยเต็ม 30 รายการแล้ว"
        details["subtasks"].append({"title": name, "done": False})
        message = "✓ เพิ่มงานย่อยแล้ว"
    else:
        text = str(form.get("subtask_no", ""))
        if not text.isascii() or not text.isdigit() or len(text) > 3:
            return "✗ ไม่พบงานย่อยนี้"
        index = int(text)
        if index >= len(details["subtasks"]):
            return "✗ ไม่พบงานย่อยนี้"
        details["subtasks"][index]["done"] = not details["subtasks"][index]["done"]
        details["started"] = True
        details["progress_on"] = date.today().isoformat()
        message = "✓ อัปเดตงานย่อยแล้ว · บันทึกชั่วโมงแยกเพื่อปรับความคืบหน้า"
    row["details"] = details
    return message


def handle(form):
    action = form.get("action", "")
    if action in ("start", "complete", "reopen"):
        return models.quick_action(form)
    if action not in ("add", "update", "delete", "log_time", "add_subtask", "toggle_subtask"):
        return "✗ ไม่รู้จักคำสั่ง"
    rows = storage.load()
    if action == "add":
        return save_assignment(form, rows)
    index = models.row_index(form, rows)
    if index is None:
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
    if action == "update":
        return save_assignment(form, rows, index)
    if action == "delete":
        rows.pop(index)
        storage.save(rows)
        return "✓ ลบงานและประวัติของงานนี้แล้ว"
    if action == "log_time":
        message = log_time(form, rows[index])
    else:
        message = change_subtask(form, rows[index])
    if message.startswith("✓"):
        storage.save(rows)
    return message
