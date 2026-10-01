# models.py — คลาสและกติกากลางของระบบ

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 450 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `f29d799be760ceeddac418fd3313fc5de5e6f9cc47b365444bae9571094422ba`

**ผู้ศึกษา/บทบาท:** นายวายุ ทาโสม · PM

## 1. หน้าที่และการเชื่อมต่อ

แทนงานหนึ่งชิ้นด้วย Assignment และรวมสูตร ลำดับงาน สถานะ ประวัติ และการเปลี่ยนสถานะที่ทุกหน้าใช้ร่วมกัน

- **รับเข้า:** row งาน 7 field, สมาชิกจาก team.json, form ที่ app.py ส่งให้ และชั่วโมงว่างรายวัน
- **ผลลัพธ์:** ข้อมูลแสดงผลที่คำนวณแล้ว dict/list/tuple และข้อความผลการบันทึก; บางฟังก์ชันเขียน data.json หรือ settings

**เกี่ยวข้องกับ:** storage.py (อ่าน/เขียนงาน); team.json (ข้อมูลสมาชิก); planner_settings.json (งบรายวัน); datetime, hashlib, json, math, os (standard library)

## 2. ลำดับทำงาน

1. สร้าง Assignment จาก field หลักและคำนวณ remaining/days/progress
2. สร้าง view ของงาน เติมเจ้าของ สถานะ ป้ายวันส่ง งานย่อย และ version
3. รวมภาระงานตามกำหนดส่ง หักเวลา work วันนี้ และตรวจเวลาไม่พอ
4. เรียงลำดับแล้วแบ่งเวลาวันนี้ไม่เกินงบคงเหลือ
5. แยก completed และนับสถิติพร้อม focus
6. ตรวจ version ของฟอร์มก่อนเปลี่ยนสถานะและบันทึก
7. รวม history แบบแยกชั่วโมงทำจริงจากเหตุการณ์อื่น

## 3. จุดที่ต้องอธิบายให้ถูก

- dict(row) สำเนาระดับบน; details_of ใช้ JSON round trip เพื่อคัดลอกข้อมูลซ้อนที่เป็น JSON
- ไม่มี permanent ID สำหรับงาน; no เป็นตำแหน่งเริ่ม 0 และ SHA ตรวจเนื้อหาเดิม
- hash ไม่ใช่ login, CSRF token หรือ file lock; JSON พร้อมกันหลาย process ยังอาจเขียนทับ
- progress เป็นยอด done_hours จึงรวมผลปิดงานตามประมาณ ส่วน actual_total รวม work เท่านั้น
- ceil_tenth ใช้ epsilon เล็กน้อยเพื่อลดผลคลาดเคลื่อน float; ความเสี่ยงตัดสินจาก raw_gap
- selection loop และการรวมภาระมีลักษณะ O(n²) เหมาะกับข้อมูลขนาดเล็กในรายวิชา

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q003: ทำไมใช้ Python และ Flask?](../TEACHER_QUESTIONS.md#q003)
- [Q011: class Assignment คืออะไร?](../TEACHER_QUESTIONS.md#q011)
- [Q012: __init__ มีหน้าที่อะไร?](../TEACHER_QUESTIONS.md#q012)
- [Q013: self หมายถึงอะไร?](../TEACHER_QUESTIONS.md#q013)
- [Q014: attribute กับ method ต่างกันอย่างไร?](../TEACHER_QUESTIONS.md#q014)
- [Q015: list กับ dict ใช้ต่างกันอย่างไรในงานนี้?](../TEACHER_QUESTIONS.md#q015)
- [Q016: for กับ while ใช้ตรงไหน?](../TEACHER_QUESTIONS.md#q016)
- [Q017: if/elif/else ทำงานตามลำดับอย่างไร?](../TEACHER_QUESTIONS.md#q017)
- [Q020: try/except และ None ใช้เพื่ออะไร?](../TEACHER_QUESTIONS.md#q020)
- [Q021: remaining_hours คำนวณอย่างไร?](../TEACHER_QUESTIONS.md#q021)
- [Q022: progress คำนวณอย่างไร ทำไม 1.5 จาก 4 ได้ 37%?](../TEACHER_QUESTIONS.md#q022)
- [Q023: days_left เป็นค่าติดลบได้หรือไม่?](../TEACHER_QUESTIONS.md#q023)
- [Q024: ทำไมต้องตรวจ math.isfinite?](../TEACHER_QUESTIONS.md#q024)
- [Q025: ทำไม read_date ตรวจ isoformat กลับอีกครั้ง?](../TEACHER_QUESTIONS.md#q025)
- [Q026: dict(row) กับ details_of คัดลอกต่างกันอย่างไร?](../TEACHER_QUESTIONS.md#q026)
- [Q027: no กับ version ใช้เพื่ออะไร?](../TEACHER_QUESTIONS.md#q027)
- [Q028: SHA-256 ในที่นี้เข้ารหัสข้อมูลหรือไม่?](../TEACHER_QUESTIONS.md#q028)
- [Q029: ทำไมไม่ใช้ sorted(key=...) และการเรียงมีต้นทุนเท่าไร?](../TEACHER_QUESTIONS.md#q029)
- [Q030: ทำไมแยก work, adjustment, complete, reopen?](../TEACHER_QUESTIONS.md#q030)
- [Q032: เรียงตามความเร่งด่วนด้วยอะไร?](../TEACHER_QUESTIONS.md#q032)
- [Q033: งานสำคัญสูงที่ส่งไกลจะขึ้นก่อนงานส่งพรุ่งนี้หรือไม่?](../TEACHER_QUESTIONS.md#q033)
- [Q034: ยังไม่เริ่มกับกำลังทำต่างกันอย่างไร?](../TEACHER_QUESTIONS.md#q034)
- [Q035: งานกำลังทำและเกินกำหนดพร้อมกันได้หรือไม่?](../TEACHER_QUESTIONS.md#q035)
- [Q036: soon_count รวมงานเกินกำหนดหรือไม่?](../TEACHER_QUESTIONS.md#q036)
- [Q037: ทำไมเวลาแนะนำวันนี้ไม่เกินเวลาว่าง?](../TEACHER_QUESTIONS.md#q037)
- [Q038: ทำวันนี้ 1.5 ชั่วโมง จากงบ 4 ระบบควรแนะนำเพิ่มเท่าไร?](../TEACHER_QUESTIONS.md#q038)
- [Q039: ถ้าวันนี้ครบงบแต่ยังมีงานค้าง ทำอย่างไร?](../TEACHER_QUESTIONS.md#q039)
- [Q040: กดเสร็จแล้วตัวเลข Overview เปลี่ยนอย่างไร?](../TEACHER_QUESTIONS.md#q040)
- [Q048: ทำไมประวัติจริงไม่สร้างจาก done_hours เดิมทั้งหมด?](../TEACHER_QUESTIONS.md#q048)
- [Q049: กดเปิดกลับคืนอะไร และทุกงานเสร็จเปิดกลับได้หรือไม่?](../TEACHER_QUESTIONS.md#q049)
- [Q051: ทำไมคำนวณจำนวนวันด้วย days_left + 1?](../TEACHER_QUESTIONS.md#q051)
- [Q052: ภาระสะสมคืออะไร?](../TEACHER_QUESTIONS.md#q052)
- [Q053: สองงาน 3 และ 4 ชั่วโมงส่งวันนี้ ว่าง 4 ผลเป็นอย่างไร?](../TEACHER_QUESTIONS.md#q053)
- [Q054: งาน 18 ชั่วโมงส่งพรุ่งนี้ ว่าง 4 ต่อวัน ขาดเท่าไร?](../TEACHER_QUESTIONS.md#q054)
- [Q055: บันทึก work วันนี้แล้วสูตรความจุเปลี่ยนอย่างไร?](../TEACHER_QUESTIONS.md#q055)
- [Q056: ว่าง 2 วันนี้ทำแล้ว 1 แต่ยังเหลืองานวันนี้ 2 ผลเท่าไร?](../TEACHER_QUESTIONS.md#q056)
- [Q057: งานเกินกำหนดถูกคำนวณหารด้วยวันติดลบหรือไม่?](../TEACHER_QUESTIONS.md#q057)
- [Q058: ทำไมขาดจริง 0.01 แสดง 0.1 และยังเสี่ยง?](../TEACHER_QUESTIONS.md#q058)
- [Q060: required_daily เป็น 0 แต่ยังมีงานเสี่ยงได้หรือไม่?](../TEACHER_QUESTIONS.md#q060)
- [Q066: hidden ป้องกันผู้ใช้แก้ค่าได้หรือไม่?](../TEACHER_QUESTIONS.md#q066)
- [Q081: data.json เก็บกี่ field?](../TEACHER_QUESTIONS.md#q081)
- [Q083: ข้อมูลเก่า 5 field ยังเปิดได้หรือไม่?](../TEACHER_QUESTIONS.md#q083)
- [Q097: version ป้องกันผู้ใช้สองคนบันทึกพร้อมกันทั้งหมดหรือไม่?](../TEACHER_QUESTIONS.md#q097)
- [Q098: ถ้าจะเปิดเป็นบริการหลายคนต้องพัฒนาอะไร?](../TEACHER_QUESTIONS.md#q098)
- [Q100: ถ้าอาจารย์ให้เปลี่ยนโจทย์หรือจับ bug สด ควรเริ่มตรงไหน?](../TEACHER_QUESTIONS.md#q100)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `Assignment` | L16–L36 | ประกาศ class `Assignment` เป็นแบบแทนงาน; ไม่ได้สร้าง object จนกว่าจะเรียก constructor |
| `__init__` | L17–L25 | ประกาศฟังก์ชัน `__init__`: รับข้อมูล 7 field และเก็บใน self; priority ปกติและ details ว่างเป็นค่าเริ่มต้นสำหรับข้อมูลเก่า |
| `remaining_hours` | L27–L28 | ประกาศฟังก์ชัน `remaining_hours`: คืนชั่วโมง estimate−done ไม่ติดลบ และปัด 2 ตำแหน่ง ไม่มีการเขียนไฟล์ |
| `days_left` | L30–L31 | ประกาศฟังก์ชัน `days_left`: คืนจำนวนวันส่ง−วันนี้ของ Python อาจเป็นลบ ไม่ใช้เวลาในวัน |
| `progress` | L33–L36 | ประกาศฟังก์ชัน `progress`: คืนเปอร์เซ็นต์ done/estimate แบบ int และจำกัด 0–100; estimate ไม่บวกคืน 0 |
| `read_number` | L39–L46 | ประกาศฟังก์ชัน `read_number`: ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity |
| `read_date` | L49–L56 | ประกาศฟังก์ชัน `read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None |
| `daily_hours` | L59–L63 | ประกาศฟังก์ชัน `daily_hours`: อ่านเลขผ่าน read_number แล้วรับเฉพาะ 0.1–12 ชั่วโมง |
| `load_daily_hours` | L66–L75 | ประกาศฟังก์ชัน `load_daily_hours`: อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `save_daily_hours` | L78–L80 | ประกาศฟังก์ชัน `save_daily_hours`: เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน |
| `team_data` | L83–L85 | ประกาศฟังก์ชัน `team_data`: อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `details_of` | L88–L100 | ประกาศฟังก์ชัน `details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ |
| `version_of` | L103–L105 | ประกาศฟังก์ชัน `version_of`: serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส |
| `ceil_tenth` | L108–L109 | ประกาศฟังก์ชัน `ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float |
| `task_view` | L112–L169 | ประกาศฟังก์ชัน `task_view`: สร้าง view จาก row: คำนวณชั่วโมง วัน เปอร์เซ็นต์ สถานะ เจ้าของ deadline งานย่อย stale และ version |
| `all_views` | L172–L178 | ประกาศฟังก์ชัน `all_views`: วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่ |
| `order_items` | L181–L192 | ประกาศฟังก์ชัน `order_items`: selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda |
| `order_key` | L195–L210 | ประกาศฟังก์ชัน `order_key`: คืน tuple ที่ใช้เทียบลำดับ; mode deadline คืนวัน/index; urgency ตามเกณฑ์ 6 ข้อที่กำหนด |
| `worked_today` | L213–L219 | ประกาศฟังก์ชัน `worked_today`: รวม history kind=work ที่ date ตรงวันนี้ของทุก item รวมงานเสร็จ ปัด 2 ตำแหน่ง |
| `annotate_plan` | L222–L267 | ประกาศฟังก์ชัน `annotate_plan`: คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count |
| `today_plan` | L270–L292 | ประกาศฟังก์ชัน `today_plan`: เรียง pending แล้วเติมเหตุผลและ today_hours โดยลด budget ทุกงาน คืน ordered กับ recommendations |
| `overview` | L295–L327 | ประกาศฟังก์ชัน `overview`: รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `record_history` | L330–L336 | ประกาศฟังก์ชัน `record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง |
| `row_index` | L339–L348 | ประกาศฟังก์ชัน `row_index`: รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None |
| `quick_action` | L351–L403 | ประกาศฟังก์ชัน `quick_action`: โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน |
| `work_history` | L406–L433 | ประกาศฟังก์ชัน `work_history`: รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work |
| `daily_history` | L436–L450 | ประกาศฟังก์ชัน `daily_history`: รวม history work ต่อ date เป็น hours/count โดยใช้รายการที่เรียงวันที่แล้ว |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `Assignment` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `AttributeError` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `HERE` | โฟลเดอร์ root ที่ได้จากตำแหน่งไฟล์ models.py |
| `OSError` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `OverflowError` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `PRIORITIES` | dict แปล priority เป็นข้อความไทย |
| `SETTINGS_FILE` | path ของ planner_settings.json |
| `TEAM_FILE` | path ของ team.json |
| `TypeError` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `ValueError` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `__file__` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `__init__` | รับข้อมูล 7 field และเก็บใน self; priority ปกติและ details ว่างเป็นค่าเริ่มต้นสำหรับข้อมูลเก่า |
| `abspath` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `action` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `actual_today` | ชั่วโมงประวัติ work ของวันนี้ |
| `actual_total` | ชั่วโมง work จริงที่มีบันทึกทั้งหมด |
| `all_views` | วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่ |
| `annotate_plan` | คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count |
| `append` | เพิ่มหนึ่งรายการต่อท้าย list |
| `budget` | งบเวลาที่ยังแบ่งให้รายการถัดไปได้ |
| `capacity` | ชั่วโมงความจุที่ยังมีถึงวันส่งหลังหักเวลา work วันนี้ |
| `ceil` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `ceil_tenth` | จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float |
| `completed` | รายการงานที่ remaining=0 |
| `course` | ชื่อวิชา |
| `cumulative` | ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ |
| `daily_history` | รวม history work ต่อ date เป็น hours/count โดยใช้รายการที่เรียงวันที่แล้ว |
| `daily_hours` | เวลาว่างรายวันที่ตั้งไว้ |
| `date` | ชนิดวันที่ระดับวันจาก datetime |
| `datetime` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `day` | สรุปวันที่หนึ่งใน daily_history |
| `days` | จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท |
| `days_left` | วันส่ง−วันนี้ |
| `details` | dict รายละเอียดซ้อนที่สำเนาแล้ว |
| `details_of` | สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ |
| `dict` | ชนิด map; dict(row) เป็นสำเนาระดับบน |
| `dirname` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `done_hours` | ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ |
| `due_date` | วันส่งมาตรฐาน YYYY-MM-DD |
| `dump` | เขียน JSON ลงไฟล์ |
| `dumps` | แปลง object เป็นข้อความ JSON |
| `encode` | แปลงข้อความเป็น bytes UTF-8 |
| `encoding` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `ensure_ascii` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `entry` | รายการประวัติหนึ่งครั้ง |
| `estimated_hours` | ชั่วโมงที่คาดว่าจะใช้ทั้งงาน |
| `existing` | สรุปวันที่พบแล้ว หรือ None |
| `file` | ไฟล์ที่เปิดใน with |
| `first` | รายการที่มี key น้อยที่สุดในรอบเลือก |
| `float` | แปลงเป็นเลขทศนิยม ยังต้องตรวจ finite |
| `focus` | งาน pending แรกตามความเร่งด่วน หรือ None |
| `form` | dict ของข้อมูลฟอร์ม POST |
| `fromisoformat` | แปลงข้อความมาตรฐานเป็น date |
| `get` | อ่านค่า dict พร้อม default เมื่อไม่มี key |
| `hashlib` | standard library สำหรับค่า hash |
| `hexdigest` | คืน hash เป็น string เลขฐานสิบหก |
| `history` | ประวัติหลายรายการ |
| `hours` | จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน |
| `indent` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `index` | ตำแหน่งที่ผ่านตรวจขอบเขต |
| `int` | แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress |
| `isascii` | ตรวจอักขระอยู่ใน ASCII |
| `isdigit` | ตรวจว่าเป็นกลุ่มตัวเลข; ใน no ใช้คู่ isascii ป้องกัน unicode digit |
| `isfinite` | ตรวจว่าเป็นเลขจำกัด ไม่ใช่ NaN/Infinity |
| `isinstance` | ตรวจชนิด object |
| `isoformat` | แปลง date เป็น YYYY-MM-DD |
| `item` | dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน |
| `items` | list ของข้อมูลแสดงผล |
| `join` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `json` | standard library serialize/parse JSON |
| `kind` | ชนิด event work/adjustment/complete/reopen |
| `latest` | ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก |
| `len` | จำนวนสมาชิก/อักขระ |
| `line` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `list` | ชนิดรายการ; list(items) สำเนารายการระดับบน |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `load_daily_hours` | อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2 |
| `loads` | แปลงข้อความ JSON กลับเป็น object |
| `math` | standard library finite และ ceil |
| `max` | เลือกค่ามากที่สุด |
| `member` | สมาชิกหนึ่งคน |
| `members` | list สมาชิกจาก team.json |
| `message` | ข้อความคืนให้ app แสดง banner |
| `min` | เลือกค่าน้อยที่สุด |
| `mode` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `note` | หมายเหตุของประวัติ |
| `on_date` | วันที่ทำงานที่ผู้ใช้เลือก |
| `open` | เปิดไฟล์ตาม mode/encoding ที่กำหนด |
| `order_items` | selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda |
| `order_key` | คืน tuple ที่ใช้เทียบลำดับ; mode deadline คืนวัน/index; urgency ตามเกณฑ์ 6 ข้อที่กำหนด |
| `ordered` | รายการหลังเรียงตามเกณฑ์ |
| `os` | standard library จัดการ path |
| `other` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `overdue_count` | จำนวนงานค้างที่วันส่งก่อนวันนี้ |
| `overdue_rank` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `overview` | รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `path` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `pending` | รายการงานที่ remaining>0 |
| `pop` | ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ |
| `position` | ตัวนับตำแหน่งงานเริ่ม 0 |
| `previous` | row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท |
| `priority` | ระดับ high/normal/low |
| `priority_rank` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `progress` | เปอร์เซ็นต์แบบจำนวนเต็ม |
| `progress_date` | วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale |
| `quick_action` | โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน |
| `raw_gap` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `read_date` | อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None |
| `read_number` | ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity |
| `recommendations` | งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้ |
| `record_history` | เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง |
| `remaining` | ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท |
| `remaining_hours` | คืนชั่วโมง estimate−done ไม่ติดลบ และปัด 2 ตำแหน่ง ไม่มีการเขียนไฟล์ |
| `remaining_total` | ผลรวมชั่วโมงคงเหลือ pending |
| `remove` | เอารายการที่เท่ากับค่าที่ให้หนึ่งรายการออกจาก list |
| `required` | ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท |
| `result` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `risk_count` | จำนวนงานที่ at_risk จริง |
| `risk_rank` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `round` | ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ |
| `row` | dict ข้อมูลงานหนึ่งรายการ |
| `row_index` | รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None |
| `rows` | list ข้อมูลงานจาก storage |
| `save` | เขียนทั้งรายการงานผ่าน storage |
| `save_daily_hours` | เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน |
| `self` | object ของงานที่เมธอดกำลังทำงานอยู่ |
| `setdefault` | เติม default เฉพาะ key ที่ยังไม่มี |
| `settings` | object ของค่าชั่วโมงรายวัน |
| `sha256` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `soon_count` | งานค้างส่งวันนี้ถึงอีก 3 วัน ไม่รวมเกินกำหนด |
| `sort_keys` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `spent` | work วันนี้ที่ถูก cap ไม่เกินงบรายวัน |
| `stale_count` | จำนวนงานค้างที่ไม่มีวันอัปเดต/ผ่านอย่างน้อย 2 วัน |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `str` | แปลงเป็นข้อความ |
| `subtask` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `task` | Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน |
| `task_view` | สร้าง view จาก row: คำนวณชั่วโมง วัน เปอร์เซ็นต์ สถานะ เจ้าของ deadline งานย่อย stale และ version |
| `team_data` | อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `text` | ข้อความก่อนแปลงหรือ serialize |
| `title` | ชื่องาน/ชื่อหัวข้อขึ้นกับ dict |
| `today` | วันที่ปัจจุบันจากเครื่อง Python |
| `today_plan` | เรียง pending แล้วเติมเหตุผลและ today_hours โดยลด budget ทุกงาน คืน ordered กับ recommendations |
| `today_remaining` | เวลางบวันนี้ที่ยังจัดสรรเพิ่มได้ |
| `total` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `value` | ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน |
| `version_of` | serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส |
| `work_history` | รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work |
| `worked_today` | รวม history kind=work ที่ date ตรงวันนี้ของทุก item รวมงานเสร็จ ปัด 2 ตำแหน่ง |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
"""Assignment, shared calculations, and form actions for Deadline Compass."""
from datetime import date
import hashlib
import json
import math
import os

import storage

HERE = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(HERE, "planner_settings.json")
TEAM_FILE = os.path.join(HERE, "team.json")
PRIORITIES = {"high": "สูง", "normal": "ปกติ", "low": "ต่ำ"}


class Assignment:
    def __init__(self, title, course, due_date, estimated_hours, done_hours,
                 priority="normal", details=None):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.estimated_hours = estimated_hours
        self.done_hours = done_hours
        self.priority = priority
        self.details = details or {}

    def remaining_hours(self):
        return round(max(0, self.estimated_hours - self.done_hours), 2)

    def days_left(self):
        return (date.fromisoformat(self.due_date) - date.today()).days

    def progress(self):
        if self.estimated_hours <= 0:
            return 0
        return min(100, max(0, int(self.done_hours * 100 / self.estimated_hours)))


def read_number(text):
    try:
        value = float(text)
    except (TypeError, ValueError, OverflowError):
        return None
    if not math.isfinite(value):
        return None
    return value


def read_date(text):
    try:
        result = date.fromisoformat(str(text))
    except (TypeError, ValueError):
        return None
    if result.isoformat() != text:
        return None
    return result


def daily_hours(text):
    value = read_number(text)
    if value is None or value < 0.1 or value > 12:
        return None
    return value


def load_daily_hours():
    try:
        with open(SETTINGS_FILE, encoding="utf-8") as file:
            settings = json.load(file)
        value = daily_hours(settings.get("daily_hours"))
    except (OSError, ValueError, AttributeError):
        value = None
    if value is None:
        return 2
    return value


def save_daily_hours(value):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
        json.dump({"daily_hours": value}, file, ensure_ascii=False, indent=2)


def team_data():
    with open(TEAM_FILE, encoding="utf-8") as file:
        return json.load(file)


def details_of(row):
    # Make an independent copy, including the nested subtasks and history.
    details = row.get("details", {})
    if not isinstance(details, dict):
        details = {}
    details = json.loads(json.dumps(details, ensure_ascii=False))
    details.setdefault("started", row["done_hours"] > 0)
    details.setdefault("owner", "")
    details.setdefault("subtasks", [])
    details.setdefault("history", [])
    details.setdefault("progress_on", "")
    details.setdefault("created_on", "")
    return details


def version_of(row):
    text = json.dumps(row, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ceil_tenth(value):
    return math.ceil(max(0, value) * 10 - 0.000000001) / 10


def task_view(row, position, members):
    details = details_of(row)
    task = Assignment(row["title"], row["course"], row["due_date"],
                      row["estimated_hours"], row["done_hours"],
                      row.get("priority", "normal"), details)
    item = dict(row)
    item["details"] = details
    item["priority"] = task.priority
    item["priority_label"] = PRIORITIES.get(task.priority, "ปกติ")
    item["no"] = position
    item["version"] = version_of(row)
    item["remaining_hours"] = task.remaining_hours()
    item["days_left"] = task.days_left()
    item["progress"] = task.progress()
    item["owner_name"] = "ยังไม่มีผู้รับผิดชอบ"
    for member in members:
        if member["id"] == details["owner"]:
            item["owner_name"] = member["name"]
    if item["remaining_hours"] == 0:
        item["status"] = "เสร็จแล้ว"
        item["status_icon"] = "✓"
        item["tone"] = "good"
    elif details["started"] or task.done_hours > 0:
        item["status"] = "กำลังทำ"
        item["status_icon"] = "▶"
        item["tone"] = "gold"
    else:
        item["status"] = "ยังไม่เริ่ม"
        item["status_icon"] = "○"
        item["tone"] = ""
    if item["days_left"] < 0:
        item["deadline_label"] = "เกินกำหนด " + str(-item["days_left"]) + " วัน"
        item["deadline_icon"] = "!"
        item["deadline_tone"] = "bad"
    elif item["days_left"] <= 3:
        item["deadline_label"] = "ใกล้ถึงกำหนด · อีก " + str(item["days_left"]) + " วัน"
        if item["days_left"] == 0:
            item["deadline_label"] = "ใกล้ถึงกำหนด · ส่งวันนี้"
        item["deadline_icon"] = "◷"
        item["deadline_tone"] = "gold"
    else:
        item["deadline_label"] = "ส่งอีก " + str(item["days_left"]) + " วัน"
        item["deadline_icon"] = "▣"
        item["deadline_tone"] = ""
    item["subtask_done"] = 0
    for subtask in details["subtasks"]:
        if subtask.get("done"):
            item["subtask_done"] = item["subtask_done"] + 1
    item["subtask_count"] = len(details["subtasks"])
    item["stale"] = False
    progress_date = read_date(details["progress_on"])
    if progress_date is None:
        progress_date = read_date(details["created_on"])
    if progress_date is None:
        item["stale"] = item["remaining_hours"] > 0
    elif item["remaining_hours"] > 0:
        item["stale"] = (date.today() - progress_date).days >= 2
    return item


def all_views(rows, members):
    items = []
    position = 0
    for row in rows:
        items.append(task_view(row, position, members))
        position = position + 1
    return items


def order_items(items, mode="urgency"):
    # Selection loop adapted from catalog/ranking.
    remaining = list(items)
    ordered = []
    while remaining:
        first = remaining[0]
        for item in remaining:
            if order_key(item, mode) < order_key(first, mode):
                first = item
        ordered.append(first)
        remaining.remove(first)
    return ordered


def order_key(item, mode):
    if mode == "deadline":
        return (item["due_date"], item["no"])
    overdue_rank = 1
    if item["days_left"] < 0:
        overdue_rank = 0
    risk_rank = 1
    if item.get("at_risk"):
        risk_rank = 0
    priority_rank = 1
    if item["priority"] == "high":
        priority_rank = 0
    elif item["priority"] == "low":
        priority_rank = 2
    return (overdue_rank, item["due_date"], -item["remaining_hours"],
            risk_rank, priority_rank, item["no"])


def worked_today(items):
    total = 0
    for item in items:
        for entry in item["details"]["history"]:
            if entry["kind"] == "work" and entry["date"] == date.today().isoformat():
                total = total + entry["hours"]
    return round(total, 2)


def annotate_plan(items, hours):
    spent = min(hours, worked_today(items))
    pending = []
    for item in items:
        if item["remaining_hours"] > 0:
            pending.append(item)
    ordered = order_items(pending, "deadline")
    risk_count = 0
    for task in ordered:
        cumulative = 0
        # Equal deadlines share the whole day's cumulative workload.
        for other in ordered:
            if other["due_date"] <= task["due_date"]:
                cumulative = cumulative + other["remaining_hours"]
        task["cumulative_hours"] = round(cumulative, 2)
        task["available_daily"] = hours
        task["at_risk"] = False
        if task["days_left"] < 0:
            task["plan_status"] = "เกินกำหนด"
            task["plan_icon"] = "!"
            task["plan_tone"] = "bad"
            task["gap"] = task["remaining_hours"]
            task["hours_per_day"] = task["remaining_hours"]
            task["shortfall_per_day"] = 0
            task["available_hours"] = 0
            task["at_risk"] = True
        else:
            days = task["days_left"] + 1
            capacity = days * hours - spent
            required = (cumulative + spent) / days
            raw_gap = max(0, cumulative - capacity)
            task["available_hours"] = round(capacity, 2)
            task["hours_per_day"] = ceil_tenth(required)
            task["gap"] = ceil_tenth(raw_gap)
            task["shortfall_per_day"] = ceil_tenth(max(0, required - hours))
            task["plan_status"] = "ตามแผน"
            task["plan_icon"] = "✓"
            task["plan_tone"] = "good"
            if raw_gap > 0.000000001:
                task["plan_status"] = "เวลาไม่พอ"
                task["plan_icon"] = "!"
                task["plan_tone"] = "bad"
                task["at_risk"] = True
        if task["at_risk"]:
            risk_count = risk_count + 1
    return ordered, risk_count


def today_plan(pending, budget):
    ordered = order_items(pending)
    recommendations = []
    for task in ordered:
        task["today_hours"] = 0
        task["reasons"] = []
        if task["days_left"] < 0:
            task["reasons"].append("เกินกำหนดแล้ว ควรติดต่อผู้สอนและจัดการก่อน")
        elif task["days_left"] <= 3:
            task["reasons"].append("ใกล้ถึงกำหนด ควรเริ่มก่อน")
        if task["remaining_hours"] >= 6:
            task["reasons"].append("ใช้เวลามาก ควรแบ่งเป็นงานย่อย")
        if task["at_risk"]:
            task["reasons"].append("งานนี้เสี่ยงไม่ทันเมื่อเทียบกับเวลาที่มี")
        if task["priority"] == "high":
            task["reasons"].append("ตั้งความสำคัญไว้สูง")
        if not task["reasons"]:
            task["reasons"].append("วันส่งใกล้ที่สุดในงานที่เหลือ")
        if budget > 0.000000001:
            task["today_hours"] = round(min(task["remaining_hours"], budget), 2)
            budget = round(max(0, budget - task["today_hours"]), 2)
            recommendations.append(task)
    return ordered, recommendations


def overview(rows, hours):
    members = team_data()["members"]
    items = all_views(rows, members)
    pending, risk_count = annotate_plan(items, hours)
    actual_today = worked_today(items)
    today_remaining = round(max(0, hours - actual_today), 2)
    ordered, recommendations = today_plan(pending, today_remaining)
    completed = []
    soon_count = 0
    overdue_count = 0
    stale_count = 0
    remaining_total = 0
    for item in items:
        if item["remaining_hours"] == 0:
            completed.append(item)
        else:
            remaining_total = remaining_total + item["remaining_hours"]
            if item["days_left"] < 0:
                overdue_count = overdue_count + 1
            elif item["days_left"] <= 3:
                soon_count = soon_count + 1
            if item["stale"]:
                stale_count = stale_count + 1
    focus = None
    if ordered:
        focus = ordered[0]
    return {"items": ordered, "completed": completed, "all_items": items,
            "recommendations": recommendations, "focus": focus,
            "open_count": len(ordered), "completed_count": len(completed),
            "soon_count": soon_count, "overdue_count": overdue_count,
            "remaining_total": round(remaining_total, 2), "risk_count": risk_count,
            "daily_hours": hours, "stale_count": stale_count,
            "actual_today": actual_today, "today_remaining": today_remaining}


def record_history(row, hours, kind, on_date, note=""):
    details = details_of(row)
    details["history"].append({"date": on_date, "hours": round(hours, 2),
                               "kind": kind, "note": note})
    details["started"] = True
    details["progress_on"] = date.today().isoformat()
    row["details"] = details


def row_index(form, rows):
    text = str(form.get("no", ""))
    if text == "" or not text.isascii() or not text.isdigit() or len(text) > 8:
        return None
    index = int(text)
    if index >= len(rows):
        return None
    if form.get("version", "") != version_of(rows[index]):
        return None
    return index


def quick_action(form):
    """Shared transitions from Overview, Manage, and Plan."""
    rows = storage.load()
    index = row_index(form, rows)
    if index is None:
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
    row = rows[index]
    details = details_of(row)
    action = form.get("action", "")
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
    if action == "start":
        if remaining == 0:
            return "✗ งานนี้เสร็จแล้ว"
        details["started"] = True
        details["progress_on"] = date.today().isoformat()
        row["details"] = details
        message = "✓ เริ่มงานนี้แล้ว เปิดหน้าจัดการงานเพื่อบันทึกเวลาและงานย่อย"
    elif action == "complete":
        if remaining == 0:
            return "✓ งานนี้เสร็จแล้ว"
        details["before_complete"] = row["done_hours"]
        details["subtasks_before_complete"] = []
        for subtask in details["subtasks"]:
            details["subtasks_before_complete"].append(subtask.get("done", False))
            subtask["done"] = True
        details["completed_on"] = date.today().isoformat()
        row["details"] = details
        row["done_hours"] = row["estimated_hours"]
        record_history(row, remaining, "complete", date.today().isoformat(),
                       "ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง")
        message = "✓ ทำเครื่องหมายว่าเสร็จแล้ว งานย้ายไปหมวดเสร็จแล้ว"
    elif action == "reopen":
        if remaining > 0 or "before_complete" not in details:
            return "✗ ยกเลิกได้เฉพาะงานที่กดทำเครื่องหมายเสร็จแล้ว หากต้องปรับเวลาทำจริงให้แก้ไขข้อมูลงาน"
        row["done_hours"] = min(row["estimated_hours"],
                                details["before_complete"])
        if row["done_hours"] >= row["estimated_hours"]:
            row["done_hours"] = 0
        previous = details.pop("subtasks_before_complete", [])
        position = 0
        for subtask in details["subtasks"]:
            if position < len(previous):
                subtask["done"] = previous[position]
            position = position + 1
        details.pop("completed_on", None)
        details["started"] = True
        row["details"] = details
        record_history(row, 0, "reopen", date.today().isoformat(), "เปิดงานกลับมาทำต่อ")
        message = "✓ เปิดงานกลับมาทำต่อแล้ว"
    else:
        return "✗ ไม่รู้จักคำสั่ง"
    storage.save(rows)
    return message


def work_history(items):
    history = []
    actual_total = 0
    for item in items:
        for entry in item["details"]["history"]:
            line = dict(entry)
            line["title"] = item["title"]
            line["course"] = item["course"]
            line["owner_name"] = item["owner_name"]
            line["label"] = "บันทึกเวลาทำงาน"
            if entry["kind"] == "work":
                actual_total = actual_total + entry["hours"]
            elif entry["kind"] == "complete":
                line["label"] = "ปิดงานตามเวลาประมาณ"
            elif entry["kind"] == "adjustment":
                line["label"] = "ปรับยอดความคืบหน้า"
            elif entry["kind"] == "reopen":
                line["label"] = "เปิดงานอีกครั้ง"
            history.append(line)
    ordered = []
    while history:
        latest = history[0]
        for entry in history:
            if entry["date"] > latest["date"]:
                latest = entry
        ordered.append(latest)
        history.remove(latest)
    return ordered, round(actual_total, 2)


def daily_history(history):
    days = []
    for entry in history:
        if entry["kind"] != "work":
            continue
        existing = None
        for day in days:
            if day["date"] == entry["date"]:
                existing = day
        if existing is None:
            existing = {"date": entry["date"], "hours": 0, "count": 0}
            days.append(existing)
        existing["hours"] = round(existing["hours"] + entry["hours"], 2)
        existing["count"] = existing["count"] + 1
    return days
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Assignment, shared calculations, and form actions for Deadline Compass."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน

### L2

```python
from datetime import date
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from datetime import date`
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime

### L3

```python
import hashlib
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import hashlib`
- ชื่อที่ต้องรู้: `hashlib` = standard library สำหรับค่า hash

### L4

```python
import json
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import json`
- ชื่อที่ต้องรู้: `json` = standard library serialize/parse JSON

### L5

```python
import math
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import math`
- ชื่อที่ต้องรู้: `math` = standard library finite และ ceil

### L6

```python
import os
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import os`
- ชื่อที่ต้องรู้: `os` = standard library จัดการ path

### L7

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L8

```python
import storage
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import storage`
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้

### L9

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L10

```python
HERE = os.path.dirname(os.path.abspath(__file__))
```

- เก็บผล เรียก `os.path.dirname` ด้วย argument ที่แสดงในโค้ด ลง `HERE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `HERE` = โฟลเดอร์ root ที่ได้จากตำแหน่งไฟล์ models.py; `os` = standard library จัดการ path

### L11

```python
SETTINGS_FILE = os.path.join(HERE, "planner_settings.json")
```

- เก็บผล เรียก `os.path.join` ด้วย argument ที่แสดงในโค้ด ลง `SETTINGS_FILE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `SETTINGS_FILE` = path ของ planner_settings.json; `os` = standard library จัดการ path; `HERE` = โฟลเดอร์ root ที่ได้จากตำแหน่งไฟล์ models.py

### L12

```python
TEAM_FILE = os.path.join(HERE, "team.json")
```

- เก็บผล เรียก `os.path.join` ด้วย argument ที่แสดงในโค้ด ลง `TEAM_FILE`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `TEAM_FILE` = path ของ team.json; `os` = standard library จัดการ path; `HERE` = โฟลเดอร์ root ที่ได้จากตำแหน่งไฟล์ models.py

### L13

```python
PRIORITIES = {"high": "สูง", "normal": "ปกติ", "low": "ต่ำ"}
```

- เก็บผล dict ที่มี key `'high'`, `'normal'`, `'low'` ลง `PRIORITIES`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `PRIORITIES` = dict แปล priority เป็นข้อความไทย

### L14

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L15

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L16

```python
class Assignment:
```

- ประกาศ class `Assignment` เป็นแบบแทนงาน; ไม่ได้สร้าง object จนกว่าจะเรียก constructor
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L17

```python
    def __init__(self, title, course, due_date, estimated_hours, done_hours,
```

- ประกาศฟังก์ชัน `__init__`: รับข้อมูล 7 field และเก็บใน self; priority ปกติและ details ว่างเป็นค่าเริ่มต้นสำหรับข้อมูลเก่า
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `course` = ชื่อวิชา; `due_date` = วันส่งมาตรฐาน YYYY-MM-DD; `estimated_hours` = ชั่วโมงที่คาดว่าจะใช้ทั้งงาน; `done_hours` = ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

```python
                 priority="normal", details=None):
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L17: ประกาศฟังก์ชัน `__init__`: รับข้อมูล 7 field และเก็บใน self; priority ปกติและ details ว่างเป็นค่าเริ่มต้นสำหรับข้อมูลเก่า
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `priority` = ระดับ high/normal/low; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 17 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L19

```python
        self.title = title
```

- เก็บผล `title` ลง `self.title`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L20

```python
        self.course = course
```

- เก็บผล `course` ลง `self.course`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `course` = ชื่อวิชา
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L21

```python
        self.due_date = due_date
```

- เก็บผล `due_date` ลง `self.due_date`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `due_date` = วันส่งมาตรฐาน YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L22

```python
        self.estimated_hours = estimated_hours
```

- เก็บผล `estimated_hours` ลง `self.estimated_hours`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `estimated_hours` = ชั่วโมงที่คาดว่าจะใช้ทั้งงาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L23

```python
        self.done_hours = done_hours
```

- เก็บผล `done_hours` ลง `self.done_hours`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `done_hours` = ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L24

```python
        self.priority = priority
```

- เก็บผล `priority` ลง `self.priority`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `priority` = ระดับ high/normal/low
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L25

```python
        self.details = details or {}
```

- เก็บผล `details` หรือ dict ที่มี key  ลง `self.details`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L26

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L27

```python
    def remaining_hours(self):
```

- ประกาศฟังก์ชัน `remaining_hours`: คืนชั่วโมง estimate−done ไม่ติดลบ และปัด 2 ตำแหน่ง ไม่มีการเขียนไฟล์
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L28

```python
        return round(max(0, self.estimated_hours - self.done_hours), 2)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `round`(`max`(`0`, (`self.estimated_hours` ลบ `self.done_hours`)), `2`)
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `max` = เลือกค่ามากที่สุด; `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `estimated_hours` = ชั่วโมงที่คาดว่าจะใช้ทั้งงาน; `done_hours` = ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L30

```python
    def days_left(self):
```

- ประกาศฟังก์ชัน `days_left`: คืนจำนวนวันส่ง−วันนี้ของ Python อาจเป็นลบ ไม่ใช้เวลาในวัน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `days_left` = วันส่ง−วันนี้; `self` = object ของงานที่เมธอดกำลังทำงานอยู่
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L31

```python
        return (date.fromisoformat(self.due_date) - date.today()).days
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `(date.fromisoformat(self.due_date) - date.today()).days`
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `-` ลบ/เครื่องหมายติดลบ
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `fromisoformat` = แปลงข้อความมาตรฐานเป็น date; `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `due_date` = วันส่งมาตรฐาน YYYY-MM-DD; `today` = วันที่ปัจจุบันจากเครื่อง Python; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L32

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L33

```python
    def progress(self):
```

- ประกาศฟังก์ชัน `progress`: คืนเปอร์เซ็นต์ done/estimate แบบ int และจำกัด 0–100; estimate ไม่บวกคืน 0
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `progress` = เปอร์เซ็นต์แบบจำนวนเต็ม; `self` = object ของงานที่เมธอดกำลังทำงานอยู่
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L34

```python
        if self.estimated_hours <= 0:
```

- ตรวจเงื่อนไข: `self.estimated_hours` ไม่เกิน `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `<=` น้อยกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `estimated_hours` = ชั่วโมงที่คาดว่าจะใช้ทั้งงาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L35

```python
            return 0
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `0`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

```python
        return min(100, max(0, int(self.done_hours * 100 / self.estimated_hours)))
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `min`(`100`, `max`(`0`, `int`(((`self.done_hours` คูณ/ทำซ้ำ `100`) หาร/ต่อ Path `self.estimated_hours`))))
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง; `/` หาร; กับ pathlib.Path เป็นการต่อ path; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `min` = เลือกค่าน้อยที่สุด; `max` = เลือกค่ามากที่สุด; `int` = แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress; `self` = object ของงานที่เมธอดกำลังทำงานอยู่; `done_hours` = ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ; `estimated_hours` = ชั่วโมงที่คาดว่าจะใช้ทั้งงาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L37

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L38

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L39

```python
def read_number(text):
```

- ประกาศฟังก์ชัน `read_number`: ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize

### L40

```python
    try:
```

- ลองคำสั่งใน try; หากเกิด exception ที่ระบุจึงเข้า except
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
        value = float(text)
```

- เก็บผล `float`(`text`) ลง `value`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `float` = แปลงเป็นเลขทศนิยม ยังต้องตรวจ finite; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L42

```python
    except (TypeError, ValueError, OverflowError):
```

- รับ exception tuple [`TypeError`, `ValueError`, `OverflowError`] แล้วทำ branch นี้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L43

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L44

```python
    if not math.isfinite(value):
```

- ตรวจเงื่อนไข: ไม่เป็นจริง: เรียก `math.isfinite` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `math` = standard library finite และ ceil; `isfinite` = ตรวจว่าเป็นเลขจำกัด ไม่ใช่ NaN/Infinity; `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L45

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L46

```python
    return value
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `value`
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L47

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L48

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L49

```python
def read_date(text):
```

- ประกาศฟังก์ชัน `read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize

### L50

```python
    try:
```

- ลองคำสั่งใน try; หากเกิด exception ที่ระบุจึงเข้า except
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L51

```python
        result = date.fromisoformat(str(text))
```

- เก็บผล เรียก `date.fromisoformat` ด้วย argument ที่แสดงในโค้ด ลง `result`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `fromisoformat` = แปลงข้อความมาตรฐานเป็น date; `str` = แปลงเป็นข้อความ; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L52

```python
    except (TypeError, ValueError):
```

- รับ exception tuple [`TypeError`, `ValueError`] แล้วทำ branch นี้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L53

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L54

```python
    if result.isoformat() != text:
```

- ตรวจเงื่อนไข: เรียก `result.isoformat` ด้วย argument ที่แสดงในโค้ด ไม่เท่ากับ `text`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `!=` เปรียบเทียบไม่เท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isoformat` = แปลง date เป็น YYYY-MM-DD; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L55

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L56

```python
    return result
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `result`
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L57

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L58

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L59

```python
def daily_hours(text):
```

- ประกาศฟังก์ชัน `daily_hours`: อ่านเลขผ่าน read_number แล้วรับเฉพาะ 0.1–12 ชั่วโมง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `daily_hours` = เวลาว่างรายวันที่ตั้งไว้; `text` = ข้อความก่อนแปลงหรือ serialize

### L60

```python
    value = read_number(text)
```

- เก็บผล เรียก `read_number`: ลอง float และตรวจ finite; คืน None เมื่อแปลงไม่ได้หรือเป็น NaN/Infinity ลง `value`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L61

```python
    if value is None or value < 0.1 or value > 12:
```

- ตรวจเงื่อนไข: `value` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) หรือ `value` น้อยกว่า `0.1` หรือ `value` มากกว่า `12`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L62

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L63

```python
    return value
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `value`
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L64

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L65

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L66

```python
def load_daily_hours():
```

- ประกาศฟังก์ชัน `load_daily_hours`: อ่าน settings และตรวจค่า; หากไฟล์/โครงสร้าง/ค่าผิด ใช้ 2
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L67

```python
    try:
```

- ลองคำสั่งใน try; หากเกิด exception ที่ระบุจึงเข้า except
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L68

```python
        with open(SETTINGS_FILE, encoding="utf-8") as file:
```

- ใช้ resource ใน with: เรียก `open` ด้วย argument ที่แสดงในโค้ด; ออกจาก block แล้วปิด resource ตาม context manager
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `open` = เปิดไฟล์ตาม mode/encoding ที่กำหนด; `SETTINGS_FILE` = path ของ planner_settings.json; `file` = ไฟล์ที่เปิดใน with
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L69

```python
            settings = json.load(file)
```

- เก็บผล เรียก `json.load` ด้วย argument ที่แสดงในโค้ด ลง `settings`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `settings` = object ของค่าชั่วโมงรายวัน; `json` = standard library serialize/parse JSON; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `file` = ไฟล์ที่เปิดใน with
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L70

```python
        value = daily_hours(settings.get("daily_hours"))
```

- เก็บผล เรียก `daily_hours`: อ่านเลขผ่าน read_number แล้วรับเฉพาะ 0.1–12 ชั่วโมง ลง `value`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `daily_hours` = เวลาว่างรายวันที่ตั้งไว้; `settings` = object ของค่าชั่วโมงรายวัน; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L71

```python
    except (OSError, ValueError, AttributeError):
```

- รับ exception tuple [`OSError`, `ValueError`, `AttributeError`] แล้วทำ branch นี้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L72

```python
        value = None
```

- เก็บผล None (ไม่มีค่าที่ใช้ได้) ลง `value`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L73

```python
    if value is None:
```

- ตรวจเงื่อนไข: `value` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L74

```python
        return 2
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `2`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L75

```python
    return value
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `value`
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L76

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L77

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L78

```python
def save_daily_hours(value):
```

- ประกาศฟังก์ชัน `save_daily_hours`: เขียน object daily_hours ลง SETTINGS_FILE ด้วย UTF-8; ผู้เรียกต้องตรวจค่าก่อน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน

### L79

```python
    with open(SETTINGS_FILE, "w", encoding="utf-8") as file:
```

- ใช้ resource ใน with: เรียก `open` ด้วย argument ที่แสดงในโค้ด; ออกจาก block แล้วปิด resource ตาม context manager
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `open` = เปิดไฟล์ตาม mode/encoding ที่กำหนด; `SETTINGS_FILE` = path ของ planner_settings.json; `file` = ไฟล์ที่เปิดใน with
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L80

```python
        json.dump({"daily_hours": value}, file, ensure_ascii=False, indent=2)
```

- เรียก `json.dump` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `json` = standard library serialize/parse JSON; `dump` = เขียน JSON ลงไฟล์; `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `file` = ไฟล์ที่เปิดใน with; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L81

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L82

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L83

```python
def team_data():
```

- ประกาศฟังก์ชัน `team_data`: อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท

### L84

```python
    with open(TEAM_FILE, encoding="utf-8") as file:
```

- ใช้ resource ใน with: เรียก `open` ด้วย argument ที่แสดงในโค้ด; ออกจาก block แล้วปิด resource ตาม context manager
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `open` = เปิดไฟล์ตาม mode/encoding ที่กำหนด; `TEAM_FILE` = path ของ team.json; `file` = ไฟล์ที่เปิดใน with
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L85

```python
        return json.load(file)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `json.load` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `json` = standard library serialize/parse JSON; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `file` = ไฟล์ที่เปิดใน with
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L86

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L87

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L88

```python
def details_of(row):
```

- ประกาศฟังก์ชัน `details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ

### L89

```python
    # Make an independent copy, including the nested subtasks and history.
```

- comment สำหรับผู้อ่าน: Make an independent copy, including the nested subtasks and history.
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L90

```python
    details = row.get("details", {})
```

- เก็บผล อ่าน `'details'` จาก `row` พร้อม default เมื่อไม่มี ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `row` = dict ข้อมูลงานหนึ่งรายการ; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L91

```python
    if not isinstance(details, dict):
```

- ตรวจเงื่อนไข: ไม่เป็นจริง: เรียก `isinstance` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isinstance` = ตรวจชนิด object; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `dict` = ชนิด map; dict(row) เป็นสำเนาระดับบน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L92

```python
        details = {}
```

- เก็บผล dict ที่มี key  ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L93

```python
    details = json.loads(json.dumps(details, ensure_ascii=False))
```

- เก็บผล เรียก `json.loads` ด้วย argument ที่แสดงในโค้ด ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `json` = standard library serialize/parse JSON; `loads` = แปลงข้อความ JSON กลับเป็น object; `dumps` = แปลง object เป็นข้อความ JSON; `False` = boolean เท็จ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L94

```python
    details.setdefault("started", row["done_hours"] > 0)
```

- เติม `'started'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L95

```python
    details.setdefault("owner", "")
```

- เติม `'owner'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L96

```python
    details.setdefault("subtasks", [])
```

- เติม `'subtasks'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L97

```python
    details.setdefault("history", [])
```

- เติม `'history'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L98

```python
    details.setdefault("progress_on", "")
```

- เติม `'progress_on'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L99

```python
    details.setdefault("created_on", "")
```

- เติม `'created_on'` ใน `details` เฉพาะเมื่อ key หาย
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `setdefault` = เติม default เฉพาะ key ที่ยังไม่มี
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L100

```python
    return details
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `details`
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L101

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L102

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L103

```python
def version_of(row):
```

- ประกาศฟังก์ชัน `version_of`: serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ

### L104

```python
    text = json.dumps(row, ensure_ascii=False, sort_keys=True)
```

- เก็บผล เรียก `json.dumps` ด้วย argument ที่แสดงในโค้ด ลง `text`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize; `json` = standard library serialize/parse JSON; `dumps` = แปลง object เป็นข้อความ JSON; `row` = dict ข้อมูลงานหนึ่งรายการ; `False` = boolean เท็จ; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L105

```python
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `hashlib.sha256(text.encode('utf-8')).hexdigest` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `hashlib` = standard library สำหรับค่า hash; `text` = ข้อความก่อนแปลงหรือ serialize; `encode` = แปลงข้อความเป็น bytes UTF-8; `hexdigest` = คืน hash เป็น string เลขฐานสิบหก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L106

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L107

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L108

```python
def ceil_tenth(value):
```

- ประกาศฟังก์ชัน `ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน

### L109

```python
    return math.ceil(max(0, value) * 10 - 0.000000001) / 10
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: (เรียก `math.ceil` ด้วย argument ที่แสดงในโค้ด หาร/ต่อ Path `10`)
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง; `-` ลบ/เครื่องหมายติดลบ; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `math` = standard library finite และ ceil; `max` = เลือกค่ามากที่สุด; `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L110

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L111

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L112

```python
def task_view(row, position, members):
```

- ประกาศฟังก์ชัน `task_view`: สร้าง view จาก row: คำนวณชั่วโมง วัน เปอร์เซ็นต์ สถานะ เจ้าของ deadline งานย่อย stale และ version
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `position` = ตัวนับตำแหน่งงานเริ่ม 0; `members` = list สมาชิกจาก team.json

### L113

```python
    details = details_of(row)
```

- เก็บผล เรียก `details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L114

```python
    task = Assignment(row["title"], row["course"], row["due_date"],
```

- เก็บผล เรียก `Assignment` ด้วย argument ที่แสดงในโค้ด ลง `task`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L115

```python
                      row["estimated_hours"], row["done_hours"],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L114: เก็บผล เรียก `Assignment` ด้วย argument ที่แสดงในโค้ด ลง `task`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 22 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L116

```python
                      row.get("priority", "normal"), details)
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L114: เก็บผล เรียก `Assignment` ด้วย argument ที่แสดงในโค้ด ลง `task`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 22 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L117

```python
    item = dict(row)
```

- เก็บผล `dict`(`row`) ลง `item`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `dict` = ชนิด map; dict(row) เป็นสำเนาระดับบน; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L118

```python
    item["details"] = details
```

- เก็บผล `details` ลง `item['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L119

```python
    item["priority"] = task.priority
```

- เก็บผล `task.priority` ลง `item['priority']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `priority` = ระดับ high/normal/low
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L120

```python
    item["priority_label"] = PRIORITIES.get(task.priority, "ปกติ")
```

- เก็บผล อ่าน `task.priority` จาก `PRIORITIES` พร้อม default เมื่อไม่มี ลง `item['priority_label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `PRIORITIES` = dict แปล priority เป็นข้อความไทย; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `priority` = ระดับ high/normal/low
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L121

```python
    item["no"] = position
```

- เก็บผล `position` ลง `item['no']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L122

```python
    item["version"] = version_of(row)
```

- เก็บผล เรียก `version_of`: serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส ลง `item['version']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L123

```python
    item["remaining_hours"] = task.remaining_hours()
```

- เก็บผล เรียก `task.remaining_hours`: คืนชั่วโมง estimate−done ไม่ติดลบ และปัด 2 ตำแหน่ง ไม่มีการเขียนไฟล์ ลง `item['remaining_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L124

```python
    item["days_left"] = task.days_left()
```

- เก็บผล เรียก `task.days_left`: คืนจำนวนวันส่ง−วันนี้ของ Python อาจเป็นลบ ไม่ใช้เวลาในวัน ลง `item['days_left']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `days_left` = วันส่ง−วันนี้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L125

```python
    item["progress"] = task.progress()
```

- เก็บผล เรียก `task.progress`: คืนเปอร์เซ็นต์ done/estimate แบบ int และจำกัด 0–100; estimate ไม่บวกคืน 0 ลง `item['progress']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `progress` = เปอร์เซ็นต์แบบจำนวนเต็ม
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L126

```python
    item["owner_name"] = "ยังไม่มีผู้รับผิดชอบ"
```

- เก็บผล `'ยังไม่มีผู้รับผิดชอบ'` ลง `item['owner_name']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L127

```python
    for member in members:
```

- วน `members` ให้ `member` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน; `members` = list สมาชิกจาก team.json
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L128

```python
        if member["id"] == details["owner"]:
```

- ตรวจเงื่อนไข: `member['id']` (อ่าน key/index) เท่ากับ `details['owner']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L129

```python
            item["owner_name"] = member["name"]
```

- เก็บผล `member['name']` (อ่าน key/index) ลง `item['owner_name']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `member` = สมาชิกหนึ่งคน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L130

```python
    if item["remaining_hours"] == 0:
```

- ตรวจเงื่อนไข: `item['remaining_hours']` (อ่าน key/index) เท่ากับ `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L131

```python
        item["status"] = "เสร็จแล้ว"
```

- เก็บผล `'เสร็จแล้ว'` ลง `item['status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L132

```python
        item["status_icon"] = "✓"
```

- เก็บผล `'✓'` ลง `item['status_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L133

```python
        item["tone"] = "good"
```

- เก็บผล `'good'` ลง `item['tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L134

```python
    elif details["started"] or task.done_hours > 0:
```

- ตรวจเงื่อนไข: `details['started']` (อ่าน key/index) หรือ `task.done_hours` มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `done_hours` = ยอดความคืบหน้าสะสม รวมการปรับ/ปิดงานตามประมาณ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L135

```python
        item["status"] = "กำลังทำ"
```

- เก็บผล `'กำลังทำ'` ลง `item['status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L136

```python
        item["status_icon"] = "▶"
```

- เก็บผล `'▶'` ลง `item['status_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L137

```python
        item["tone"] = "gold"
```

- เก็บผล `'gold'` ลง `item['tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L138

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L139

```python
        item["status"] = "ยังไม่เริ่ม"
```

- เก็บผล `'ยังไม่เริ่ม'` ลง `item['status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L140

```python
        item["status_icon"] = "○"
```

- เก็บผล `'○'` ลง `item['status_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L141

```python
        item["tone"] = ""
```

- เก็บผล `''` ลง `item['tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L142

```python
    if item["days_left"] < 0:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) น้อยกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L143

```python
        item["deadline_label"] = "เกินกำหนด " + str(-item["days_left"]) + " วัน"
```

- เก็บผล ((`'เกินกำหนด '` บวก/ต่อ `str`(`-item['days_left']`)) บวก/ต่อ `' วัน'`) ลง `item['deadline_label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `(` เปิดกลุ่มนิพจน์/argument/tuple; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `str` = แปลงเป็นข้อความ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L144

```python
        item["deadline_icon"] = "!"
```

- เก็บผล `'!'` ลง `item['deadline_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L145

```python
        item["deadline_tone"] = "bad"
```

- เก็บผล `'bad'` ลง `item['deadline_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L146

```python
    elif item["days_left"] <= 3:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) ไม่เกิน `3`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<=` น้อยกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L147

```python
        item["deadline_label"] = "ใกล้ถึงกำหนด · อีก " + str(item["days_left"]) + " วัน"
```

- เก็บผล ((`'ใกล้ถึงกำหนด · อีก '` บวก/ต่อ `str`(`item['days_left']` (อ่าน key/index))) บวก/ต่อ `' วัน'`) ลง `item['deadline_label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `str` = แปลงเป็นข้อความ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L148

```python
        if item["days_left"] == 0:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) เท่ากับ `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L149

```python
            item["deadline_label"] = "ใกล้ถึงกำหนด · ส่งวันนี้"
```

- เก็บผล `'ใกล้ถึงกำหนด · ส่งวันนี้'` ลง `item['deadline_label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L150

```python
        item["deadline_icon"] = "◷"
```

- เก็บผล `'◷'` ลง `item['deadline_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L151

```python
        item["deadline_tone"] = "gold"
```

- เก็บผล `'gold'` ลง `item['deadline_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L152

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L153

```python
        item["deadline_label"] = "ส่งอีก " + str(item["days_left"]) + " วัน"
```

- เก็บผล ((`'ส่งอีก '` บวก/ต่อ `str`(`item['days_left']` (อ่าน key/index))) บวก/ต่อ `' วัน'`) ลง `item['deadline_label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `str` = แปลงเป็นข้อความ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L154

```python
        item["deadline_icon"] = "▣"
```

- เก็บผล `'▣'` ลง `item['deadline_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L155

```python
        item["deadline_tone"] = ""
```

- เก็บผล `''` ลง `item['deadline_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L156

```python
    item["subtask_done"] = 0
```

- เก็บผล `0` ลง `item['subtask_done']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L157

```python
    for subtask in details["subtasks"]:
```

- วน `details['subtasks']` (อ่าน key/index) ให้ `subtask` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L158

```python
        if subtask.get("done"):
```

- ตรวจเงื่อนไข: อ่าน `'done'` จาก `subtask` พร้อม default เมื่อไม่มี; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L159

```python
            item["subtask_done"] = item["subtask_done"] + 1
```

- เก็บผล (`item['subtask_done']` (อ่าน key/index) บวก/ต่อ `1`) ลง `item['subtask_done']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L160

```python
    item["subtask_count"] = len(details["subtasks"])
```

- เก็บผล `len`(`details['subtasks']` (อ่าน key/index)) ลง `item['subtask_count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `len` = จำนวนสมาชิก/อักขระ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L161

```python
    item["stale"] = False
```

- เก็บผล `False` ลง `item['stale']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `False` = boolean เท็จ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L162

```python
    progress_date = read_date(details["progress_on"])
```

- เก็บผล เรียก `read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None ลง `progress_date`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `progress_date` = วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L163

```python
    if progress_date is None:
```

- ตรวจเงื่อนไข: `progress_date` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `progress_date` = วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L164

```python
        progress_date = read_date(details["created_on"])
```

- เก็บผล เรียก `read_date`: อ่านวันและเทียบ isoformat ให้ตรง YYYY-MM-DD; คืน date หรือ None ลง `progress_date`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `progress_date` = วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L165

```python
    if progress_date is None:
```

- ตรวจเงื่อนไข: `progress_date` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `progress_date` = วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L166

```python
        item["stale"] = item["remaining_hours"] > 0
```

- เก็บผล `item['remaining_hours']` (อ่าน key/index) มากกว่า `0` ลง `item['stale']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `>` มากกว่า
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L167

```python
    elif item["remaining_hours"] > 0:
```

- ตรวจเงื่อนไข: `item['remaining_hours']` (อ่าน key/index) มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L168

```python
        item["stale"] = (date.today() - progress_date).days >= 2
```

- เก็บผล `(date.today() - progress_date).days` อย่างน้อย `2` ลง `item['stale']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `-` ลบ/เครื่องหมายติดลบ; `>=` มากกว่าหรือเท่ากับ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `progress_date` = วันที่อัปเดตล่าสุด/วันที่สร้างที่ใช้เช็ก stale; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L169

```python
    return item
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `item`
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L170

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L171

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L172

```python
def all_views(rows, members):
```

- ประกาศฟังก์ชัน `all_views`: วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `members` = list สมาชิกจาก team.json

### L173

```python
    items = []
```

- เก็บผล list [] ลง `items`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L174

```python
    position = 0
```

- เก็บผล `0` ลง `position`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L175

```python
    for row in rows:
```

- วน `rows` ให้ `row` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L176

```python
        items.append(task_view(row, position, members))
```

- เพิ่ม เรียก `task_view`: สร้าง view จาก row: คำนวณชั่วโมง วัน เปอร์เซ็นต์ สถานะ เจ้าของ deadline งานย่อย stale และ version ไปท้าย `items`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `row` = dict ข้อมูลงานหนึ่งรายการ; `position` = ตัวนับตำแหน่งงานเริ่ม 0; `members` = list สมาชิกจาก team.json
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L177

```python
        position = position + 1
```

- เก็บผล (`position` บวก/ต่อ `1`) ลง `position`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L178

```python
    return items
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `items`
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L179

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L180

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L181

```python
def order_items(items, mode="urgency"):
```

- ประกาศฟังก์ชัน `order_items`: selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล

### L182

```python
    # Selection loop adapted from catalog/ranking.
```

- comment สำหรับผู้อ่าน: Selection loop adapted from catalog/ranking.
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L183

```python
    remaining = list(items)
```

- เก็บผล `list`(`items`) ลง `remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `list` = ชนิดรายการ; list(items) สำเนารายการระดับบน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L184

```python
    ordered = []
```

- เก็บผล list [] ลง `ordered`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L185

```python
    while remaining:
```

- ทำซ้ำขณะ `remaining` เป็นจริง; body ต้องเปลี่ยนข้อมูลจนจบรอบได้
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L186

```python
        first = remaining[0]
```

- เก็บผล `remaining[0]` (อ่าน key/index) ลง `first`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `first` = รายการที่มี key น้อยที่สุดในรอบเลือก; `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L187

```python
        for item in remaining:
```

- วน `remaining` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L188

```python
            if order_key(item, mode) < order_key(first, mode):
```

- ตรวจเงื่อนไข: เรียก `order_key`: คืน tuple ที่ใช้เทียบลำดับ; mode deadline คืนวัน/index; urgency ตามเกณฑ์ 6 ข้อที่กำหนด น้อยกว่า เรียก `order_key`: คืน tuple ที่ใช้เทียบลำดับ; mode deadline คืนวัน/index; urgency ตามเกณฑ์ 6 ข้อที่กำหนด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `first` = รายการที่มี key น้อยที่สุดในรอบเลือก
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L189

```python
                first = item
```

- เก็บผล `item` ลง `first`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `first` = รายการที่มี key น้อยที่สุดในรอบเลือก; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L190

```python
        ordered.append(first)
```

- เพิ่ม `first` ไปท้าย `ordered`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `first` = รายการที่มี key น้อยที่สุดในรอบเลือก
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L191

```python
        remaining.remove(first)
```

- เอาสมาชิก/key ออกจาก `remaining` ตาม argument ในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `remove` = เอารายการที่เท่ากับค่าที่ให้หนึ่งรายการออกจาก list; `first` = รายการที่มี key น้อยที่สุดในรอบเลือก
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L192

```python
    return ordered
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `ordered`
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L193

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L194

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L195

```python
def order_key(item, mode):
```

- ประกาศฟังก์ชัน `order_key`: คืน tuple ที่ใช้เทียบลำดับ; mode deadline คืนวัน/index; urgency ตามเกณฑ์ 6 ข้อที่กำหนด
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน

### L196

```python
    if mode == "deadline":
```

- ตรวจเงื่อนไข: `mode` เท่ากับ `'deadline'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L197

```python
        return (item["due_date"], item["no"])
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [`item['due_date']` (อ่าน key/index), `item['no']` (อ่าน key/index)]
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L198

```python
    overdue_rank = 1
```

- เก็บผล `1` ลง `overdue_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L199

```python
    if item["days_left"] < 0:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) น้อยกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L200

```python
        overdue_rank = 0
```

- เก็บผล `0` ลง `overdue_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L201

```python
    risk_rank = 1
```

- เก็บผล `1` ลง `risk_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L202

```python
    if item.get("at_risk"):
```

- ตรวจเงื่อนไข: อ่าน `'at_risk'` จาก `item` พร้อม default เมื่อไม่มี; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L203

```python
        risk_rank = 0
```

- เก็บผล `0` ลง `risk_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L204

```python
    priority_rank = 1
```

- เก็บผล `1` ลง `priority_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L205

```python
    if item["priority"] == "high":
```

- ตรวจเงื่อนไข: `item['priority']` (อ่าน key/index) เท่ากับ `'high'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L206

```python
        priority_rank = 0
```

- เก็บผล `0` ลง `priority_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L207

```python
    elif item["priority"] == "low":
```

- ตรวจเงื่อนไข: `item['priority']` (อ่าน key/index) เท่ากับ `'low'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L208

```python
        priority_rank = 2
```

- เก็บผล `2` ลง `priority_rank`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L209

```python
    return (overdue_rank, item["due_date"], -item["remaining_hours"],
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple จำนวน 6 สมาชิกตามโค้ด
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `-` ลบ/เครื่องหมายติดลบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L210

```python
            risk_rank, priority_rank, item["no"])
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L209: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple จำนวน 6 สมาชิกตามโค้ด
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L211

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L212

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L213

```python
def worked_today(items):
```

- ประกาศฟังก์ชัน `worked_today`: รวม history kind=work ที่ date ตรงวันนี้ของทุก item รวมงานเสร็จ ปัด 2 ตำแหน่ง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล

### L214

```python
    total = 0
```

- เก็บผล `0` ลง `total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L215

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L216

```python
        for entry in item["details"]["history"]:
```

- วน `item['details']['history']` (อ่าน key/index) ให้ `entry` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L217

```python
            if entry["kind"] == "work" and entry["date"] == date.today().isoformat():
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) เท่ากับ `'work'` และ `entry['date']` (อ่าน key/index) เท่ากับ เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L218

```python
                total = total + entry["hours"]
```

- เก็บผล (`total` บวก/ต่อ `entry['hours']` (อ่าน key/index)) ลง `total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L219

```python
    return round(total, 2)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `round`(`total`, `2`)
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L220

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L221

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L222

```python
def annotate_plan(items, hours):
```

- ประกาศฟังก์ชัน `annotate_plan`: คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน

### L223

```python
    spent = min(hours, worked_today(items))
```

- เก็บผล `min`(`hours`, เรียก `worked_today`: รวม history kind=work ที่ date ตรงวันนี้ของทุก item รวมงานเสร็จ ปัด 2 ตำแหน่ง) ลง `spent`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `spent` = work วันนี้ที่ถูก cap ไม่เกินงบรายวัน; `min` = เลือกค่าน้อยที่สุด; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L224

```python
    pending = []
```

- เก็บผล list [] ลง `pending`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `pending` = รายการงานที่ remaining>0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L225

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L226

```python
        if item["remaining_hours"] > 0:
```

- ตรวจเงื่อนไข: `item['remaining_hours']` (อ่าน key/index) มากกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L227

```python
            pending.append(item)
```

- เพิ่ม `item` ไปท้าย `pending`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `pending` = รายการงานที่ remaining>0; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L228

```python
    ordered = order_items(pending, "deadline")
```

- เก็บผล เรียก `order_items`: selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda ลง `ordered`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `pending` = รายการงานที่ remaining>0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L229

```python
    risk_count = 0
```

- เก็บผล `0` ลง `risk_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `risk_count` = จำนวนงานที่ at_risk จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L230

```python
    for task in ordered:
```

- วน `ordered` ให้ `task` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L231

```python
        cumulative = 0
```

- เก็บผล `0` ลง `cumulative`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `cumulative` = ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L232

```python
        # Equal deadlines share the whole day's cumulative workload.
```

- comment สำหรับผู้อ่าน: Equal deadlines share the whole day's cumulative workload.
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L233

```python
        for other in ordered:
```

- วน `ordered` ให้ `other` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L234

```python
            if other["due_date"] <= task["due_date"]:
```

- ตรวจเงื่อนไข: `other['due_date']` (อ่าน key/index) ไม่เกิน `task['due_date']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<=` น้อยกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L235

```python
                cumulative = cumulative + other["remaining_hours"]
```

- เก็บผล (`cumulative` บวก/ต่อ `other['remaining_hours']` (อ่าน key/index)) ลง `cumulative`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `cumulative` = ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L236

```python
        task["cumulative_hours"] = round(cumulative, 2)
```

- เก็บผล `round`(`cumulative`, `2`) ลง `task['cumulative_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `cumulative` = ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L237

```python
        task["available_daily"] = hours
```

- เก็บผล `hours` ลง `task['available_daily']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L238

```python
        task["at_risk"] = False
```

- เก็บผล `False` ลง `task['at_risk']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `False` = boolean เท็จ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L239

```python
        if task["days_left"] < 0:
```

- ตรวจเงื่อนไข: `task['days_left']` (อ่าน key/index) น้อยกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L240

```python
            task["plan_status"] = "เกินกำหนด"
```

- เก็บผล `'เกินกำหนด'` ลง `task['plan_status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L241

```python
            task["plan_icon"] = "!"
```

- เก็บผล `'!'` ลง `task['plan_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L242

```python
            task["plan_tone"] = "bad"
```

- เก็บผล `'bad'` ลง `task['plan_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L243

```python
            task["gap"] = task["remaining_hours"]
```

- เก็บผล `task['remaining_hours']` (อ่าน key/index) ลง `task['gap']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L244

```python
            task["hours_per_day"] = task["remaining_hours"]
```

- เก็บผล `task['remaining_hours']` (อ่าน key/index) ลง `task['hours_per_day']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L245

```python
            task["shortfall_per_day"] = 0
```

- เก็บผล `0` ลง `task['shortfall_per_day']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L246

```python
            task["available_hours"] = 0
```

- เก็บผล `0` ลง `task['available_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L247

```python
            task["at_risk"] = True
```

- เก็บผล `True` ลง `task['at_risk']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `True` = boolean จริง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L248

```python
        else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L249

```python
            days = task["days_left"] + 1
```

- เก็บผล (`task['days_left']` (อ่าน key/index) บวก/ต่อ `1`) ลง `days`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L250

```python
            capacity = days * hours - spent
```

- เก็บผล ((`days` คูณ/ทำซ้ำ `hours`) ลบ `spent`) ลง `capacity`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง; `-` ลบ/เครื่องหมายติดลบ
- ชื่อที่ต้องรู้: `capacity` = ชั่วโมงความจุที่ยังมีถึงวันส่งหลังหักเวลา work วันนี้; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `spent` = work วันนี้ที่ถูก cap ไม่เกินงบรายวัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L251

```python
            required = (cumulative + spent) / days
```

- เก็บผล ((`cumulative` บวก/ต่อ `spent`) หาร/ต่อ Path `days`) ลง `required`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `+` บวกเลข/ต่อข้อความตามชนิด; `)` ปิดกลุ่มที่เปิดด้วย (; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท; `cumulative` = ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ; `spent` = work วันนี้ที่ถูก cap ไม่เกินงบรายวัน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L252

```python
            raw_gap = max(0, cumulative - capacity)
```

- เก็บผล `max`(`0`, (`cumulative` ลบ `capacity`)) ลง `raw_gap`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `max` = เลือกค่ามากที่สุด; `cumulative` = ชั่วโมงงานสะสมถึงกำหนดส่งที่ตรวจ; `capacity` = ชั่วโมงความจุที่ยังมีถึงวันส่งหลังหักเวลา work วันนี้
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L253

```python
            task["available_hours"] = round(capacity, 2)
```

- เก็บผล `round`(`capacity`, `2`) ลง `task['available_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `capacity` = ชั่วโมงความจุที่ยังมีถึงวันส่งหลังหักเวลา work วันนี้
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L254

```python
            task["hours_per_day"] = ceil_tenth(required)
```

- เก็บผล เรียก `ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float ลง `task['hours_per_day']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L255

```python
            task["gap"] = ceil_tenth(raw_gap)
```

- เก็บผล เรียก `ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float ลง `task['gap']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L256

```python
            task["shortfall_per_day"] = ceil_tenth(max(0, required - hours))
```

- เก็บผล เรียก `ceil_tenth`: จำกัดไม่ติดลบและปัดขึ้น 0.1 ชั่วโมง พร้อม epsilon เล็กเพื่อลดการปัดเกินจาก float ลง `task['shortfall_per_day']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `max` = เลือกค่ามากที่สุด; `required` = ชั่วโมงเฉลี่ยที่ต้องทำ/ค่าสูงสุดของช่วงตามบริบท; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L257

```python
            task["plan_status"] = "ตามแผน"
```

- เก็บผล `'ตามแผน'` ลง `task['plan_status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L258

```python
            task["plan_icon"] = "✓"
```

- เก็บผล `'✓'` ลง `task['plan_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L259

```python
            task["plan_tone"] = "good"
```

- เก็บผล `'good'` ลง `task['plan_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L260

```python
            if raw_gap > 0.000000001:
```

- ตรวจเงื่อนไข: `raw_gap` มากกว่า `1e-09`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L261

```python
                task["plan_status"] = "เวลาไม่พอ"
```

- เก็บผล `'เวลาไม่พอ'` ลง `task['plan_status']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L262

```python
                task["plan_icon"] = "!"
```

- เก็บผล `'!'` ลง `task['plan_icon']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L263

```python
                task["plan_tone"] = "bad"
```

- เก็บผล `'bad'` ลง `task['plan_tone']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L264

```python
                task["at_risk"] = True
```

- เก็บผล `True` ลง `task['at_risk']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `True` = boolean จริง
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L265

```python
        if task["at_risk"]:
```

- ตรวจเงื่อนไข: `task['at_risk']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L266

```python
            risk_count = risk_count + 1
```

- เก็บผล (`risk_count` บวก/ต่อ `1`) ลง `risk_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `risk_count` = จำนวนงานที่ at_risk จริง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L267

```python
    return ordered, risk_count
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [`ordered`, `risk_count`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `risk_count` = จำนวนงานที่ at_risk จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L268

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L269

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L270

```python
def today_plan(pending, budget):
```

- ประกาศฟังก์ชัน `today_plan`: เรียง pending แล้วเติมเหตุผลและ today_hours โดยลด budget ทุกงาน คืน ordered กับ recommendations
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `pending` = รายการงานที่ remaining>0; `budget` = งบเวลาที่ยังแบ่งให้รายการถัดไปได้

### L271

```python
    ordered = order_items(pending)
```

- เก็บผล เรียก `order_items`: selection loop เลือก key น้อยที่สุดซ้ำจนรายการที่เหลือว่าง ไม่ใช้ sorted/lambda ลง `ordered`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `pending` = รายการงานที่ remaining>0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L272

```python
    recommendations = []
```

- เก็บผล list [] ลง `recommendations`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `recommendations` = งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L273

```python
    for task in ordered:
```

- วน `ordered` ให้ `task` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L274

```python
        task["today_hours"] = 0
```

- เก็บผล `0` ลง `task['today_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L275

```python
        task["reasons"] = []
```

- เก็บผล list [] ลง `task['reasons']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L276

```python
        if task["days_left"] < 0:
```

- ตรวจเงื่อนไข: `task['days_left']` (อ่าน key/index) น้อยกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L277

```python
            task["reasons"].append("เกินกำหนดแล้ว ควรติดต่อผู้สอนและจัดการก่อน")
```

- เพิ่ม `'เกินกำหนดแล้ว ควรติดต่อผู้สอนและจัดการก่อน'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L278

```python
        elif task["days_left"] <= 3:
```

- ตรวจเงื่อนไข: `task['days_left']` (อ่าน key/index) ไม่เกิน `3`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<=` น้อยกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L279

```python
            task["reasons"].append("ใกล้ถึงกำหนด ควรเริ่มก่อน")
```

- เพิ่ม `'ใกล้ถึงกำหนด ควรเริ่มก่อน'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L280

```python
        if task["remaining_hours"] >= 6:
```

- ตรวจเงื่อนไข: `task['remaining_hours']` (อ่าน key/index) อย่างน้อย `6`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L281

```python
            task["reasons"].append("ใช้เวลามาก ควรแบ่งเป็นงานย่อย")
```

- เพิ่ม `'ใช้เวลามาก ควรแบ่งเป็นงานย่อย'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L282

```python
        if task["at_risk"]:
```

- ตรวจเงื่อนไข: `task['at_risk']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L283

```python
            task["reasons"].append("งานนี้เสี่ยงไม่ทันเมื่อเทียบกับเวลาที่มี")
```

- เพิ่ม `'งานนี้เสี่ยงไม่ทันเมื่อเทียบกับเวลาที่มี'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L284

```python
        if task["priority"] == "high":
```

- ตรวจเงื่อนไข: `task['priority']` (อ่าน key/index) เท่ากับ `'high'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L285

```python
            task["reasons"].append("ตั้งความสำคัญไว้สูง")
```

- เพิ่ม `'ตั้งความสำคัญไว้สูง'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L286

```python
        if not task["reasons"]:
```

- ตรวจเงื่อนไข: ไม่เป็นจริง: `task['reasons']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L287

```python
            task["reasons"].append("วันส่งใกล้ที่สุดในงานที่เหลือ")
```

- เพิ่ม `'วันส่งใกล้ที่สุดในงานที่เหลือ'` ไปท้าย `task['reasons']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L288

```python
        if budget > 0.000000001:
```

- ตรวจเงื่อนไข: `budget` มากกว่า `1e-09`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `budget` = งบเวลาที่ยังแบ่งให้รายการถัดไปได้
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L289

```python
            task["today_hours"] = round(min(task["remaining_hours"], budget), 2)
```

- เก็บผล `round`(`min`(`task['remaining_hours']` (อ่าน key/index), `budget`), `2`) ลง `task['today_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `min` = เลือกค่าน้อยที่สุด; `budget` = งบเวลาที่ยังแบ่งให้รายการถัดไปได้
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L290

```python
            budget = round(max(0, budget - task["today_hours"]), 2)
```

- เก็บผล `round`(`max`(`0`, (`budget` ลบ `task['today_hours']` (อ่าน key/index))), `2`) ลง `budget`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `budget` = งบเวลาที่ยังแบ่งให้รายการถัดไปได้; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `max` = เลือกค่ามากที่สุด; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L291

```python
            recommendations.append(task)
```

- เพิ่ม `task` ไปท้าย `recommendations`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `recommendations` = งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L292

```python
    return ordered, recommendations
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [`ordered`, `recommendations`]
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `recommendations` = งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L293

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L294

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L295

```python
def overview(rows, hours):
```

- ประกาศฟังก์ชัน `overview`: รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน

### L296

```python
    members = team_data()["members"]
```

- เก็บผล `team_data()['members']` (อ่าน key/index) ลง `members`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `members` = list สมาชิกจาก team.json
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L297

```python
    items = all_views(rows, members)
```

- เก็บผล เรียก `all_views`: วน row ทีละรายการ เรียก task_view พร้อม position ตั้งแต่ 0 แล้วคืน list ใหม่ ลง `items`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล; `rows` = list ข้อมูลงานจาก storage; `members` = list สมาชิกจาก team.json
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L298

```python
    pending, risk_count = annotate_plan(items, hours)
```

- เก็บผล เรียก `annotate_plan`: คัด pending และเติมภาระสะสม/ความจุ/เฉลี่ย/ส่วนขาด/สถานะใน view คืน ordered กับ risk_count ลง `(pending, risk_count)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `pending` = รายการงานที่ remaining>0; `risk_count` = จำนวนงานที่ at_risk จริง; `items` = list ของข้อมูลแสดงผล; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L299

```python
    actual_today = worked_today(items)
```

- เก็บผล เรียก `worked_today`: รวม history kind=work ที่ date ตรงวันนี้ของทุก item รวมงานเสร็จ ปัด 2 ตำแหน่ง ลง `actual_today`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `actual_today` = ชั่วโมงประวัติ work ของวันนี้; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L300

```python
    today_remaining = round(max(0, hours - actual_today), 2)
```

- เก็บผล `round`(`max`(`0`, (`hours` ลบ `actual_today`)), `2`) ลง `today_remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `today_remaining` = เวลางบวันนี้ที่ยังจัดสรรเพิ่มได้; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `max` = เลือกค่ามากที่สุด; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `actual_today` = ชั่วโมงประวัติ work ของวันนี้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L301

```python
    ordered, recommendations = today_plan(pending, today_remaining)
```

- เก็บผล เรียก `today_plan`: เรียง pending แล้วเติมเหตุผลและ today_hours โดยลด budget ทุกงาน คืน ordered กับ recommendations ลง `(ordered, recommendations)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `recommendations` = งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้; `pending` = รายการงานที่ remaining>0; `today_remaining` = เวลางบวันนี้ที่ยังจัดสรรเพิ่มได้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L302

```python
    completed = []
```

- เก็บผล list [] ลง `completed`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `completed` = รายการงานที่ remaining=0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L303

```python
    soon_count = 0
```

- เก็บผล `0` ลง `soon_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `soon_count` = งานค้างส่งวันนี้ถึงอีก 3 วัน ไม่รวมเกินกำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L304

```python
    overdue_count = 0
```

- เก็บผล `0` ลง `overdue_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `overdue_count` = จำนวนงานค้างที่วันส่งก่อนวันนี้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L305

```python
    stale_count = 0
```

- เก็บผล `0` ลง `stale_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `stale_count` = จำนวนงานค้างที่ไม่มีวันอัปเดต/ผ่านอย่างน้อย 2 วัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L306

```python
    remaining_total = 0
```

- เก็บผล `0` ลง `remaining_total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `remaining_total` = ผลรวมชั่วโมงคงเหลือ pending
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L307

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L308

```python
        if item["remaining_hours"] == 0:
```

- ตรวจเงื่อนไข: `item['remaining_hours']` (อ่าน key/index) เท่ากับ `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L309

```python
            completed.append(item)
```

- เพิ่ม `item` ไปท้าย `completed`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `completed` = รายการงานที่ remaining=0; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L310

```python
        else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L311

```python
            remaining_total = remaining_total + item["remaining_hours"]
```

- เก็บผล (`remaining_total` บวก/ต่อ `item['remaining_hours']` (อ่าน key/index)) ลง `remaining_total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `remaining_total` = ผลรวมชั่วโมงคงเหลือ pending; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L312

```python
            if item["days_left"] < 0:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) น้อยกว่า `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<` น้อยกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L313

```python
                overdue_count = overdue_count + 1
```

- เก็บผล (`overdue_count` บวก/ต่อ `1`) ลง `overdue_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `overdue_count` = จำนวนงานค้างที่วันส่งก่อนวันนี้
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L314

```python
            elif item["days_left"] <= 3:
```

- ตรวจเงื่อนไข: `item['days_left']` (อ่าน key/index) ไม่เกิน `3`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `<=` น้อยกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L315

```python
                soon_count = soon_count + 1
```

- เก็บผล (`soon_count` บวก/ต่อ `1`) ลง `soon_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `soon_count` = งานค้างส่งวันนี้ถึงอีก 3 วัน ไม่รวมเกินกำหนด
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L316

```python
            if item["stale"]:
```

- ตรวจเงื่อนไข: `item['stale']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L317

```python
                stale_count = stale_count + 1
```

- เก็บผล (`stale_count` บวก/ต่อ `1`) ลง `stale_count`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `stale_count` = จำนวนงานค้างที่ไม่มีวันอัปเดต/ผ่านอย่างน้อย 2 วัน
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L318

```python
    focus = None
```

- เก็บผล None (ไม่มีค่าที่ใช้ได้) ลง `focus`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `focus` = งาน pending แรกตามความเร่งด่วน หรือ None; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L319

```python
    if ordered:
```

- ตรวจเงื่อนไข: `ordered`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L320

```python
        focus = ordered[0]
```

- เก็บผล `ordered[0]` (อ่าน key/index) ลง `focus`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `focus` = งาน pending แรกตามความเร่งด่วน หรือ None; `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L321

```python
    return {"items": ordered, "completed": completed, "all_items": items,
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `completed` = รายการงานที่ remaining=0; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L322

```python
            "recommendations": recommendations, "focus": focus,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `recommendations` = งานที่ได้รับการจัดสรรเวลาเพิ่มวันนี้; `focus` = งาน pending แรกตามความเร่งด่วน หรือ None
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L323

```python
            "open_count": len(ordered), "completed_count": len(completed),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `ordered` = รายการหลังเรียงตามเกณฑ์; `completed` = รายการงานที่ remaining=0
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L324

```python
            "soon_count": soon_count, "overdue_count": overdue_count,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `soon_count` = งานค้างส่งวันนี้ถึงอีก 3 วัน ไม่รวมเกินกำหนด; `overdue_count` = จำนวนงานค้างที่วันส่งก่อนวันนี้
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L325

```python
            "remaining_total": round(remaining_total, 2), "risk_count": risk_count,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `remaining_total` = ผลรวมชั่วโมงคงเหลือ pending; `risk_count` = จำนวนงานที่ at_risk จริง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L326

```python
            "daily_hours": hours, "stale_count": stale_count,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `stale_count` = จำนวนงานค้างที่ไม่มีวันอัปเดต/ผ่านอย่างน้อย 2 วัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L327

```python
            "actual_today": actual_today, "today_remaining": today_remaining}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L321: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'items'`, `'completed'`, `'all_items'`, `'recommendations'`, `'focus'`, `'open_count'`, `'completed_count'`, `'soon_count'`, `'overdue_count'`, `'remaining_total'`, `'risk_count'`, `'daily_hours'`, `'stale_count'`, `'actual_today'`, `'today_remaining'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `actual_today` = ชั่วโมงประวัติ work ของวันนี้; `today_remaining` = เวลางบวันนี้ที่ยังจัดสรรเพิ่มได้
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L328

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L329

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L330

```python
def record_history(row, hours, kind, on_date, note=""):
```

- ประกาศฟังก์ชัน `record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `kind` = ชนิด event work/adjustment/complete/reopen; `on_date` = วันที่ทำงานที่ผู้ใช้เลือก; `note` = หมายเหตุของประวัติ

### L331

```python
    details = details_of(row)
```

- เก็บผล เรียก `details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L332

```python
    details["history"].append({"date": on_date, "hours": round(hours, 2),
```

- เพิ่ม dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'` ไปท้าย `details['history']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `on_date` = วันที่ทำงานที่ผู้ใช้เลือก; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L333

```python
                               "kind": kind, "note": note})
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L332: เพิ่ม dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'` ไปท้าย `details['history']` (อ่าน key/index)
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `kind` = ชนิด event work/adjustment/complete/reopen; `note` = หมายเหตุของประวัติ
- ย่อหน้า 31 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L334

```python
    details["started"] = True
```

- เก็บผล `True` ลง `details['started']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L335

```python
    details["progress_on"] = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `details['progress_on']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L336

```python
    row["details"] = details
```

- เก็บผล `details` ลง `row['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L337

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L338

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L339

```python
def row_index(form, rows):
```

- ประกาศฟังก์ชัน `row_index`: รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage

### L340

```python
    text = str(form.get("no", ""))
```

- เก็บผล `str`(อ่าน `'no'` จาก `form` พร้อม default เมื่อไม่มี) ลง `text`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize; `str` = แปลงเป็นข้อความ; `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L341

```python
    if text == "" or not text.isascii() or not text.isdigit() or len(text) > 8:
```

- ตรวจเงื่อนไข: `text` เท่ากับ `''` หรือ ไม่เป็นจริง: เรียก `text.isascii` ด้วย argument ที่แสดงในโค้ด หรือ ไม่เป็นจริง: เรียก `text.isdigit` ด้วย argument ที่แสดงในโค้ด หรือ `len`(`text`) มากกว่า `8`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `text` = ข้อความก่อนแปลงหรือ serialize; `isascii` = ตรวจอักขระอยู่ใน ASCII; `isdigit` = ตรวจว่าเป็นกลุ่มตัวเลข; ใน no ใช้คู่ isascii ป้องกัน unicode digit; `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L342

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L343

```python
    index = int(text)
```

- เก็บผล `int`(`text`) ลง `index`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `int` = แปลงเป็นจำนวนเต็ม ตัดเศษของเลขบวกใน progress; `text` = ข้อความก่อนแปลงหรือ serialize
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L344

```python
    if index >= len(rows):
```

- ตรวจเงื่อนไข: `index` อย่างน้อย `len`(`rows`); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>=` มากกว่าหรือเท่ากับ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `len` = จำนวนสมาชิก/อักขระ; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L345

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L346

```python
    if form.get("version", "") != version_of(rows[index]):
```

- ตรวจเงื่อนไข: อ่าน `'version'` จาก `form` พร้อม default เมื่อไม่มี ไม่เท่ากับ เรียก `version_of`: serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `!=` เปรียบเทียบไม่เท่ากัน; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L347

```python
        return None
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: None (ไม่มีค่าที่ใช้ได้)
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L348

```python
    return index
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `index`
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L349

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L350

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L351

```python
def quick_action(form):
```

- ประกาศฟังก์ชัน `quick_action`: โหลดงานล่าสุด ตรวจฟอร์ม เปลี่ยน start/complete/reopen และ storage.save หากผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST

### L352

```python
    """Shared transitions from Overview, Manage, and Plan."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L353

```python
    rows = storage.load()
```

- เก็บผล อ่านรายการงานล่าสุดผ่าน storage.load() ลง `rows`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `rows` = list ข้อมูลงานจาก storage; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L354

```python
    index = row_index(form, rows)
```

- เก็บผล เรียก `row_index`: รับ no ASCII digit ไม่เกิน 8 หลัก ตรวจขอบเขตและ version; คืน index หรือ None ลง `index`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `form` = dict ของข้อมูลฟอร์ม POST; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L355

```python
    if index is None:
```

- ตรวจเงื่อนไข: `index` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L356

```python
        return "✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ รายการเปลี่ยนไปแล้ว กรุณาโหลดหน้าใหม่แล้วลองอีกครั้ง'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L357

```python
    row = rows[index]
```

- เก็บผล `rows[index]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `rows` = list ข้อมูลงานจาก storage; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L358

```python
    details = details_of(row)
```

- เก็บผล เรียก `details_of`: สำเนารายละเอียดซ้อนผ่าน JSON round trip และ setdefault เฉพาะ key ที่หาย ไม่บันทึกลงไฟล์ ลง `details`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L359

```python
    action = form.get("action", "")
```

- เก็บผล อ่าน `'action'` จาก `form` พร้อม default เมื่อไม่มี ลง `action`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L360

```python
    remaining = max(0, row["estimated_hours"] - row["done_hours"])
```

- เก็บผล `max`(`0`, (`row['estimated_hours']` (อ่าน key/index) ลบ `row['done_hours']` (อ่าน key/index))) ลง `remaining`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `max` = เลือกค่ามากที่สุด; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L361

```python
    if action == "start":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'start'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L362

```python
        if remaining == 0:
```

- ตรวจเงื่อนไข: `remaining` เท่ากับ `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L363

```python
            return "✗ งานนี้เสร็จแล้ว"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ งานนี้เสร็จแล้ว'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L364

```python
        details["started"] = True
```

- เก็บผล `True` ลง `details['started']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `True` = boolean จริง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L365

```python
        details["progress_on"] = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `details['progress_on']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L366

```python
        row["details"] = details
```

- เก็บผล `details` ลง `row['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L367

```python
        message = "✓ เริ่มงานนี้แล้ว เปิดหน้าจัดการงานเพื่อบันทึกเวลาและงานย่อย"
```

- เก็บผล `'✓ เริ่มงานนี้แล้ว เปิดหน้าจัดการงานเพื่อบันทึกเวลาและงานย่อย'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L368

```python
    elif action == "complete":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'complete'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L369

```python
        if remaining == 0:
```

- ตรวจเงื่อนไข: `remaining` เท่ากับ `0`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L370

```python
            return "✓ งานนี้เสร็จแล้ว"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✓ งานนี้เสร็จแล้ว'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L371

```python
        details["before_complete"] = row["done_hours"]
```

- เก็บผล `row['done_hours']` (อ่าน key/index) ลง `details['before_complete']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L372

```python
        details["subtasks_before_complete"] = []
```

- เก็บผล list [] ลง `details['subtasks_before_complete']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L373

```python
        for subtask in details["subtasks"]:
```

- วน `details['subtasks']` (อ่าน key/index) ให้ `subtask` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L374

```python
            details["subtasks_before_complete"].append(subtask.get("done", False))
```

- เพิ่ม อ่าน `'done'` จาก `subtask` พร้อม default เมื่อไม่มี ไปท้าย `details['subtasks_before_complete']` (อ่าน key/index)
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `False` = boolean เท็จ
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L375

```python
            subtask["done"] = True
```

- เก็บผล `True` ลง `subtask['done']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `True` = boolean จริง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L376

```python
        details["completed_on"] = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `details['completed_on']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L377

```python
        row["details"] = details
```

- เก็บผล `details` ลง `row['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L378

```python
        row["done_hours"] = row["estimated_hours"]
```

- เก็บผล `row['estimated_hours']` (อ่าน key/index) ลง `row['done_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L379

```python
        record_history(row, remaining, "complete", date.today().isoformat(),
```

- เรียก `record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L380

```python
                       "ปิดงานตามเวลาประมาณ ไม่ใช่ชั่วโมงทำงานจริง")
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L379: เรียก `record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 23 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L381

```python
        message = "✓ ทำเครื่องหมายว่าเสร็จแล้ว งานย้ายไปหมวดเสร็จแล้ว"
```

- เก็บผล `'✓ ทำเครื่องหมายว่าเสร็จแล้ว งานย้ายไปหมวดเสร็จแล้ว'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L382

```python
    elif action == "reopen":
```

- ตรวจเงื่อนไข: `action` เท่ากับ `'reopen'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L383

```python
        if remaining > 0 or "before_complete" not in details:
```

- ตรวจเงื่อนไข: `remaining` มากกว่า `0` หรือ `'before_complete'` ไม่อยู่ใน `details`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `remaining` = ชั่วโมงคงเหลือหรือรายการที่เหลือในการเรียงตามบริบท; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L384

```python
            return "✗ ยกเลิกได้เฉพาะงานที่กดทำเครื่องหมายเสร็จแล้ว หากต้องปรับเวลาทำจริงให้แก้ไขข้อมูลงาน"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ยกเลิกได้เฉพาะงานที่กดทำเครื่องหมายเสร็จแล้ว หากต้องปรับเวลาทำจริงให้แก้ไขข้อมูลงาน'`
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L385

```python
        row["done_hours"] = min(row["estimated_hours"],
```

- เก็บผล `min`(`row['estimated_hours']` (อ่าน key/index), `details['before_complete']` (อ่าน key/index)) ลง `row['done_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `min` = เลือกค่าน้อยที่สุด
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L386

```python
                                details["before_complete"])
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L385: เก็บผล `min`(`row['estimated_hours']` (อ่าน key/index), `details['before_complete']` (อ่าน key/index)) ลง `row['done_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 32 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L387

```python
        if row["done_hours"] >= row["estimated_hours"]:
```

- ตรวจเงื่อนไข: `row['done_hours']` (อ่าน key/index) อย่างน้อย `row['estimated_hours']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>=` มากกว่าหรือเท่ากับ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L388

```python
            row["done_hours"] = 0
```

- เก็บผล `0` ลง `row['done_hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L389

```python
        previous = details.pop("subtasks_before_complete", [])
```

- เก็บผล เอาสมาชิก/key ออกจาก `details` ตาม argument ในโค้ด ลง `previous`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L390

```python
        position = 0
```

- เก็บผล `0` ลง `position`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L391

```python
        for subtask in details["subtasks"]:
```

- วน `details['subtasks']` (อ่าน key/index) ให้ `subtask` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L392

```python
            if position < len(previous):
```

- ตรวจเงื่อนไข: `position` น้อยกว่า `len`(`previous`); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `<` น้อยกว่า; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `position` = ตัวนับตำแหน่งงานเริ่ม 0; `len` = จำนวนสมาชิก/อักขระ; `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L393

```python
                subtask["done"] = previous[position]
```

- เก็บผล `previous[position]` (อ่าน key/index) ลง `subtask['done']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `previous` = row/ค่าก่อนเปลี่ยน หรือสถานะงานย่อยก่อนปิดตามบริบท; `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L394

```python
            position = position + 1
```

- เก็บผล (`position` บวก/ต่อ `1`) ลง `position`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `position` = ตัวนับตำแหน่งงานเริ่ม 0
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L395

```python
        details.pop("completed_on", None)
```

- เอาสมาชิก/key ออกจาก `details` ตาม argument ในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `pop` = ลบ key หรือ index และคืนค่า; หาก dict ให้ default ใช้เมื่อไม่พบ; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L396

```python
        details["started"] = True
```

- เก็บผล `True` ลง `details['started']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว; `True` = boolean จริง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L397

```python
        row["details"] = details
```

- เก็บผล `details` ลง `row['details']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `details` = dict รายละเอียดซ้อนที่สำเนาแล้ว
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L398

```python
        record_history(row, 0, "reopen", date.today().isoformat(), "เปิดงานกลับมาทำต่อ")
```

- เรียก `record_history`: เติม event ลง row ในหน่วยความจำ ปรับ started/progress_on; ไม่เรียก storage.save เอง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L399

```python
        message = "✓ เปิดงานกลับมาทำต่อแล้ว"
```

- เก็บผล `'✓ เปิดงานกลับมาทำต่อแล้ว'` ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L400

```python
    else:
```

- else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L401

```python
        return "✗ ไม่รู้จักคำสั่ง"
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `'✗ ไม่รู้จักคำสั่ง'`
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L402

```python
    storage.save(rows)
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `rows` = list ข้อมูลงานจาก storage
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L403

```python
    return message
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `message`
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L404

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L405

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L406

```python
def work_history(items):
```

- ประกาศฟังก์ชัน `work_history`: รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `items` = list ของข้อมูลแสดงผล

### L407

```python
    history = []
```

- เก็บผล list [] ลง `history`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L408

```python
    actual_total = 0
```

- เก็บผล `0` ลง `actual_total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `actual_total` = ชั่วโมง work จริงที่มีบันทึกทั้งหมด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L409

```python
    for item in items:
```

- วน `items` ให้ `item` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน; `items` = list ของข้อมูลแสดงผล
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L410

```python
        for entry in item["details"]["history"]:
```

- วน `item['details']['history']` (อ่าน key/index) ให้ `entry` รับสมาชิกทีละรอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L411

```python
            line = dict(entry)
```

- เก็บผล `dict`(`entry`) ลง `line`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `dict` = ชนิด map; dict(row) เป็นสำเนาระดับบน; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L412

```python
            line["title"] = item["title"]
```

- เก็บผล `item['title']` (อ่าน key/index) ลง `line['title']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L413

```python
            line["course"] = item["course"]
```

- เก็บผล `item['course']` (อ่าน key/index) ลง `line['course']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L414

```python
            line["owner_name"] = item["owner_name"]
```

- เก็บผล `item['owner_name']` (อ่าน key/index) ลง `line['owner_name']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `item` = dict สำหรับแสดงผล/รายการที่กำลังวนตามบริบทฟังก์ชัน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L415

```python
            line["label"] = "บันทึกเวลาทำงาน"
```

- เก็บผล `'บันทึกเวลาทำงาน'` ลง `line['label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L416

```python
            if entry["kind"] == "work":
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) เท่ากับ `'work'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L417

```python
                actual_total = actual_total + entry["hours"]
```

- เก็บผล (`actual_total` บวก/ต่อ `entry['hours']` (อ่าน key/index)) ลง `actual_total`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `actual_total` = ชั่วโมง work จริงที่มีบันทึกทั้งหมด; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L418

```python
            elif entry["kind"] == "complete":
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) เท่ากับ `'complete'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L419

```python
                line["label"] = "ปิดงานตามเวลาประมาณ"
```

- เก็บผล `'ปิดงานตามเวลาประมาณ'` ลง `line['label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L420

```python
            elif entry["kind"] == "adjustment":
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) เท่ากับ `'adjustment'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L421

```python
                line["label"] = "ปรับยอดความคืบหน้า"
```

- เก็บผล `'ปรับยอดความคืบหน้า'` ลง `line['label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L422

```python
            elif entry["kind"] == "reopen":
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) เท่ากับ `'reopen'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L423

```python
                line["label"] = "เปิดงานอีกครั้ง"
```

- เก็บผล `'เปิดงานอีกครั้ง'` ลง `line['label']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L424

```python
            history.append(line)
```

- เพิ่ม `line` ไปท้าย `history`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ; `append` = เพิ่มหนึ่งรายการต่อท้าย list
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L425

```python
    ordered = []
```

- เก็บผล list [] ลง `ordered`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L426

```python
    while history:
```

- ทำซ้ำขณะ `history` เป็นจริง; body ต้องเปลี่ยนข้อมูลจนจบรอบได้
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L427

```python
        latest = history[0]
```

- เก็บผล `history[0]` (อ่าน key/index) ลง `latest`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `latest` = ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก; `history` = ประวัติหลายรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L428

```python
        for entry in history:
```

- วน `history` ให้ `entry` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `history` = ประวัติหลายรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L429

```python
            if entry["date"] > latest["date"]:
```

- ตรวจเงื่อนไข: `entry['date']` (อ่าน key/index) มากกว่า `latest['date']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `>` มากกว่า; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `latest` = ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L430

```python
                latest = entry
```

- เก็บผล `entry` ลง `latest`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `latest` = ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L431

```python
        ordered.append(latest)
```

- เพิ่ม `latest` ไปท้าย `ordered`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `latest` = ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L432

```python
        history.remove(latest)
```

- เอาสมาชิก/key ออกจาก `history` ตาม argument ในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ; `remove` = เอารายการที่เท่ากับค่าที่ให้หนึ่งรายการออกจาก list; `latest` = ประวัติที่มีวันที่ใหม่ที่สุดในรอบเลือก
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L433

```python
    return ordered, round(actual_total, 2)
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: tuple [`ordered`, `round`(`actual_total`, `2`)]
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `ordered` = รายการหลังเรียงตามเกณฑ์; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `actual_total` = ชั่วโมง work จริงที่มีบันทึกทั้งหมด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L434

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L435

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L436

```python
def daily_history(history):
```

- ประกาศฟังก์ชัน `daily_history`: รวม history work ต่อ date เป็น hours/count โดยใช้รายการที่เรียงวันที่แล้ว
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ

### L437

```python
    days = []
```

- เก็บผล list [] ลง `days`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L438

```python
    for entry in history:
```

- วน `history` ให้ `entry` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง; `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L439

```python
        if entry["kind"] != "work":
```

- ตรวจเงื่อนไข: `entry['kind']` (อ่าน key/index) ไม่เท่ากับ `'work'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `!=` เปรียบเทียบไม่เท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L440

```python
            continue
```

- ข้ามส่วนที่เหลือของรอบนี้และไปสมาชิกถัดไป
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L441

```python
        existing = None
```

- เก็บผล None (ไม่มีค่าที่ใช้ได้) ลง `existing`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L442

```python
        for day in days:
```

- วน `days` ให้ `day` รับสมาชิกทีละรอบ
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `day` = สรุปวันที่หนึ่งใน daily_history; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L443

```python
            if day["date"] == entry["date"]:
```

- ตรวจเงื่อนไข: `day['date']` (อ่าน key/index) เท่ากับ `entry['date']` (อ่าน key/index); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `day` = สรุปวันที่หนึ่งใน daily_history; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L444

```python
                existing = day
```

- เก็บผล `day` ลง `existing`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None; `day` = สรุปวันที่หนึ่งใน daily_history
- ย่อหน้า 16 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L445

```python
        if existing is None:
```

- ตรวจเงื่อนไข: `existing` เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้); เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None; `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L446

```python
            existing = {"date": entry["date"], "hours": 0, "count": 0}
```

- เก็บผล dict ที่มี key `'date'`, `'hours'`, `'count'` ลง `existing`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L447

```python
            days.append(existing)
```

- เพิ่ม `existing` ไปท้าย `days`
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `append` = เพิ่มหนึ่งรายการต่อท้าย list; `existing` = สรุปวันที่พบแล้ว หรือ None
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L448

```python
        existing["hours"] = round(existing["hours"] + entry["hours"], 2)
```

- เก็บผล `round`((`existing['hours']` (อ่าน key/index) บวก/ต่อ `entry['hours']` (อ่าน key/index)), `2`) ลง `existing['hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `+` บวกเลข/ต่อข้อความตามชนิด; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None; `round` = ปัดตัวเลขตามจำนวนตำแหน่งที่ระบุ; `entry` = รายการประวัติหนึ่งครั้ง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L449

```python
        existing["count"] = existing["count"] + 1
```

- เก็บผล (`existing['count']` (อ่าน key/index) บวก/ต่อ `1`) ลง `existing['count']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `existing` = สรุปวันที่พบแล้ว หรือ None
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L450

```python
    return days
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `days`
- ชื่อที่ต้องรู้: `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
