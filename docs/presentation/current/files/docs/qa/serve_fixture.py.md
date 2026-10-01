# docs/qa/serve_fixture.py — เว็บสาธิตด้วยข้อมูลชั่วคราว

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 43 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `2b18adc71201f76e75360644d0772b15fcaf6d3b4fb4ce832a05aac3f8b64667`

**ผู้ศึกษา/บทบาท:** QA

## 1. หน้าที่และการเชื่อมต่อ

เปิดแอปจริงพอร์ต 5002 แต่แยก data/sample/settings สำหรับทดลองกดปุ่ม

- **รับเข้า:** schema ของงาน สมาชิกจริงจาก team.json และวันที่เครื่อง
- **ผลลัพธ์:** Flask local demo ที่ http://127.0.0.1:5002/page1

**เกี่ยวข้องกับ:** app/models/storage; tempfile/pathlib standard library

## 2. ลำดับทำงาน

1. หาตำแหน่ง root และเพิ่มให้ import app ได้
2. สร้าง TemporaryDirectory และเปลี่ยน path ใน process ทดสอบ
3. เติมงานค้าง งานวันนี้ งานใหญ่ งานเสร็จ และงานย่อยตัวอย่าง
4. บันทึก settings 4 ชั่วโมงและเปิด server debug=False

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่เปลี่ยนตัวแปรของ server อีก process ที่พอร์ต 5000/5001
- ต้องหยุด server เดิมที่ 5002 ก่อนรันซ้ำ
- เป็นเว็บสาธิตชั่วคราวไม่ใช่สคริปต์ deploy

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q018: return ต่างจาก print อย่างไร?](../../../TEACHER_QUESTIONS.md#q018)
- [Q050: กดลบงานแล้วประวัติยังอยู่หรือไม่?](../../../TEACHER_QUESTIONS.md#q050)
- [Q093: ทดสอบอย่างไรไม่ให้ข้อมูลจริงหาย?](../../../TEACHER_QUESTIONS.md#q093)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `fixture_task` | L16–L22 | ประกาศฟังก์ชัน `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `DATA_FILE` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `Path` | pathlib path object ของ script QA |
| `ROOT` | root workspace ที่ script QA หาได้ |
| `SAMPLE_FILE` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `SETTINGS_FILE` | path ของ planner_settings.json |
| `TemporaryDirectory` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `__file__` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `__name__` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `app` | module Flask router ที่อาจารย์ให้ |
| `date` | ชนิดวันที่ระดับวันจาก datetime |
| `datetime` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `days` | จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท |
| `debug` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `done` | ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น |
| `dumps` | แปลง object เป็นข้อความ JSON |
| `encoding` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `ensure_ascii` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `estimate` | ชั่วโมงประมาณของงาน |
| `fixture_task` | สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว |
| `folder` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `host` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `insert` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `isoformat` | แปลง date เป็น YYYY-MM-DD |
| `json` | standard library serialize/parse JSON |
| `members` | list สมาชิกจาก team.json |
| `models` | module คลาสและฟังก์ชันกลาง |
| `owner` | string รหัสสมาชิกที่รับงาน หรือว่าง |
| `parents` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `path` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `pathlib` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `port` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `prefix` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `print` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `priority` | ระดับ high/normal/low |
| `resolve` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `rows` | list ข้อมูลงานจาก storage |
| `run` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `save` | เขียนทั้งรายการงานผ่าน storage |
| `save_daily_hours` | เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `str` | แปลงเป็นข้อความ |
| `sys` | standard library ที่ QA ใช้เพิ่ม root ใน import path |
| `team_data` | อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `tempfile` | standard library สร้างพื้นที่ชั่วคราว |
| `timedelta` | ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง |
| `title` | ชื่องาน/ชื่อหัวข้อขึ้นกับ dict |
| `today` | วันที่ปัจจุบันจากเครื่อง Python |
| `write_text` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
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
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Temporary UI demo at port 5002; never writes the project's task data."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน

### L2

```python
from datetime import date, timedelta
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from datetime import date, timedelta`
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง

### L3

```python
import json
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import json`
- ชื่อที่ต้องรู้: `json` = standard library serialize/parse JSON

### L4

```python
from pathlib import Path
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from pathlib import Path`
- ชื่อที่ต้องรู้: `Path` = pathlib path object ของ script QA

### L5

```python
import sys
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import sys`
- ชื่อที่ต้องรู้: `sys` = standard library ที่ QA ใช้เพิ่ม root ใน import path

### L6

```python
import tempfile
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import tempfile`
- ชื่อที่ต้องรู้: `tempfile` = standard library สร้างพื้นที่ชั่วคราว

### L7

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L8

```python
ROOT = Path(__file__).resolve().parents[2]
```

- เก็บผล `Path(__file__).resolve().parents[2]` (อ่าน key/index) ลง `ROOT`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `ROOT` = root workspace ที่ script QA หาได้; `Path` = pathlib path object ของ script QA

### L9

```python
sys.path.insert(0, str(ROOT))
```

- เรียก `sys.path.insert` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `sys` = standard library ที่ QA ใช้เพิ่ม root ใน import path; `str` = แปลงเป็นข้อความ; `ROOT` = root workspace ที่ script QA หาได้

### L10

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L11

```python
import app
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import app`
- ชื่อที่ต้องรู้: `app` = module Flask router ที่อาจารย์ให้

### L12

```python
import models
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import models`
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง

### L13

```python
import storage
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import storage`
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้

### L14

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L15

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L16

```python
def fixture_task(title, days, estimate, done=0, owner="", priority="normal"):
```

- ประกาศฟังก์ชัน `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `priority` = ระดับ high/normal/low

### L17

```python
    return {"title": title, "course": "วิชาทดสอบระบบ",
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

```python
            "due_date": (date.today() + timedelta(days=days)).isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `+` บวกเลข/ต่อข้อความตามชนิด; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L19

```python
            "estimated_hours": estimate, "done_hours": done, "priority": priority,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `priority` = ระดับ high/normal/low
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L20

```python
            "details": {"owner": owner, "started": done > 0, "subtasks": [],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `{` เปิด dict/set ตามบริบท; `,` คั่นสมาชิก/argument; `>` มากกว่า; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L21

```python
                        "history": [], "created_on": date.today().isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 24 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L22

```python
                        "progress_on": ""}}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set
- ย่อหน้า 24 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L23

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L24

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L25

```python
if __name__ == "__main__":
```

- ตรวจเงื่อนไข: `__name__` เท่ากับ `'__main__'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L26

```python
    with tempfile.TemporaryDirectory(prefix="deadline-ui-") as folder:
```

- ใช้ resource ใน with: เรียก `tempfile.TemporaryDirectory` ด้วย argument ที่แสดงในโค้ด; ออกจาก block แล้วปิด resource ตาม context manager
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `tempfile` = standard library สร้างพื้นที่ชั่วคราว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L27

```python
        storage.DATA_FILE = str(Path(folder) / "data.json")
```

- เก็บผล `str`((เรียก `Path` ด้วย argument ที่แสดงในโค้ด หาร/ต่อ Path `'data.json'`)) ลง `storage.DATA_FILE`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `str` = แปลงเป็นข้อความ; `Path` = pathlib path object ของ script QA
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L28

```python
        storage.SAMPLE_FILE = str(Path(folder) / "sample.json")
```

- เก็บผล `str`((เรียก `Path` ด้วย argument ที่แสดงในโค้ด หาร/ต่อ Path `'sample.json'`)) ลง `storage.SAMPLE_FILE`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `str` = แปลงเป็นข้อความ; `Path` = pathlib path object ของ script QA
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

```python
        models.SETTINGS_FILE = str(Path(folder) / "settings.json")
```

- เก็บผล `str`((เรียก `Path` ด้วย argument ที่แสดงในโค้ด หาร/ต่อ Path `'settings.json'`)) ลง `models.SETTINGS_FILE`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `SETTINGS_FILE` = path ของ planner_settings.json; `str` = แปลงเป็นข้อความ; `Path` = pathlib path object ของ script QA
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L30

```python
        members = models.team_data()["members"]
```

- เก็บผล `models.team_data()['members']` (อ่าน key/index) ลง `members`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L31

```python
        rows = [fixture_task("งานทดสอบเกินกำหนด", -1, 2, 1, members[0]["id"]),
```

- เก็บผล list [เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว] ลง `rows`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `members` = list สมาชิกจาก team.json
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L32

```python
                fixture_task("ออกแบบหน้ารายงานวันนี้", 0, 3, owner=members[1]["id"],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L31: เก็บผล list [เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว] ลง `rows`
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `members` = list สมาชิกจาก team.json
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L33

```python
                             priority="high"),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L31: เก็บผล list [เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว] ลง `rows`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `priority` = ระดับ high/normal/low
- ย่อหน้า 29 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L34

```python
                fixture_task("โครงงานทดสอบภาระสะสม", 1, 18),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L31: เก็บผล list [เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว] ลง `rows`
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L35

```python
                fixture_task("เอกสารที่ทำเสร็จแล้ว", 4, 2, 2, members[2]["id"])]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L31: เก็บผล list [เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว, เรียก `fixture_task`: สร้าง row จำลองตามวันที่วันนี้เพื่อใช้ในเว็บสาธิตข้อมูลชั่วคราว] ลง `rows`
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

```python
        rows[1]["details"]["subtasks"] = [{"title": "ร่างหน้าจอ", "done": False},
```

- เก็บผล list [dict ที่มี key `'title'`, `'done'`, dict ที่มี key `'title'`, `'done'`] ลง `rows[1]['details']['subtasks']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L37

```python
                                          {"title": "ทดสอบบนมือถือ", "done": False}]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L36: เก็บผล list [dict ที่มี key `'title'`, `'done'`, dict ที่มี key `'title'`, `'done'`] ลง `rows[1]['details']['subtasks']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `False` = boolean เท็จ
- ย่อหน้า 42 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L38

```python
        storage.save(rows)
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L39

```python
        Path(storage.SAMPLE_FILE).write_text(json.dumps(rows, ensure_ascii=False),
```

- เรียก `Path(storage.SAMPLE_FILE).write_text` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `Path` = pathlib path object ของ script QA; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `json` = standard library serialize/parse JSON; `dumps` = แปลง object เป็นข้อความ JSON; `rows` = list ข้อมูลงานจาก storage; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L40

```python
                                             encoding="utf-8")
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L39: เรียก `Path(storage.SAMPLE_FILE).write_text` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 45 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
        models.save_daily_hours(4)
```

- เรียก `models.save_daily_hours`: เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L42

```python
        print("UI test data only: http://127.0.0.1:5002/page1")
```

- เรียก `print` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L43

```python
        app.app.run(host="127.0.0.1", port=5002, debug=False)
```

- เรียก `app.app.run` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `app` = module Flask router ที่อาจารย์ให้; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
