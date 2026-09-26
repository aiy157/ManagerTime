"""Add, edit, and delete assignments based on catalog/form."""
from datetime import date

import models
import storage

TITLE = "จัดการงาน"


def build():
    items = []
    position = 0
    for row in storage.load():
        item = dict(row)
        item["no"] = position
        task = models.Assignment(row["title"], row["course"], row["due_date"],
                                 row["estimated_hours"], row["done_hours"])
        item["remaining_hours"] = task.remaining_hours()
        items.append(item)
        position = position + 1
    return {"items": items, "count": len(items)}


def read_hours(text):
    try:
        value = float(text)
    except (TypeError, ValueError):
        return None
    if value != value or value in (float("inf"), float("-inf")):
        return None
    return value


def check(form):
    title = form.get("title", "").strip()
    course = form.get("course", "").strip()
    due_date = form.get("due_date", "")
    estimate = read_hours(form.get("estimated_hours", ""))
    done = read_hours(form.get("done_hours", "0"))

    if title == "" or course == "":
        return None, "กรุณากรอกชื่องานและวิชา"
    if len(title) > 80 or len(course) > 40:
        return None, "ชื่องานหรือวิชายาวเกินไป"
    try:
        date.fromisoformat(due_date)
    except ValueError:
        return None, "กรุณาเลือกวันส่งที่ถูกต้อง"
    if estimate is None or estimate <= 0 or estimate > 200:
        return None, "ชั่วโมงที่คาดว่าจะใช้ต้องมากกว่า 0 และไม่เกิน 200"
    if done is None or done < 0 or done > estimate:
        return None, "ชั่วโมงที่ทำแล้วต้องอยู่ระหว่าง 0 ถึงชั่วโมงที่คาดว่าจะใช้"

    return {"title": title, "course": course, "due_date": due_date,
            "estimated_hours": estimate, "done_hours": done}, ""


def handle(form):
    action = form.get("action", "")
    items = storage.load()

    if action == "add":
        task, error = check(form)
        if error:
            return "✗ " + error
        items.append(task)
        storage.save(items)
        return "✓ เพิ่มงานแล้ว"

    position = form.get("no", "")
    if not position.isdigit() or int(position) >= len(items):
        return "✗ ไม่พบงานนี้"
    index = int(position)

    if action == "delete":
        items.pop(index)
        storage.save(items)
        return "✓ ลบงานแล้ว"
    if action == "update":
        task, error = check(form)
        if error:
            return "✗ " + error
        items[index] = task
        storage.save(items)
        return "✓ บันทึกการแก้ไขแล้ว"
    return "✗ ไม่รู้จักคำสั่ง"
