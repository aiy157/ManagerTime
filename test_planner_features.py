"""Business tests for the upgraded planner; all mutations use temporary files."""
from datetime import date, timedelta
import errno
import json
import os

import pytest

import app
import models
import storage
from pages import page1, page2, page3, team


def task(title="งาน A", days=1, estimate=4, done=0, priority="normal", owner=""):
    return {"title": title, "course": "การเขียนโปรแกรม",
            "due_date": (date.today() + timedelta(days=days)).isoformat(),
            "estimated_hours": estimate, "done_hours": done, "priority": priority,
            "details": {"owner": owner, "started": done > 0, "subtasks": [],
                        "history": [], "created_on": date.today().isoformat(),
                        "progress_on": ""}}


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    data_file = tmp_path / "data.json"
    sample_file = tmp_path / "data.sample.json"
    data_file.write_text("[]", encoding="utf-8")
    sample_file.write_text("[]", encoding="utf-8")
    monkeypatch.setattr(storage, "DATA_FILE", str(data_file))
    monkeypatch.setattr(storage, "SAMPLE_FILE", str(sample_file))
    monkeypatch.setattr(models, "SETTINGS_FILE", str(tmp_path / "settings.json"))
    return app.app.test_client()


def fields(row, index=0, action="complete"):
    return {"action": action, "no": str(index), "version": models.version_of(row)}


def add_form(**changes):
    form = {"action": "add", "title": "งานใหม่", "course": "ฟิสิกส์",
            "due_date": (date.today() + timedelta(days=2)).isoformat(),
            "estimated_hours": "4", "done_hours": "0", "priority": "normal",
            "owner": ""}
    form.update(changes)
    return form


def test_existing_five_fields_still_load_without_rewriting(isolated):
    row = task()
    del row["priority"]
    del row["details"]
    storage.save([row])
    before = storage.load()
    for path in ("/", "/page1", "/page2", "/page3", "/team"):
        response = isolated.get(path)
        assert response.status_code == 200
        assert "ยังไม่พร้อม" not in response.get_data(as_text=True)
    assert storage.load() == before


def test_add_owner_priority_and_subtasks_keeps_seven_fields(isolated):
    owner = models.team_data()["members"][0]["id"]
    form = add_form(owner=owner, priority="high", subtasks="วิเคราะห์\nออกแบบ\nทดสอบ")
    response = isolated.post("/page2", data=form, follow_redirects=True)
    assert "เพิ่มงานแล้ว" in response.get_data(as_text=True)
    row = storage.load()[0]
    assert len(row) == 7
    assert row["details"]["owner"] == owner
    assert row["priority"] == "high"
    assert len(row["details"]["subtasks"]) == 3
    assert not row["details"]["history"]


@pytest.mark.parametrize("changes", [
    {"title": "   "}, {"course": ""}, {"title": "ก" * 81}, {"course": "ก" * 41},
    {"due_date": "2026-02-30"}, {"due_date": "20260930"},
    {"estimated_hours": "0"}, {"estimated_hours": "-1"},
    {"estimated_hours": "200.1"}, {"estimated_hours": "nan"},
    {"estimated_hours": "inf"}, {"done_hours": "-1"}, {"done_hours": "5"},
    {"priority": "unknown"}, {"owner": "999999"},
])
def test_invalid_add_does_not_mutate_data(isolated, changes):
    storage.save([task()])
    before = storage.load()
    message = page2.handle(add_form(**changes))
    assert message.startswith("✗")
    assert storage.load() == before


def test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated(isolated):
    form = add_form(due_date=(date.today() - timedelta(days=1)).isoformat())
    assert page2.handle(form).startswith("✗")
    assert storage.load() == []
    form["acknowledge_past"] = "yes"
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    form.update(fields(row, action="update"))
    del form["acknowledge_past"]
    form["title"] = "อัปเดตงานค้าง"
    assert page2.handle(form).startswith("✓")
    assert storage.load()[0]["title"] == "อัปเดตงานค้าง"


def test_start_complete_reopen_updates_all_pages_and_preserves_real_hours(isolated):
    row = task(done=1)
    row["details"]["subtasks"] = [{"title": "ออกแบบ", "done": True},
                                 {"title": "ทดสอบ", "done": False}]
    storage.save([row])
    assert page1.handle(fields(row, action="start")).startswith("✓")
    row = storage.load()[0]
    assert page1.handle(fields(row)).startswith("✓")
    saved = storage.load()[0]
    assert saved["done_hours"] == 4
    assert all(subtask["done"] for subtask in saved["details"]["subtasks"])
    assert page1.build()["open_count"] == 0
    assert page1.build()["completed_count"] == 1
    assert page3.build({})["risk_count"] == 0
    history, actual = models.work_history(page2.build()["items"])
    assert actual == 0
    assert history[0]["kind"] == "complete"
    assert page1.handle(fields(saved, action="reopen")).startswith("✓")
    saved = storage.load()[0]
    assert saved["done_hours"] == 1
    assert [subtask["done"] for subtask in saved["details"]["subtasks"]] == [True, False]


def test_work_logs_accumulate_real_hours_and_subtasks_are_independent(isolated):
    row = task()
    row["details"]["subtasks"] = [{"title": "ทดสอบ", "done": False}]
    storage.save([row])
    form = fields(row, action="log_time")
    form.update(hours="1.5", work_date=date.today().isoformat(), note="ทำส่วนแรก")
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    assert row["done_hours"] == 1.5
    assert page1.build()["items"][0]["progress"] == 37
    form = fields(row, action="toggle_subtask")
    form["subtask_no"] = "0"
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    assert row["details"]["subtasks"][0]["done"]
    assert row["done_hours"] == 1.5
    form = fields(row, action="log_time")
    form.update(hours="2.5", work_date=date.today().isoformat())
    assert page2.handle(form).startswith("✓")
    assert page1.build()["open_count"] == 0
    assert page2.build()["actual_total"] == 4


def test_overlogging_and_future_work_date_are_rejected(isolated):
    row = task()
    storage.save([row])
    form = fields(row, action="log_time")
    form.update(hours="5", work_date=date.today().isoformat())
    assert page2.handle(form).startswith("✗")
    form.update(hours="1", work_date=(date.today() + timedelta(days=1)).isoformat())
    assert page2.handle(form).startswith("✗")
    assert storage.load()[0]["done_hours"] == 0


def test_stale_row_cannot_modify_a_shifted_or_updated_task(isolated):
    first, second = task("ก่อน"), task("หลัง")
    storage.save([first, second])
    stale_form = fields(second, 1)
    assert page2.handle(fields(first, action="delete")).startswith("✓")
    assert page1.handle(stale_form).startswith("✗")
    assert storage.load()[0]["title"] == "หลัง"
    assert storage.load()[0]["done_hours"] == 0
    stale_form = fields(storage.load()[0], action="complete")
    row = storage.load()[0]
    row["title"] = "ชื่อใหม่"
    storage.save([row])
    assert page1.handle(stale_form).startswith("✗")


@pytest.mark.parametrize("number", ["²", "-1", "", "99999999999999999999"])
def test_bad_indices_do_not_crash_or_save(isolated, number):
    row = task()
    storage.save([row])
    form = fields(row)
    form["no"] = number
    assert page1.handle(form).startswith("✗")
    assert storage.load()[0]["done_hours"] == 0


def test_plan_uses_daily_capacity_and_groups_identical_deadlines(isolated):
    storage.save([task("วันนี้", 0, 3), task("พรุ่งนี้", 1, 4)])
    plan = page3.build({"hours": "2"})
    assert [row["gap"] for row in plan["tasks"]] == [1, 3]
    assert plan["risk_count"] == 2
    assert page3.build({"hours": "4"})["risk_count"] == 0
    storage.save([task("งานแรก", 0, 3), task("งานสอง", 0, 4)])
    plan = page3.build({"hours": "4"})
    assert [row["gap"] for row in plan["tasks"]] == [3, 3]
    assert [row["cumulative_hours"] for row in plan["tasks"]] == [7, 7]
    assert plan["risk_count"] == 2


def test_plan_example_nine_required_four_available_and_five_short(isolated):
    storage.save([task(estimate=18, days=1)])
    plan = page3.build({"hours": "4"})
    row = plan["tasks"][0]
    assert row["hours_per_day"] == 9
    assert row["shortfall_per_day"] == 5
    assert row["gap"] == 10
    assert plan["required_daily"] == 9
    assert plan["daily_shortfall"] == 5


def test_overdue_included_and_tiny_shortfall_never_looks_on_track(isolated):
    storage.save([task("ค้าง", -1, 2), task("อนาคต", 1, 3)])
    plan = page3.build({"hours": "2"})
    assert plan["tasks"][1]["cumulative_hours"] == 5
    assert plan["tasks"][1]["gap"] == 1
    storage.save([task(estimate=2.01, days=0)])
    row = page3.build({"hours": "2"})["tasks"][0]
    assert row["at_risk"]
    assert row["gap"] == 0.1


def test_daily_hours_saved_and_used_across_pages(isolated):
    assert page3.handle({"action": "save_hours", "hours": "4"}).startswith("✓")
    assert page1.build()["daily_hours"] == 4
    assert page3.build({})["daily_hours"] == 4
    assert team.build()["daily_hours"] == 4
    for value in ("0", "12.1", "abc", "nan", "inf"):
        assert page3.handle({"action": "save_hours", "hours": value}).startswith("✗")
        assert page3.build({"hours": value})["daily_hours"] == 4


def test_recommendations_never_overbook_today_and_use_priority_tiebreak(isolated):
    storage.save([task("ไกล", 7, 10), task("ใกล้", 1, 1), task("ค้าง", -1, 1)])
    overview = page1.build()
    assert overview["focus"]["title"] == "ค้าง"
    assert [row["title"] for row in overview["recommendations"]] == ["ค้าง", "ใกล้"]
    assert sum(row["today_hours"] for row in overview["recommendations"]) <= 2
    storage.save([task("ต่ำ", 2, 2, priority="low"), task("สูง", 2, 2, priority="high")])
    assert page1.build()["focus"]["title"] == "สูง"


def test_team_counts_progress_and_unassigned_tasks(isolated):
    owner = models.team_data()["members"][0]["id"]
    storage.save([task("ของสมาชิก", 2, 4, 1, owner=owner), task("ไม่มอบหมาย")])
    summary = team.build()
    member = summary["members"][0]
    assert member["assignment_count"] == 1
    assert member["open_count"] == 1
    assert member["progress"] == 25
    assert len(summary["unassigned"]) == 1
    storage.save([task("ภาระมาก", 2, 20, owner=owner)])
    assert team.build()["members"][0]["overloaded"]


def test_empty_and_completed_only_data_have_no_focus(isolated):
    assert page1.build()["focus"] is None
    assert page3.build({})["tasks"] == []
    storage.save([task(estimate=4, done=4)])
    assert page3.build({})["tasks"] == []
    assert len(page1.build()["completed"]) == 1


def test_all_forms_have_versions_and_templates_escape_user_input(isolated):
    storage.save([task(title='<script>alert("x")</script>')])
    for path in ("/page1", "/page2", "/page3", "/team"):
        html = isolated.get(path).get_data(as_text=True)
        assert "ยังไม่พร้อม" not in html
        assert '<script>alert("x")</script>' not in html
        if path != "/team":
            assert 'name="version"' in html
    row = storage.load()[0]
    response = isolated.post("/page1", data=fields(row), follow_redirects=True)
    assert "งานที่เสร็จแล้ว" in response.get_data(as_text=True)
    assert storage.load()[0]["done_hours"] == 4


def test_today_work_reduces_recommendation_budget_and_capacity(isolated):
    done = task("เสร็จแล้ว", days=0, estimate=1, done=1)
    done["details"]["history"] = [{"date": date.today().isoformat(),
                                    "hours": 1, "kind": "work", "note": ""}]
    pending = task("วันนี้", days=0, estimate=2)
    storage.save([done, pending])
    result = page1.build()
    assert result["actual_today"] == 1
    assert result["today_remaining"] == 1
    assert result["recommendations"][0]["today_hours"] == 1
    plan = page3.build({})["tasks"][0]
    assert plan["available_hours"] == 1
    assert plan["hours_per_day"] == 3
    assert plan["gap"] == 1
    done["details"]["history"][0]["hours"] = 2
    storage.save([done, pending])
    assert page1.build()["recommendations"] == []
    assert page1.build()["open_count"] == 1


def test_past_logs_and_estimated_completion_do_not_consume_today(isolated):
    row = task("ก่อนหน้า", done=1)
    row["details"]["history"] = [
        {"date": (date.today() - timedelta(days=1)).isoformat(),
         "hours": 1, "kind": "work", "note": ""}]
    storage.save([row, task("วันนี้", days=0)])
    assert page1.handle(fields(row)).startswith("✓")
    assert page1.build()["actual_today"] == 0
    assert page1.build()["today_remaining"] == 2
    assert page2.build()["daily_history"][0]["hours"] == 1
    assert page2.build()["actual_total"] == 1


def test_reopen_requires_prior_manual_completion(isolated):
    for row in (task(), task(estimate=4, done=4)):
        storage.save([row])
        assert page1.handle(fields(row, action="reopen")).startswith("✗")
        assert storage.load() == [row]


def test_daily_summary_groups_actual_work_only(isolated):
    row = task()
    today = date.today().isoformat()
    row["details"]["history"] = [
        {"date": today, "hours": 1, "kind": "work", "note": "ส่วนแรก"},
        {"date": today, "hours": 1.5, "kind": "work", "note": "ส่วนสอง"},
        {"date": today, "hours": 8, "kind": "complete", "note": ""}]
    storage.save([row])
    summary = page2.build()
    assert summary["daily_history"] == [{"date": today, "hours": 2.5, "count": 2}]
    assert summary["actual_total"] == 2.5


@pytest.fixture
def read_only_runtime(tmp_path, monkeypatch, isolated):
    """Simulate a read-only deployment without changing the project files."""
    bundle = tmp_path / "bundle"
    scratch = tmp_path / "scratch"
    bundle.mkdir()
    scratch.mkdir()
    row = task()
    row["details"]["subtasks"] = [{"title": "ทดสอบ", "done": False}]
    (bundle / "data.json").write_text(json.dumps([row]), encoding="utf-8")
    (bundle / "planner_settings.json").write_text('{"daily_hours": 2}', encoding="utf-8")
    monkeypatch.setattr(models, "HERE", str(bundle))
    monkeypatch.setattr(storage, "DATA_FILE", str(bundle / "data.json"))
    monkeypatch.setattr(models, "SETTINGS_FILE", str(bundle / "planner_settings.json"))
    monkeypatch.delenv("DEADLINE_DATA_DIR", raising=False)
    monkeypatch.setattr(models.tempfile, "gettempdir", lambda: str(scratch))
    original_tempfile = models.tempfile.TemporaryFile

    def deny_bundle(*args, **kwargs):
        if os.path.abspath(kwargs.get("dir", "")) == str(bundle):
            raise OSError(errno.EROFS, "Read-only file system")
        return original_tempfile(*args, **kwargs)

    monkeypatch.setattr(models.tempfile, "TemporaryFile", deny_bundle)
    monkeypatch.setattr(models, "STORAGE_NOTICE", models.configure_storage())
    return isolated, bundle, scratch


@pytest.mark.parametrize("action", ["start", "complete", "reopen", "update", "delete",
                                         "log_time", "add_subtask", "toggle_subtask"])
def test_read_only_runtime_supports_all_task_actions(read_only_runtime, action):
    client, bundle, scratch = read_only_runtime
    if action == "reopen":
        row = storage.load()[0]
        assert page2.handle(fields(row, action="complete")).startswith("✓")
    row = storage.load()[0]
    form = fields(row, action=action)
    if action == "update":
        form.update(add_form(title="งานที่แก้ไข"))
        form["action"] = action
    elif action == "log_time":
        form.update(hours="1", work_date=date.today().isoformat())
    elif action == "add_subtask":
        form["subtask_title"] = "เตรียมส่ง"
    elif action == "toggle_subtask":
        form["subtask_no"] = "0"
    response = client.post("/page2", data=form, follow_redirects=True)
    html = response.get_data(as_text=True)
    assert "ยังไม่พร้อม" not in html
    assert "✓" in html
    assert "ข้อมูลเก็บชั่วคราว" in html
    assert os.path.commonpath([storage.DATA_FILE, str(scratch)]) == str(scratch)
    saved = storage.load()
    if action == "start":
        assert saved[0]["details"]["started"]
    elif action == "complete":
        assert saved[0]["done_hours"] == saved[0]["estimated_hours"]
    elif action == "reopen":
        assert saved[0]["done_hours"] == 0
    elif action == "update":
        assert saved[0]["title"] == "งานที่แก้ไข"
    elif action == "delete":
        assert saved == []
    elif action == "log_time":
        assert saved[0]["done_hours"] == 1
    elif action == "add_subtask":
        assert len(saved[0]["details"]["subtasks"]) == 2
    else:
        assert saved[0]["details"]["subtasks"][0]["done"]
    assert json.loads((bundle / "data.json").read_text(encoding="utf-8"))[0]["done_hours"] == 0


def test_read_only_runtime_add_settings_and_reinitialization(read_only_runtime):
    client, bundle, scratch = read_only_runtime
    response = client.post("/page2", data=add_form(), follow_redirects=True)
    assert "เพิ่มงานแล้ว" in response.get_data(as_text=True)
    assert len(storage.load()) == 2
    response = client.post("/page3", data={"action": "save_hours", "hours": "4"}, follow_redirects=True)
    assert "บันทึกเวลาว่างแล้ว" in response.get_data(as_text=True)
    before = storage.load()
    models.configure_storage()
    assert storage.load() == before
    assert models.load_daily_hours() == 4
    for path in ("/page1", "/page2", "/page3", "/team", "/page3?hours=invalid"):
        html = client.get(path).get_data(as_text=True)
        assert "ยังไม่พร้อม" not in html
        assert "ข้อมูลเก็บชั่วคราว" in html
    html = client.get("/page3?hours=invalid").get_data(as_text=True)
    assert "กรุณากรอกเวลาว่าง" in html
    assert json.loads((bundle / "planner_settings.json").read_text(encoding="utf-8"))["daily_hours"] == 2


def test_writable_local_storage_stays_in_project(isolated, tmp_path, monkeypatch):
    monkeypatch.delenv("DEADLINE_DATA_DIR", raising=False)
    monkeypatch.setattr(models, "HERE", str(tmp_path))
    data_file = storage.DATA_FILE
    settings_file = models.SETTINGS_FILE
    assert models.configure_storage() == ""
    assert storage.DATA_FILE == data_file
    assert models.SETTINGS_FILE == settings_file
    assert page2.handle(add_form()).startswith("✓")
    assert len(storage.load()) == 1
    assert page3.handle({"action": "save_hours", "hours": "4"}).startswith("✓")
    assert models.load_daily_hours() == 4


def test_configured_data_directory_preserves_existing_files(isolated, tmp_path, monkeypatch):
    destination = tmp_path / "persistent"
    destination.mkdir()
    row = task("งานเดิมในพื้นที่จัดเก็บ")
    (destination / "data.json").write_text(json.dumps([row]), encoding="utf-8")
    (destination / "planner_settings.json").write_text('{"daily_hours": 3}', encoding="utf-8")
    monkeypatch.setenv("DEADLINE_DATA_DIR", str(destination))
    assert models.configure_storage() == ""
    assert storage.load() == [row]
    assert models.load_daily_hours() == 3
    assert page2.handle(add_form()).startswith("✓")
    models.configure_storage()
    assert len(storage.load()) == 2
    assert storage.reset()
    assert storage.load() == []


@pytest.mark.parametrize("code", [errno.ENOSPC, errno.EIO])
def test_storage_initialization_does_not_hide_other_io_errors(isolated, monkeypatch, code):
    monkeypatch.delenv("DEADLINE_DATA_DIR", raising=False)

    def fail(*args, **kwargs):
        raise OSError(code, "Cannot write")

    monkeypatch.setattr(models.tempfile, "TemporaryFile", fail)
    with pytest.raises(OSError) as error:
        models.configure_storage()
    assert error.value.errno == code
