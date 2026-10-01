"""Team directory and assignment workload, extending the given team page."""
import models
import storage

TITLE = "ทีม"
TITLES = ["นางสาว", "นาย", "นาง", "ว่าที่ร้อยตรี", "Mr.", "Ms.", "Miss"]


def initial_of(name):
    name = name.strip()
    for prefix in TITLES:
        if name.startswith(prefix):
            name = name[len(prefix):].strip()
    if name == "":
        return "?"
    return name[0]


def member_summary(member, items, hours):
    result = dict(member)
    result["initial"] = initial_of(member["name"])
    assigned = []
    total = 0
    done = 0
    remaining = 0
    open_count = 0
    for item in items:
        if item["details"]["owner"] == member["id"]:
            assigned.append(item)
            total = total + item["estimated_hours"]
            done = done + min(item["estimated_hours"], item["done_hours"])
            remaining = remaining + item["remaining_hours"]
            if item["remaining_hours"] > 0:
                open_count = open_count + 1
    progress = 0
    if total > 0:
        progress = min(100, int(done * 100 / total))
    own_tasks, risks = models.annotate_plan(assigned, hours)
    result["assignments"] = assigned
    result["assignment_count"] = len(assigned)
    result["open_count"] = open_count
    result["progress"] = progress
    result["remaining_hours"] = round(remaining, 2)
    result["risk_count"] = risks
    result["overloaded"] = remaining > hours * 7 or risks > 0
    return result


def build():
    data = models.team_data()
    hours = models.load_daily_hours()
    items = models.all_views(storage.load(), data["members"])
    members = []
    known_owners = []
    for member in data["members"]:
        known_owners.append(member["id"])
        members.append(member_summary(member, items, hours))
    unassigned = []
    for item in items:
        if item["details"]["owner"] not in known_owners and item["remaining_hours"] > 0:
            unassigned.append(item)
    return {"group": data["group"], "members": members, "count": len(members),
            "unassigned": unassigned, "daily_hours": hours,
            "weekly_capacity": round(hours * 7, 1)}
