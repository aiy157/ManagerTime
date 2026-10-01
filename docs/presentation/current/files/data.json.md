# data.json — ข้อมูลใช้งานจริง

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 124 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `37c0d8486cb635c457a7f93d0c2105be420c1321ce91483fd21f8b513ed33b47`

**ผู้ศึกษา/บทบาท:** ข้อมูลร่วมของทุกหน้า

## 1. หน้าที่และการเชื่อมต่อ

เก็บงานที่หน้า Manage บันทึกและทุกหน้าอ่าน

- **รับเข้า:** รายการที่ผ่าน Python validation
- **ผลลัพธ์:** JSON list ของ dict งาน 7 field

**เกี่ยวข้องกับ:** storage.py; models.Assignment; ทุกหน้า

## 2. ลำดับทำงาน

1. array ระดับบนเก็บหนึ่ง object ต่อหนึ่งงาน
2. field หลักเก็บชื่อ วิชา วัน และชั่วโมง
3. priority เก็บค่าระดับความสำคัญ
4. details เก็บ owner, started, subtasks, history และวันกิจกรรม

## 3. จุดที่ต้องอธิบายให้ถูก

- snapshot วันที่ 1 ตุลาคมมี 7 งาน เหลือรวม 25 ชั่วโมง มีหนึ่งงานถูกทำเครื่องหมายเสร็จตามการใช้งานจริง; ค่า due/stats เปลี่ยนตามวันเครื่อง
- history มีเหตุการณ์ complete ที่ผู้ใช้บันทึกไว้ ไม่ใช่ชั่วโมงทำงานจริง และไม่สร้างการทำงานย้อนหลังเพิ่มเติม
- การบันทึกเขียนทั้งไฟล์ ไม่ใช่ transaction ของฐานข้อมูล

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q010: ทำงานโดยไม่ต่ออินเทอร์เน็ตได้หรือไม่?](../TEACHER_QUESTIONS.md#q010)
- [Q015: list กับ dict ใช้ต่างกันอย่างไรในงานนี้?](../TEACHER_QUESTIONS.md#q015)
- [Q081: data.json เก็บกี่ field?](../TEACHER_QUESTIONS.md#q081)
- [Q082: ทำไมรายละเอียดใหม่อยู่ใน details?](../TEACHER_QUESTIONS.md#q082)
- [Q098: ทำไมบน Vercel บันทึกไม่ได้ และแก้แล้วเก็บถาวรหรือไม่?](../TEACHER_QUESTIONS.md#q098)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```json
[
  {
    "title": "รายงานการทดลองวงจร",
    "course": "ฟิสิกส์",
    "due_date": "2026-09-26",
    "estimated_hours": 6,
    "done_hours": 6,
    "priority": "normal",
    "details": {
      "owner": "",
      "started": true,
      "subtasks": [],
      "history": [
        {
          "date": "2026-10-01",
          "hours": 4,
          "kind": "complete",
          "note": "ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง"
        }
      ],
      "created_on": "",
      "progress_on": "2026-10-01",
      "before_complete": 2,
      "subtasks_before_complete": [],
      "completed_on": "2026-10-01"
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
    "done_hours": 6,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[0].done_hours` = `6` (number)
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
      "history": [
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[0].details.history` เก็บหลายรายการเรียงลำดับ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L14

```json
        {
```

- เปิด object `$[0].details.history[0]` เก็บ key:value

### L15

```json
          "date": "2026-10-01",
```

- key `date`: วันที่ของประวัติ
- `$[0].details.history[0].date` = `"2026-10-01"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L16

```json
          "hours": 4,
```

- key `hours`: ชั่วโมงตามชนิดรายการ
- `$[0].details.history[0].hours` = `4` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L17

```json
          "kind": "complete",
```

- key `kind`: ชนิด work/adjustment/complete/reopen
- `$[0].details.history[0].kind` = `"complete"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L18

```json
          "note": "ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง"
```

- key `note`: หมายเหตุ
- `$[0].details.history[0].note` = `"ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L19

```json
        }
```

- ปิด object `$[0].details.history[0]`

### L20

```json
      ],
```

- ปิด array `$[0].details.history` จำนวน 1 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L21

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[0].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L22

```json
      "progress_on": "2026-10-01",
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[0].details.progress_on` = `"2026-10-01"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L23

```json
      "before_complete": 2,
```

- key `before_complete`: ยอดก่อนกดปิดเพื่อเปิดกลับ
- `$[0].details.before_complete` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L24

```json
      "subtasks_before_complete": [],
```

- key `subtasks_before_complete`: ค่าของโครงสร้างนี้
- เปิด array `$[0].details.subtasks_before_complete` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[0].details.subtasks_before_complete` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L25

```json
      "completed_on": "2026-10-01"
```

- key `completed_on`: วันที่ปิดงาน
- `$[0].details.completed_on` = `"2026-10-01"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L26

```json
    }
```

- ปิด object `$[0].details`

### L27

```json
  },
```

- ปิด object `$[0]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L28

```json
  {
```

- เปิด object `$[1]` เก็บ key:value

### L29

```json
    "title": "แบบฝึกหัดอนุพันธ์",
```

- key `title`: ชื่องาน
- `$[1].title` = `"แบบฝึกหัดอนุพันธ์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L30

```json
    "course": "คณิตศาสตร์",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[1].course` = `"คณิตศาสตร์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L31

```json
    "due_date": "2026-09-27",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[1].due_date` = `"2026-09-27"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L32

```json
    "estimated_hours": 4,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[1].estimated_hours` = `4` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L33

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[1].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L34

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[1].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L35

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[1].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L36

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[1].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L37

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[1].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L38

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[1].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[1].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L39

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[1].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[1].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L40

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[1].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L41

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[1].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L42

```json
    }
```

- ปิด object `$[1].details`

### L43

```json
  },
```

- ปิด object `$[1]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L44

```json
  {
```

- เปิด object `$[2]` เก็บ key:value

### L45

```json
    "title": "สรุปผลห้องปฏิบัติการ",
```

- key `title`: ชื่องาน
- `$[2].title` = `"สรุปผลห้องปฏิบัติการ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L46

```json
    "course": "เคมี",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[2].course` = `"เคมี"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L47

```json
    "due_date": "2026-09-28",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[2].due_date` = `"2026-09-28"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L48

```json
    "estimated_hours": 5,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[2].estimated_hours` = `5` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L49

```json
    "done_hours": 1,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[2].done_hours` = `1` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L50

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[2].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L51

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[2].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L52

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[2].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L53

```json
      "started": true,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[2].details.started` = `true` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L54

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[2].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[2].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L55

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[2].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[2].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L56

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[2].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L57

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[2].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L58

```json
    }
```

- ปิด object `$[2].details`

### L59

```json
  },
```

- ปิด object `$[2]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L60

```json
  {
```

- เปิด object `$[3]` เก็บ key:value

### L61

```json
    "title": "นำเสนอหัวข้อภาษาอังกฤษ",
```

- key `title`: ชื่องาน
- `$[3].title` = `"นำเสนอหัวข้อภาษาอังกฤษ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L62

```json
    "course": "ภาษาอังกฤษ",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[3].course` = `"ภาษาอังกฤษ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L63

```json
    "due_date": "2026-10-01",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[3].due_date` = `"2026-10-01"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L64

```json
    "estimated_hours": 6,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[3].estimated_hours` = `6` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L65

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[3].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L66

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[3].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L67

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[3].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L68

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[3].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L69

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[3].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L70

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[3].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[3].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L71

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[3].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[3].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L72

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[3].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L73

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[3].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L74

```json
    }
```

- ปิด object `$[3].details`

### L75

```json
  },
```

- ปิด object `$[3]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L76

```json
  {
```

- เปิด object `$[4]` เก็บ key:value

### L77

```json
    "title": "โครงงานเขียนโปรแกรม",
```

- key `title`: ชื่องาน
- `$[4].title` = `"โครงงานเขียนโปรแกรม"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L78

```json
    "course": "การเขียนโปรแกรม",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[4].course` = `"การเขียนโปรแกรม"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L79

```json
    "due_date": "2026-10-04",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[4].due_date` = `"2026-10-04"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L80

```json
    "estimated_hours": 8,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[4].estimated_hours` = `8` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L81

```json
    "done_hours": 2,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[4].done_hours` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L82

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[4].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L83

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[4].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L84

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[4].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L85

```json
      "started": true,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[4].details.started` = `true` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L86

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[4].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[4].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L87

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[4].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[4].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L88

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[4].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L89

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[4].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L90

```json
    }
```

- ปิด object `$[4].details`

### L91

```json
  },
```

- ปิด object `$[4]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L92

```json
  {
```

- เปิด object `$[5]` เก็บ key:value

### L93

```json
    "title": "โปสเตอร์แนวคิดผลิตภัณฑ์",
```

- key `title`: ชื่องาน
- `$[5].title` = `"โปสเตอร์แนวคิดผลิตภัณฑ์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L94

```json
    "course": "การออกแบบ",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[5].course` = `"การออกแบบ"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L95

```json
    "due_date": "2026-10-06",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[5].due_date` = `"2026-10-06"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L96

```json
    "estimated_hours": 3,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[5].estimated_hours` = `3` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L97

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[5].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L98

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[5].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L99

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[5].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L100

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[5].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L101

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[5].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L102

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[5].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[5].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L103

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[5].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[5].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L104

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[5].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L105

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[5].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L106

```json
    }
```

- ปิด object `$[5].details`

### L107

```json
  },
```

- ปิด object `$[5]`
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L108

```json
  {
```

- เปิด object `$[6]` เก็บ key:value

### L109

```json
    "title": "ทบทวนก่อนสอบย่อย",
```

- key `title`: ชื่องาน
- `$[6].title` = `"ทบทวนก่อนสอบย่อย"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L110

```json
    "course": "คณิตศาสตร์",
```

- key `course`: วิชาที่เกี่ยวข้อง
- `$[6].course` = `"คณิตศาสตร์"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L111

```json
    "due_date": "2026-10-08",
```

- key `due_date`: วันส่งรูปแบบ YYYY-MM-DD
- `$[6].due_date` = `"2026-10-08"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L112

```json
    "estimated_hours": 2,
```

- key `estimated_hours`: ชั่วโมงรวมที่คาดว่าจะใช้
- `$[6].estimated_hours` = `2` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L113

```json
    "done_hours": 0,
```

- key `done_hours`: ยอดชั่วโมงความคืบหน้าสะสม
- `$[6].done_hours` = `0` (number)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L114

```json
    "priority": "normal",
```

- key `priority`: ความสำคัญ high/normal/low
- `$[6].priority` = `"normal"` (string)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L115

```json
    "details": {
```

- key `details`: รายละเอียดซ้อนของงาน
- เปิด object `$[6].details` เก็บ key:value
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L116

```json
      "owner": "",
```

- key `owner`: รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย
- `$[6].details.owner` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L117

```json
      "started": false,
```

- key `started`: boolean ว่าเริ่มงานแล้ว
- `$[6].details.started` = `false` (boolean)
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L118

```json
      "subtasks": [],
```

- key `subtasks`: list ขั้นตอนย่อย
- เปิด array `$[6].details.subtasks` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[6].details.subtasks` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L119

```json
      "history": [],
```

- key `history`: list ประวัติกิจกรรม/เวลา
- เปิด array `$[6].details.history` เก็บหลายรายการเรียงลำดับ
- ปิด array `$[6].details.history` จำนวน 0 รายการ
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L120

```json
      "created_on": "",
```

- key `created_on`: วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม
- `$[6].details.created_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L121

```json
      "progress_on": ""
```

- key `progress_on`: วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล
- `$[6].details.progress_on` = `""` (string); ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่
- comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment

### L122

```json
    }
```

- ปิด object `$[6].details`

### L123

```json
  }
```

- ปิด object `$[6]`

### L124

```json
]
```

- ปิด array `$` จำนวน 7 รายการ
