"""Assignment, shared calculations, and form actions for Deadline Compass."""
from datetime import date
import hashlib
import json
import math
import os

import storage

HERE = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(HERE, "planner_settings.json")
TEAM_FILE = os.path.join(HERE, "team.json")
PRIORITIES = {"high": "สูง", "normal": "ปกติ", "low": "ต่ำ"}


class Assignment:
    def __init__(self, title, course, due_date, estimated_hours, done_hours,
                 priority="normal", details=None):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.estimated_hours = estimated_hours
        self.done_hours = done_hours
        self.priority = priority
        self.details = details or {}

    def remaining_hours(self):
        return round(max(0, self.estimated_hours - self.done_hours), 2)

    def days_left(self):
        return (date.fromisoformat(self.due_date) - date.today()).days

    def progress(self):
        if self.estimated_hours <= 0:
            return 0
        return min(100, max(0, int(self.done_hours * 100 / self.estimated_hours)))


def read_number(text):
    try:
        value = float(text)
    except (TypeError, ValueError, OverflowError):
        return None
    if not math.isfinite(value):
        return None
    return value


def read_date(text):
    try:
        result = date.fromisoformat(str(text))
    except (TypeError, ValueError):
        return None
    if result.isoformat() != text:
        return None
    return result


def daily_hours(text):
    value = read_number(text)
    if value is None or value < 0.1 or value > 12:
        return None
    return value


def load_daily_hours():
    try:
        with open(SETTINGS_FILE, encoding="utf-8") as file:
            settings = json.load(file)
        value = daily_hours(settings.get("daily_hours"))
    except (OSError, ValueError, AttributeError):
        value = None
    if value is None:
        return 2
    return value


def save_daily_hours(value):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump({"daily_hours": value}, file, ensure_ascii=False, indent=2)


def team_data():
    with open(TEAM_FILE, encoding="utf-8") as file:
        return json.load(file)


def details_of(row):
    # Make an independent copy, including the nested subtasks and history.
    details = row.get("details", {})
    if not isinstance(details, dict):
        details = {}
    details = json.loads(json.dumps(details, ensure_ascii=False))
    details.setdefault("started", row["done_hours"] > 0)
    details.setdefault("owner", "")
    details.setdefault("subtasks", [])
    details.setdefault("history", [])
    details.setdefault("progress_on", "")
    details.setdefault("created_on", "")
    return details


def version_of(row):
    text = json.dumps(row, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ceil_tenth(value):
    return math.ceil(max(0, value) * 10 - 0.000000001) / 10


def task_view(row, position, members):
    details = details_of(row)
    task = Assignment(row["title"], row["course"], row["due_date"],
                      row["estimated_hours"], row["done_hours"],
                      row.get("priority", "normal"), details)
    item = dict(row)
    item["details"] = details
    item["priority"] = task.priority
    item["priority_label"] = PRIORITIES.get(task.priority, "ปกติ")
    item["no"] = position
    item["version"] = version_of(row)
    item["remaining_hours"] = task.remaining_hours()
    item["days_left"] = task.days_left()
    item["progress"] = task.progress()
    item["owner_name"] = "ยังไม่มีผู้รับผิดชอบ"
    for member in members:
        if member["id"] == details["owner"]:
            item["owner_name"] = member["name"]
    if item["remaining_hours"] == 0:
        item["status"] = "เสร็จแล้ว"
        item["status_icon"] = "✓"
        item["tone"] = "good"
    elif details["started"] or task.done_hours > 0:
        item["status"] = "กำลังทำ"
        item["status_icon"] = "▶"
        item["tone"] = "gold"
    else:
        item["status"] = "ยังไม่เริ่ม"
        item["status_icon"] = "○"
        item["tone"] = ""
    if item["days_left"] < 0:
        item["deadline_label"] = "เกินกำหนด " + str(-item["days_left"]) + " วัน"
        item["deadline_icon"] = "!"
        item["deadline_tone"] = "bad"
    elif item["days_left"] <= 3:
        item["deadline_label"] = "ใกล้ถึงกำหนด · อีก " + str(item["days_left"]) + " วัน"
        if item["days_left"] == 0:
            item["deadline_label"] = "ใกล้ถึงกำหนด · ส่งวันนี้"
        item["deadline_icon"] = "◷"
        item["deadline_tone"] = "gold"
    else:
        item["deadline_label"] = "ส่งอีก " + str(item["days_left"]) + " วัน"
        item["deadline_icon"] = "▣"
        item["deadline_tone"] = ""
    item["subtask_done"] = 0
    for subtask in details["subtasks"]:
        if subtask.get("done"):
            item["subtask_done"] = item["subtask_done"] + 1
    item["subtask_count"] = len(details["subtasks"])
    item["stale"] = False
    progress_date = read_date(details["progress_on"])
    if progress_date is None:
        progress_date = read_date(details["created_on"])
    if progress_date is None:
        item["stale"] = item["remaining_hours"] > 0
    elif item["remaining_hours"] > 0:
        item["stale"] = (date.today() - progress_date).days >= 2
    return item


def all_views(rows, members):
    items = []
    position = 0
    for row in rows:
        items.append(task_view(row, position, members))
        position = position + 1
    return items


def order_items(items, mode="urgency"):
    # Selection loop adapted from catalog/ranking.
    remaining = list(items)
    ordered = []
    while remaining:
        first = remaining[0]
        for item in remaining:
            if order_key(item, mode) < order_key(first, mode):
                first = item
        ordered.append(first)
        remaining.remove(first)
    return ordered


def order_key(item, mode):
    if mode == "deadline":
        return (item["due_date"], item["no"])
    overdue_rank = 1
    if item["days_left"] < 0:
        overdue_rank = 0
    risk_rank = 1
    if item.get("at_risk"):
        risk_rank = 0
    priority_rank = 1
    if item["priority"] == "high":
        priority_rank = 0
    elif item["priority"] == "low":
        priority_rank = 2
    return (overdue_rank, item["due_date"], -item["remaining_hours"],
            risk_rank, priority_rank, item["no"])


def worked_today(items):
    total = 0
    for item in items:
        for entry in item["details"]["history"]:
            if entry["kind"] == "work" and entry["date"] == date.today().isoformat():
                total = total + entry["hours"]
    return round(total, 2)


def annotate_plan(items, hours):
    spent = min(hours, worked_today(items))
    pending = []
    for item in items:
        if item["remaining_hours"] > 0:
            pending.append(item)
    ordered = order_items(pending, "deadline")
    risk_count = 0
    for task in ordered:
        cumulative = 0
        # Equal deadlines share the whole day's cumulative workload.
        for other in ordered:
            if other["due_date"] <= task["due_date"]:
                cumulative = cumulative + other["remaining_hours"]
        task["cumulative_hours"] = round(cumulative, 2)
        task["available_daily"] = hours
        task["at_risk"] = False
        if task["days_left"] < 0:
            task["plan_status"] = "เกินกำหนด"
            task["plan_icon"] = "!"
            task["plan_tone"] = "bad"
            task["gap"] = task["remaining_hours"]
            task["hours_per_day"] = task["remaining_hours"]
            task["shortfall_per_day"] = 0
            task["available_hours"] = 0
            task["at_risk"] = True
        else:
            days = task["days_left"] + 1
            capacity = days * hours - spent
            required = (cumulative + spent) / days
            raw_gap = max(0, cumulative - capacity)
            task["available_hours"] = round(capacity, 2)
            task["hours_per_day"] = ceil_tenth(required)
            task["gap"] = ceil_tenth(raw_gap)
            task["shortfall_per_day"] = ceil_tenth(max(0, required - hours))
            task["plan_status"] = "ตามแผน"
            task["plan_icon"] = "✓"
            task["plan_tone"] = "good"
            if raw_gap > 0.000000001:
                task["plan_status"] = "เวลาไม่พอ"
                task["plan_icon"] = "!"
                task["plan_tone"] = "bad"
                task["at_risk"] = True
        if task["at_risk"]:
            risk_count = risk_count + 1
    return ordered, risk_count


def today_plan(pending, budget):
    ordered = order_items(pending)
    recommendations = []
    for task in ordered:
        task["today_hours"] = 0
        task["reasons"] = []
        if task["days_left"] < 0:
            task["reasons"].append("เกินกำหนดแล้ว ควรติดต่อผู้สอนและจัดการก่อน")
        elif task["days_left"] <= 3:
            task["reasons"].append("ใกล้ถึงกำหนด ควรเริ่มก่อน")
        if task["remaining_hours"] >= 6:
            task["reasons"].append("ใช้เวลามาก ควรแบ่งเป็นงานย่อย")
        if task["at_risk"]:
            task["reasons"].append("งานนี้เสี่ยงไม่ทันเมื่อเทียบกับเวลาที่มี")
        if task["priority"] == "high":
            task["reasons"].append("ตั้งความสำคัญไว้สูง")
        if not task["reasons"]:
            task["reasons"].append("วันส่งใกล้ที่สุดในงานที่เหลือ")
        if budget > 0.000000001:
            task["today_hours"] = round(min(task["remaining_hours"], budget), 2)
            budget = round(max(0, budget - task["today_hours"]), 2)
            recommendations.append(task)
    return ordered, recommendations


def overview(rows, hours):
    members = team_data()["members"]
    items = all_views(rows, members)
    pending, risk_count = annotate_plan(items, hours)
    actual_today = worked_today(items)
    today_remaining = round(max(0, hours - actual_today), 2)
    ordered, recommendations = today_plan(pending, today_remaining)
    completed = []
    soon_count = 0
    overdue_count = 0
    stale_count = 0
    remaining_total = 0
    for item in items:
        if item["remaining_hours"] == 0:
            completed.append(item)
        else:
            remaining_total = remaining_total + item["remaining_hours"]
            if item["days_left"] < 0:
                overdue_count = overdue_count + 1
            elif item["days_left"] <= 3:
                soon_count = soon_count + 1
            if item["stale"]:
                stale_count = stale_count + 1
    focus = None
    if ordered:
        focus = ordered[0]
    return {"items": ordered, "completed": completed, "all_items": items,
            "recommendations": recommendations, "focus": focus,
            "open_count": len(ordered), "completed_count": len(completed),
            "soon_count": soon_count, "overdue_count": overdue_count,
            "remaining_total": round(remaining_total, 2), "risk_count": risk_count,
            "daily_hours": hours, "stale_count": stale_count,
            "actual_today": actual_today, "today_remaining": today_remaining}


def record_history(row, hours, kind, on_date, note=""):
    details = details_of(row)
    details["history"].append({"date": on_date, "hours": round(hours, 2),
                               "kind": kind, "note": note})
    details["started"] = True
    details["progress_on"] = date.today().isoformat()
    row["details"] = details


def row_index(form, rows):
    text = str(form.get("no", ""))
    if text == "" or not text.isascii() or not text.isdigit() or len(text) > 8:
        return None
    index = int(text)
    if index >= len(rows):
        return None
    if form.get("version", "") != version_of(rows[index]):
        return None
    return index


def quick_action(form):
    """Shared transitions from Overview, Manage, and Plan."""
    rows = storage.load()
    index = row_index(form, rows)
    if index is None:
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
    row = rows[index]
    details = details_of(row)
    action = form.get("action", "")
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
    if action == "start":
        if remaining == 0:
            return "✗ งานนี้เสร็จแล้ว"
        details["started"] = True
        details["progress_on"] = date.today().isoformat()
        row["details"] = details
        message = "✓ เริ่มงานนี้แล้ว เปิดหน้าจัดการงานเพื่อบันทึกเวลาและงานย่อย"
    elif action == "complete":
        if remaining == 0:
            return "✓ งานนี้เสร็จแล้ว"
        details["before_complete"] = row["done_hours"]
        details["subtasks_before_complete"] = []
        for subtask in details["subtasks"]:
            details["subtasks_before_complete"].append(subtask.get("done", False))
            subtask["done"] = True
        details["completed_on"] = date.today().isoformat()
        row["details"] = details
        row["done_hours"] = row["estimated_hours"]
        record_history(row, remaining, "complete", date.today().isoformat(),
                       "ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง")
        message = "✓ ทำเครื่องหมายว่าเสร็จแล้ว งานย้ายไปหมวดเสร็จแล้ว"
    elif action == "reopen":
        if remaining > 0 or "before_complete" not in details:
            return "✗ ยกเลิกได้เฉพาะงานที่กดทำเครื่องหมายเสร็จแล้ว หากต้องปรับเวลาทำจริงให้แก้ไขข้อมูลงาน"
        row["done_hours"] = min(row["estimated_hours"],
                                details["before_complete"])
        if row["done_hours"] >= row["estimated_hours"]:
            row["done_hours"] = 0
        previous = details.pop("subtasks_before_complete", [])
        position = 0
        for subtask in details["subtasks"]:
            if position < len(previous):
                subtask["done"] = previous[position]
            position = position + 1
        details.pop("completed_on", None)
        details["started"] = True
        row["details"] = details
        record_history(row, 0, "reopen", date.today().isoformat(), "เปิดงานกลับมาทำต่อ")
        message = "✓ เปิดงานกลับมาทำต่อแล้ว"
    else:
        return "✗ ไม่รู้จักคำสั่ง"
    storage.save(rows)
    return message


def work_history(items):
    history = []
    actual_total = 0
    for item in items:
        for entry in item["details"]["history"]:
            line = dict(entry)
            line["title"] = item["title"]
            line["course"] = item["course"]
            line["owner_name"] = item["owner_name"]
            line["label"] = "บันทึกเวลาทำงาน"
            if entry["kind"] == "work":
                actual_total = actual_total + entry["hours"]
            elif entry["kind"] == "complete":
                line["label"] = "ปิดงานตามเวลาประมาณ"
            elif entry["kind"] == "adjustment":
                line["label"] = "ปรับยอดความคืบหน้า"
            elif entry["kind"] == "reopen":
                line["label"] = "เปิดงานอีกครั้ง"
            history.append(line)
    ordered = []
    while history:
        latest = history[0]
        for entry in history:
            if entry["date"] > latest["date"]:
                latest = entry
        ordered.append(latest)
        history.remove(latest)
    return ordered, round(actual_total, 2)


def daily_history(history):
    days = []
    for entry in history:
        if entry["kind"] != "work":
            continue
        existing = None
        for day in days:
            if day["date"] == entry["date"]:
                existing = day
        if existing is None:
            existing = {"date": entry["date"], "hours": 0, "count": 0}
            days.append(existing)
        existing["hours"] = round(existing["hours"] + entry["hours"], 2)
        existing["count"] = existing["count"] + 1
    return days
