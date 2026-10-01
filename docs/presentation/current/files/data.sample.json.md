# data.sample.json — ข้อมูลตัวอย่างสำหรับคืนค่า

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 114 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `8de58894b4763ae0c8ce088b1096d6695773b861fbef8b2a019a45f27f0ee5df`

**ผู้ศึกษา/บทบาท:** ข้อมูลสำรองตั้งต้น

## 1. หน้าที่และการเชื่อมต่อ

เป็นต้นทางที่ storage.reset คืน data.json ระหว่างตรวจ

- **รับเข้า:** ชุดตัวอย่างที่ตั้งใจเก็บเป็น baseline
- **ผลลัพธ์:** งานตัวอย่าง 7 field เช่นเดียวกับ data.json

**เกี่ยวข้องกับ:** storage.reset; check_project.py

## 2. ลำดับทำงาน

1. อ่าน schema เช่นเดียวกับ data.json
2. ตัวตรวจอาจใช้ไฟล์นี้คัดลอกทับข้อมูลปัจจุบัน

## 3. จุดที่ต้องอธิบายให้ถูก

- sample ไม่ใช่ backup อัตโนมัติของงานล่าสุด
- ก่อน check.bat ต้องสำรอง data.json แยกไฟล์ และคืนหลังตรวจ
- ขณะจัดเอกสารนี้ data กับ sample เท่ากัน ไม่แปลว่าจะเท่ากันหลังผู้ใช้เพิ่มงาน

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q084: sample ต่างจาก data อย่างไร?](../TEACHER_QUESTIONS.md#q084)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```json
[
  {
    "title": "รายงานการทดลองวงจร",
    "course": "ฟิสิกส์",
    "due_date": "2026-09-26",
    "estimated_hours": 6,
    "done_hours": 2,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": true,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "แบบฝึกหัดอนุพันธ์",
    "course": "คณิตศาสตร์",
    "due_date": "2026-09-27",
    "estimated_hours": 4,
    "done_hours": 0,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": false,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "สรุปผลห้องปฏิบัติการ",
    "course": "เคมี",
    "due_date": "2026-09-28",
    "estimated_hours": 5,
    "done_hours": 1,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": true,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "นำเสนอหัวข้อภาษาอังกฤษ",
    "course": "ภาษาอังกฤษ",
    "due_date": "2026-10-01",
    "estimated_hours": 6,
    "done_hours": 0,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": false,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "โครงงานเขียนโปรแกรม",
    "course": "การเขียนโปรแกรม",
    "due_date": "2026-10-04",
    "estimated_hours": 8,
    "done_hours": 2,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": true,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "โปสเตอร์แนวคิดผลิตภัณฑ์",
    "course": "การออกแบบ",
    "due_date": "2026-10-06",
    "estimated_hours": 3,
    "done_hours": 0,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": false,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  },
  {
    "title": "ทบทวนก่อนสอบย่อย",
    "course": "คณิตศาสตร์",
    "due_date": "2026-10-08",
    "estimated_hours": 2,
    "done_hours": 0,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": false,
      "subtasks": [],
      "history": [],
      "created_on": "",
      "progress_on": ""
    }
  }
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
  {
```

- เปิด object `$[0]` เก็บ key:value

### L3

```json
    "title": "รายงานการทดลองวงจร",
```

- key `title`: ชื่องาน
- `$[0].title` = `"รายงานการทดลองวงจร"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L4

```json
    "course": "ฟิสิกส์",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[0].course` = `"ฟิสิกส์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L5

```json
    "due_date": "2026-09-26",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[0].due_date` = `"2026-09-26"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L6

```json
    "estimated_hours": 6,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[0].estimated_hours` = `6` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L7

```json
    "done_hours": 2,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[0].done_hours` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L8

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[0].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L9

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[0].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L10

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[0].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L11

```json
      "started": true,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[0].details.started` = `true` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L12

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[0].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[0].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L13

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[0].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[0].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L14

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[0].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L15

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[0].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L16

```json
    }
```

- ปิด object `$[0].details`

### L17

```json
  },
```

- ปิด object `$[0]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L18

```json
  {
```

- เปิด object `$[1]` เก็บ key:value

### L19

```json
    "title": "แบบฝึกหัดอนุพันธ์",
```

- key `title`: ชื่องาน
- `$[1].title` = `"แบบฝึกหัดอนุพันธ์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L20

```json
    "course": "คณิตศาสตร์",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[1].course` = `"คณิตศาสตร์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L21

```json
    "due_date": "2026-09-27",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[1].due_date` = `"2026-09-27"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L22

```json
    "estimated_hours": 4,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[1].estimated_hours` = `4` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L23

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[1].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L24

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[1].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L25

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[1].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L26

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[1].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L27

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[1].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L28

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[1].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[1].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L29

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[1].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[1].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L30

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[1].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L31

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[1].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L32

```json
    }
```

- ปิด object `$[1].details`

### L33

```json
  },
```

- ปิด object `$[1]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L34

```json
  {
```

- เปิด object `$[2]` เก็บ key:value

### L35

```json
    "title": "สรุปผลห้องปฏิบัติการ",
```

- key `title`: ชื่องาน
- `$[2].title` = `"สรุปผลห้องปฏิบัติการ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L36

```json
    "course": "เคมี",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[2].course` = `"เคมี"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L37

```json
    "due_date": "2026-09-28",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[2].due_date` = `"2026-09-28"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L38

```json
    "estimated_hours": 5,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[2].estimated_hours` = `5` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L39

```json
    "done_hours": 1,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[2].done_hours` = `1` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L40

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[2].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L41

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[2].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L42

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[2].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L43

```json
      "started": true,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[2].details.started` = `true` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L44

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[2].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[2].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L45

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[2].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[2].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L46

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[2].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L47

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[2].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L48

```json
    }
```

- ปิด object `$[2].details`

### L49

```json
  },
```

- ปิด object `$[2]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L50

```json
  {
```

- เปิด object `$[3]` เก็บ key:value

### L51

```json
    "title": "นำเสนอหัวข้อภาษาอังกฤษ",
```

- key `title`: ชื่องาน
- `$[3].title` = `"นำเสนอหัวข้อภาษาอังกฤษ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L52

```json
    "course": "ภาษาอังกฤษ",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[3].course` = `"ภาษาอังกฤษ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L53

```json
    "due_date": "2026-10-01",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[3].due_date` = `"2026-10-01"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L54

```json
    "estimated_hours": 6,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[3].estimated_hours` = `6` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L55

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[3].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L56

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[3].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L57

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[3].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L58

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[3].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L59

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[3].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L60

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[3].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[3].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L61

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[3].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[3].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L62

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[3].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L63

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[3].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L64

```json
    }
```

- ปิด object `$[3].details`

### L65

```json
  },
```

- ปิด object `$[3]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L66

```json
  {
```

- เปิด object `$[4]` เก็บ key:value

### L67

```json
    "title": "โครงงานเขียนโปรแกรม",
```

- key `title`: ชื่องาน
- `$[4].title` = `"โครงงานเขียนโปรแกรม"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L68

```json
    "course": "การเขียนโปรแกรม",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[4].course` = `"การเขียนโปรแกรม"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L69

```json
    "due_date": "2026-10-04",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[4].due_date` = `"2026-10-04"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L70

```json
    "estimated_hours": 8,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[4].estimated_hours` = `8` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L71

```json
    "done_hours": 2,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[4].done_hours` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L72

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[4].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L73

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[4].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L74

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[4].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L75

```json
      "started": true,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[4].details.started` = `true` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L76

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[4].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[4].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L77

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[4].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[4].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L78

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[4].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L79

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[4].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L80

```json
    }
```

- ปิด object `$[4].details`

### L81

```json
  },
```

- ปิด object `$[4]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L82

```json
  {
```

- เปิด object `$[5]` เก็บ key:value

### L83

```json
    "title": "โปสเตอร์แนวคิดผลิตภัณฑ์",
```

- key `title`: ชื่องาน
- `$[5].title` = `"โปสเตอร์แนวคิดผลิตภัณฑ์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L84

```json
    "course": "การออกแบบ",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[5].course` = `"การออกแบบ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L85

```json
    "due_date": "2026-10-06",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[5].due_date` = `"2026-10-06"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L86

```json
    "estimated_hours": 3,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[5].estimated_hours` = `3` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L87

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[5].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L88

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[5].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L89

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[5].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L90

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[5].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L91

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[5].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L92

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[5].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[5].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L93

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[5].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[5].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L94

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[5].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L95

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[5].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L96

```json
    }
```

- ปิด object `$[5].details`

### L97

```json
  },
```

- ปิด object `$[5]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L98

```json
  {
```

- เปิด object `$[6]` เก็บ key:value

### L99

```json
    "title": "ทบทวนก่อนสอบย่อย",
```

- key `title`: ชื่องาน
- `$[6].title` = `"ทบทวนก่อนสอบย่อย"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L100

```json
    "course": "คณิตศาสตร์",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[6].course` = `"คณิตศาสตร์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L101

```json
    "due_date": "2026-10-08",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[6].due_date` = `"2026-10-08"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L102

```json
    "estimated_hours": 2,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[6].estimated_hours` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L103

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[6].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L104

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[6].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L105

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[6].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L106

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[6].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L107

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[6].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L108

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[6].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[6].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L109

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[6].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[6].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L110

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[6].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L111

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[6].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L112

```json
    }
```

- ปิด object `$[6].details`

### L113

```json
  }
```

- ปิด object `$[6]`

### L114

```json
]
```

- ปิด array `$` จำนวน 7 รายการ
