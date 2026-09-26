"""Dashboard based on catalog/list and catalog/stats."""
import models
import storage

TITLE = "ภาพรวมงาน"


def build():
    items = []
    open_count = 0
    soon_count = 0
    overdue_count = 0
    remaining_total = 0

    for row in storage.load():
        task = models.Assignment(row["title"], row["course"], row["due_date"],
                                 row["estimated_hours"], row["done_hours"])
        remaining = task.remaining_hours()
        days = task.days_left()
        item = dict(row)
        item["remaining_hours"] = remaining
        item["days_left"] = days
        item["progress"] = 0
        if row["estimated_hours"] > 0:
            item["progress"] = min(100, int(row["done_hours"] * 100 / row["estimated_hours"]))

        if remaining == 0:
            item["status"] = "เสร็จแล้ว"
            item["tone"] = "good"
        else:
            open_count = open_count + 1
            remaining_total = remaining_total + remaining
            if days < 0:
                overdue_count = overdue_count + 1
                item["status"] = "เกินกำหนด " + str(-days) + " วัน"
                item["tone"] = "bad"
            elif days == 0:
                soon_count = soon_count + 1
                item["status"] = "ส่งวันนี้"
                item["tone"] = "bad"
            elif days <= 3:
                soon_count = soon_count + 1
                item["status"] = "อีก " + str(days) + " วัน"
                item["tone"] = "gold"
            else:
                item["status"] = "อีก " + str(days) + " วัน"
                item["tone"] = ""
        items.append(item)

    # Keep unfinished work nearest to its deadline at the top of the dashboard.
    ordered = []
    while items:
        first = items[0]
        for item in items:
            if first["remaining_hours"] == 0 and item["remaining_hours"] > 0:
                first = item
            elif item["remaining_hours"] > 0 and first["remaining_hours"] > 0 and item["due_date"] < first["due_date"]:
                first = item
        ordered.append(first)
        items.remove(first)

    return {"items": ordered, "open_count": open_count, "soon_count": soon_count,
            "overdue_count": overdue_count, "remaining_total": remaining_total}
