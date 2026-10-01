# pages/team.py — Python ของหน้าทีม

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 64 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `29d6c2d3dd3196c6aa1b37c57d1f41233314f6614028a8a0d9add6830bdef82a`

**ผู้ศึกษา/บทบาท:** ทีม CodeMind · อ่านข้อมูลบทบาทจริงจาก team.json

## 1. หน้าที่และการเชื่อมต่อ

รวมงานของสมาชิกตาม owner และตรวจงานไม่มอบหมาย/ภาระงานมาก

- **รับเข้า:** team.json, data.json และเกณฑ์ชั่วโมงเดียวที่ตั้งใน Plan
- **ผลลัพธ์:** group, members ที่เติมสถิติ, count, unassigned, daily_hours และ weekly_capacity

**เกี่ยวข้องกับ:** models.team_data/all_views/annotate_plan; storage.load; templates/team.html

## 2. ลำดับทำงาน

1. initial_of ตัดคำนำหน้าที่รู้จักและดึงอักขระแรก
2. member_summary คัดงานที่ owner ตรง id
3. รวมชั่วโมงและคำนวณ progress แบบถ่วงตาม estimated_hours
4. ตรวจความเสี่ยงเฉพาะงานคนนั้นและเทียบงบ 7 วัน
5. build วนทุกคนและคัด pending ที่ไม่รู้จัก owner

## 3. จุดที่ต้องอธิบายให้ถูก

- เกณฑ์รายวันเดียวกันใช้กับทุกคน ยังไม่มีตารางว่างรายคน
- ความคืบหน้าเป็นยอดชั่วโมงประมาณ/ทำแล้ว ไม่ใช่การประเมินคุณภาพหรือคะแนนสมาชิก
- member_summary คืน assignments ทั้งเสร็จและค้าง; unassigned นับเฉพาะค้าง
- own_tasks เป็นค่ารับกลับจาก annotate_plan ที่ไม่ได้ใช้ต่อ; risks ใช้ตัดสิน overloaded

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q002: กลุ่มเป้าหมายคือใคร?](../../TEACHER_QUESTIONS.md#q002)
- [Q016: for กับ while ใช้ตรงไหน?](../../TEACHER_QUESTIONS.md#q016)
- [Q086: Team นับจำนวนงานอย่างไร?](../../TEACHER_QUESTIONS.md#q086)
- [Q087: Team คำนวณ progress ของสมาชิกอย่างไร?](../../TEACHER_QUESTIONS.md#q087)
- [Q088: ตัวอย่างงาน 2 ชม. เสร็จและงาน 8 ชม. ยังไม่เริ่ม progress เท่าไร?](../../TEACHER_QUESTIONS.md#q088)
- [Q089: อะไรทำให้ขึ้นควรช่วยแบ่งงาน?](../../TEACHER_QUESTIONS.md#q089)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `initial_of` | L9–L16 | ประกาศฟังก์ชัน `initial_of`: ตัดคำนำหน้าชื่อที่รู้จักและคืนอักขระแรก หรือ ? หากชื่อว่าง; ไม่ยืนยันตัวตน |
| `member_summary` | L19–L46 | ประกาศฟังก์ชัน `member_summary`: คัดงานของ member รวมชั่วโมง/progress/count และตรวจ risk หรือภาระเกินงบ 7 วัน |
| `build` | L49–L64 | ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `TITLE` | ชื่อหน้าสำหรับเมนูที่ app อ่าน |
| `TITLES` | คำนำหน้าที่ตัดออกก่อนดึงอักษรชื่อ |
| `all_views` | วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่ |
| `annotate_plan` | คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count |
| `append` | เพิ่มหนึ่งรายการต่อท้าย list |
| `assigned` | งานที่ owner ตรงสมาชิก |
| `build` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `data` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `dict` | ชนิด map; dict(row) เป็นสำเนาระดับบน |
| `done` | ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น |
| `hours` | จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน |
| `initial_of` | ตัดคำนำหน้าชื่อที่รู้จักและคืนอักขระแรก หรือ ? หากชื่อว่าง; ไม่ยืนยันตัวตน |
| `int` | แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress |
| `item` | dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน |
| `items` | list ของข้อมูลแสดงผล |
| `known_owners` | รหัสสมาชิกที่รู้จัก |
| `len` | จำนวนสมาชิก/อักขระ |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `load_daily_hours` | อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `member` | สมาชิกหนึ่งคน |
| `member_summary` | คัดงานของ member รวมชั่วโมง/progress/count และตรวจ risk หรือภาระเกินงบ 7 วัน |
| `members` | list สมาชิกจาก team.json |
| `min` | เลือกค่าน้อยที่สุด |
| `models` | module คลาสและฟังก์ชันกลาง |
| `name` | ชื่อสมาชิก/ข้อความงานย่อยตามบริบท |
| `open_count` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `own_tasks` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `prefix` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `progress` | เปอร์เซ็นต์แบบจำนวนเต็ม |
| `remaining` | ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท |
| `result` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `risks` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `round` | ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ |
| `startswith` | ตรวจว่าข้อความขึ้นต้นตามที่กำหนด |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `strip` | ตัดช่องว่างริมข้อความทั้งสองด้าน |
| `team_data` | อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `total` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `unassigned` | pending ที่ owner ว่าง/ไม่ตรงรหัสสมาชิก |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
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
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Team directory and assignment workload, extending the given team page."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน

### L2

```python
import models
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import models`
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง

### L3

```python
import storage
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import storage`
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้

### L4

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L5

```python
TITLE = "ทีม"
```

- เก็บผล `'ทีม'` ลง `TITLE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `TITLE` = ชื่อหน้าสำหรับเมนูที่ app อ่าน

### L6

```python
TITLES = ["นางสาว", "นาย", "นาง", "ว่าที่ร้อยตรี", "Mr.", "Ms.", "Miss"]
```

- เก็บผล list จำนวน 7 สมาชิกตามโค้ด ลง `TITLES`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `TITLES` = คำนำหน้าที่ตัดออกก่อนดึงอักษรชื่อ

### L7

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L8

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L9

```python
def initial_of(name):
```

- ประกาศฟังก์ชัน `initial_of`: ตัดคำนำหน้าชื่อที่รู้จักและคืนอักขระแรก หรือ ? หากชื่อว่าง; ไม่ยืนยันตัวตน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท

### L10

```python
    name = name.strip()
```

- เก็บผล เรียก `name.strip` ด้วย argument ที่แสดงในโค้ด ลง `name`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L11

```python
    for prefix in TITLES:
```

- วน `TITLES` ให้ `prefix` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `TITLES` = คำนำหน้าที่ตัดออกก่อนดึงอักษรชื่อ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L12

```python
        if name.startswith(prefix):
```

- ตรวจเงื่อนไข: เรียก `name.startswith` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L13

```python
            name = name[len(prefix):].strip()
```

- เก็บผล เรียก `name[len(prefix):].strip` ด้วย argument ที่แสดงในโค้ด ลง `name`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท; `len` = จำนวนสมาชิก/อักขระ; `strip` = ตัดช่องว่างริมข้อความทั้งสองด้าน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L14

```python
    if name == "":
```

- ตรวจเงื่อนไข: `name` เท่ากับ `''`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L15

```python
        return "?"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'?'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L16

```python
    return name[0]
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `name[0]` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `name` = ชื่อสมาชิก/ข้อความงานย่อยตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L17

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L18

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L19

```python
def member_summary(member, items, hours):
```

- ประกาศฟังก์ชัน `member_summary`: คัดงานของ member รวมชั่วโมง/progress/count และตรวจ risk หรือภาระเกินงบ 7 วัน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน; `items` = list ของข้อมูลแสดงผล; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน

### L20

```python
    result = dict(member)
```

- เก็บผล `dict`(`member`) ลง `result`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `dict` = ชนิด map; dict(row) เป็นสำเนาระดับบน; `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L21

```python
    result["initial"] = initial_of(member["name"])
```

- เก็บผล เรียก `initial_of`: ตัดคำนำหน้าชื่อที่รู้จักและคืนอักขระแรก หรือ ? หากชื่อว่าง; ไม่ยืนยันตัวตน ลง `result['initial']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L22

```python
    assigned = []
```

- เก็บผล list [] ลง `assigned`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `assigned` = งานที่ owner ตรงสมาชิก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L23

```python
    total = 0
```

- เก็บผล `0` ลง `total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L24

```python
    done = 0
```

- เก็บผล `0` ลง `done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L25

```python
    remaining = 0
```

- เก็บผล `0` ลง `remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L26

```python
    open_count = 0
```

- เก็บผล `0` ลง `open_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L27

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L28

```python
        if item["details"]["owner"] == member["id"]:
```

- ตรวจเงื่อนไข: `item['details']['owner']` (อ่าน key/index) เท่ากับ `member['id']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `member` = สมาชิกหนึ่งคน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

```python
            assigned.append(item)
```

- เพิ่ม `item` ไปท้าย `assigned`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `assigned` = งานที่ owner ตรงสมาชิก; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L30

```python
            total = total + item["estimated_hours"]
```

- เก็บผล (`total` บวก/ต่อ `item['estimated_hours']` (อ่าน key/index)) ลง `total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L31

```python
            done = done + min(item["estimated_hours"], item["done_hours"])
```

- เก็บผล (`done` บวก/ต่อ `min`(`item['estimated_hours']` (อ่าน key/index), `item['done_hours']` (อ่าน key/index))) ลง `done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `min` = เลือกค่าน้อยที่สุด; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L32

```python
            remaining = remaining + item["remaining_hours"]
```

- เก็บผล (`remaining` บวก/ต่อ `item['remaining_hours']` (อ่าน key/index)) ลง `remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L33

```python
            if item["remaining_hours"] > 0:
```

- ตรวจเงื่อนไข: `item['remaining_hours']` (อ่าน key/index) มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L34

```python
                open_count = open_count + 1
```

- เก็บผล (`open_count` บวก/ต่อ `1`) ลง `open_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L35

```python
    progress = 0
```

- เก็บผล `0` ลง `progress`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `progress` = เปอร์เซ็นต์แบบจำนวนเต็ม
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

```python
    if total > 0:
```

- ตรวจเงื่อนไข: `total` มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L37

```python
        progress = min(100, int(done * 100 / total))
```

- เก็บผล `min`(`100`, `int`(((`done` คูณ/ทำซ้ำ `100`) หาร/ต่อ Path `total`))) ลง `progress`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง; `/` หาร; กับ pathlib.Path เป็นการต่อ path; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `progress` = เปอร์เซ็นต์แบบจำนวนเต็ม; `min` = เลือกค่าน้อยที่สุด; `int` = แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L38

```python
    own_tasks, risks = models.annotate_plan(assigned, hours)
```

- เก็บผล เรียก `models.annotate_plan`: คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count ลง `(own_tasks, risks)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `assigned` = งานที่ owner ตรงสมาชิก; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L39

```python
    result["assignments"] = assigned
```

- เก็บผล `assigned` ลง `result['assignments']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `assigned` = งานที่ owner ตรงสมาชิก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L40

```python
    result["assignment_count"] = len(assigned)
```

- เก็บผล `len`(`assigned`) ลง `result['assignment_count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `assigned` = งานที่ owner ตรงสมาชิก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
    result["open_count"] = open_count
```

- เก็บผล `open_count` ลง `result['open_count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L42

```python
    result["progress"] = progress
```

- เก็บผล `progress` ลง `result['progress']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `progress` = เปอร์เซ็นต์แบบจำนวนเต็ม
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L43

```python
    result["remaining_hours"] = round(remaining, 2)
```

- เก็บผล `round`(`remaining`, `2`) ลง `result['remaining_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L44

```python
    result["risk_count"] = risks
```

- เก็บผล `risks` ลง `result['risk_count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L45

```python
    result["overloaded"] = remaining > hours * 7 or risks > 0
```

- เก็บผล `remaining` มากกว่า (`hours` คูณ/ทำซ้ำ `7`) หรือ `risks` มากกว่า `0` ลง `result['overloaded']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `>` มากกว่า; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L46

```python
    return result
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `result`
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L47

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L48

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L49

```python
def build():
```

- ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L50

```python
    data = models.team_data()
```

- เก็บผล เรียก `models.team_data`: อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย ลง `data`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L51

```python
    hours = models.load_daily_hours()
```

- เก็บผล เรียก `models.load_daily_hours`: อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 ลง `hours`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L52

```python
    items = models.all_views(storage.load(), data["members"])
```

- เก็บผล เรียก `models.all_views`: วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่ ลง `items`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล; `models` = module คลาสและฟังก์ชันกลาง; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L53

```python
    members = []
```

- เก็บผล list [] ลง `members`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L54

```python
    known_owners = []
```

- เก็บผล list [] ลง `known_owners`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `known_owners` = รหัสสมาชิกที่รู้จัก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L55

```python
    for member in data["members"]:
```

- วน `data['members']` (อ่าน key/index) ให้ `member` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L56

```python
        known_owners.append(member["id"])
```

- เพิ่ม `member['id']` (อ่าน key/index) ไปท้าย `known_owners`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `known_owners` = รหัสสมาชิกที่รู้จัก; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `member` = สมาชิกหนึ่งคน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L57

```python
        members.append(member_summary(member, items, hours))
```

- เพิ่ม เรียก `member_summary`: คัดงานของ member รวมชั่วโมง/progress/count และตรวจ risk หรือภาระเกินงบ 7 วัน ไปท้าย `members`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `member` = สมาชิกหนึ่งคน; `items` = list ของข้อมูลแสดงผล; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L58

```python
    unassigned = []
```

- เก็บผล list [] ลง `unassigned`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `unassigned` = pending ที่ owner ว่าง/ไม่ตรงรหัสสมาชิก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L59

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L60

```python
        if item["details"]["owner"] not in known_owners and item["remaining_hours"] > 0:
```

- ตรวจเงื่อนไข: `item['details']['owner']` (อ่าน key/index) ไม่อยู่ใน `known_owners` และ `item['remaining_hours']` (อ่าน key/index) มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `known_owners` = รหัสสมาชิกที่รู้จัก
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L61

```python
            unassigned.append(item)
```

- เพิ่ม `item` ไปท้าย `unassigned`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `unassigned` = pending ที่ owner ว่าง/ไม่ตรงรหัสสมาชิก; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L62

```python
    return {"group": data["group"], "members": members, "count": len(members),
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'group'`, `'members'`, `'count'`, `'unassigned'`, `'daily_hours'`, `'weekly_capacity'`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json; `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L63

```python
            "unassigned": unassigned, "daily_hours": hours,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L62: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'group'`, `'members'`, `'count'`, `'unassigned'`, `'daily_hours'`, `'weekly_capacity'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `unassigned` = pending ที่ owner ว่าง/ไม่ตรงรหัสสมาชิก; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L64

```python
            "weekly_capacity": round(hours * 7, 1)}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L62: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'group'`, `'members'`, `'count'`, `'unassigned'`, `'daily_hours'`, `'weekly_capacity'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
