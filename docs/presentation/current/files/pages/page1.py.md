# pages/page1.py — Python ของหน้า Overview

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 23 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `b7d6819c28320d2c2c5a15095ca69d36a2e765fac6f7ade01947f37fb0e3f6c8`

**ผู้ศึกษา/บทบาท:** นางสาวลักขณา ศรีโพธิ์ · Page 1

## 1. หน้าที่และการเชื่อมต่อ

เตรียมภาพรวมและข้อมูลขั้นต่ำสำหรับเตือน พร้อมส่งคำสั่งเริ่ม/ปิด/เปิดกลับไปยังฟังก์ชันกลาง

- **รับเข้า:** งานจาก storage.load() และชั่วโมงจาก models.load_daily_hours(); POST form
- **ผลลัพธ์:** context สำหรับ page1.html พร้อม reminder_tasks; handle คืนข้อความ

**เกี่ยวข้องกับ:** models.overview; storage.load; models.quick_action; templates/page1.html; static/js/reminders.js

## 2. ลำดับทำงาน

1. build อ่านงานกับค่าชั่วโมงและเรียก overview
2. วนเฉพาะรายการ pending เพื่อสร้าง reminder_tasks 6 ค่า
3. เติมข้อมูลเตือนใน context แล้วคืน dict
4. handle อนุญาต start/complete/reopen และปฏิเสธ action อื่น

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่มี route หรือ request ในไฟล์นี้ app.py จัดการให้
- reminder_tasks ไม่ส่ง details/history/รหัสสมาชิกทั้งหมด
- ฟอร์มใช้ version ผ่าน macro; ไม่ควรรับตำแหน่งอย่างเดียว

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q001: โครงการนี้แก้ปัญหาอะไร?](../../TEACHER_QUESTIONS.md#q001)
- [Q003: ทำไมใช้ Python และ Flask?](../../TEACHER_QUESTIONS.md#q003)
- [Q005: ทำไมหนึ่งหน้ามีทั้ง .py และ .html?](../../TEACHER_QUESTIONS.md#q005)
- [Q018: return ต่างจาก print อย่างไร?](../../TEACHER_QUESTIONS.md#q018)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `build` | L8–L17 | ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET |
| `handle` | L20–L23 | ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `TITLE` | ชื่อหน้าสำหรับเมนูที่ app อ่าน |
| `append` | เพิ่มหนึ่งรายการต่อท้าย list |
| `build` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `context` | dict ที่คืนให้ template |
| `form` | dict ของข้อมูลฟอร์ม POST |
| `get` | อ่านค่า dict พร้อม default เมื่อไม่มี key |
| `handle` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `item` | dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `load_daily_hours` | อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `models` | module คลาสและฟังก์ชันกลาง |
| `overview` | รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `quick_action` | โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน |
| `reminders` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
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
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Overview adapted from catalog/list, stats, ranking, and cart actions."""
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
TITLE = "ภาพรวมงาน"
```

- เก็บผล `'ภาพรวมงาน'` ลง `TITLE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `TITLE` = ชื่อหน้าสำหรับเมนูที่ app อ่าน

### L6

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L7

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L8

```python
def build():
```

- ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L9

```python
    context = models.overview(storage.load(), models.load_daily_hours())
```

- เก็บผล เรียก `models.overview`: รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ ลง `context`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L10

```python
    reminders = []
```

- เก็บผล list [] ลง `reminders`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L11

```python
    for item in context["items"]:
```

- วน `context['items']` (อ่าน key/index) ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L12

```python
        reminders.append({"title": item["title"], "due_date": item["due_date"],
```

- เพิ่ม dict ที่มี key `'title'`, `'due_date'`, `'remaining_hours'`, `'at_risk'`, `'stale'`, `'today_hours'` ไปท้าย `reminders`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `append` = เพิ่มหนึ่งรายการต่อท้าย list; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L13

```python
                          "remaining_hours": item["remaining_hours"],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L12: เพิ่ม dict ที่มี key `'title'`, `'due_date'`, `'remaining_hours'`, `'at_risk'`, `'stale'`, `'today_hours'` ไปท้าย `reminders`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 26 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L14

```python
                          "at_risk": item["at_risk"], "stale": item["stale"],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L12: เพิ่ม dict ที่มี key `'title'`, `'due_date'`, `'remaining_hours'`, `'at_risk'`, `'stale'`, `'today_hours'` ไปท้าย `reminders`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 26 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L15

```python
                          "today_hours": item["today_hours"]})
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L12: เพิ่ม dict ที่มี key `'title'`, `'due_date'`, `'remaining_hours'`, `'at_risk'`, `'stale'`, `'today_hours'` ไปท้าย `reminders`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 26 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L16

```python
    context["reminder_tasks"] = reminders
```

- เก็บผล `reminders` ลง `context['reminder_tasks']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L17

```python
    return context
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `context`
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L19

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L20

```python
def handle(form):
```

- ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST

### L21

```python
    if form.get("action", "") in ("start", "complete", "reopen"):
```

- ตรวจเงื่อนไข: อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี อยู่ใน tuple [`'start'`, `'complete'`, `'reopen'`]; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L22

```python
        return models.quick_action(form)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `models.quick_action`: โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L23

```python
    return "✗ ไม่รู้จักคำสั่ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่รู้จักคำสั่ง'`
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
