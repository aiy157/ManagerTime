# คำถามที่อาจารย์อาจถาม พร้อมแนวคำตอบ 100 ข้อ

โครงการเดดไลน์ไม่ชนกัน · CodeMind กลุ่ม 6 · 1 ตุลาคม 2569 (2026-10-01)

ชุดนี้เป็นแนวซ้อมจาก source และข้อกำหนดจริง ไม่รับประกันว่าอาจารย์จะถามทุกข้อ ตอบตามสิ่งที่มีในโค้ด ไม่อ้างว่ามี login, push, database หรือ commit ของทุกคนหากยังไม่มีหลักฐาน

## ลำดับอ่านแนะนำ

- ทุกคน: Q001–Q010, Q014–Q020 และ Q091–Q100
- นายวายุ: Q011–Q030, Q051–Q060 และ Q081–Q090
- นางสาวลักขณา: Q031–Q040 และ Q073–Q079
- นายไกรวิชญ์: Q041–Q050 และ Q061–Q072
- นายธีรเดช: Q051–Q060, Q091–Q100 และอ่าน Node/fixture ประกอบ

## 20 ข้อที่ควรตอบได้ก่อนนำเสนอ

Q001, Q003, Q005, Q008, Q011, Q012, Q015, Q021, Q022, Q027, Q030, Q032, Q037, Q043, Q046, Q054, Q055, Q077, Q092, Q093

## ปัญหาและสถาปัตยกรรม

**ผู้ซ้อมหลัก:** ทุกคน โดยนายวายุเริ่มอธิบาย

<a id="q001"></a>

### Q001 — โครงการนี้แก้ปัญหาอะไร?

**แนวคำตอบ:** ช่วยนักศึกษาที่มีงานหลายวิชารู้ว่าควรเริ่มชิ้นใดวันนี้และเวลาที่มีพอหรือไม่ โดยแสดงภาระสะสมและติดตามความคืบหน้า ไม่ได้เปลี่ยนกำหนดส่งให้ผู้สอนโดยอัตโนมัติ

**เปิดประกอบ:** [templates/home.html](files/templates/home.html.md), [pages/page1.py](files/pages/page1.py.md), [pages/page3.py](files/pages/page3.py.md)

<a id="q002"></a>

### Q002 — กลุ่มเป้าหมายคือใคร?

**แนวคำตอบ:** นักศึกษาหรือผู้ที่ต้องจัดงานหลายชิ้นกับเวลาว่างจำกัด ในโครงงานนี้ใช้ข้อมูลร่วมในเครื่องและมีสมาชิก CodeMind ให้มอบหมายงาน ยังไม่มีบัญชีแยกคน

**เปิดประกอบ:** [team.json](files/team.json.md), [pages/team.py](files/pages/team.py.md)

<a id="q003"></a>

### Q003 — ทำไมใช้ Python และ Flask?

**แนวคำตอบ:** อาจารย์กำหนด skeleton Python/Flask ไว้แล้ว จึงใช้โครงที่ให้และดัดแปลง catalog เพื่ออธิบาย if, loop, function และ class ตามรายวิชา Flask ใน app.py จัด route ให้โดยเราไม่แก้ไฟล์นั้น

**เปิดประกอบ:** [pages/page1.py](files/pages/page1.py.md), [models.py](files/models.py.md)

<a id="q004"></a>

### Q004 — Frontend และ Backend ต่างกันอย่างไร?

**แนวคำตอบ:** Backend คือ Python ที่ตรวจและคำนวณก่อนบันทึก Frontend คือ HTML/CSS และ JavaScript ที่ผู้ใช้เห็นหรือโต้ตอบ เปรียบเหมือนครัวคำนวณและจัดอาหาร ส่วนหน้าร้านแสดงเมนูกับรับคำสั่ง

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [templates/page2.html](files/templates/page2.html.md), [static/style.css](files/static/style.css.md)

<a id="q005"></a>

### Q005 — ทำไมหนึ่งหน้ามีทั้ง .py และ .html?

**แนวคำตอบ:** ไฟล์ .py คืนข้อมูลจาก build หรือรับ form ใน handle ส่วน .html ใช้ Jinja แสดงข้อมูล app.py จับคู่ตามชื่อ เช่น page1.py กับ page1.html ทำให้สูตรกับหน้าตาไม่ปะปน

**เปิดประกอบ:** [pages/page1.py](files/pages/page1.py.md), [templates/page1.html](files/templates/page1.html.md)

<a id="q006"></a>

### Q006 — หน้าแรกคือ index.html หรือไม่?

**แนวคำตอบ:** ไม่มี index.html ใน workspace นี้ route / ใช้ templates/home.html ซึ่ง extends base.html เป็นทางเข้าเว็บไซต์ ไม่อ่านงานเพื่อคำนวณยอด

**เปิดประกอบ:** [templates/home.html](files/templates/home.html.md)

<a id="q007"></a>

### Q007 — ผู้ใช้กดบันทึกแล้วข้อมูลเดินทางอย่างไร?

**แนวคำตอบ:** form method=post ส่งชื่อช่องกับค่าให้ app.py จากนั้นเรียก handle(form) ตรวจข้อมูลและ storage.save เมื่อผ่าน แล้ว redirect กลับ GET เพื่อ build และแสดงผลใหม่

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q008"></a>

### Q008 — build() กับ handle() ต่างกันอย่างไร?

**แนวคำตอบ:** build ทำงานเมื่อเปิดหน้า GET และคืน dict ให้ template handle ทำงานเมื่อส่งฟอร์ม POST และคืนข้อความผลการทำงาน ถ้าต้องเปลี่ยนข้อมูลใช้ handle พร้อม validation

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [pages/page3.py](files/pages/page3.py.md)

<a id="q009"></a>

### Q009 — ทำไมไม่เก็บงานในตัวแปรระดับบนของ page.py?

**แนวคำตอบ:** app.py โหลด page module ใหม่ทุก request ตัวแปรใน module จึงไม่ใช่ที่เก็บสถานะถาวร งานเก็บใน data.json ผ่าน storage และงบรายวันอยู่ settings

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [planner_settings.json](files/planner_settings.json.md)

<a id="q010"></a>

### Q010 — ทำงานโดยไม่ต่ออินเทอร์เน็ตได้หรือไม่?

**แนวคำตอบ:** ใช้งานในเครื่องได้เมื่อมี environment ของโครงการและเปิด Python server ไว้ ข้อมูล ฟอนต์สำรอง และไฟล์เว็บอยู่ในเครื่อง ยังไม่ใช่ PWA ที่ปิด server แล้วใช้ต่อได้หรือระบบ sync หลายเครื่อง

**เปิดประกอบ:** [static/style.css](files/static/style.css.md), [data.json](files/data.json.md)

## พื้นฐาน Python และคลาส

**ผู้ซ้อมหลัก:** นายวายุ; เจ้าของแต่ละหน้าอธิบายส่วนตน

<a id="q011"></a>

### Q011 — class Assignment คืออะไร?

**แนวคำตอบ:** เป็นแบบแทนงานหนึ่งชิ้น รวมข้อมูลชื่องาน วันส่ง ชั่วโมง และเมธอดพื้นฐาน เปรียบเหมือนแบบฟอร์มมาตรฐานเดียวที่สร้างงานได้หลายใบ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q012"></a>

### Q012 — __init__ มีหน้าที่อะไร?

**แนวคำตอบ:** ทำงานเมื่อสร้าง Assignment รับ field ของ row และเก็บเป็น attribute ของ object เช่น self.title ค่า priority/details มี default เพื่ออ่านข้อมูลเก่าได้

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q013"></a>

### Q013 — self หมายถึงอะไร?

**แนวคำตอบ:** หมายถึง object งานที่เมธอดกำลังทำงานอยู่ self.done_hours ของงาน A กับงาน B จึงแยกกัน ไม่ใช่ตัวแปรรวมของทั้งระบบ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q014"></a>

### Q014 — attribute กับ method ต่างกันอย่างไร?

**แนวคำตอบ:** attribute เก็บข้อมูล เช่น due_date ส่วน method เป็นการทำงานของ object เช่น remaining_hours() ที่ใช้ข้อมูลแล้วคืนคำตอบ เครื่องหมายวงเล็บแสดงการเรียกเมธอด

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q015"></a>

### Q015 — list กับ dict ใช้ต่างกันอย่างไรในงานนี้?

**แนวคำตอบ:** list เก็บงานหลายรายการและอ้างด้วยตำแหน่ง ส่วน dict เก็บ field ของงานหนึ่งชิ้น เช่น row['title'] details เป็น dict ซ้อนที่มี list ของ subtasks/history

**เปิดประกอบ:** [data.json](files/data.json.md), [models.py](files/models.py.md)

<a id="q016"></a>

### Q016 — for กับ while ใช้ตรงไหน?

**แนวคำตอบ:** for ใช้อ่านทุกงาน ทุกสมาชิก และทุกประวัติ while ใช้เลือกงานถัดไปในการเรียงจนรายการที่เหลือว่าง แต่ละรอบต้องเอารายการที่เลือกออกเพื่อให้จบ

**เปิดประกอบ:** [models.py](files/models.py.md), [pages/team.py](files/pages/team.py.md)

<a id="q017"></a>

### Q017 — if/elif/else ทำงานตามลำดับอย่างไร?

**แนวคำตอบ:** ตรวจเงื่อนไขแรกก่อน หากจริงทำส่วนนั้นและข้าม elif/else ในชุดเดียวกัน เช่นสถานะงานตรวจเสร็จก่อนกำลังทำ อย่างไรก็ตามชุด if วันส่งแยกจากชุดสถานะการทำงาน

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q018"></a>

### Q018 — return ต่างจาก print อย่างไร?

**แนวคำตอบ:** return ส่งคำตอบกลับให้ผู้เรียก เช่น build คืน dict ไป app.py ส่วน print แสดงข้อความใน terminal เช่นเว็บสาธิตบอกที่อยู่ ไม่มีการส่งผลแทน return

**เปิดประกอบ:** [pages/page1.py](files/pages/page1.py.md), [docs/qa/serve_fixture.py](files/docs/qa/serve_fixture.py.md)

<a id="q019"></a>

### Q019 — ทำไมใช้ form.get แทน form['x']?

**แนวคำตอบ:** บางช่องเช่น checkbox ที่ไม่ติ๊กไม่ถูกส่งมา get ใส่ default ได้และไม่เกิด KeyError แต่ยังต้องตรวจว่าค่านั้นถูกต้อง ไม่ใช่แค่มี default แล้วบันทึก

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md)

<a id="q020"></a>

### Q020 — try/except และ None ใช้เพื่ออะไร?

**แนวคำตอบ:** ลองแปลงตัวเลข/วันแล้วรับกรณีแปลงไม่ได้ ฟังก์ชันอ่านคืน None เพื่อบอกว่าไม่มีค่าที่ใช้ได้ ไม่ใช้ 0 แทนทุก error เพราะ 0 มีความหมายจริงใน done_hours

**เปิดประกอบ:** [models.py](files/models.py.md), [pages/page2.py](files/pages/page2.py.md)

## สูตรและฟังก์ชันร่วมใน models.py

**ผู้ซ้อมหลัก:** นายวายุ

<a id="q021"></a>

### Q021 — remaining_hours คำนวณอย่างไร?

**แนวคำตอบ:** นำ estimated_hours ลบ done_hours จำกัดอย่างน้อย 0 และ round 2 ตำแหน่ง เช่น 8−2 = 6 ชั่วโมง ผลลัพธ์เป็นค่าประมาณตามที่ผู้ใช้กรอก

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q022"></a>

### Q022 — progress คำนวณอย่างไร ทำไม 1.5 จาก 4 ได้ 37%?

**แนวคำตอบ:** done_hours × 100 ÷ estimated_hours แล้วใช้ int ตัดเศษ 37.5 จึงเป็น 37 ไม่ใช่ round เป็น 38 จำกัด 0–100 และกรณีเวลารวมไม่บวกคืน 0

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q023"></a>

### Q023 — days_left เป็นค่าติดลบได้หรือไม่?

**แนวคำตอบ:** ได้ เพราะวันส่งลบวันนี้ ถ้าวันส่งเมื่อวานจะเป็น −1 ใช้แสดงเกินกำหนดหนึ่งวัน การคำนวณตามวันที่เครื่อง Python ไม่มีเวลาส่งระดับชั่วโมง

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q024"></a>

### Q024 — ทำไมต้องตรวจ math.isfinite?

**แนวคำตอบ:** float('nan') หรือ float('inf') แปลงสำเร็จ แต่ไม่ใช่ชั่วโมงที่ใช้วางแผนได้ isfinite ปฏิเสธค่าพวกนี้ก่อนตรวจช่วงและบันทึก

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q025"></a>

### Q025 — ทำไม read_date ตรวจ isoformat กลับอีกครั้ง?

**แนวคำตอบ:** ต้องการรับ YYYY-MM-DD ที่เป็นวันจริงและรูปแบบมาตรฐาน แม้ตัวแปลงอ่านบางรูปแบบได้ก็ต้องเท่ากับรูปแบบ canonical ไม่รับ 20260930 เป็นวันส่ง

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q026"></a>

### Q026 — dict(row) กับ details_of คัดลอกต่างกันอย่างไร?

**แนวคำตอบ:** dict(row) สำเนา dict ระดับบน แต่ข้อมูลซ้อนยังอ้างร่วม details_of ใช้ json.dumps แล้ว json.loads เพื่อสำเนาข้อมูลซ้อนที่ serialize เป็น JSON ได้ ป้องกันเติมค่าหรือแก้งานย่อยของ view แล้วไปแตะ row ต้นฉบับ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q027"></a>

### Q027 — no กับ version ใช้เพื่ออะไร?

**แนวคำตอบ:** no คือ index งานใน list ตั้งแต่ 0 ส่วน version คือ SHA-256 ของเนื้อหา row ฟอร์มต้องตรงทั้งตำแหน่งและเนื้อหาล่าสุด มิฉะนั้นปฏิเสธ เพื่อไม่ไปแก้งานที่เลื่อนตำแหน่ง

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/_task_card.html](files/templates/_task_card.html.md)

<a id="q028"></a>

### Q028 — SHA-256 ในที่นี้เข้ารหัสข้อมูลหรือไม่?

**แนวคำตอบ:** ไม่ใช่การเข้ารหัสที่ถอดกลับได้และไม่ใช่รหัสผ่าน เป็นค่าตรวจว่า row เดิมเปลี่ยนหรือไม่ ไม่ให้ login หรือป้องกันการบันทึกพร้อมกันด้วย file lock

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q029"></a>

### Q029 — ทำไมไม่ใช้ sorted(key=...) และการเรียงมีต้นทุนเท่าไร?

**แนวคำตอบ:** ใช้ selection loop ตาม catalog/ranking และกติกาพื้นฐานของรายวิชา ต้องตรวจรายการที่เหลือหลายรอบ ลักษณะ O(n²) เหมาะกับข้อมูลเล็ก หากใช้งานจำนวนมากค่อยปรับตามขอบเขตใหม่

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q030"></a>

### Q030 — ทำไมแยก work, adjustment, complete, reopen?

**แนวคำตอบ:** เพื่อแยกเวลาทำจริงจากการแก้ยอด/ประกาศเสร็จ/ยกเลิกการปิด actual_total และ worked_today รวมเฉพาะ work ส่วนเหตุการณ์อื่นยังแสดงในประวัติให้ตรวจที่มาได้

**เปิดประกอบ:** [models.py](files/models.py.md), [pages/page2.py](files/pages/page2.py.md)

## หน้า Overview และคำแนะนำวันนี้

**ผู้ซ้อมหลัก:** นางสาวลักขณา

<a id="q031"></a>

### Q031 — Overview ตอบคำถามสำคัญอะไร?

**แนวคำตอบ:** วันนี้ควรเริ่มงานใด เพราะอะไร ควรแบ่งเวลาเท่าไร และยังมีงานค้างกี่รายการ พร้อมทางลัดเริ่ม ปิด และบันทึกเวลา

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md)

<a id="q032"></a>

### Q032 — เรียงตามความเร่งด่วนด้วยอะไร?

**แนวคำตอบ:** เทียบทีละเกณฑ์: เกินกำหนดก่อน วันส่งใกล้ก่อน ชั่วโมงคงเหลือมากก่อน ความเสี่ยงก่อน ความสำคัญสูงก่อน และ index เดิม หากเกณฑ์ก่อนต่างกันไม่ใช้เกณฑ์หลังทับลำดับ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q033"></a>

### Q033 — งานสำคัญสูงที่ส่งไกลจะขึ้นก่อนงานส่งพรุ่งนี้หรือไม่?

**แนวคำตอบ:** ตามโค้ดปัจจุบันไม่ เพราะวันส่งมาก่อน priority ความสำคัญสูงใช้เมื่อเกณฑ์ก่อนหน้าตรงกัน ต้องอธิบายตามลำดับ tuple จริง ไม่กล่าวว่า high ชนะทุกกรณี

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q034"></a>

### Q034 — ยังไม่เริ่มกับกำลังทำต่างกันอย่างไร?

**แนวคำตอบ:** ยังไม่เริ่มคือ remaining>0, started ไม่จริงและ done เป็น 0 กำลังทำเมื่อกด start หรือมี done>0 งานเสร็จตรวจ remaining=0 ก่อนสองสถานะนี้

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q035"></a>

### Q035 — งานกำลังทำและเกินกำหนดพร้อมกันได้หรือไม่?

**แนวคำตอบ:** ได้ เพราะสถานะการทำงานกับป้ายวันส่งเป็นคนละชุด เพื่อบอกทั้งความคืบหน้าและความเร่งด่วน ไม่บังคับให้ป้ายหนึ่งกลบอีกป้าย

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/_task_card.html](files/templates/_task_card.html.md)

<a id="q036"></a>

### Q036 — soon_count รวมงานเกินกำหนดหรือไม่?

**แนวคำตอบ:** ไม่รวม นับเฉพาะ pending ที่ days_left ตั้งแต่ 0 ถึง 3 รวมส่งวันนี้ งานเกินกำหนดไป overdue_count และงานเสร็จไม่ถูกนับ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q037"></a>

### Q037 — ทำไมเวลาแนะนำวันนี้ไม่เกินเวลาว่าง?

**แนวคำตอบ:** today_plan เริ่มด้วยงบที่เหลือหลังหัก work วันนี้ แต่ละงานใช้ min(remaining,budget) แล้วลด budget ก่อนงานถัดไป จึงไม่จัดสรรซ้ำเกินงบ

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q038"></a>

### Q038 — ทำวันนี้ 1.5 ชั่วโมง จากงบ 4 ระบบควรแนะนำเพิ่มเท่าไร?

**แนวคำตอบ:** รวมคำแนะนำเพิ่มได้ไม่เกิน 2.5 ชั่วโมง แม้งานที่ทำเสร็จแล้วมีประวัติ work วันนี้ เวลานั้นก็ถูกนับด้วยเพื่อไม่ใช้วันเดิมซ้ำ

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/page1.html](files/templates/page1.html.md)

<a id="q039"></a>

### Q039 — ถ้าวันนี้ครบงบแต่ยังมีงานค้าง ทำอย่างไร?

**แนวคำตอบ:** ไม่มี recommendations เพิ่มและแสดงว่าบันทึกเวลาครบงบแล้ว พร้อมให้ดูแผนวันถัดไป งานยังอยู่ใน pending ไม่ถูกทำเครื่องหมายเสร็จเอง

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md), [models.py](files/models.py.md)

<a id="q040"></a>

### Q040 — กดเสร็จแล้วตัวเลข Overview เปลี่ยนอย่างไร?

**แนวคำตอบ:** ตั้ง done เท่า estimate ปิดงานย่อยและบันทึก complete เมื่อเปิดหน้าใหม่ pending ลด completed เพิ่ม และงานออกจาก remaining_total แต่ actual_total ไม่เพิ่มตามชั่วโมงประมาณ

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/page1.html](files/templates/page1.html.md)

## Manage ฟอร์ม งานย่อย และประวัติ

**ผู้ซ้อมหลัก:** นายไกรวิชญ์

<a id="q041"></a>

### Q041 — ฟอร์มเพิ่มงานบังคับข้อมูลใด?

**แนวคำตอบ:** ชื่อ วิชา วันส่ง เวลารวม และยอดทำแล้วที่มีค่า default 0 ต้องถูกต้อง เลือก priority ที่มีในรายการ owner ไม่จำเป็น และงานย่อยไม่จำเป็น

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q042"></a>

### Q042 — ตรวจชั่วโมงช่วงเท่าไร?

**แนวคำตอบ:** estimate 0.1–200 และ done 0–estimate ชั่วโมงจริงของครั้งใหม่ต้องอย่างน้อย 0.1 และไม่เกิน remaining ตรวจค่าที่ finite ก่อนบันทึก

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md)

<a id="q043"></a>

### Q043 — ชั่วโมงทั้งหมด ชั่วโมงที่ทำแล้ว และชั่วโมงครั้งนี้ต่างกันอย่างไร?

**แนวคำตอบ:** estimated คือขนาดรวมงาน done คือยอดสะสม log_time.hours คือชั่วโมงที่เพิ่มในครั้งใหม่ เช่นรวม 4 ทำแล้ว 1 บันทึกครั้งนี้ 1.5 จะมียอด 2.5 ไม่แทนยอดเดิมเป็น 1.5

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q044"></a>

### Q044 — เลือกวันส่งอดีตแล้วทำไมยังบันทึกได้?

**แนวคำตอบ:** ระบบต้องติดตามงานค้าง จึงเพิ่มหรือเปลี่ยนไปอดีตได้เมื่อ acknowledge_past=yes พร้อมเตือน แต่หากแก้งานเดิมที่มีวันส่งอดีตเดิมอยู่แล้วไม่บังคับยืนยันซ้ำ

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [static/js/forms.js](files/static/js/forms.js.md)

<a id="q045"></a>

### Q045 — ถ้าปิด JavaScript จะข้าม validation ได้หรือไม่?

**แนวคำตอบ:** ไม่ Python check/log_time/change_subtask ตรวจซ้ำก่อน storage.save แม้เบราว์เซอร์ไม่มีข้อความทันที ข้อมูลผิดก็ถูกปฏิเสธ

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [static/js/forms.js](files/static/js/forms.js.md)

<a id="q046"></a>

### Q046 — ติ๊กงานย่อยแล้ว progress เพิ่มเองหรือไม่?

**แนวคำตอบ:** ไม่ งานย่อยวัดว่าขั้นตอนเสร็จหรือยัง เปอร์เซ็นต์หลักใช้ done_hours ต้องบันทึกชั่วโมงแยก เพื่อไม่เดาว่าแต่ละขั้นตอนใช้เวลามากเท่ากัน

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q047"></a>

### Q047 — งานย่อยมีข้อจำกัดอะไร?

**แนวคำตอบ:** ไม่เกิน 30 รายการ ชื่อ 1–100 ตัวอักษรหลัง trim เพิ่มในงาน pending ได้ และปุ่มตัวอย่างเติม 6 ขั้นตอน การแทนรายการตัวอย่างที่มีข้อความอยู่ถามยืนยันใน UI

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [static/js/forms.js](files/static/js/forms.js.md)

<a id="q048"></a>

### Q048 — ทำไมประวัติจริงไม่สร้างจาก done_hours เดิมทั้งหมด?

**แนวคำตอบ:** done เดิมอาจเป็นยอดรวมที่ไม่รู้วันทำและอาจมาจากการปรับประมาณ ถ้าสร้างวันที่ขึ้นเองจะให้ประวัติผิด จึงรวมรายวันเฉพาะรายการ work ที่ผู้ใช้บันทึก

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q049"></a>

### Q049 — กดเปิดกลับคืนอะไร และทุกงานเสร็จเปิดกลับได้หรือไม่?

**แนวคำตอบ:** คืนยอดและสถานะงานย่อยก่อนปุ่ม complete เฉพาะงานที่มี before_complete หากเสร็จจาก work จนครบและไม่มี snapshot ให้แก้ข้อมูลชั่วโมงผ่านฟอร์มแทน

**เปิดประกอบ:** [models.py](files/models.py.md), [templates/_task_card.html](files/templates/_task_card.html.md)

<a id="q050"></a>

### Q050 — กดลบงานแล้วประวัติยังอยู่หรือไม่?

**แนวคำตอบ:** ลบทั้ง row จึงลบ details/subtasks/history ของงานนั้นด้วย ไม่มีถังขยะ ต้องสำรองก่อนลองข้อมูลจริง หรือใช้เว็บ fixture ที่แยกข้อมูลชั่วคราว

**เปิดประกอบ:** [pages/page2.py](files/pages/page2.py.md), [docs/qa/serve_fixture.py](files/docs/qa/serve_fixture.py.md)

## Plan และคำถามคำนวณ

**ผู้ซ้อมหลัก:** นายธีรเดชและนายวายุ

<a id="q051"></a>

### Q051 — ทำไมคำนวณจำนวนวันด้วย days_left + 1?

**แนวคำตอบ:** นับวันนี้เป็นวันที่ทำงานได้ด้วย ส่งพรุ่งนี้ days_left=1 จึงมี 2 วัน ถ้าไม่นับวันนี้จะประเมินเวลาที่มีต่างจากสมมติฐานปัจจุบัน

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q052"></a>

### Q052 — ภาระสะสมคืออะไร?

**แนวคำตอบ:** ผลรวม remaining ของ pending ทุกงานที่ due_date ก่อนหรือเท่ากับ deadline ที่กำลังตรวจ รวมงานค้างอดีตด้วย เพื่อไม่ให้แต่ละงานใช้ความจุวันเดียวกันแยกกันจนดูเหมือนทันทั้งหมด

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q053"></a>

### Q053 — สองงาน 3 และ 4 ชั่วโมงส่งวันนี้ ว่าง 4 ผลเป็นอย่างไร?

**แนวคำตอบ:** ภาระของวันเดียวกัน 7 ชั่วโมง ความจุ 4 ขาดรวม 3 ทั้งสองการ์ดใช้ cumulative=7 และ gap=3 เหมือนกัน เพราะต้องเสร็จทั้งคู่ก่อนวันเดียวกัน

**เปิดประกอบ:** [models.py](files/models.py.md), [test_planner_features.py](files/test_planner_features.py.md)

<a id="q054"></a>

### Q054 — งาน 18 ชั่วโมงส่งพรุ่งนี้ ว่าง 4 ต่อวัน ขาดเท่าไร?

**แนวคำตอบ:** ไม่มี work วันนี้จึงมี 2 วัน ความจุ 8 ต้องเฉลี่ย 9 ขาด 5 ชั่วโมงต่อวัน และขาดรวม 10 ไม่บวกเฉลี่ยของงานหลายการ์ดซ้ำกัน

**เปิดประกอบ:** [models.py](files/models.py.md), [test_planner_features.py](files/test_planner_features.py.md)

<a id="q055"></a>

### Q055 — บันทึก work วันนี้แล้วสูตรความจุเปลี่ยนอย่างไร?

**แนวคำตอบ:** หัก min(ชั่วโมงจริงวันนี้,งบรายวัน) ออกจาก days×hours ชั่วโมงเฉลี่ยใช้ (cumulative+spent)/days เพื่อเทียบยอดที่เหลือกับวันที่ใช้ไปแล้วอย่างสอดคล้อง

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q056"></a>

### Q056 — ว่าง 2 วันนี้ทำแล้ว 1 แต่ยังเหลืองานวันนี้ 2 ผลเท่าไร?

**แนวคำตอบ:** ความจุที่เหลือ 1 ขาดรวม 1 ชั่วโมง ต้องเฉลี่ยของวันรวมที่ใช้ไปแล้ว 3 ชั่วโมงเทียบงบ 2 จึงขาด 1 ต่อวัน และแนะนำเพิ่มรวมไม่เกิน 1

**เปิดประกอบ:** [models.py](files/models.py.md), [test_planner_features.py](files/test_planner_features.py.md)

<a id="q057"></a>

### Q057 — งานเกินกำหนดถูกคำนวณหารด้วยวันติดลบหรือไม่?

**แนวคำตอบ:** ไม่ มี branch เกินกำหนดให้ available_hours=0 และ at_risk=True ภาระยังรวมในกำหนดอนาคต ควรติดต่อผู้สอนเพื่อตกลงวันใหม่ ไม่แสดงว่าชั่วโมงลบคือเวลาว่าง

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q058"></a>

### Q058 — ทำไมขาดจริง 0.01 แสดง 0.1 และยังเสี่ยง?

**แนวคำตอบ:** ตัดสิน raw_gap ก่อนปัดตัวเลข แล้ว ceil_tenth ปัดขึ้นหนึ่งตำแหน่งเพื่อไม่แสดงขาดเป็น 0 ชั่วโมงทั้งที่ยังมีส่วนขาด epsilon เล็กช่วยเรื่องคลาดเคลื่อนของ float

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q059"></a>

### Q059 — ค่าทดลอง hours ใน URL กับปุ่มบันทึกต่างกันอย่างไร?

**แนวคำตอบ:** GET hours ใช้คำนวณรอบแสดงนั้น ไม่บันทึกและไม่เปลี่ยน Overview แต่ POST save_hours เขียน settings เพื่อใช้ร่วม ค่าไม่ถูกต้องใช้เดิมพร้อมข้อความ

**เปิดประกอบ:** [pages/page3.py](files/pages/page3.py.md), [planner_settings.json](files/planner_settings.json.md)

<a id="q060"></a>

### Q060 — required_daily เป็น 0 แต่ยังมีงานเสี่ยงได้หรือไม่?

**แนวคำตอบ:** ได้ถ้าเหลือแต่งานเกินกำหนด ตัวสรุปหาเฉลี่ยเฉพาะ tasks ที่ days_left>=0 จึงไม่มีงานอนาคตให้หาเฉลี่ย งานอดีตยังเป็น at_risk และต้องจัดการ ไม่ใช่ไม่มีงานค้าง

**เปิดประกอบ:** [pages/page3.py](files/pages/page3.py.md), [models.py](files/models.py.md)

## HTML Jinja CSS และมือถือ

**ผู้ซ้อมหลัก:** นายไกรวิชญ์และเจ้าของ template

<a id="q061"></a>

### Q061 — extends base.html ทำอะไร?

**แนวคำตอบ:** ใช้โครงหัวเว็บ เมนู footer และ main เดิม แล้วแทนเนื้อหาใน block content ทำให้ทุกหน้ามีรูปแบบร่วมและไม่แก้ base ที่อาจารย์ห้ามแก้

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md), [templates/home.html](files/templates/home.html.md)

<a id="q062"></a>

### Q062 — {{ }} กับ {% %} ต่างกันอย่างไร?

**แนวคำตอบ:** {{ }} แสดงค่าหรือนิพจน์ เช่นชื่องาน ส่วน {% %} ควบคุม template เช่น if/for/block/macro ไม่ใช่ JavaScript และรันฝั่ง server ก่อนส่ง HTML

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md)

<a id="q063"></a>

### Q063 — macro ใน _task_card.html คืออะไร?

**แนวคำตอบ:** เป็นแม่แบบย่อยรับ item/page_name แล้วสร้าง HTML ใช้ซ้ำ row_fields ทำ hidden ค่า quick_actions ทำปุ่ม และ task_card ทำการ์ด เพื่อไม่ให้แต่ละหน้าส่ง version ต่างกัน

**เปิดประกอบ:** [templates/_task_card.html](files/templates/_task_card.html.md)

<a id="q064"></a>

### Q064 — ทำไมไฟล์ macro ไม่ extends base?

**แนวคำตอบ:** ไฟล์นี้เป็นส่วนย่อยที่ import ภายในหน้า ไม่ใช่หน้า route หาก extends base จะสร้างหัว/ท้ายเต็มซ้ำผิดหน้าที่ของ component

**เปิดประกอบ:** [templates/_task_card.html](files/templates/_task_card.html.md)

<a id="q065"></a>

### Q065 — input name กับ id ต่างกันอย่างไร?

**แนวคำตอบ:** name ใช้เป็น key ที่ส่งใน form เช่น action ส่วน id ใช้ผูก label/JavaScript และ anchor ใน DOM ช่องแต่ละงานเติม item.no เพื่อไม่ชนกัน

**เปิดประกอบ:** [templates/page2.html](files/templates/page2.html.md)

<a id="q066"></a>

### Q066 — hidden ป้องกันผู้ใช้แก้ค่าได้หรือไม่?

**แนวคำตอบ:** ไม่ เพียงไม่แสดงช่อง ผู้ใช้ส่งค่าเองได้ Python จึงตรวจ action, no, version และข้อมูลใหม่เสมอ hidden version ก็ไม่ใช่ตัวระบุสิทธิ์

**เปิดประกอบ:** [templates/_task_card.html](files/templates/_task_card.html.md), [models.py](files/models.py.md)

<a id="q067"></a>

### Q067 — ทำไมไม่ใช้สีบอกสถานะอย่างเดียว?

**แนวคำตอบ:** เพิ่มข้อความและไอคอนให้เข้าใจได้แม้แยกสีไม่สะดวก แถบ progress มี role และค่าตัวเลข ส่วน label/help ช่วยผู้ใช้และเครื่องมืออ่านหน้าจอ ยังไม่อ้างว่าผ่าน audit accessibility ทุกมาตรฐาน

**เปิดประกอบ:** [templates/_task_card.html](files/templates/_task_card.html.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q068"></a>

### Q068 — ทำอย่างไรให้เมนูและการ์ดเหมาะกับมือถือ?

**แนวคำตอบ:** CSS ใช้ flex-wrap, grid และ media queries 720/640 px ปรับการ์ด/ฟอร์มเป็นแนวตั้ง ลดขนาดองค์ประกอบตกแต่ง และให้ปุ่ม/ช่องหลักสูงอย่างน้อย 44px

**เปิดประกอบ:** [static/style.css](files/static/style.css.md)

<a id="q069"></a>

### Q069 — ตารางประวัติยาวกว่าจอจะทำอย่างไร?

**แนวคำตอบ:** อยู่ใน deadline-table-scroll ที่ overflow-x:auto ตารางมี min-width อ่านได้และเลื่อนเฉพาะกรอบ ไม่ทำให้ document ทั้งหน้ากว้างออกไป มี tabindex และ aria-label สำหรับการเข้าถึงกรอบ

**เปิดประกอบ:** [templates/page2.html](files/templates/page2.html.md), [static/style.css](files/static/style.css.md)

<a id="q070"></a>

### Q070 — มี Tailwind หรือโหลด Google Fonts หรือไม่?

**แนวคำตอบ:** ไม่มี ใช้ CSS ของ skeleton กับส่วนท้ายที่เพิ่ม ฟอนต์เป็น font stack ของเครื่อง เช่น Segoe UI/Sarabun/Noto Sans Thai หากไม่มีจะใช้ตัวถัดไป ไม่อ้างว่าได้ฟอนต์เดียวกันทุกเครื่อง

**เปิดประกอบ:** [static/style.css](files/static/style.css.md)

## JavaScript และการแจ้งเตือน

**ผู้ซ้อมหลัก:** นางสาวลักขณา; ไกรวิชญ์อธิบาย forms.js

<a id="q071"></a>

### Q071 — forms.js มีหน้าที่อะไร?

**แนวคำตอบ:** เพิ่มคำเตือนทันทีในฟอร์ม ยืนยันวันส่งอดีต ตั้ง aria-invalid เติมงานย่อยตัวอย่าง และเปิด details เมื่อเข้าลิงก์ #task-no ไม่เขียนไฟล์งานโดยตรง

**เปิดประกอบ:** [static/js/forms.js](files/static/js/forms.js.md)

<a id="q072"></a>

### Q072 — defer ที่ script หมายถึงอะไรในโครงการ?

**แนวคำตอบ:** ให้สคริปต์ภายนอกทำงานหลังเบราว์เซอร์แยก HTML เสร็จ โค้ดจึงหา form/reminder-data ที่อยู่ในหน้าได้ เรายังต้องตรวจว่า element มีจริงก่อนใช้

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md), [templates/page2.html](files/templates/page2.html.md)

<a id="q073"></a>

### Q073 — ระบบเตือนงานประเภทใด?

**แนวคำตอบ:** pending ที่ใกล้ส่งไม่เกิน 3 วัน/เกินกำหนด หรือ at_risk หรือมี today_hours>0 หรือ stale ใช้ OR ระหว่างเงื่อนไข งานเสร็จไม่เข้าเกณฑ์

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q074"></a>

### Q074 — ผู้ใช้ต้องอนุญาตอะไร?

**แนวคำตอบ:** ต้องกดเปิดการแจ้งเตือนและอนุญาต Notification จากเบราว์เซอร์ในบริบทที่รองรับ ถ้าถูก denied แสดงคำแนะนำการตั้งค่าและใช้ไฟล์ปฏิทิน ระบบงานยังใช้ได้

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q075"></a>

### Q075 — ทำไมไม่เตือนซ้ำทุกนาที?

**แนวคำตอบ:** signature จำชุดชื่อ วันส่ง ความเสี่ยง stale และการมีงานวันนี้ใน localStorage ตามวันกับตัวแปรของแท็บ เมื่อเหมือนเดิมจะข้าม ชุดเงื่อนไขใหม่จึงอาจเตือนเพิ่มได้

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q076"></a>

### Q076 — ข้อมูลในอีกแท็บเปลี่ยน ระบบเตือนรู้ได้อย่างไร?

**แนวคำตอบ:** fetch หน้า Overview เดิมทุก 60000 ms และเมื่อกลับมาเปิดแท็บ อ่าน JSON reminder-data ใหม่ ถ้าเปลี่ยนแสดงลิงก์โหลดภาพรวมใหม่ การ์ดบนหน้าจอไม่ได้ถูกแทนทั้งหมดเอง

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md), [templates/page1.html](files/templates/page1.html.md)

<a id="q077"></a>

### Q077 — ปิดเว็บแล้วแจ้งเตือนต่อหรือไม่?

**แนวคำตอบ:** ไม่มี service worker/push/background scheduler ในงานนี้ ต้องเปิด Overview และ Python ไว้ หากต้องการเตือนภายหลังใช้นำเข้า .ics ในแอปปฏิทินและตรวจสิทธิ์ของแอปนั้น

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q078"></a>

### Q078 — ถ้า server ไม่ตอบ การเตือนทำให้หน้าพังหรือไม่?

**แนวคำตอบ:** มี try/catch และ AbortController รอ 10 วินาที เก็บข้อมูลล่าสุดที่มีและปลด flag refreshing ใน finally อย่างไรก็ตามข้อมูลนั้นอาจเก่าจนดึงสำเร็จรอบถัดไป

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q079"></a>

### Q079 — ไฟล์ .ics สร้างกิจกรรมลักษณะใด?

**แนวคำตอบ:** VEVENT ทั้งวัน DTSTART คือวันส่ง DTEND คือวันถัดไปแบบไม่นับรวม VALARM ขอเตือน -P1D ผู้ใช้ต้องนำเข้าเอง ไม่ได้เรียก Google Calendar API หรือซิงก์อัตโนมัติ

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

<a id="q080"></a>

### Q080 — ทำไมต้อง escapeCalendarText และ revokeObjectURL?

**แนวคำตอบ:** escape backslash/newline/comma/semicolon ให้ข้อความเข้ารูปแบบไฟล์ปฏิทิน ส่วน revokeObjectURL คืนทรัพยากร URL ของ Blob หลังใช้ ไม่ใช่ลบงานใน data.json

**เปิดประกอบ:** [static/js/reminders.js](files/static/js/reminders.js.md)

## ข้อมูลและหน้าทีม

**ผู้ซ้อมหลัก:** นายวายุและเจ้าของงานที่สาธิต

<a id="q081"></a>

### Q081 — data.json เก็บกี่ field?

**แนวคำตอบ:** ต่อหนึ่งงานมี 7 field: title, course, due_date, estimated_hours, done_hours, priority, details ค่าแสดงผลอย่าง progress/no/gap เป็น view ที่คำนวณ ไม่ได้บันทึกเป็น field ใหม่ทุกครั้ง

**เปิดประกอบ:** [data.json](files/data.json.md), [models.py](files/models.py.md)

<a id="q082"></a>

### Q082 — ทำไมรายละเอียดใหม่อยู่ใน details?

**แนวคำตอบ:** รวมข้อมูลซ้อน owner/started/subtasks/history/วันกิจกรรมไว้ใต้ field เดียว โดยยังรักษาข้อมูลหลักของงานและขอบเขต 7 field ไม่กล่าวว่าข้อมูลซ้อนนับเป็น 7 ช่องทั้งหมด

**เปิดประกอบ:** [data.json](files/data.json.md)

<a id="q083"></a>

### Q083 — ข้อมูลเก่า 5 field ยังเปิดได้หรือไม่?

**แนวคำตอบ:** ได้ Assignment มี default และ details_of ใส่ค่าเริ่มต้น priority ปกติ รายการใหม่เขียน 7 field การเปิด GET ไม่ควร rewrite ไฟล์เก่าโดยอัตโนมัติ

**เปิดประกอบ:** [models.py](files/models.py.md), [test_planner_features.py](files/test_planner_features.py.md)

<a id="q084"></a>

### Q084 — sample ต่างจาก data อย่างไร?

**แนวคำตอบ:** data คือข้อมูลปัจจุบันที่ผู้ใช้แก้ sample คือชุดตั้งต้นสำหรับ reset ไม่เป็นสำรองสดอัตโนมัติ เมื่อรันตัวตรวจอาจทับ data ด้วย sample

**เปิดประกอบ:** [data.sample.json](files/data.sample.json.md), [check.bat](files/check.bat.md)

<a id="q085"></a>

### Q085 — ทำไมเก็บรหัสสมาชิกเป็น string?

**แนวคำตอบ:** เป็นตัวระบุสำหรับจับคู่ owner ไม่ได้นำมาบวก/ลบ และควรรักษาตัวอักษรทุกหลัก รวมกรณีรหัสขึ้นต้นศูนย์ตามรูปแบบข้อมูล

**เปิดประกอบ:** [team.json](files/team.json.md)

<a id="q086"></a>

### Q086 — Team นับจำนวนงานอย่างไร?

**แนวคำตอบ:** เลือกงานที่ details.owner ตรง member.id นับ assignment_count ทั้งหมด และ open_count เฉพาะ remaining>0 งานค้างที่ owner ว่างหรือไม่รู้จักแสดงใน unassigned

**เปิดประกอบ:** [pages/team.py](files/pages/team.py.md)

<a id="q087"></a>

### Q087 — Team คำนวณ progress ของสมาชิกอย่างไร?

**แนวคำตอบ:** รวม done ของงานทั้งหมดที่มอบหมายแล้วหารผลรวม estimate คูณ 100 ไม่ใช้ค่าเฉลี่ยเปอร์เซ็นต์รายงานที่ให้งานเล็ก/ใหญ่มีน้ำหนักเท่ากัน จำกัดสูงสุด 100

**เปิดประกอบ:** [pages/team.py](files/pages/team.py.md)

<a id="q088"></a>

### Q088 — ตัวอย่างงาน 2 ชม. เสร็จและงาน 8 ชม. ยังไม่เริ่ม progress เท่าไร?

**แนวคำตอบ:** รวม done=2 และ estimate=10 จึง 20% ไม่ใช่เฉลี่ย (100+0)/2=50% และยังคงมีงานค้างหนึ่งรายการ

**เปิดประกอบ:** [pages/team.py](files/pages/team.py.md)

<a id="q089"></a>

### Q089 — อะไรทำให้ขึ้นควรช่วยแบ่งงาน?

**แนวคำตอบ:** ชั่วโมงค้างมากกว่า daily_hours×7 หรือมีงานเสี่ยงตามกำหนดของคนนั้น เกณฑ์ใช้ชั่วโมงรายวันเดียวทุกคน ยังไม่วัดตารางเรียนหรือกำลังทำงานรายบุคคล

**เปิดประกอบ:** [pages/team.py](files/pages/team.py.md), [templates/team.html](files/templates/team.html.md)

<a id="q090"></a>

### Q090 — บทบาทสมาชิกกับงานที่มอบหมายและ Git เป็นเรื่องเดียวกันหรือไม่?

**แนวคำตอบ:** role/task ใน team.json คือการแบ่งหน้าที่รายวิชา owner คือผู้รับผิดชอบงานในแอป ส่วน commit ต้องตรวจ git log ของจริง การมีชื่อบน Team ไม่พิสูจน์ว่าเขียนหรือ commit ครบทุกคน

**เปิดประกอบ:** [team.json](files/team.json.md), [PAGES.md](files/PAGES.md.md)

## QA ความปลอดภัย และการตอบข้อจำกัด

**ผู้ซ้อมหลัก:** นายธีรเดช; ทุกคนต้องเข้าใจข้อจำกัด

<a id="q091"></a>

### Q091 — ตัวตรวจอาจารย์ได้ 60/60 แปลว่าได้ 100 แล้วหรือไม่?

**แนวคำตอบ:** ไม่ 60 คือส่วนหน้าเว็บและพื้นฐาน Python อีก 40 อาจารย์ประเมินทีม/นำเสนอ ผลตรวจไม่รับประกันทุกกรณีหรือคุณภาพระดับบริการจริง

**เปิดประกอบ:** [PAGES.md](files/PAGES.md.md), [check.bat](files/check.bat.md)

<a id="q092"></a>

### Q092 — pytest 55 passed ประกอบด้วยอะไร?

**แนวคำตอบ:** ของอาจารย์ 4 กรณี และของกลุ่ม 51 กรณี แบ่งเป็น 38 กรณีสำหรับคุณสมบัติเดิมกับ 13 กรณีสำหรับพื้นที่อ่านอย่างเดียว รวมการขยาย parameter จาก def เดียว จึงไม่ใช่ 55 ชื่อฟังก์ชันทดสอบ ผลรอบก่อนหน้าวันที่ 30 กันยายนมี 42 กรณี อ้าง QA ตามวันตรวจจริง

**เปิดประกอบ:** [test_planner_features.py](files/test_planner_features.py.md)

<a id="q093"></a>

### Q093 — ทดสอบอย่างไรไม่ให้ข้อมูลจริงหาย?

**แนวคำตอบ:** pytest เพิ่มใช้ tmp_path กับ monkeypatch เปลี่ยน data/sample/settings สำหรับการตรวจในเบราว์เซอร์ใช้ serve_fixture พอร์ต 5002 ส่วน check.bat ต้องสำรอง data แยกก่อนและคืนหลัง

**เปิดประกอบ:** [test_planner_features.py](files/test_planner_features.py.md), [docs/qa/serve_fixture.py](files/docs/qa/serve_fixture.py.md), [check.bat](files/check.bat.md)

<a id="q094"></a>

### Q094 — ทำไม HTTP 200 อย่างเดียวไม่พอพิสูจน์ว่าหน้าใช้ได้?

**แนวคำตอบ:** app.py อาจแสดงหน้า 'ยังไม่พร้อม' พร้อมสถานะ 200 ชุดทดสอบจึงตรวจข้อความนี้ด้วย และต้องทดสอบการบันทึก/สูตร/สถานะ ไม่ดูแค่ response code

**เปิดประกอบ:** [test_planner_features.py](files/test_planner_features.py.md)

<a id="q095"></a>

### Q095 — ชุด Node พิสูจน์ว่าแจ้งเตือนเด้งจริงหรือไม่?

**แนวคำตอบ:** ไม่ จำลอง DOM/Notification/fetch ใน vm ตรวจการตัดสินใจและไฟล์ ICS เท่านั้น ต้องลองสิทธิ์และการแจ้งเตือนของเบราว์เซอร์/OS บนเครื่องนำเสนอจริง

**เปิดประกอบ:** [docs/qa/test_reminders.cjs](files/docs/qa/test_reminders.cjs.md)

<a id="q096"></a>

### Q096 — ป้องกัน XSS อย่างไร?

**แนวคำตอบ:** แม่แบบ Jinja escape ชื่อ/ข้อความตามโครงเดิม และฝัง JSON ด้วย tojson มี test ตรวจว่าชื่อที่มี script ไม่กลายเป็นแท็กที่รัน แต่ยังไม่ใช่ security audit ของทุกเส้นทางใน app.py เดิม

**เปิดประกอบ:** [templates/page1.html](files/templates/page1.html.md), [test_planner_features.py](files/test_planner_features.py.md)

<a id="q097"></a>

### Q097 — version ป้องกันผู้ใช้สองคนบันทึกพร้อมกันทั้งหมดหรือไม่?

**แนวคำตอบ:** ไม่ ป้องกันฟอร์มที่เห็น row เก่า/เลื่อนตำแหน่งก่อนเริ่มบันทึก แต่ไม่มี atomic compare-and-swap/file lock ระหว่างอ่านและเขียน จึงยังมีโอกาสทับกันในระบบหลาย process

**เปิดประกอบ:** [models.py](files/models.py.md)

<a id="q098"></a>

### Q098 — ทำไมบน Vercel บันทึกไม่ได้ และแก้แล้วเก็บถาวรหรือไม่?

**แนวคำตอบ:** พื้นที่โครงการอ่านอย่างเดียวทำให้เกิด EROFS จึงมี configure_storage เลือกพื้นที่ชั่วคราวเมื่อพื้นที่เดิมเขียนไม่ได้และชี้ storage.DATA_FILE/settings ไปที่นั่น โดยไม่แก้ storage.py หน้าเว็บแจ้งว่าข้อมูลอาจหายหรือไม่ต่อเนื่อง หากต้องเก็บถาวรหลายคนต้องต่อฐานข้อมูลหรือพื้นที่ถาวรจริง เพิ่ม transaction/ID/สิทธิ์ ไม่ถือว่า /tmp แก้การเก็บข้อมูลถาวรแล้ว

**เปิดประกอบ:** [models.py](files/models.py.md), [data.json](files/data.json.md)

<a id="q099"></a>

### Q099 — ใช้ AI ช่วยแล้วอธิบายการทำงานอย่างไรให้ตรงความจริง?

**แนวคำตอบ:** กล่าวว่าใช้ผู้ช่วยตามกติกา แต่สมาชิกต้องศึกษาฟังก์ชันและอธิบายผล/ข้อจำกัดด้วยตนเอง ไม่กล่าวว่าเขียนทั้งหมดเองหรือมี commit ครบถ้าไม่มีหลักฐาน

**เปิดประกอบ:** [PAGES.md](files/PAGES.md.md)

<a id="q100"></a>

### Q100 — ถ้าอาจารย์ให้เปลี่ยนโจทย์หรือจับ bug สด ควรเริ่มตรงไหน?

**แนวคำตอบ:** หาว่าสิ่งที่เปลี่ยนเป็นข้อมูล สูตร หรือหน้าตา แล้วเปิด data/check หรือ models/template ที่รับผิดชอบ อธิบายกรณีคาดหวังก่อนแก้ จากนั้นรันทดสอบที่เกี่ยวข้องและคงไฟล์ห้ามแก้ไว้

**เปิดประกอบ:** [models.py](files/models.py.md), [pages/page2.py](files/pages/page2.py.md), [test_planner_features.py](files/test_planner_features.py.md)

## วิธีซ้อมให้ตอบจากความเข้าใจ

1. อ่านคำถามก่อน โดยยังไม่ดูคำตอบ
2. ตอบสั้น ๆ 20–40 วินาทีและชี้ฟังก์ชันหรือ field ที่ใช้จริง
3. หากเป็นสูตร ให้เขียนตัวเลขตัวอย่างก่อนเทียบหน้าจอ
4. ให้เพื่อนถามต่อว่า ถ้ารายการว่าง/ข้อมูลผิด/ปิดหน้า จะเกิดอะไร
5. ถ้าเป็นข้อจำกัดให้ตอบตรง ไม่เติมคุณสมบัติที่ยังไม่มี

อ่าน [สารบัญรายไฟล์](README.md), [คู่มือรวมพร้อมโค้ดทุกไฟล์](PROJECT_DETAIL_ALL.md) และ [ผังงานปัจจุบัน](../FLOWCHARTS.md)
