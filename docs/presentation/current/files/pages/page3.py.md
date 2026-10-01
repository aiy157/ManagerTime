# pages/page3.py — Python ของหน้า Plan

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 41 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `06f96a88064c539ce3ed76025db75e9c2be0875c1b5ea5cf4ba87e2b9911f821`

**ผู้ศึกษา/บทบาท:** นายธีรเดช ฤทธิ์คำรพ · Page 3 / QA

## 1. หน้าที่และการเชื่อมต่อ

รับค่าชั่วโมงที่บันทึกไว้หรือค่าทดลองจาก URL เตรียมแผน และบันทึกงบเวลาให้ใช้ร่วมกับ Overview

- **รับเข้า:** query dict, form ของ save_hours/quick action, งาน และ settings
- **ผลลัพธ์:** tasks ตามวันส่ง, required_daily, daily_shortfall, notice และ context กลาง

**เกี่ยวข้องกับ:** models.load_daily_hours/daily_hours/save_daily_hours; models.overview/order_items/ceil_tenth; storage.load; templates/page3.html

## 2. ลำดับทำงาน

1. อ่านชั่วโมงที่บันทึกเป็นค่าเริ่มต้น
2. หากมี hours ใน URL ตรวจค่า; ไม่ถูกต้องใช้ค่าเดิมและ notice
3. overview คำนวณแผน จากนั้นเรียง tasks ตาม deadline
4. หาค่าสูงสุดของ hours_per_day เฉพาะวันส่งที่ยังไม่ผ่าน
5. handle save_hours ตรวจ 0.1–12 แล้วเขียน settings; quick action ใช้ฟังก์ชันกลาง

## 3. จุดที่ต้องอธิบายให้ถูก

- ค่า GET hours ใช้ในรอบแสดง ไม่เขียนไฟล์; ปุ่ม POST บันทึกจึงเปลี่ยนค่าที่ทุกหน้าอ่าน
- required_daily ไม่บวกค่าเฉลี่ยทุกงานเพราะจะนับภาระซ้ำ
- ถ้ามีแต่งานเกินกำหนด required_daily เป็น 0 แต่งานเหล่านั้นยังขึ้นเกินกำหนด

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q001: โครงการนี้แก้ปัญหาอะไร?](../../TEACHER_QUESTIONS.md#q001)
- [Q008: build() กับ handle() ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q008)
- [Q059: ค่าทดลอง hours ใน URL กับปุ่มบันทึกต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q059)
- [Q060: required_daily เป็น 0 แต่ยังมีงานเสี่ยงได้หรือไม่?](../../TEACHER_QUESTIONS.md#q060)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `build` | L8–L29 | ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET |
| `handle` | L32–L41 | ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `TITLE` | ชื่อหน้าสำหรับเมนูที่ app อ่าน |
| `build` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `ceil_tenth` | จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float |
| `context` | dict ที่คืนให้ template |
| `daily_hours` | เวลาว่างรายวันที่ตั้งไว้ |
| `form` | dict ของข้อมูลฟอร์ม POST |
| `get` | อ่านค่า dict พร้อม default เมื่อไม่มี key |
| `handle` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `hours` | จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `load_daily_hours` | อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `max` | เลือกค่ามากที่สุด |
| `models` | module คลาสและฟังก์ชันกลาง |
| `notice` | ข้อความเตือนจาก build |
| `order_items` | selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda |
| `overview` | รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `query` | dict ของค่าจาก URL ใน GET |
| `quick_action` | โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน |
| `requested` | ค่าชั่วโมงทดลองใน query ที่ผ่านตรวจหรือ None |
| `required` | ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท |
| `save_daily_hours` | เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `task` | Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
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
    if notice:
        if context["notice"]:
            notice = notice + " · " + context["notice"]
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
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Plan calculator adapted from catalog/ranking and calculator."""
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
TITLE = "แผนก่อนวันส่ง"
```

- เก็บผล `'แผนก่อนวันส่ง'` ลง `TITLE`
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
def build(query):
```

- ประกาศฟังก์ชัน `build`: build เตรียม context จาก GET
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `query` = dict ของค่าจาก URL ใน GET

### L9

```python
    hours = models.load_daily_hours()
```

- เก็บผล เรียก `models.load_daily_hours`: อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 ลง `hours`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L10

```python
    notice = ""
```

- เก็บผล `''` ลง `notice`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `notice` = ข้อความเตือนจาก build
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L11

```python
    if "hours" in query:
```

- ตรวจเงื่อนไข: `'hours'` อยู่ใน `query`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `query` = dict ของค่าจาก URL ใน GET
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L12

```python
        requested = models.daily_hours(query.get("hours", ""))
```

- เก็บผล เรียก `models.daily_hours`: อ่านเลขผ่าน read_number แล้วรับเฉพาะ 0.1–12 ชั่วโมง ลง `requested`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `requested` = ค่าชั่วโมงทดลองใน query ที่ผ่านตรวจหรือ None; `models` = module คลาสและฟังก์ชันกลาง; `daily_hours` = เวลาว่างรายวันที่ตั้งไว้; `query` = dict ของค่าจาก URL ใน GET; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L13

```python
        if requested is None:
```

- ตรวจเงื่อนไข: `requested` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `requested` = ค่าชั่วโมงทดลองใน query ที่ผ่านตรวจหรือ None; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L14

```python
            notice = "กรุณากรอกเวลาว่าง 0.1 ถึง 12 ชั่วโมง ใช้ค่าที่บันทึกไว้แทน"
```

- เก็บผล `'กรุณากรอกเวลาว่าง 0.1 ถึง 12 ชั่วโมง ใช้ค่าที่บันทึกไว้แทน'` ลง `notice`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `notice` = ข้อความเตือนจาก build
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L15

```python
        else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L16

```python
            hours = requested
```

- เก็บผล `requested` ลง `hours`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `requested` = ค่าชั่วโมงทดลองใน query ที่ผ่านตรวจหรือ None
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L17

```python
    context = models.overview(storage.load(), hours)
```

- เก็บผล เรียก `models.overview`: รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ ลง `context`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

```python
    context["tasks"] = models.order_items(context["items"], "deadline")
```

- เก็บผล เรียก `models.order_items`: selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda ลง `context['tasks']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L19

```python
    if notice:
```

- ตรวจเงื่อนไข: `notice`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `notice` = ข้อความเตือนจาก build
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L20

```python
        if context["notice"]:
```

- ตรวจเงื่อนไข: `context['notice']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L21

```python
            notice = notice + " · " + context["notice"]
```

- เก็บผล ((`notice` บวก/ต่อ `' · '`) บวก/ต่อ `context['notice']` (อ่าน key/index)) ลง `notice`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `notice` = ข้อความเตือนจาก build; `context` = dict ที่คืนให้ template
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L22

```python
        context["notice"] = notice
```

- เก็บผล `notice` ลง `context['notice']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `notice` = ข้อความเตือนจาก build
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L23

```python
    required = 0
```

- เก็บผล `0` ลง `required`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L24

```python
    for task in context["tasks"]:
```

- วน `context['tasks']` (อ่าน key/index) ให้ `task` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L25

```python
        if task["days_left"] >= 0:
```

- ตรวจเงื่อนไข: `task['days_left']` (อ่าน key/index) อย่างน้อย `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L26

```python
            required = max(required, task["hours_per_day"])
```

- เก็บผล `max`(`required`, `task['hours_per_day']` (อ่าน key/index)) ลง `required`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท; `max` = เลือกค่ามากที่สุด; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L27

```python
    context["required_daily"] = required
```

- เก็บผล `required` ลง `context['required_daily']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L28

```python
    context["daily_shortfall"] = models.ceil_tenth(max(0, required - hours))
```

- เก็บผล เรียก `models.ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float ลง `context['daily_shortfall']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template; `models` = module คลาสและฟังก์ชันกลาง; `max` = เลือกค่ามากที่สุด; `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

```python
    return context
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `context`
- ชื่อที่ต้องรู้: `context` = dict ที่คืนให้ template
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L30

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L31

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L32

```python
def handle(form):
```

- ประกาศฟังก์ชัน `handle`: handle รับฟอร์ม POST และคืนข้อความ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST

### L33

```python
    if form.get("action", "") in ("start", "complete", "reopen"):
```

- ตรวจเงื่อนไข: อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี อยู่ใน tuple [`'start'`, `'complete'`, `'reopen'`]; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L34

```python
        return models.quick_action(form)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `models.quick_action`: โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L35

```python
    if form.get("action", "") != "save_hours":
```

- ตรวจเงื่อนไข: อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี ไม่เท่ากับ `'save_hours'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `!=` เปรียบเทียบไม่เท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

```python
        return "✗ ไม่รู้จักคำสั่ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่รู้จักคำสั่ง'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L37

```python
    hours = models.daily_hours(form.get("hours", ""))
```

- เก็บผล เรียก `models.daily_hours`: อ่านเลขผ่าน read_number แล้วรับเฉพาะ 0.1–12 ชั่วโมง ลง `hours`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `models` = module คลาสและฟังก์ชันกลาง; `daily_hours` = เวลาว่างรายวันที่ตั้งไว้; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L38

```python
    if hours is None:
```

- ตรวจเงื่อนไข: `hours` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L39

```python
        return "✗ เวลาว่างต้องตั้งแต่ 0.1 ถึง 12 ชั่วโมงต่อวัน"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ เวลาว่างต้องตั้งแต่ 0.1 ถึง 12 ชั่วโมงต่อวัน'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L40

```python
    models.save_daily_hours(hours)
```

- เรียก `models.save_daily_hours`: เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
    return "✓ บันทึกเวลาว่างแล้ว ภาพรวมและแผนใช้ค่านี้ร่วมกัน"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✓ บันทึกเวลาว่างแล้ว ภาพรวมและแผนใช้ค่านี้ร่วมกัน'`
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
