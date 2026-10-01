"""Overview adapted from catalog/list, stats, ranking, and cart actions."""
import models
import storage

TITLE = "ภาพรวมงาน"


def build():
    context = models.overview(storage.load(), models.load_daily_hours())
    reminders = []
    for item in context["items"]:
        reminders.append({"title": item["title"], "due_date": item["due_date"],
                          "remaining_hours": item["remaining_hours"],
                          "at_risk": item["at_risk"], "stale": item["stale"],
                          "today_hours": item["today_hours"]})
    context["reminder_tasks"] = reminders
    return context


def handle(form):
    if form.get("action", "") in ("start", "complete", "reopen"):
        return models.quick_action(form)
    return "✗ ไม่รู้จักคำสั่ง"
