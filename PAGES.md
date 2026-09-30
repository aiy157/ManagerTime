# PAGES · แดชบอร์ดความคืบหน้า

กรอกสัปดาห์ที่ 1 แล้วอัปเดตทุกครั้งที่ commit — อาจารย์ดูไฟล์นี้ + `git log` แทนการถาม

**หัวข้อ:** เดดไลน์ไม่ชนกัน
**ชื่อกลุ่ม:** CodeMind · กลุ่ม 6
**data.json เก็บอะไร (field):** title, course, due_date, estimated_hours, done_hours
**คัดลอก data.json → data.sample.json แล้ว:** [x]

## team — หน้าทีม (สัปดาห์ 0)
- [x] กรอก `team.json` ครบทุกคน (ชื่อ, รหัส, บทบาท, งานที่รับผิดชอบ)
- [x] เปิด /team เห็นชื่อทุกคน
- [ ] commit `team: members filled` + push

## page1 — ผู้รับผิดชอบ: นางสาวลักขณา ศรีโพธิ์ · แบบจาก catalog: list + stats
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page1 ได้ ไม่มี TODO
- [x] `check.bat` → /page1 ✓ ไม่มี warning
- [ ] commit `page1: ...`

## page2 — ผู้รับผิดชอบ: นายไกรวิชญ์ บุ้งทอง · แบบจาก catalog: form
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page2 ได้ ไม่มี TODO
- [x] `check.bat` → /page2 ✓ ไม่มี warning
- [ ] commit `page2: ...`

## page3 — ผู้รับผิดชอบ: นายธีรเดช ฤทธิ์คำรพ · แบบจาก catalog: ranking + calculator
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
- [x] ใช้ field ของ data.json ของกลุ่ม
- [x] เปิด /page3 ได้ ไม่มี TODO
- [x] `check.bat` → /page3 ✓ ไม่มี warning
- [ ] commit `page3: ...`

## models.py — ผู้รับผิดชอบ: นายวายุ ทาโสม
- [x] เปลี่ยนชื่อ class ให้ตรงหัวข้อ, field ตรง data.json
- [x] method 1 ตัวที่มีประโยชน์ (ไม่เหลือ TODO)
- [x] มีหน้าใดหน้าหนึ่งใช้ class นี้ (เช่น แบบ detail)
- [x] `python check_project.py` → class ✓ 9/9
- [ ] commit `models: ...`

## ส่งงาน
- [x] `check.bat` → 60/60, pytest 4 passed, ไม่มี warning
- [ ] ทุกคนอยู่ใน `git log`
- [ ] นำเสนอ: ทุกคนอธิบายหน้าของตัวเอง 1 นาที

## หมายเหตุเรื่องข้อมูล

หน้านี้มีฟอร์มบันทึกงาน ก่อนรัน `check.bat` หรือ `check.sh` หลังจากกรอกงานจริงแล้ว ให้คัดลอก `data.json` ไป `data.sample.json` ก่อน เพราะตัวตรวจจะคืน `data.json` จากไฟล์สำรองนี้เมื่อทดสอบฟอร์ม
