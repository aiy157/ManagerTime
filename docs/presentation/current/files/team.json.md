# team.json — ชื่อกลุ่ม สมาชิก และหน้าที่รายวิชา

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 14 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `08a3ff548fe93720618fd6764cd75415a10d4ff04bf6300f094bbddfd9180427`

**ผู้ศึกษา/บทบาท:** สมาชิก CodeMind ทั้ง 4 คน

## 1. หน้าที่และการเชื่อมต่อ

เก็บชื่อกลุ่ม/หัวข้อและข้อมูลสมาชิกที่ใช้หัวเว็บ เมนูทีม และรายการเลือก owner

- **รับเข้า:** ชื่อและบทบาทที่ผู้ใช้ให้
- **ผลลัพธ์:** object มี group และ members

**เกี่ยวข้องกับ:** app.py inject_globals; models.team_data; pages/team.py; pages/page2.py

## 2. ลำดับทำงาน

1. group เก็บ name/section/topic/description
2. members เก็บ name/id/role/task คนละ object
3. รหัสสมาชิกเป็น string ใช้จับคู่ owner

## 3. จุดที่ต้องอธิบายให้ถูก

- task เป็นหน้าที่ในโครงงานรายวิชา ไม่ใช่รายการการบ้านที่แอปบันทึก
- การมีชื่อใน JSON ไม่ได้พิสูจน์ว่าแต่ละคนมี commit แล้ว ต้องดู git log
- ไม่สร้างบัญชีหรือสิทธิ์ login จากรหัสนักศึกษา

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q002: กลุ่มเป้าหมายคือใคร?](../TEACHER_QUESTIONS.md#q002)
- [Q085: ทำไมเก็บรหัสสมาชิกเป็น string?](../TEACHER_QUESTIONS.md#q085)
- [Q090: บทบาทสมาชิกกับงานที่มอบหมายและ Git เป็นเรื่องเดียวกันหรือไม่?](../TEACHER_QUESTIONS.md#q090)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```json
{
  "group": {
    "name": "CodeMind",
    "section": "กลุ่ม 6",
    "topic": "เดดไลน์ไม่ชนกัน",
    "description": "เว็บช่วยบันทึกงาน วางแผนเวลา และเตือนก่อนงานหลายวิชาชนกัน"
  },
  "members": [
    {"name": "นางสาวลักขณา ศรีโพธิ์", "id": "69130840153", "role": "Backend Dev (Python)", "task": "page1 · ภาพรวมงาน"},
    {"name": "นายวายุ ทาโสม", "id": "69130840182", "role": "Project Lead (PM)", "task": "models.py · Assignment"},
    {"name": "นายไกรวิชญ์ บุ้งทอง", "id": "69130840247", "role": "Frontend Dev (HTML/CSS)", "task": "page2 · จัดการงาน"},
    {"name": "นายธีรเดช ฤทธิ์คำรพ", "id": "69130840320", "role": "QA / Test", "task": "page3 · แผนก่อนวันส่ง และ check.bat"}
  ]
}
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```json
{
```

- เปิด object `$` เก็บ key:value

### L2

```json
  "group": {
```

- key `group`: ข้อมูลกลุ่ม
- เปิด object `$.group` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L3

```json
    "name": "CodeMind",
```

- key `name`: ชื่อกลุ่ม/สมาชิกตาม path
- `$.group.name` = `"CodeMind"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L4

```json
    "section": "กลุ่ม 6",
```

- key `section`: ข้อความกลุ่มหรือ section ที่ผู้ใช้ให้
- `$.group.section` = `"กลุ่ม 6"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L5

```json
    "topic": "เดดไลน์ไม่ชนกัน",
```

- key `topic`: หัวข้อโครงการ
- `$.group.topic` = `"เดดไลน์ไม่ชนกัน"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L6

```json
    "description": "เว็บช่วยบันทึกงาน วางแผนเวลา และเตือนก่อนงานหลายวิชาชนกัน"
```

- key `description`: คำอธิบายหัวข้อ
- `$.group.description` = `"เว็บช่วยบันทึกงาน วางแผนเวลา และเตือนก่อนงานหลายวิชาชนกัน"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L7

```json
  },
```

- ปิด object `$.group`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L8

```json
  "members": [
```

- key `members`: รายการสมาชิก
- เปิด array `$.members` เก็บหลายรายการเรียงลำดับ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L9

```json
    {"name": "นางสาวลักขณา ศรีโพธิ์", "id": "69130840153", "role": "Backend Dev (Python)", "task": "page1 · ภาพรวมงาน"},
```

- เปิด object `$.members[0]` เก็บ key:value
- key `name`: ชื่อกลุ่ม/สมาชิกตาม path
- `$.members[0].name` = `"นางสาวลักขณา ศรีโพธิ์"` (string)
- key `id`: รหัสสมาชิกแบบ string
- `$.members[0].id` = `"69130840153"` (string)
- key `role`: บทบาทในรายวิชา
- `$.members[0].role` = `"Backend Dev (Python)"` (string)
- key `task`: ส่วนของโครงงานรายวิชาที่รับผิดชอบ
- `$.members[0].task` = `"page1 · ภาพรวมงาน"` (string)
- ปิด object `$.members[0]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L10

```json
    {"name": "นายวายุ ทาโสม", "id": "69130840182", "role": "Project Lead (PM)", "task": "models.py · Assignment"},
```

- เปิด object `$.members[1]` เก็บ key:value
- key `name`: ชื่อกลุ่ม/สมาชิกตาม path
- `$.members[1].name` = `"นายวายุ ทาโสม"` (string)
- key `id`: รหัสสมาชิกแบบ string
- `$.members[1].id` = `"69130840182"` (string)
- key `role`: บทบาทในรายวิชา
- `$.members[1].role` = `"Project Lead (PM)"` (string)
- key `task`: ส่วนของโครงงานรายวิชาที่รับผิดชอบ
- `$.members[1].task` = `"models.py · Assignment"` (string)
- ปิด object `$.members[1]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L11

```json
    {"name": "นายไกรวิชญ์ บุ้งทอง", "id": "69130840247", "role": "Frontend Dev (HTML/CSS)", "task": "page2 · จัดการงาน"},
```

- เปิด object `$.members[2]` เก็บ key:value
- key `name`: ชื่อกลุ่ม/สมาชิกตาม path
- `$.members[2].name` = `"นายไกรวิชญ์ บุ้งทอง"` (string)
- key `id`: รหัสสมาชิกแบบ string
- `$.members[2].id` = `"69130840247"` (string)
- key `role`: บทบาทในรายวิชา
- `$.members[2].role` = `"Frontend Dev (HTML/CSS)"` (string)
- key `task`: ส่วนของโครงงานรายวิชาที่รับผิดชอบ
- `$.members[2].task` = `"page2 · จัดการงาน"` (string)
- ปิด object `$.members[2]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L12

```json
    {"name": "นายธีรเดช ฤทธิ์คำรพ", "id": "69130840320", "role": "QA / Test", "task": "page3 · แผนก่อนวันส่ง และ check.bat"}
```

- เปิด object `$.members[3]` เก็บ key:value
- key `name`: ชื่อกลุ่ม/สมาชิกตาม path
- `$.members[3].name` = `"นายธีรเดช ฤทธิ์คำรพ"` (string)
- key `id`: รหัสสมาชิกแบบ string
- `$.members[3].id` = `"69130840320"` (string)
- key `role`: บทบาทในรายวิชา
- `$.members[3].role` = `"QA / Test"` (string)
- key `task`: ส่วนของโครงงานรายวิชาที่รับผิดชอบ
- `$.members[3].task` = `"page3 · แผนก่อนวันส่ง และ check.bat"` (string)
- ปิด object `$.members[3]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L13

```json
  ]
```

- ปิด array `$.members` จำนวน 4 รายการ

### L14

```json
}
```

- ปิด object `$`
