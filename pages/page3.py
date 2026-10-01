"""Plan calculator adapted from catalog/ranking and calculator."""
import models
import storage

TITLE = "แผนก่อนวันส่ง"


def build(query):
    hours = models.load_daily_hours()
    notice = ""
    if "hours" in query:
        requested = models.daily_hours(query.get("hours", ""))
        if requested is None:
            notice = "กรุณากรอกเวลาว่าง 0.1 ถึง 12 ชั่วโมง ใช้ค่าที่บันทึกไว้แทน"
        else:
            hours = requested
    context = models.overview(storage.load(), hours)
    context["tasks"] = models.order_items(context["items"], "deadline")
    context["notice"] = notice
    required = 0
    for task in context["tasks"]:
        if task["days_left"] >= 0:
            required = max(required, task["hours_per_day"])
    context["required_daily"] = required
    context["daily_shortfall"] = models.ceil_tenth(max(0, required - hours))
    return context


def handle(form):
    if form.get("action", "") in ("start", "complete", "reopen"):
        return models.quick_action(form)
    if form.get("action", "") != "save_hours":
        return "✗ ไม่รู้จักคำสั่ง"
    hours = models.daily_hours(form.get("hours", ""))
    if hours is None:
        return "✗ เวลาว่างต้องตั้งแต่ 0.1 ถึง 12 ชั่วโมงต่อวัน"
    models.save_daily_hours(hours)
    return "✓ บันทึกเวลาว่างแล้ว ภาพรวมและแผนใช้ค่านี้ร่วมกัน"
