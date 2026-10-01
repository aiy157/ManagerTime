"""Temporary UI demo at port 5002; never writes the project's task data."""
from datetime import date, timedelta
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

import app
import models
import storage


def fixture_task(title, days, estimate, done=0, owner="", priority="normal"):
    return {"title": title, "course": "วิชาทดสอบระบบ",
            "due_date": (date.today() + timedelta(days=days)).isoformat(),
            "estimated_hours": estimate, "done_hours": done, "priority": priority,
            "details": {"owner": owner, "started": done > 0, "subtasks": [],
                        "history": [], "created_on": date.today().isoformat(),
                        "progress_on": ""}}


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="deadline-ui-") as folder:
        storage.DATA_FILE = str(Path(folder) / "data.json")
        storage.SAMPLE_FILE = str(Path(folder) / "sample.json")
        models.SETTINGS_FILE = str(Path(folder) / "settings.json")
        members = models.team_data()["members"]
        rows = [fixture_task("งานทดสอบเกินกำหนด", -1, 2, 1, members[0]["id"]),
                fixture_task("ออกแบบหน้ารายงานวันนี้", 0, 3, owner=members[1]["id"],
                             priority="high"),
                fixture_task("โครงงานทดสอบภาระสะสม", 1, 18),
                fixture_task("เอกสารที่ทำเสร็จแล้ว", 4, 2, 2, members[2]["id"])]
        rows[1]["details"]["subtasks"] = [{"title": "ร่างหน้าจอ", "done": False},
                                          {"title": "ทดสอบบนมือถือ", "done": False}]
        storage.save(rows)
        Path(storage.SAMPLE_FILE).write_text(json.dumps(rows, ensure_ascii=False),
                                             encoding="utf-8")
        models.save_daily_hours(4)
        print("UI test data only: http://127.0.0.1:5002/page1")
        app.app.run(host="127.0.0.1", port=5002, debug=False)
