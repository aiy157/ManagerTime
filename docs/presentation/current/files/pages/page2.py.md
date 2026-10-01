# pages/page2.py — Python ของหน้าจัดการงาน

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 173 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `074946470958f467465fbb85ca0cdfcc21e39bcd199c09eaa4e7e315a13f4fa6`

**ผู้ศึกษา/บทบาท:** นายไกรวิชญ์ บุ้งทอง · Page 2

## 1. หน้าที่และการเชื่อมต่อ

ตรวจและบันทึกการเพิ่ม แก้ ลบ ชั่วโมงจริง และงานย่อย พร้อมเตรียมประวัติให้หน้า Manage

- **รับเข้า:** ข้อมูลปัจจุบัน สมาชิก form และวันที่เครื่อง
- **ผลลัพธ์:** context ของ page2.html หรือข้อความสำเร็จ/ผิดพลาด; รายการงานที่ผ่านตรวจถูกเขียนด้วย storage.save

**เกี่ยวข้องกับ:** models.overview; models.read_number/read_date; models.row_index/record_history; storage.load/save; templates/page2.html

## 2. ลำดับทำงาน

1. build เตรียม all_items, count, members, today, history, actual_total และ daily_history
2. check ตรวจข้อความ วันที่ เวลา priority และ owner ก่อนสร้าง 7 field
3. save_assignment รักษาประวัติเดิมและบันทึกส่วนต่างเป็น adjustment
4. log_time เพิ่มชั่วโมงจริงของครั้งนั้นและเพิ่มประวัติ work
5. change_subtask เพิ่มหรือติ๊กขั้นตอนโดยไม่เพิ่มชั่วโมง
6. handle แยก action และตรวจ no/version ก่อนแตะรายการเดิม

## 3. จุดที่ต้องอธิบายให้ถูก

- เบราว์เซอร์ช่วยตรวจแต่ Python เป็นด่านที่ห้ามข้าม
- เปลี่ยนวันส่งเป็นอดีตต้อง acknowledge_past=yes; วันส่งเดิมที่ผ่านแล้วแก้ข้อมูลอื่นได้
- delete ลบงานพร้อมงานย่อยและประวัติของงานนั้น ไม่มีถังขยะ
- form มาจาก HTTP เป็นข้อความ; แปลงตัวเลขก่อนใช้
- แก้ยอดสะสมไม่เท่ากับเวลาทำจริงรายวัน; ต้องเลือก log_time สำหรับการทำครั้งใหม่

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q004: Frontend และ Backend ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q004)
- [Q007: ผู้ใช้กดบันทึกแล้วข้อมูลเดินทางอย่างไร?](../../TEACHER_QUESTIONS.md#q007)
- [Q008: build() กับ handle() ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q008)
- [Q009: ทำไมไม่เก็บงานในตัวแปรระดับบนของ page.py?](../../TEACHER_QUESTIONS.md#q009)
- [Q019: ทำไมใช้ form.get แทน form['x']?](../../TEACHER_QUESTIONS.md#q019)
- [Q020: try/except และ None ใช้เพื่ออะไร?](../../TEACHER_QUESTIONS.md#q020)
- [Q030: ทำไมแยก work, adjustment, complete, reopen?](../../TEACHER_QUESTIONS.md#q030)
- [Q041: ฟอร์มเพิ่มงานบังคับข้อมูลใด?](../../TEACHER_QUESTIONS.md#q041)
- [Q042: ตรวจชั่วโมงช่วงเท่าไร?](../../TEACHER_QUESTIONS.md#q042)
- [Q043: ชั่วโมงทั้งหมด ชั่วโมงที่ทำแล้ว และชั่วโมงครั้งนี้ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q043)
- [Q044: เลือกวันส่งอดีตแล้วทำไมยังบันทึกได้?](../../TEACHER_QUESTIONS.md#q044)
- [Q045: ถ้าปิด JavaScript จะข้าม validation ได้หรือไม่?](../../TEACHER_QUESTIONS.md#q045)
- [Q046: ติ๊กงานย่อยแล้ว progress เพิ่มเองหรือไม่?](../../TEACHER_QUESTIONS.md#q046)
- [Q047: งานย่อยมีข้อจำกัดอะไร?](../../TEACHER_QUESTIONS.md#q047)
- [Q050: กดลบงานแล้วประวัติยังอยู่หรือไม่?](../../TEACHER_QUESTIONS.md#q050)
- [Q100: ถ้าอาจารย์ให้เปลี่ยนโจทย์หรือจับ bug สด ควรเริ่มตรงไหน?](../../TEACHER_QUESTIONS.md#q100)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `build` | L10–L20 | ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET |
| `read_hours` | L23–L24 | ประกาศฟังก์ชัน `read_hours`: ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา |
| `check` | L27–L73 | ประกาศฟังก์ชัน `check`: ตรวจข้อมูล form ให้ครบทั้งรูปแบบ ช่วง วันส่ง และเจ้าของ; คืน task,error และรักษา details เดิมเมื่อแก้ |
| `save_assignment` | L76–L103 | ประกาศฟังก์ชัน `save_assignment`: สร้าง task ที่ผ่าน check เพิ่มหรือแทน row และบันทึกส่วนต่าง done เป็น adjustment ก่อน storage.save |
| `log_time` | L106–L119 | ประกาศฟังก์ชัน `log_time`: ตรวจชั่วโมงครั้งนี้ วันที่ไม่ใช่อนาคต และหมายเหตุ เพิ่ม done และ event work ใน row ที่ส่งมา |
| `change_subtask` | L122–L146 | ประกาศฟังก์ชัน `change_subtask`: ตรวจ pending และจำนวน/ชื่อ/index งานย่อย แล้วเพิ่มหรือสลับ done โดยไม่แก้ชั่วโมง |
| `handle` | L149–L173 | ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `PRIORITIES` | dict แปล priority เป็นข้อความไทย |
| `TITLE` | ชื่อหน้าสำหรับเมนูที่ app อ่าน |
| `abs` | ค่าสัมบูรณ์ของส่วนต่าง |
| `action` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `actual_total` | ชั่วโมง work จริงที่มีบันทึกทั้งหมด |
| `append` | เพิ่มหนึ่งรายการต่อท้าย list |
| `build` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `change_subtask` | ตรวจ pending และจำนวน/ชื่อ/index งานย่อย แล้วเพิ่มหรือสลับ done โดยไม่แก้ชั่วโมง |
| `check` | ตรวจข้อมูล form ให้ครบทั้งรูปแบบ ช่วง วันส่ง และเจ้าของ; คืน task,error และรักษา details เดิมเมื่อแก้ |
| `context` | dict ที่คืนให้ template |
| `course` | ชื่อวิชา |
| `daily_history` | รวม history work ต่อ date เป็น hours/count โดยใช้รายการที่เรียงวันที่แล้ว |
| `date` | ชนิดวันที่ระดับวันจาก datetime |
| `datetime` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `delta` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `details` | dict รายละเอียดซ้อนที่สำเนาแล้ว |
| `details_of` | สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ |
| `done` | ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น |
| `due` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `due_text` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `error` | ข้อความข้อผิดพลาดจาก check |
| `estimate` | ชั่วโมงประมาณของงาน |
| `form` | dict ของข้อมูลฟอร์ม POST |
| `get` | อ่านค่า dict พร้อม default เมื่อไม่มี key |
| `handle` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `history` | ประวัติหลายรายการ |
| `hours` | จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน |
| `index` | ตำแหน่งที่ผ่านตรวจขอบเขต |
| `int` | แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress |
| `isascii` | ตรวจอักขระอยู่ใน ASCII |
| `isdigit` | ตรวจว่าเป็นกลุ่มตัวเลข; ใน no ใช้คู่ isascii ป้องกัน unicode digit |
| `isoformat` | แปลง date เป็น YYYY-MM-DD |
| `len` | จำนวนสมาชิก/อักขระ |
| `line` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `lines` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `load_daily_hours` | อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `log_time` | ตรวจชั่วโมงครั้งนี้ วันที่ไม่ใช่อนาคต และหมายเหตุ เพิ่ม done และ event work ใน row ที่ส่งมา |
| `max` | เลือกค่ามากที่สุด |
| `member` | สมาชิกหนึ่งคน |
| `message` | ข้อความคืนให้ app แสดง banner |
| `models` | module คลาสและฟังก์ชันกลาง |
| `name` | ชื่อสมาชิก/ข้อความงานย่อยตามบริบท |
| `note` | หมายเหตุของประวัติ |
| `old_done` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `on_date` | วันที่ทำงานที่ผู้ใช้เลือก |
| `overview` | รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `owner` | string รหัสสมาชิกที่รับงาน หรือว่าง |
| `pop` | ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ |
| `previous` | row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท |
| `priority` | ระดับ high/normal/low |
| `quick_action` | โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน |
| `read_date` | อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None |
| `read_hours` | ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา |
| `read_number` | ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity |
| `record_history` | เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง |
| `remaining` | ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท |
| `round` | ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ |
| `row` | dict ข้อมูลงานหนึ่งรายการ |
| `row_index` | รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None |
| `rows` | list ข้อมูลงานจาก storage |
| `same_past_date` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `save` | เขียนทั้งรายการงานผ่าน storage |
| `save_assignment` | สร้าง task ที่ผ่าน check เพิ่มหรือแทน row และบันทึกส่วนต่าง done เป็น adjustment ก่อน storage.save |
| `splitlines` | แยกข้อความเป็นหลายบรรทัด |
| `startswith` | ตรวจว่าข้อความขึ้นต้นตามที่กำหนด |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `str` | แปลงเป็นข้อความ |
| `strip` | ตัดช่องว่างริมข้อความทั้งสองด้าน |
| `task` | Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน |
| `team_data` | อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `text` | ข้อความก่อนแปลงหรือ serialize |
| `title` | ชื่องาน/ชื่อหัวข้อขึ้นกับ dict |
| `today` | วันที่ปัจจุบันจากเครื่อง Python |
| `valid_owner` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `work_history` | รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
"""Manage assignments, subtasks, and work logs; adapted from catalog/form."""
from datetime import date

import models
import storage

TITLE = "จัดการงาน"


def build():
    context = models.overview(storage.load(), models.load_daily_hours())
    context["items"] = context["all_items"]
    context["count"] = len(context["items"])
    context["members"] = models.team_data()["members"]
    context["today"] = date.today().isoformat()
    history, actual_total = models.work_history(context["items"])
    context["history"] = history
    context["actual_total"] = actual_total
    context["daily_history"] = models.daily_history(history)
    return context


def read_hours(text):
    return models.read_number(text)


def check(form, previous=None):
    title = str(form.get("title", "") or "").strip()
    course = str(form.get("course", "") or "").strip()
    due_text = str(form.get("due_date", "") or "")
    due = models.read_date(due_text)
    estimate = read_hours(form.get("estimated_hours", ""))
    done = read_hours(form.get("done_hours", "0"))
    priority = form.get("priority", "normal")
    owner = form.get("owner", "")
    if title == "" or course == "":
        return None, "กรุณากรอกชื่องานและวิชา"
    if len(title) > 80 or len(course) > 40:
        return None, "ชื่องานไม่เกิน 80 และวิชาไม่เกิน 40 ตัวอักษร"
    if due is None:
        return None, "กรุณาเลือกวันส่งที่ถูกต้อง"
    if estimate is None or estimate < 0.1 or estimate > 200:
        return None, "เวลาที่คาดว่าจะใช้ทั้งหมดต้องตั้งแต่ 0.1 ถึง 200 ชั่วโมง"
    if done is None or done < 0 or done > estimate:
        return None, "เวลาที่ทำแล้วต้องตั้งแต่ 0 ถึงเวลาทั้งหมด"
    if priority not in models.PRIORITIES:
        return None, "กรุณาเลือกระดับความสำคัญที่มีในรายการ"
    valid_owner = owner == ""
    for member in models.team_data()["members"]:
        if member["id"] == owner:
            valid_owner = True
    if not valid_owner:
        return None, "ไม่พบสมาชิกที่รับผิดชอบ"
    same_past_date = previous is not None and previous["due_date"] == due_text
    if due < date.today() and not same_past_date and form.get("acknowledge_past") != "yes":
        return None, "วันส่งผ่านไปแล้ว หากต้องการติดตามงานค้าง ให้ยืนยันบันทึกงานเกินกำหนด"
    details = {"owner": owner, "started": done > 0, "subtasks": [],
               "history": [], "created_on": date.today().isoformat(),
               "progress_on": ""}
    if previous is not None:
        details = models.details_of(previous)
        details["owner"] = owner
    else:
        lines = str(form.get("subtasks", "") or "").splitlines()
        for line in lines:
            name = line.strip()
            if name:
                if len(name) > 100 or len(details["subtasks"]) >= 30:
                    return None, "งานย่อยไม่เกิน 30 รายการ ชื่อแต่ละรายการไม่เกิน 100 ตัวอักษร"
                details["subtasks"].append({"title": name, "done": False})
    return {"title": title, "course": course, "due_date": due_text,
            "estimated_hours": round(estimate, 2), "done_hours": round(done, 2),
            "priority": priority, "details": details}, ""


def save_assignment(form, rows, index=None):
    previous = None
    if index is not None:
        previous = rows[index]
    task, error = check(form, previous)
    if error:
        return "✗ " + error
    old_done = 0
    if previous is not None:
        old_done = previous["done_hours"]
    delta = task["done_hours"] - old_done
    if abs(delta) > 0.000000001:
        models.record_history(task, delta, "adjustment", date.today().isoformat(),
                              "ปรับยอดชั่วโมงที่ทำแล้ว ไม่ใช่รายการบันทึกเวลารายวัน")
    if task["done_hours"] < task["estimated_hours"]:
        task["details"].pop("completed_on", None)
        task["details"].pop("before_complete", None)
        task["details"].pop("subtasks_before_complete", None)
    if index is None:
        rows.append(task)
        message = "✓ เพิ่มงานแล้ว"
    else:
        rows[index] = task
        message = "✓ บันทึกการแก้ไขแล้ว"
    storage.save(rows)
    if task["due_date"] < date.today().isoformat():
        message = message + " · งานนี้เกินกำหนด ควรตรวจแผนและติดต่อผู้สอน"
    return message


def log_time(form, row):
    hours = read_hours(form.get("hours", ""))
    on_date = models.read_date(form.get("work_date", ""))
    note = str(form.get("note", "") or "").strip()
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
    if hours is None or hours < 0.1 or hours > remaining:
        return "✗ ชั่วโมงที่บันทึกต้องตั้งแต่ 0.1 และไม่เกินชั่วโมงที่เหลือ"
    if on_date is None or on_date > date.today():
        return "✗ วันที่ทำงานต้องเป็นวันที่ถูกต้องและไม่ใช่อนาคต"
    if len(note) > 120:
        return "✗ หมายเหตุไม่เกิน 120 ตัวอักษร"
    row["done_hours"] = round(row["done_hours"] + hours, 2)
    models.record_history(row, hours, "work", on_date.isoformat(), note)
    return "✓ บันทึกเวลาทำงานจริงแล้ว"


def change_subtask(form, row):
    details = models.details_of(row)
    if row["done_hours"] >= row["estimated_hours"]:
        return "✗ เปิดงานกลับมาทำต่อก่อนแก้ไขงานย่อย"
    if form.get("action", "") == "add_subtask":
        name = str(form.get("subtask_title", "") or "").strip()
        if name == "" or len(name) > 100:
            return "✗ ชื่องานย่อยต้องมี 1 ถึง 100 ตัวอักษร"
        if len(details["subtasks"]) >= 30:
            return "✗ งานย่อยเต็ม 30 รายการแล้ว"
        details["subtasks"].append({"title": name, "done": False})
        message = "✓ เพิ่มงานย่อยแล้ว"
    else:
        text = str(form.get("subtask_no", ""))
        if not text.isascii() or not text.isdigit() or len(text) > 3:
            return "✗ ไม่พบงานย่อยนี้"
        index = int(text)
        if index >= len(details["subtasks"]):
            return "✗ ไม่พบงานย่อยนี้"
        details["subtasks"][index]["done"] = not details["subtasks"][index]["done"]
        details["started"] = True
        details["progress_on"] = date.today().isoformat()
        message = "✓ อัปเดตงานย่อยแล้ว · บันทึกชั่วโมงแยกเพื่อปรับความคืบหน้า"
    row["details"] = details
    return message


def handle(form):
    action = form.get("action", "")
    if action in ("start", "complete", "reopen"):
        return models.quick_action(form)
    if action not in ("add", "update", "delete", "log_time", "add_subtask", "toggle_subtask"):
        return "✗ ไม่รู้จักคำสั่ง"
    rows = storage.load()
    if action == "add":
        return save_assignment(form, rows)
    index = models.row_index(form, rows)
    if index is None:
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
    if action == "update":
        return save_assignment(form, rows, index)
    if action == "delete":
        rows.pop(index)
        storage.save(rows)
        return "✓ ลบงานและประวัติของงานนี้แล้ว"
    if action == "log_time":
        message = log_time(form, rows[index])
    else:
        message = change_subtask(form, rows[index])
    if message.startswith("✓"):
        storage.save(rows)
    return message
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Manage assignments, subtasks, and work logs; adapted from catalog/form."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน

### L2

```python
from datetime import date
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from datetime import date`
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime

### L3

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L4

```python
import models
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import models`
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง

### L5

```python
import storage
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import storage`
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้

### L6

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L7

```python
TITLE = "จัดการงาน"
```

- เก็บผล `'จัดการงาน'` ลง `TITLE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `TITLE` = ชื่อหน้าสำหรับเมนูที่ app อ่าน

### L8

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L9

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L10

```python
def build():
```

- ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L11

```python
    context = models.overview(storage.load(), models.load_daily_hours())
```

- เก็บผล เรียก `models.overview`: รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ ลง `context`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L12

```python
    context["items"] = context["all_items"]
```

- เก็บผล `context['all_items']` (อ่าน key/index) ลง `context['items']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L13

```python
    context["count"] = len(context["items"])
```

- เก็บผล `len`(`context['items']` (อ่าน key/index)) ลง `context['count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L14

```python
    context["members"] = models.team_data()["members"]
```

- เก็บผล `models.team_data()['members']` (อ่าน key/index) ลง `context['members']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L15

```python
    context["today"] = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `context['today']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L16

```python
    history, actual_total = models.work_history(context["items"])
```

- เก็บผล เรียก `models.work_history`: รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work ลง `(history, actual_total)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ; `actual_total` = ชั่วโมง work จริงที่มีบันทึกทั้งหมด; `models` = module คลาสและฟังก์ชันกลาง; `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L17

```python
    context["history"] = history
```

- เก็บผล `history` ลง `context['history']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

```python
    context["actual_total"] = actual_total
```

- เก็บผล `actual_total` ลง `context['actual_total']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `actual_total` = ชั่วโมง work จริงที่มีบันทึกทั้งหมด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L19

```python
    context["daily_history"] = models.daily_history(history)
```

- เก็บผล เรียก `models.daily_history`: รวม history work ต่อ date เป็น hours/count โดยใช้รายการที่เรียงวันที่แล้ว ลง `context['daily_history']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง; `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L20

```python
    return context
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `context`
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L21

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L22

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L23

```python
def read_hours(text):
```

- ประกาศฟังก์ชัน `read_hours`: ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize

### L24

```python
    return models.read_number(text)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `models.read_number`: ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L25

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L26

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L27

```python
def check(form, previous=None):
```

- ประกาศฟังก์ชัน `check`: ตรวจข้อมูล form ให้ครบทั้งรูปแบบ ช่วง วันส่ง และเจ้าของ; คืน task,error และรักษา details เดิมเมื่อแก้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง

### L28

```python
    title = str(form.get("title", "") or "").strip()
```

- เก็บผล เรียก `str(form.get('title', '') or '').strip` ด้วย argument ที่แสดงในโค้ด ลง `title`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

```python
    course = str(form.get("course", "") or "").strip()
```

- เก็บผล เรียก `str(form.get('course', '') or '').strip` ด้วย argument ที่แสดงในโค้ด ลง `course`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `course` = ชื่อวิชา; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L30

```python
    due_text = str(form.get("due_date", "") or "")
```

- เก็บผล `str`(อ่าน `'due_date'` จาก `form` พร้อม default เมื่อไม่มี หรือ `''`) ลง `due_text`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L31

```python
    due = models.read_date(due_text)
```

- เก็บผล เรียก `models.read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None ลง `due`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L32

```python
    estimate = read_hours(form.get("estimated_hours", ""))
```

- เก็บผล เรียก `read_hours`: ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา ลง `estimate`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `estimate` = ชั่วโมงประมาณของงาน; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L33

```python
    done = read_hours(form.get("done_hours", "0"))
```

- เก็บผล เรียก `read_hours`: ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา ลง `done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L34

```python
    priority = form.get("priority", "normal")
```

- เก็บผล อ่าน `'priority'` จาก `form` พร้อม default เมื่อไม่มี ลง `priority`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `priority` = ระดับ high/normal/low; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L35

```python
    owner = form.get("owner", "")
```

- เก็บผล อ่าน `'owner'` จาก `form` พร้อม default เมื่อไม่มี ลง `owner`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

```python
    if title == "" or course == "":
```

- ตรวจเงื่อนไข: `title` เท่ากับ `''` หรือ `course` เท่ากับ `''`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `course` = ชื่อวิชา
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L37

```python
        return None, "กรุณากรอกชื่องานและวิชา"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'กรุณากรอกชื่องานและวิชา'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L38

```python
    if len(title) > 80 or len(course) > 40:
```

- ตรวจเงื่อนไข: `len`(`title`) มากกว่า `80` หรือ `len`(`course`) มากกว่า `40`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `course` = ชื่อวิชา
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L39

```python
        return None, "ชื่องานไม่เกิน 80 และวิชาไม่เกิน 40 ตัวอักษร"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'ชื่องานไม่เกิน 80 และวิชาไม่เกิน 40 ตัวอักษร'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L40

```python
    if due is None:
```

- ตรวจเงื่อนไข: `due` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
        return None, "กรุณาเลือกวันส่งที่ถูกต้อง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'กรุณาเลือกวันส่งที่ถูกต้อง'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L42

```python
    if estimate is None or estimate < 0.1 or estimate > 200:
```

- ตรวจเงื่อนไข: `estimate` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) หรือ `estimate` น้อยกว่า `0.1` หรือ `estimate` มากกว่า `200`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `estimate` = ชั่วโมงประมาณของงาน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L43

```python
        return None, "เวลาที่คาดว่าจะใช้ทั้งหมดต้องตั้งแต่ 0.1 ถึง 200 ชั่วโมง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'เวลาที่คาดว่าจะใช้ทั้งหมดต้องตั้งแต่ 0.1 ถึง 200 ชั่วโมง'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L44

```python
    if done is None or done < 0 or done > estimate:
```

- ตรวจเงื่อนไข: `done` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) หรือ `done` น้อยกว่า `0` หรือ `done` มากกว่า `estimate`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง; `estimate` = ชั่วโมงประมาณของงาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L45

```python
        return None, "เวลาที่ทำแล้วต้องตั้งแต่ 0 ถึงเวลาทั้งหมด"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'เวลาที่ทำแล้วต้องตั้งแต่ 0 ถึงเวลาทั้งหมด'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L46

```python
    if priority not in models.PRIORITIES:
```

- ตรวจเงื่อนไข: `priority` ไม่อยู่ใน `models.PRIORITIES`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `priority` = ระดับ high/normal/low; `models` = module คลาสและฟังก์ชันกลาง; `PRIORITIES` = dict แปล priority เป็นข้อความไทย
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L47

```python
        return None, "กรุณาเลือกระดับความสำคัญที่มีในรายการ"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'กรุณาเลือกระดับความสำคัญที่มีในรายการ'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L48

```python
    valid_owner = owner == ""
```

- เก็บผล `owner` เท่ากับ `''` ลง `valid_owner`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L49

```python
    for member in models.team_data()["members"]:
```

- วน `models.team_data()['members']` (อ่าน key/index) ให้ `member` รับสมาชิกทีละรอบ
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L50

```python
        if member["id"] == owner:
```

- ตรวจเงื่อนไข: `member['id']` (อ่าน key/index) เท่ากับ `owner`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L51

```python
            valid_owner = True
```

- เก็บผล `True` ลง `valid_owner`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `True` = boolean จริง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L52

```python
    if not valid_owner:
```

- ตรวจเงื่อนไข: ไม่เป็นจริง: `valid_owner`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L53

```python
        return None, "ไม่พบสมาชิกที่รับผิดชอบ"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'ไม่พบสมาชิกที่รับผิดชอบ'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L54

```python
    same_past_date = previous is not None and previous["due_date"] == due_text
```

- เก็บผล `previous` ไม่เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) และ `previous['due_date']` (อ่าน key/index) เท่ากับ `due_text` ลง `same_past_date`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L55

```python
    if due < date.today() and not same_past_date and form.get("acknowledge_past") != "yes":
```

- ตรวจเงื่อนไข: `due` น้อยกว่า เรียก `date.today` ด้วย argument ที่แสดงในโค้ด และ ไม่เป็นจริง: `same_past_date` และ อ่าน `'acknowledge_past'` จาก `form` พร้อม default เมื่อไม่มี ไม่เท่ากับ `'yes'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `!=` เปรียบเทียบไม่เท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L56

```python
        return None, "วันส่งผ่านไปแล้ว หากต้องการติดตามงานค้าง ให้ยืนยันบันทึกงานเกินกำหนด"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'วันส่งผ่านไปแล้ว หากต้องการติดตามงานค้าง ให้ยืนยันบันทึกงานเกินกำหนด'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L57

```python
    details = {"owner": owner, "started": done > 0, "subtasks": [],
```

- เก็บผล dict ที่มี key `'owner'`, `'started'`, `'subtasks'`, `'history'`, `'created_on'`, `'progress_on'` ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `>` มากกว่า; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L58

```python
               "history": [], "created_on": date.today().isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L57: เก็บผล dict ที่มี key `'owner'`, `'started'`, `'subtasks'`, `'history'`, `'created_on'`, `'progress_on'` ลง `details`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 15 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L59

```python
               "progress_on": ""}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L57: เก็บผล dict ที่มี key `'owner'`, `'started'`, `'subtasks'`, `'history'`, `'created_on'`, `'progress_on'` ลง `details`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set
- ย่อหน้า 15 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L60

```python
    if previous is not None:
```

- ตรวจเงื่อนไข: `previous` ไม่เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L61

```python
        details = models.details_of(previous)
```

- เก็บผล เรียก `models.details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `models` = module คลาสและฟังก์ชันกลาง; `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L62

```python
        details["owner"] = owner
```

- เก็บผล `owner` ลง `details['owner']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L63

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L64

```python
        lines = str(form.get("subtasks", "") or "").splitlines()
```

- เก็บผล เรียก `str(form.get('subtasks', '') or '').splitlines` ด้วย argument ที่แสดงในโค้ด ลง `lines`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `splitlines` = แยกข้อความเป็นหลายบรรทัด
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L65

```python
        for line in lines:
```

- วน `lines` ให้ `line` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L66

```python
            name = line.strip()
```

- เก็บผล เรียก `line.strip` ด้วย argument ที่แสดงในโค้ด ลง `name`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L67

```python
            if name:
```

- ตรวจเงื่อนไข: `name`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L68

```python
                if len(name) > 100 or len(details["subtasks"]) >= 30:
```

- ตรวจเงื่อนไข: `len`(`name`) มากกว่า `100` หรือ `len`(`details['subtasks']` (อ่าน key/index)) อย่างน้อย `30`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L69

```python
                    return None, "งานย่อยไม่เกิน 30 รายการ ชื่อแต่ละรายการไม่เกิน 100 ตัวอักษร"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [None (ไม่มีค่าที่ใช้ได้), `'งานย่อยไม่เกิน 30 รายการ ชื่อแต่ละรายการไม่เกิน 100 ตัวอักษร'`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 20 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L70

```python
                details["subtasks"].append({"title": name, "done": False})
```

- เพิ่ม dict ที่มี key `'title'`, `'done'` ไปท้าย `details['subtasks']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `False` = boolean เท็จ
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L71

```python
    return {"title": title, "course": course, "due_date": due_text,
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`, `''`]
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `course` = ชื่อวิชา
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L72

```python
            "estimated_hours": round(estimate, 2), "done_hours": round(done, 2),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L71: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`, `''`]
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L73

```python
            "priority": priority, "details": details}, ""
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L71: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`, `''`]
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `priority` = ระดับ high/normal/low; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L74

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L75

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L76

```python
def save_assignment(form, rows, index=None):
```

- ประกาศฟังก์ชัน `save_assignment`: สร้าง task ที่ผ่าน check เพิ่มหรือแทน row และบันทึกส่วนต่าง done เป็น adjustment ก่อน storage.save
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง

### L77

```python
    previous = None
```

- เก็บผล None (ไม่มีค่าที่ใช้ได้) ลง `previous`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L78

```python
    if index is not None:
```

- ตรวจเงื่อนไข: `index` ไม่เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L79

```python
        previous = rows[index]
```

- เก็บผล `rows[index]` (อ่าน key/index) ลง `previous`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L80

```python
    task, error = check(form, previous)
```

- เก็บผล เรียก `check`: ตรวจข้อมูล form ให้ครบทั้งรูปแบบ ช่วง วันส่ง และเจ้าของ; คืน task,error และรักษา details เดิมเมื่อแก้ ลง `(task, error)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `error` = ข้อความข้อผิดพลาดจาก check; `form` = dict ของข้อมูลฟอร์ม POST; `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L81

```python
    if error:
```

- ตรวจเงื่อนไข: `error`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `error` = ข้อความข้อผิดพลาดจาก check
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L82

```python
        return "✗ " + error
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: (`'✗ '` บวก/ต่อ `error`)
- เครื่องหมาย: `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `error` = ข้อความข้อผิดพลาดจาก check
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L83

```python
    old_done = 0
```

- เก็บผล `0` ลง `old_done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L84

```python
    if previous is not None:
```

- ตรวจเงื่อนไข: `previous` ไม่เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L85

```python
        old_done = previous["done_hours"]
```

- เก็บผล `previous['done_hours']` (อ่าน key/index) ลง `old_done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L86

```python
    delta = task["done_hours"] - old_done
```

- เก็บผล (`task['done_hours']` (อ่าน key/index) ลบ `old_done`) ลง `delta`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `-` ลบ/เครื่องหมายติดลบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L87

```python
    if abs(delta) > 0.000000001:
```

- ตรวจเงื่อนไข: `abs`(`delta`) มากกว่า `1e-09`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `abs` = ค่าสัมบูรณ์ของส่วนต่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L88

```python
        models.record_history(task, delta, "adjustment", date.today().isoformat(),
```

- เรียก `models.record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L89

```python
                              "ปรับยอดชั่วโมงที่ทำแล้ว ไม่ใช่รายการบันทึกเวลารายวัน")
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L88: เรียก `models.record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 30 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L90

```python
    if task["done_hours"] < task["estimated_hours"]:
```

- ตรวจเงื่อนไข: `task['done_hours']` (อ่าน key/index) น้อยกว่า `task['estimated_hours']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L91

```python
        task["details"].pop("completed_on", None)
```

- เอาสมาชิก/key ออกจาก `task['details']` (อ่าน key/index) ตาม argument ในโค้ด
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L92

```python
        task["details"].pop("before_complete", None)
```

- เอาสมาชิก/key ออกจาก `task['details']` (อ่าน key/index) ตาม argument ในโค้ด
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L93

```python
        task["details"].pop("subtasks_before_complete", None)
```

- เอาสมาชิก/key ออกจาก `task['details']` (อ่าน key/index) ตาม argument ในโค้ด
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L94

```python
    if index is None:
```

- ตรวจเงื่อนไข: `index` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L95

```python
        rows.append(task)
```

- เพิ่ม `task` ไปท้าย `rows`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L96

```python
        message = "✓ เพิ่มงานแล้ว"
```

- เก็บผล `'✓ เพิ่มงานแล้ว'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L97

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L98

```python
        rows[index] = task
```

- เก็บผล `task` ลง `rows[index]`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L99

```python
        message = "✓ บันทึกการแก้ไขแล้ว"
```

- เก็บผล `'✓ บันทึกการแก้ไขแล้ว'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L100

```python
    storage.save(rows)
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L101

```python
    if task["due_date"] < date.today().isoformat():
```

- ตรวจเงื่อนไข: `task['due_date']` (อ่าน key/index) น้อยกว่า เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L102

```python
        message = message + " · งานนี้เกินกำหนด ควรตรวจแผนและติดต่อผู้สอน"
```

- เก็บผล (`message` บวก/ต่อ `' · งานนี้เกินกำหนด ควรตรวจแผนและติดต่อผู้สอน'`) ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L103

```python
    return message
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `message`
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L104

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L105

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L106

```python
def log_time(form, row):
```

- ประกาศฟังก์ชัน `log_time`: ตรวจชั่วโมงครั้งนี้ วันที่ไม่ใช่อนาคต และหมายเหตุ เพิ่ม done และ event work ใน row ที่ส่งมา
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ

### L107

```python
    hours = read_hours(form.get("hours", ""))
```

- เก็บผล เรียก `read_hours`: ส่งต่อไป models.read_number เพื่อไม่ทำ validation ตัวเลขคนละกติกา ลง `hours`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L108

```python
    on_date = models.read_date(form.get("work_date", ""))
```

- เก็บผล เรียก `models.read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None ลง `on_date`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `on_date` = วันที่ทำงานที่ผู้ใช้เลือก; `models` = module คลาสและฟังก์ชันกลาง; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L109

```python
    note = str(form.get("note", "") or "").strip()
```

- เก็บผล เรียก `str(form.get('note', '') or '').strip` ด้วย argument ที่แสดงในโค้ด ลง `note`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `note` = หมายเหตุของประวัติ; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L110

```python
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
```

- เก็บผล `max`(`0`, (`row['estimated_hours']` (อ่าน key/index) ลบ `row['done_hours']` (อ่าน key/index))) ลง `remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `max` = เลือกค่ามากที่สุด; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L111

```python
    if hours is None or hours < 0.1 or hours > remaining:
```

- ตรวจเงื่อนไข: `hours` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) หรือ `hours` น้อยกว่า `0.1` หรือ `hours` มากกว่า `remaining`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง; `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L112

```python
        return "✗ ชั่วโมงที่บันทึกต้องตั้งแต่ 0.1 และไม่เกินชั่วโมงที่เหลือ"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ชั่วโมงที่บันทึกต้องตั้งแต่ 0.1 และไม่เกินชั่วโมงที่เหลือ'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L113

```python
    if on_date is None or on_date > date.today():
```

- ตรวจเงื่อนไข: `on_date` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) หรือ `on_date` มากกว่า เรียก `date.today` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>` มากกว่า; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `on_date` = วันที่ทำงานที่ผู้ใช้เลือก; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L114

```python
        return "✗ วันที่ทำงานต้องเป็นวันที่ถูกต้องและไม่ใช่อนาคต"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ วันที่ทำงานต้องเป็นวันที่ถูกต้องและไม่ใช่อนาคต'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L115

```python
    if len(note) > 120:
```

- ตรวจเงื่อนไข: `len`(`note`) มากกว่า `120`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `note` = หมายเหตุของประวัติ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L116

```python
        return "✗ หมายเหตุไม่เกิน 120 ตัวอักษร"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ หมายเหตุไม่เกิน 120 ตัวอักษร'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L117

```python
    row["done_hours"] = round(row["done_hours"] + hours, 2)
```

- เก็บผล `round`((`row['done_hours']` (อ่าน key/index) บวก/ต่อ `hours`), `2`) ลง `row['done_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `+` บวกเลข/ต่อข้อความตามชนิด; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L118

```python
    models.record_history(row, hours, "work", on_date.isoformat(), note)
```

- เรียก `models.record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `row` = dict ข้อมูลงานหนึ่งรายการ; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `on_date` = วันที่ทำงานที่ผู้ใช้เลือก; `isoformat` = แปลง date เป็น YYYY-MM-DD; `note` = หมายเหตุของประวัติ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L119

```python
    return "✓ บันทึกเวลาทำงานจริงแล้ว"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✓ บันทึกเวลาทำงานจริงแล้ว'`
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L120

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L121

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L122

```python
def change_subtask(form, row):
```

- ประกาศฟังก์ชัน `change_subtask`: ตรวจ pending และจำนวน/ชื่อ/index งานย่อย แล้วเพิ่มหรือสลับ done โดยไม่แก้ชั่วโมง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ

### L123

```python
    details = models.details_of(row)
```

- เก็บผล เรียก `models.details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `models` = module คลาสและฟังก์ชันกลาง; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L124

```python
    if row["done_hours"] >= row["estimated_hours"]:
```

- ตรวจเงื่อนไข: `row['done_hours']` (อ่าน key/index) อย่างน้อย `row['estimated_hours']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L125

```python
        return "✗ เปิดงานกลับมาทำต่อก่อนแก้ไขงานย่อย"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ เปิดงานกลับมาทำต่อก่อนแก้ไขงานย่อย'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L126

```python
    if form.get("action", "") == "add_subtask":
```

- ตรวจเงื่อนไข: อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี เท่ากับ `'add_subtask'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L127

```python
        name = str(form.get("subtask_title", "") or "").strip()
```

- เก็บผล เรียก `str(form.get('subtask_title', '') or '').strip` ด้วย argument ที่แสดงในโค้ด ลง `name`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L128

```python
        if name == "" or len(name) > 100:
```

- ตรวจเงื่อนไข: `name` เท่ากับ `''` หรือ `len`(`name`) มากกว่า `100`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L129

```python
            return "✗ ชื่องานย่อยต้องมี 1 ถึง 100 ตัวอักษร"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ชื่องานย่อยต้องมี 1 ถึง 100 ตัวอักษร'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L130

```python
        if len(details["subtasks"]) >= 30:
```

- ตรวจเงื่อนไข: `len`(`details['subtasks']` (อ่าน key/index)) อย่างน้อย `30`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L131

```python
            return "✗ งานย่อยเต็ม 30 รายการแล้ว"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ งานย่อยเต็ม 30 รายการแล้ว'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L132

```python
        details["subtasks"].append({"title": name, "done": False})
```

- เพิ่ม dict ที่มี key `'title'`, `'done'` ไปท้าย `details['subtasks']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L133

```python
        message = "✓ เพิ่มงานย่อยแล้ว"
```

- เก็บผล `'✓ เพิ่มงานย่อยแล้ว'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L134

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L135

```python
        text = str(form.get("subtask_no", ""))
```

- เก็บผล `str`(อ่าน `'subtask_no'` จาก `form` พร้อม default เมื่อไม่มี) ลง `text`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L136

```python
        if not text.isascii() or not text.isdigit() or len(text) > 3:
```

- ตรวจเงื่อนไข: ไม่เป็นจริง: เรียก `text.isascii` ด้วย argument ที่แสดงในโค้ด หรือ ไม่เป็นจริง: เรียก `text.isdigit` ด้วย argument ที่แสดงในโค้ด หรือ `len`(`text`) มากกว่า `3`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize; `isascii` = ตรวจอักขระอยู่ใน ASCII; `isdigit` = ตรวจว่าเป็นกลุ่มตัวเลข; ใน no ใช้คู่ isascii ป้องกัน unicode digit; `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L137

```python
            return "✗ ไม่พบงานย่อยนี้"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่พบงานย่อยนี้'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L138

```python
        index = int(text)
```

- เก็บผล `int`(`text`) ลง `index`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `int` = แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L139

```python
        if index >= len(details["subtasks"]):
```

- ตรวจเงื่อนไข: `index` อย่างน้อย `len`(`details['subtasks']` (อ่าน key/index)); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>=` มากกว่าหรือเท่ากับ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `len` = จำนวนสมาชิก/อักขระ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L140

```python
            return "✗ ไม่พบงานย่อยนี้"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่พบงานย่อยนี้'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L141

```python
        details["subtasks"][index]["done"] = not details["subtasks"][index]["done"]
```

- เก็บผล ไม่เป็นจริง: `details['subtasks'][index]['done']` (อ่าน key/index) ลง `details['subtasks'][index]['done']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L142

```python
        details["started"] = True
```

- เก็บผล `True` ลง `details['started']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `True` = boolean จริง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L143

```python
        details["progress_on"] = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `details['progress_on']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L144

```python
        message = "✓ อัปเดตงานย่อยแล้ว · บันทึกชั่วโมงแยกเพื่อปรับความคืบหน้า"
```

- เก็บผล `'✓ อัปเดตงานย่อยแล้ว · บันทึกชั่วโมงแยกเพื่อปรับความคืบหน้า'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L145

```python
    row["details"] = details
```

- เก็บผล `details` ลง `row['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L146

```python
    return message
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `message`
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L147

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L148

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L149

```python
def handle(form):
```

- ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST

### L150

```python
    action = form.get("action", "")
```

- เก็บผล อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี ลง `action`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L151

```python
    if action in ("start", "complete", "reopen"):
```

- ตรวจเงื่อนไข: `action` อยู่ใน tuple [`'start'`, `'complete'`, `'reopen'`]; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L152

```python
        return models.quick_action(form)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `models.quick_action`: โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L153

```python
    if action not in ("add", "update", "delete", "log_time", "add_subtask", "toggle_subtask"):
```

- ตรวจเงื่อนไข: `action` ไม่อยู่ใน tuple จำนวน 6 สมาชิกตามโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L154

```python
        return "✗ ไม่รู้จักคำสั่ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่รู้จักคำสั่ง'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L155

```python
    rows = storage.load()
```

- เก็บผล อ่านรายการงานล่าสุดผ่าน storage.load() ลง `rows`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L156

```python
    if action == "add":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'add'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L157

```python
        return save_assignment(form, rows)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `save_assignment`: สร้าง task ที่ผ่าน check เพิ่มหรือแทน row และบันทึกส่วนต่าง done เป็น adjustment ก่อน storage.save
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L158

```python
    index = models.row_index(form, rows)
```

- เก็บผล เรียก `models.row_index`: รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None ลง `index`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `models` = module คลาสและฟังก์ชันกลาง; `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L159

```python
    if index is None:
```

- ตรวจเงื่อนไข: `index` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L160

```python
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L161

```python
    if action == "update":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'update'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L162

```python
        return save_assignment(form, rows, index)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `save_assignment`: สร้าง task ที่ผ่าน check เพิ่มหรือแทน row และบันทึกส่วนต่าง done เป็น adjustment ก่อน storage.save
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L163

```python
    if action == "delete":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'delete'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L164

```python
        rows.pop(index)
```

- เอาสมาชิก/key ออกจาก `rows` ตาม argument ในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L165

```python
        storage.save(rows)
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L166

```python
        return "✓ ลบงานและประวัติของงานนี้แล้ว"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✓ ลบงานและประวัติของงานนี้แล้ว'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L167

```python
    if action == "log_time":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'log_time'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L168

```python
        message = log_time(form, rows[index])
```

- เก็บผล เรียก `log_time`: ตรวจชั่วโมงครั้งนี้ วันที่ไม่ใช่อนาคต และหมายเหตุ เพิ่ม done และ event work ใน row ที่ส่งมา ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner; `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L169

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L170

```python
        message = change_subtask(form, rows[index])
```

- เก็บผล เรียก `change_subtask`: ตรวจ pending และจำนวน/ชื่อ/index งานย่อย แล้วเพิ่มหรือสลับ done โดยไม่แก้ชั่วโมง ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner; `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L171

```python
    if message.startswith("✓"):
```

- ตรวจเงื่อนไข: เรียก `message.startswith` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L172

```python
        storage.save(rows)
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L173

```python
    return message
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `message`
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
