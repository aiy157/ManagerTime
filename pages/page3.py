"""Deadline order and workload estimate based on catalog/ranking and calculator."""
import models
import storage

TITLE = "แผนก่อนวันส่ง"


def build(query):
    notice = ""
    try:
        daily_hours = float(query.get("hours", "2"))
    except ValueError:
        daily_hours = 2
        notice = "ใช้ค่าเริ่มต้น 2 ชั่วโมงต่อวัน"
    if daily_hours != daily_hours or daily_hours in (float("inf"), float("-inf")) or daily_hours <= 0 or daily_hours > 12:
        daily_hours = 2
        notice = "กรุณาระบุเวลาว่างมากกว่า 0 และไม่เกิน 12 ชั่วโมงต่อวัน"

    remaining = []
    for row in storage.load():
        task = models.Assignment(row["title"], row["course"], row["due_date"],
                                 row["estimated_hours"], row["done_hours"])
        if task.remaining_hours() > 0:
            remaining.append({"title": task.title, "course": task.course,
                              "due_date": task.due_date, "days_left": task.days_left(),
                              "remaining_hours": task.remaining_hours()})

    # Selection loop from catalog/ranking: nearest deadline comes first.
    ordered = []
    while remaining:
        first = remaining[0]
        for task in remaining:
            if task["due_date"] < first["due_date"]:
                first = task
        ordered.append(first)
        remaining.remove(first)

    cumulative_hours = 0
    risk_count = 0
    for task in ordered:
        cumulative_hours = cumulative_hours + task["remaining_hours"]
        if task["days_left"] < 0:
            task["status"] = "เกินกำหนด"
            task["tone"] = "bad"
            task["gap"] = task["remaining_hours"]
            risk_count = risk_count + 1
        else:
            available_hours = (task["days_left"] + 1) * daily_hours
            task["gap"] = round(max(0, cumulative_hours - available_hours), 1)
            task["hours_per_day"] = round(cumulative_hours / (task["days_left"] + 1), 1)
            if task["gap"] > 0:
                task["status"] = "เวลาไม่พอ"
                task["tone"] = "bad"
                risk_count = risk_count + 1
            elif task["days_left"] <= 3:
                task["status"] = "ควรเริ่มตอนนี้"
                task["tone"] = "gold"
            else:
                task["status"] = "ตามแผน"
                task["tone"] = "good"

    return {"tasks": ordered, "daily_hours": daily_hours, "risk_count": risk_count,
            "focus": ordered[0] if ordered else None, "notice": notice}
