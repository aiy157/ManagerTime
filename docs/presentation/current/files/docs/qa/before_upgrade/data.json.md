# docs/qa/before_upgrade/data.json — สำเนางานก่อนเพิ่ม field

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 9 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `74d01faf3a45a52d5f7a73d40c8593f4d49bf7d96e3d69e9d62e92dc873c17b1`

**ผู้ศึกษา/บทบาท:** QA / สำรองก่อนปรับปรุง

## 1. หน้าที่และการเชื่อมต่อ

เก็บข้อมูลเดิม 5 field เพื่อเทียบว่าไม่เปลี่ยนชื่อ วัน และชั่วโมงตอนเพิ่มคุณสมบัติ

- **รับเข้า:** data.json ก่อน migration
- **ผลลัพธ์:** snapshot ก่อนเพิ่ม priority/details

**เกี่ยวข้องกับ:** data.json ปัจจุบันเพื่อเปรียบเทียบ

## 2. ลำดับทำงาน

1. มีงานเดิม 7 รายการ
2. แต่ละงานเก็บเฉพาะ title/course/due_date/estimated_hours/done_hours

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่ใช่ไฟล์ที่ app โหลดขณะใช้งาน
- หากคืน snapshot จะเป็น schema 5 field ซึ่งโค้ดยังอ่านได้ แต่รายละเอียดใหม่จะหาย

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- อธิบายว่าไฟล์นี้เป็นข้อมูล/เครื่องมือประกอบอะไร และถูกอ่านที่ใด

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```json
[
  {"title": "รายงานการทดลองวงจร", "course": "ฟิสิกส์", "due_date": "2026-09-26", "estimated_hours": 6, "done_hours": 2},
  {"title": "แบบฝึกหัดอนุพันธ์", "course": "คณิตศาสตร์", "due_date": "2026-09-27", "estimated_hours": 4, "done_hours": 0},
  {"title": "สรุปผลห้องปฏิบัติการ", "course": "เคมี", "due_date": "2026-09-28", "estimated_hours": 5, "done_hours": 1},
  {"title": "นำเสนอหัวข้อภาษาอังกฤษ", "course": "ภาษาอังกฤษ", "due_date": "2026-10-01", "estimated_hours": 6, "done_hours": 0},
  {"title": "โครงงานเขียนโปรแกรม", "course": "การเขียนโปรแกรม", "due_date": "2026-10-04", "estimated_hours": 8, "done_hours": 2},
  {"title": "โปสเตอร์แนวคิดผลิตภัณฑ์", "course": "การออกแบบ", "due_date": "2026-10-06", "estimated_hours": 3, "done_hours": 0},
  {"title": "ทบทวนก่อนสอบย่อย", "course": "คณิตศาสตร์", "due_date": "2026-10-08", "estimated_hours": 2, "done_hours": 0}
]
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```json
[
```

- เปิด array `$` เก็บหลายรายการเรียงลำดับ

### L2

```json
  {"title": "รายงานการทดลองวงจร", "course": "ฟิสิกส์", "due_date": "2026-09-26", "estimated_hours": 6, "done_hours": 2},
```

- เปิด object `$[0]` เก็บ key:value
- key `title`: ชื่องาน
- `$[0].title` = `"รายงานการทดลองวงจร"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[0].course` = `"ฟิสิกส์"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[0].due_date` = `"2026-09-26"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[0].estimated_hours` = `6` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[0].done_hours` = `2` (number)
- ปิด object `$[0]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L3

```json
  {"title": "แบบฝึกหัดอนุพันธ์", "course": "คณิตศาสตร์", "due_date": "2026-09-27", "estimated_hours": 4, "done_hours": 0},
```

- เปิด object `$[1]` เก็บ key:value
- key `title`: ชื่องาน
- `$[1].title` = `"แบบฝึกหัดอนุพันธ์"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[1].course` = `"คณิตศาสตร์"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[1].due_date` = `"2026-09-27"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[1].estimated_hours` = `4` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[1].done_hours` = `0` (number)
- ปิด object `$[1]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L4

```json
  {"title": "สรุปผลห้องปฏิบัติการ", "course": "เคมี", "due_date": "2026-09-28", "estimated_hours": 5, "done_hours": 1},
```

- เปิด object `$[2]` เก็บ key:value
- key `title`: ชื่องาน
- `$[2].title` = `"สรุปผลห้องปฏิบัติการ"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[2].course` = `"เคมี"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[2].due_date` = `"2026-09-28"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[2].estimated_hours` = `5` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[2].done_hours` = `1` (number)
- ปิด object `$[2]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L5

```json
  {"title": "นำเสนอหัวข้อภาษาอังกฤษ", "course": "ภาษาอังกฤษ", "due_date": "2026-10-01", "estimated_hours": 6, "done_hours": 0},
```

- เปิด object `$[3]` เก็บ key:value
- key `title`: ชื่องาน
- `$[3].title` = `"นำเสนอหัวข้อภาษาอังกฤษ"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[3].course` = `"ภาษาอังกฤษ"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[3].due_date` = `"2026-10-01"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[3].estimated_hours` = `6` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[3].done_hours` = `0` (number)
- ปิด object `$[3]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L6

```json
  {"title": "โครงงานเขียนโปรแกรม", "course": "การเขียนโปรแกรม", "due_date": "2026-10-04", "estimated_hours": 8, "done_hours": 2},
```

- เปิด object `$[4]` เก็บ key:value
- key `title`: ชื่องาน
- `$[4].title` = `"โครงงานเขียนโปรแกรม"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[4].course` = `"การเขียนโปรแกรม"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[4].due_date` = `"2026-10-04"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[4].estimated_hours` = `8` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[4].done_hours` = `2` (number)
- ปิด object `$[4]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L7

```json
  {"title": "โปสเตอร์แนวคิดผลิตภัณฑ์", "course": "การออกแบบ", "due_date": "2026-10-06", "estimated_hours": 3, "done_hours": 0},
```

- เปิด object `$[5]` เก็บ key:value
- key `title`: ชื่องาน
- `$[5].title` = `"โปสเตอร์แนวคิดผลิตภัณฑ์"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[5].course` = `"การออกแบบ"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[5].due_date` = `"2026-10-06"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[5].estimated_hours` = `3` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[5].done_hours` = `0` (number)
- ปิด object `$[5]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L8

```json
  {"title": "ทบทวนก่อนสอบย่อย", "course": "คณิตศาสตร์", "due_date": "2026-10-08", "estimated_hours": 2, "done_hours": 0}
```

- เปิด object `$[6]` เก็บ key:value
- key `title`: ชื่องาน
- `$[6].title` = `"ทบทวนก่อนสอบย่อย"` (string)
- key `course`: วิชาที่เกี่ยวข้อง
- `$[6].course` = `"คณิตศาสตร์"` (string)
- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[6].due_date` = `"2026-10-08"` (string)
- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[6].estimated_hours` = `2` (number)
- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[6].done_hours` = `0` (number)
- ปิด object `$[6]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L9

```json
]
```

- ปิด array `$` จำนวน 7 รายการ
