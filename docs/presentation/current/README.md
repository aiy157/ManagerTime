# คู่มือศึกษาและซ้อมตอบ — โค้ดปัจจุบัน

เดดไลน์ไม่ชนกัน · CodeMind กลุ่ม 6 · 30 กันยายน 2569 (2026-09-30)

## เริ่มอ่านจากสามส่วนนี้

1. [คำถามอาจารย์พร้อมแนวคำตอบ 100 ข้อ](TEACHER_QUESTIONS.md)
2. [คู่มือรวมทุกไฟล์พร้อมโค้ดและคำอธิบาย](PROJECT_DETAIL_ALL.md)
3. รายละเอียดเฉพาะไฟล์ในตารางด้านล่าง

ครอบคลุม 26 ไฟล์โค้ด/ข้อมูล/เครื่องมือประกอบ รวม 2508 physical lines แต่ละไฟล์มีหน้าที่ ข้อมูลรับเข้า/ส่งออก ความสัมพันธ์ ลำดับทำงาน จุดที่ต้องระวัง โค้ดครบ และคำอธิบายรายบรรทัดพร้อม SHA-256

**ชื่อไฟล์จริง:** หน้าแรกใช้ templates/home.html ไม่มี index.html ในโครงการนี้

**ขอบเขต:** อธิบายไฟล์ของโครงการครบ รวมหน้าแรกและข้อมูลทีมที่มีอยู่ก่อนรอบล่าสุด และอธิบาย check.bat เดิมเป็นบริบท QA ไม่กล่าวว่าแก้ไฟล์เดิมทั้งหมด ไฟล์เอกสาร/ภาพประกอบมีรายการกำกับในคู่มือรวม ไม่วนอธิบายเอกสารที่กำลังสร้างเอง

## สารบัญรายไฟล์

| ไฟล์จริง | รายละเอียด | บรรทัด | หน้าที่ |
|---|---|---:|---|
| `models.py` | [เปิดอ่าน](files/models.py.md) | 450 | คลาสและกติกากลางของระบบ |
| `pages/page1.py` | [เปิดอ่าน](files/pages/page1.py.md) | 23 | Python ของหน้า Overview |
| `pages/page2.py` | [เปิดอ่าน](files/pages/page2.py.md) | 173 | Python ของหน้าจัดการงาน |
| `pages/page3.py` | [เปิดอ่าน](files/pages/page3.py.md) | 38 | Python ของหน้า Plan |
| `pages/team.py` | [เปิดอ่าน](files/pages/team.py.md) | 64 | Python ของหน้าทีม |
| `templates/home.html` | [เปิดอ่าน](files/templates/home.html.md) | 17 | HTML/Jinja ของหน้าแรก |
| `templates/page1.html` | [เปิดอ่าน](files/templates/page1.html.md) | 82 | HTML/Jinja ของ Overview |
| `templates/page2.html` | [เปิดอ่าน](files/templates/page2.html.md) | 134 | HTML/Jinja ของ Manage |
| `templates/page3.html` | [เปิดอ่าน](files/templates/page3.html.md) | 55 | HTML/Jinja ของ Plan |
| `templates/team.html` | [เปิดอ่าน](files/templates/team.html.md) | 38 | HTML/Jinja ของ Team |
| `templates/_task_card.html` | [เปิดอ่าน](files/templates/_task_card.html.md) | 60 | Macro ฟอร์มและการ์ดร่วม |
| `static/style.css` | [เปิดอ่าน](files/static/style.css.md) | 359 | CSS เดิมและส่วนที่เพิ่มสำหรับโครงการ |
| `static/js/forms.js` | [เปิดอ่าน](files/static/js/forms.js.md) | 62 | JavaScript ช่วยตรวจและใช้งานฟอร์ม |
| `static/js/reminders.js` | [เปิดอ่าน](files/static/js/reminders.js.md) | 153 | JavaScript แจ้งเตือนและไฟล์ปฏิทิน |
| `data.json` | [เปิดอ่าน](files/data.json.md) | 114 | ข้อมูลใช้งานจริง |
| `data.sample.json` | [เปิดอ่าน](files/data.sample.json.md) | 114 | ข้อมูลตัวอย่างสำหรับคืนค่า |
| `team.json` | [เปิดอ่าน](files/team.json.md) | 14 | ชื่อกลุ่ม สมาชิก และหน้าที่รายวิชา |
| `planner_settings.json` | [เปิดอ่าน](files/planner_settings.json.md) | 3 | งบเวลาว่างรายวัน |
| `test_planner_features.py` | [เปิดอ่าน](files/test_planner_features.py.md) | 325 | ชุดทดสอบธุรกิจเพิ่มเติม |
| `docs/qa/serve_fixture.py` | [เปิดอ่าน](files/docs/qa/serve_fixture.py.md) | 43 | เว็บสาธิตด้วยข้อมูลชั่วคราว |
| `docs/qa/test_reminders.cjs` | [เปิดอ่าน](files/docs/qa/test_reminders.cjs.md) | 97 | ชุดทดสอบ JavaScript ด้วยส่วนจำลอง |
| `PAGES.md` | [เปิดอ่าน](files/PAGES.md.md) | 61 | แผนแบ่งหน้าที่และความคืบหน้า |
| `README.md` | [เปิดอ่าน](files/README.md.md) | 1 | README ระดับ repository |
| `check.bat` | [เปิดอ่าน](files/check.bat.md) | 10 | ตัวเรียกตรวจของอาจารย์ (อ่านประกอบ ไม่ได้แก้) |
| `docs/qa/before_upgrade/data.json` | [เปิดอ่าน](files/docs/qa/before_upgrade/data.json.md) | 9 | สำเนางานก่อนเพิ่ม field |
| `docs/qa/before_upgrade/data.sample.json` | [เปิดอ่าน](files/docs/qa/before_upgrade/data.sample.json.md) | 9 | สำเนา sample ก่อนเพิ่ม field |

## อ่านตามหน้าที่

- **วายุ:** models.py, data/sample/settings/team JSON และสูตร Plan
- **ลักขณา:** page1.py/page1.html, macro การ์ด และ reminders.js
- **ไกรวิชญ์:** page2.py/page2.html, style.css, forms.js และ macro
- **ธีรเดช:** page3.py/page3.html, test_planner_features.py, check.bat, fixture และ Node tests
- **ทุกคน:** home.html, Team, ข้อจำกัด และการเดินทางของข้อมูล GET/POST

## เอกสารประกอบที่ยังใช้ได้

- [ผังงานแต่ละหน้า](../FLOWCHARTS.md)
- [บทนำเสนอแบ่งสมาชิก](../PRESENTATION_SCRIPT.md)
- [สรุปผู้ทดสอบ](../TESTER_SUMMARY.md)
- [สูตรและกติกาปัจจุบัน](../UPGRADE_DETAILS.md)
- [รายงานตรวจจริง](../../qa/QA_REPORT.md)

คู่มือ PYTHON_DETAIL/FRONTEND_DETAIL/JAVASCRIPT_DATA_DETAIL เดิมเป็นประวัติฉบับแรก สำหรับเลขบรรทัดปัจจุบันให้อ่านชุด current นี้

## การตรวจความตรงกับ source

source_manifest.json เก็บชื่อไฟล์ จำนวนบรรทัด SHA และจำนวนคำอธิบาย ต้องเทียบ SHA ใหม่เมื่อแก้ source ก่อนใช้เลขบรรทัดตอบอาจารย์ เอกสาร snapshot ไม่เปลี่ยนเองเมื่อผู้ใช้แก้ data หรือเพิ่มงานผ่านเว็บไซต์

การสร้างชุดนี้ตรวจ source/hash/JSON/แม่แบบและความครบถ้วนของเอกสาร ไม่ใช่การรันทดสอบการทำงานทั้งหมดซ้ำ ผล 42 passed/60 คะแนนให้ดูวันตรวจใน QA_REPORT
