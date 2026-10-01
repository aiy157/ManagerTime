# check.bat — ตัวเรียกตรวจของอาจารย์ (อ่านประกอบ ไม่ได้แก้)

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 10 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `4066797dd0e410fb8ead9ce9e20676deab95100982781a1f1c8d1f97e6832345`

**ผู้ศึกษา/บทบาท:** อาจารย์ให้; ธีรเดชเป็นผู้ใช้ตรวจ

## 1. หน้าที่และการเชื่อมต่อ

รันตัวตรวจคะแนนและ pytest ด้วย Python ใน .venv

- **รับเข้า:** โปรเจกต์ในโฟลเดอร์เดียวกับสคริปต์
- **ผลลัพธ์:** คะแนน/คำเตือนและผล pytest ใน terminal

**เกี่ยวข้องกับ:** .venv/Scripts/python.exe; check_project.py; test_pages.py/test_planner_features.py

## 2. ลำดับทำงาน

1. ตั้ง terminal UTF-8 และย้ายไปโฟลเดอร์สคริปต์
2. ตรวจว่ามี virtual environment
3. เรียก check_project.py จากนั้น pytest -q
4. pause ให้ผู้ใช้ดูผล

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่ได้รัน Node test_reminders.cjs ให้อัตโนมัติ
- ตัวตรวจ Python คืน data.json จาก sample จึงต้องสำรองก่อน
- ชื่อสมาชิกที่ดูแล check.bat ไม่ได้แปลว่าเป็นผู้เขียนสคริปต์เดิม

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q084: sample ต่างจาก data อย่างไร?](../TEACHER_QUESTIONS.md#q084)
- [Q091: ตัวตรวจอาจารย์ได้ 60/60 แปลว่าได้ 100 แล้วหรือไม่?](../TEACHER_QUESTIONS.md#q091)
- [Q093: ทดสอบอย่างไรไม่ให้ข้อมูลจริงหาย?](../TEACHER_QUESTIONS.md#q093)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```bat
@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (echo Run setup.bat first. & pause & exit /b 1)
set PYTHONIOENCODING=utf-8
".venv\Scripts\python.exe" check_project.py
echo.
echo --- pytest ---
".venv\Scripts\python.exe" -m pytest -q
pause
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```bat
@echo off
```

- ปิดการแสดงคำสั่งแต่ยังแสดงผลลัพธ์ เพื่อลดความรก terminal

### L2

```bat
chcp 65001 >nul
```

- เปลี่ยน code page เป็น UTF-8 แล้วซ่อนข้อความคำสั่งด้วย >nul

### L3

```bat
cd /d "%~dp0"
```

- ย้าย drive/โฟลเดอร์เป็นตำแหน่งสคริปต์จาก %~dp0

### L4

```bat
if not exist .venv\Scripts\python.exe (echo Run setup.bat first. & pause & exit /b 1)
```

- หากไม่มี Python ใน .venv ให้บอกทำ setup, pause และ exit /b 1

### L5

```bat
set PYTHONIOENCODING=utf-8
```

- ตั้ง encoding ของ stdout/stderr Python เป็น UTF-8

### L6

```bat
".venv\Scripts\python.exe" check_project.py
```

- เรียกตัวตรวจอาจารย์ซึ่งตรวจคะแนน/hash และอาจ reset data จาก sample

### L7

```bat
echo.
```

- แสดงบรรทัดว่าง

### L8

```bat
echo --- pytest ---
```

- แสดงหัวข้อ pytest

### L9

```bat
".venv\Scripts\python.exe" -m pytest -q
```

- รัน pytest -q ผ่าน Python ใน .venv รวม test file ที่พบ

### L10

```bat
pause
```

- pause รอผู้ใช้ดูผลก่อนปิดหน้าต่าง
