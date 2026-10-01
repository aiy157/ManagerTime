# test_planner_features.py — ชุดทดสอบธุรกิจเพิ่มเติม

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 325 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `a77f04500ea1ed11fa908af9641ace1a471ebcc0d242ec430966e840c36a3968`

**ผู้ศึกษา/บทบาท:** นายธีรเดช ฤทธิ์คำรพ · QA / ส่วนร่วม

## 1. หน้าที่และการเชื่อมต่อ

ตรวจกรณีข้อมูลผิด สถานะ สูตร งานย่อย ประวัติ ทีม และฟอร์มเก่าโดยไม่แตะงานจริง

- **รับเข้า:** ข้อมูลจำลองจาก task/add_form และ isolated fixture
- **ผลลัพธ์:** assert ผ่าน/ไม่ผ่านเมื่อใช้ pytest

**เกี่ยวข้องกับ:** pytest ที่มีอยู่แล้ว; Flask test client; tmp_path/monkeypatch; models/storage/pages

## 2. ลำดับทำงาน

1. isolated เปลี่ยนตำแหน่ง data/sample/settings ไปพื้นที่ชั่วคราว
2. helper สร้างงาน วันส่งสัมพันธ์กับวันนี้ และ form พร้อม version
3. parameter ทดสอบข้อมูลผิดหลายค่าจากฟังก์ชันเดียว
4. assert เทียบค่าที่คาดจากสูตรและการเปลี่ยนสถานะ
5. รวมกับ test_pages.py เดิมในการรัน pytest

## 3. จุดที่ต้องอธิบายให้ถูก

- มี list comprehension/decorator ใน test helper ซึ่งไม่ใช่ไฟล์นักศึกษาที่ให้คะแนน pages/models
- test client ไม่ใช่การทดสอบภาพเบราว์เซอร์หรือ Notification จริง
- ผลล่าสุดใน QA_REPORT 42 รวมของอาจารย์ 4 + เพิ่ม 38 กรณี ไม่ใช่ 42 ชื่อ def

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q053: สองงาน 3 และ 4 ชั่วโมงส่งวันนี้ ว่าง 4 ผลเป็นอย่างไร?](../TEACHER_QUESTIONS.md#q053)
- [Q054: งาน 18 ชั่วโมงส่งพรุ่งนี้ ว่าง 4 ต่อวัน ขาดเท่าไร?](../TEACHER_QUESTIONS.md#q054)
- [Q056: ว่าง 2 วันนี้ทำแล้ว 1 แต่ยังเหลืองานวันนี้ 2 ผลเท่าไร?](../TEACHER_QUESTIONS.md#q056)
- [Q083: ข้อมูลเก่า 5 field ยังเปิดได้หรือไม่?](../TEACHER_QUESTIONS.md#q083)
- [Q092: pytest 42 passed ประกอบด้วยอะไร?](../TEACHER_QUESTIONS.md#q092)
- [Q093: ทดสอบอย่างไรไม่ให้ข้อมูลจริงหาย?](../TEACHER_QUESTIONS.md#q093)
- [Q094: ทำไม HTTP 200 อย่างเดียวไม่พอพิสูจน์ว่าหน้าใช้ได้?](../TEACHER_QUESTIONS.md#q094)
- [Q096: ป้องกัน XSS อย่างไร?](../TEACHER_QUESTIONS.md#q096)
- [Q100: ถ้าอาจารย์ให้เปลี่ยนโจทย์หรือจับ bug สด ควรเริ่มตรงไหน?](../TEACHER_QUESTIONS.md#q100)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `task` | L13–L19 | ประกาศฟังก์ชัน `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ |
| `isolated` | L23–L31 | ประกาศฟังก์ชัน `isolated`: pytest fixture เปลี่ยน path data/sample/settings ไป tmp_path ผ่าน monkeypatch แล้วคืน Flask test client |
| `fields` | L34–L35 | ประกาศฟังก์ชัน `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม |
| `add_form` | L38–L44 | ประกาศฟังก์ชัน `add_form`: สร้างค่าฟอร์มเพิ่มงานที่ถูกต้องแล้ว update ด้วย changes เพื่อทดลองค่าผิดเป็นรายกรณี |
| `test_existing_five_fields_still_load_without_rewriting` | L47–L57 | ประกาศฟังก์ชัน `test_existing_five_fields_still_load_without_rewriting`: ตรวจทุกหน้าอ่านข้อมูล 5 field ได้ และ GET ไม่ rewrite รายการ |
| `test_add_owner_priority_and_subtasks_keeps_seven_fields` | L60–L70 | ประกาศฟังก์ชัน `test_add_owner_priority_and_subtasks_keeps_seven_fields`: ตรวจ POST add พร้อม owner/high/งานย่อย มี 7 field และไม่มี work ปลอม |
| `test_invalid_add_does_not_mutate_data` | L81–L86 | ประกาศฟังก์ชัน `test_invalid_add_does_not_mutate_data`: ใช้ parameter ค่าผิด 15 แบบ ตรวจข้อความผิดและข้อมูลเดิมอยู่ครบ |
| `test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated` | L89–L100 | ประกาศฟังก์ชัน `test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated`: ตรวจเพิ่มวันอดีตต้องยืนยัน แต่ update วันที่อดีตเดิมแก้ชื่อได้ |
| `test_start_complete_reopen_updates_all_pages_and_preserves_real_hours` | L103–L123 | ประกาศฟังก์ชัน `test_start_complete_reopen_updates_all_pages_and_preserves_real_hours`: ตรวจ start→complete→reopen งานย่อยคืนค่า สถิติเปลี่ยน และ complete ไม่เพิ่ม actual_total |
| `test_work_logs_accumulate_real_hours_and_subtasks_are_independent` | L126–L146 | ประกาศฟังก์ชัน `test_work_logs_accumulate_real_hours_and_subtasks_are_independent`: ตรวจ work 1.5+2.5=4, progress 37%, ติ๊กงานย่อยไม่เปลี่ยนชั่วโมง และครบงาน |
| `test_overlogging_and_future_work_date_are_rejected` | L149–L157 | ประกาศฟังก์ชัน `test_overlogging_and_future_work_date_are_rejected`: ปฏิเสธบันทึกเกิน remaining และ work_date อนาคตโดยยอดเดิมไม่เปลี่ยน |
| `test_stale_row_cannot_modify_a_shifted_or_updated_task` | L160–L172 | ประกาศฟังก์ชัน `test_stale_row_cannot_modify_a_shifted_or_updated_task`: ตรวจ form เก่าหลังลบ row ก่อนหน้าหรือเปลี่ยนชื่อไม่ไปแก้งานใหม่ |
| `test_bad_indices_do_not_crash_or_save` | L176–L182 | ประกาศฟังก์ชัน `test_bad_indices_do_not_crash_or_save`: ตรวจ unicode digit, ติดลบ, ว่าง, และเลขยาวไม่ทำให้พัง/บันทึก |
| `test_plan_uses_daily_capacity_and_groups_identical_deadlines` | L185–L195 | ประกาศฟังก์ชัน `test_plan_uses_daily_capacity_and_groups_identical_deadlines`: เทียบส่วนขาดที่งบ 2/4 และงานวันเดียวกันมี cumulative/gap เท่ากัน |
| `test_plan_example_nine_required_four_available_and_five_short` | L198–L206 | ประกาศฟังก์ชัน `test_plan_example_nine_required_four_available_and_five_short`: ตรวจตัวอย่าง 18 ชั่วโมง/2 วัน ต้อง 9 มี 4 ขาด 5 ต่อวันและ 10 รวม |
| `test_overdue_included_and_tiny_shortfall_never_looks_on_track` | L209–L217 | ประกาศฟังก์ชัน `test_overdue_included_and_tiny_shortfall_never_looks_on_track`: ตรวจงานค้างรวมในภาระอนาคต และส่วนขาด 0.01 ยังขึ้นเสี่ยง |
| `test_daily_hours_saved_and_used_across_pages` | L220–L227 | ประกาศฟังก์ชัน `test_daily_hours_saved_and_used_across_pages`: ตรวจบันทึก settings ใช้ร่วมทุกหน้า และค่าผิดไม่เปลี่ยนค่าที่บันทึก |
| `test_recommendations_never_overbook_today_and_use_priority_tiebreak` | L230–L237 | ประกาศฟังก์ชัน `test_recommendations_never_overbook_today_and_use_priority_tiebreak`: ตรวจค้างก่อน ใกล้ก่อน รวม today_hours ไม่เกินงบ และ high ชนะเมื่อเกณฑ์อื่นเท่ากัน |
| `test_team_counts_progress_and_unassigned_tasks` | L240–L250 | ประกาศฟังก์ชัน `test_team_counts_progress_and_unassigned_tasks`: ตรวจ owner/count/progress/unassigned และเกณฑ์ overloaded |
| `test_empty_and_completed_only_data_have_no_focus` | L253–L258 | ประกาศฟังก์ชัน `test_empty_and_completed_only_data_have_no_focus`: ตรวจข้อมูลว่าง/เสร็จหมดไม่มี focus และแผนไม่มี pending |
| `test_all_forms_have_versions_and_templates_escape_user_input` | L261–L272 | ประกาศฟังก์ชัน `test_all_forms_have_versions_and_templates_escape_user_input`: ตรวจไม่มีหน้าข้อผิดพลาด ชื่อ script escape hidden version และ POST ปิดได้ |
| `test_today_work_reduces_recommendation_budget_and_capacity` | L275–L292 | ประกาศฟังก์ชัน `test_today_work_reduces_recommendation_budget_and_capacity`: ตรวจ work วันนี้จากงานเสร็จลดทั้งงบคำแนะนำและความจุ และเมื่อครบไม่มีจัดสรรเพิ่ม |
| `test_past_logs_and_estimated_completion_do_not_consume_today` | L295–L305 | ประกาศฟังก์ชัน `test_past_logs_and_estimated_completion_do_not_consume_today`: ตรวจ work วันก่อนกับ complete วันนี้ไม่ลดงบวันนี้ และ summary นับจริงวันเดิม |
| `test_reopen_requires_prior_manual_completion` | L308–L312 | ประกาศฟังก์ชัน `test_reopen_requires_prior_manual_completion`: ตรวจ reopen ของงานค้างหรือเสร็จจากชั่วโมงโดยไม่มี snapshot ถูกปฏิเสธ |
| `test_daily_summary_groups_actual_work_only` | L315–L325 | ประกาศฟังก์ชัน `test_daily_summary_groups_actual_work_only`: ตรวจ work 1+1.5 วันเดียวรวม 2.5/2 ครั้ง โดย complete 8 ไม่รวม |

## 6. ชื่อและคำศัพท์ที่พบใน Python

ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน

| ชื่อ | ความหมาย |
|---|---|
| `action` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `actual` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `add_form` | สร้างค่าฟอร์มเพิ่มงานที่ถูกต้องแล้ว update ด้วย changes เพื่อทดลองค่าผิดเป็นรายกรณี |
| `all` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `app` | module Flask router ที่อาจารย์ให้ |
| `as_text` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `before` | ข้อมูลก่อนการกระทำเพื่อเทียบใน test |
| `build` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `changes` | ค่า override สำหรับสร้างข้อมูลทดลอง |
| `data` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `data_file` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `date` | ชนิดวันที่ระดับวันจาก datetime |
| `datetime` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `days` | จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท |
| `done` | ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น |
| `due_date` | วันส่งมาตรฐาน YYYY-MM-DD |
| `encoding` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `estimate` | ชั่วโมงประมาณของงาน |
| `fields` | สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม |
| `first` | รายการที่มี key น้อยที่สุดในรอบเลือก |
| `fixture` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `follow_redirects` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `form` | dict ของข้อมูลฟอร์ม POST |
| `get` | อ่านค่า dict พร้อม default เมื่อไม่มี key |
| `get_data` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `handle` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `history` | ประวัติหลายรายการ |
| `hours` | จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน |
| `html` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `index` | ตำแหน่งที่ผ่านตรวจขอบเขต |
| `isoformat` | แปลง date เป็น YYYY-MM-DD |
| `isolated` | Flask test client ที่ใช้ storage/settings ชั่วคราว |
| `json` | standard library serialize/parse JSON |
| `len` | จำนวนสมาชิก/อักขระ |
| `load` | อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก |
| `mark` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `member` | สมาชิกหนึ่งคน |
| `message` | ข้อความคืนให้ app แสดง banner |
| `models` | module คลาสและฟังก์ชันกลาง |
| `monkeypatch` | pytest helper เปลี่ยนตัวแปรและคืนเมื่อจบ test |
| `note` | หมายเหตุของประวัติ |
| `number` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `overview` | รวมข้อมูลทุกงาน แผน การจัดสรรวันนี้ และสถิติเป็น context เดียวให้ทุกหน้าใช้ |
| `owner` | string รหัสสมาชิกที่รับงาน หรือว่าง |
| `page1` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `page2` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `page3` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `pages` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `parametrize` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `path` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `pending` | รายการงานที่ remaining>0 |
| `plan` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `post` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `priority` | ระดับ high/normal/low |
| `pytest` | เครื่องมือทดสอบที่ environment โครงการมีอยู่ |
| `response` | ผล HTTP จาก test client หรือ fetch ตามภาษา |
| `result` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `row` | dict ข้อมูลงานหนึ่งรายการ |
| `sample_file` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `save` | เขียนทั้งรายการงานผ่าน storage |
| `saved` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `second` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `setattr` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `stale_form` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `startswith` | ตรวจว่าข้อความขึ้นต้นตามที่กำหนด |
| `status_code` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `storage` | module อ่าน/เขียนงานที่อาจารย์ให้ |
| `str` | แปลงเป็นข้อความ |
| `subtask` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `subtasks` | list ขั้นตอนย่อย |
| `sum` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `summary` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `task` | Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน |
| `team` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `team_data` | อ่าน TEAM_FILE JSON เป็น dict; ฟังก์ชันนี้ไม่มี fallback เมื่อไฟล์เสีย |
| `test_add_owner_priority_and_subtasks_keeps_seven_fields` | ตรวจ POST add พร้อม owner/high/งานย่อย มี 7 field และไม่มี work ปลอม |
| `test_all_forms_have_versions_and_templates_escape_user_input` | ตรวจไม่มีหน้าข้อผิดพลาด ชื่อ script escape hidden version และ POST ปิดได้ |
| `test_bad_indices_do_not_crash_or_save` | ตรวจ unicode digit, ติดลบ, ว่าง, และเลขยาวไม่ทำให้พัง/บันทึก |
| `test_client` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `test_daily_hours_saved_and_used_across_pages` | ตรวจบันทึก settings ใช้ร่วมทุกหน้า และค่าผิดไม่เปลี่ยนค่าที่บันทึก |
| `test_daily_summary_groups_actual_work_only` | ตรวจ work 1+1.5 วันเดียวรวม 2.5/2 ครั้ง โดย complete 8 ไม่รวม |
| `test_empty_and_completed_only_data_have_no_focus` | ตรวจข้อมูลว่าง/เสร็จหมดไม่มี focus และแผนไม่มี pending |
| `test_existing_five_fields_still_load_without_rewriting` | ตรวจทุกหน้าอ่านข้อมูล 5 field ได้ และ GET ไม่ rewrite รายการ |
| `test_invalid_add_does_not_mutate_data` | ใช้ parameter ค่าผิด 15 แบบ ตรวจข้อความผิดและข้อมูลเดิมอยู่ครบ |
| `test_overdue_included_and_tiny_shortfall_never_looks_on_track` | ตรวจงานค้างรวมในภาระอนาคต และส่วนขาด 0.01 ยังขึ้นเสี่ยง |
| `test_overlogging_and_future_work_date_are_rejected` | ปฏิเสธบันทึกเกิน remaining และ work_date อนาคตโดยยอดเดิมไม่เปลี่ยน |
| `test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated` | ตรวจเพิ่มวันอดีตต้องยืนยัน แต่ update วันที่อดีตเดิมแก้ชื่อได้ |
| `test_past_logs_and_estimated_completion_do_not_consume_today` | ตรวจ work วันก่อนกับ complete วันนี้ไม่ลดงบวันนี้ และ summary นับจริงวันเดิม |
| `test_plan_example_nine_required_four_available_and_five_short` | ตรวจตัวอย่าง 18 ชั่วโมง/2 วัน ต้อง 9 มี 4 ขาด 5 ต่อวันและ 10 รวม |
| `test_plan_uses_daily_capacity_and_groups_identical_deadlines` | เทียบส่วนขาดที่งบ 2/4 และงานวันเดียวกันมี cumulative/gap เท่ากัน |
| `test_recommendations_never_overbook_today_and_use_priority_tiebreak` | ตรวจค้างก่อน ใกล้ก่อน รวม today_hours ไม่เกินงบ และ high ชนะเมื่อเกณฑ์อื่นเท่ากัน |
| `test_reopen_requires_prior_manual_completion` | ตรวจ reopen ของงานค้างหรือเสร็จจากชั่วโมงโดยไม่มี snapshot ถูกปฏิเสธ |
| `test_stale_row_cannot_modify_a_shifted_or_updated_task` | ตรวจ form เก่าหลังลบ row ก่อนหน้าหรือเปลี่ยนชื่อไม่ไปแก้งานใหม่ |
| `test_start_complete_reopen_updates_all_pages_and_preserves_real_hours` | ตรวจ start→complete→reopen งานย่อยคืนค่า สถิติเปลี่ยน และ complete ไม่เพิ่ม actual_total |
| `test_team_counts_progress_and_unassigned_tasks` | ตรวจ owner/count/progress/unassigned และเกณฑ์ overloaded |
| `test_today_work_reduces_recommendation_budget_and_capacity` | ตรวจ work วันนี้จากงานเสร็จลดทั้งงบคำแนะนำและความจุ และเมื่อครบไม่มีจัดสรรเพิ่ม |
| `test_work_logs_accumulate_real_hours_and_subtasks_are_independent` | ตรวจ work 1.5+2.5=4, progress 37%, ติ๊กงานย่อยไม่เปลี่ยนชั่วโมง และครบงาน |
| `timedelta` | ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง |
| `title` | ชื่องาน/ชื่อหัวข้อขึ้นกับ dict |
| `tmp_path` | พื้นที่ชั่วคราวของ pytest |
| `today` | วันที่ปัจจุบันจากเครื่อง Python |
| `update` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `value` | ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน |
| `version_of` | serialize row แบบ sort_keys แล้วคืน SHA-256 hex สำหรับตรวจฟอร์มเดิม ไม่ใช่การเข้ารหัส |
| `work_date` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |
| `work_history` | รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work |
| `write_text` | ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```python
"""Business tests for the upgraded planner; all mutations use temporary files."""
from datetime import date, timedelta
import json

import pytest

import app
import models
import storage
from pages import page1, page2, page3, team


def task(title="งาน A", days=1, estimate=4, done=0, priority="normal", owner=""):
    return {"title": title, "course": "การเขียนโปรแกรม",
            "due_date": (date.today() + timedelta(days=days)).isoformat(),
            "estimated_hours": estimate, "done_hours": done, "priority": priority,
            "details": {"owner": owner, "started": done > 0, "subtasks": [],
                        "history": [], "created_on": date.today().isoformat(),
                        "progress_on": ""}}


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    data_file = tmp_path / "data.json"
    sample_file = tmp_path / "data.sample.json"
    data_file.write_text("[]", encoding="utf-8")
    sample_file.write_text("[]", encoding="utf-8")
    monkeypatch.setattr(storage, "DATA_FILE", str(data_file))
    monkeypatch.setattr(storage, "SAMPLE_FILE", str(sample_file))
    monkeypatch.setattr(models, "SETTINGS_FILE", str(tmp_path / "settings.json"))
    return app.app.test_client()


def fields(row, index=0, action="complete"):
    return {"action": action, "no": str(index), "version": models.version_of(row)}


def add_form(**changes):
    form = {"action": "add", "title": "งานใหม่", "course": "ฟิสิกส์",
            "due_date": (date.today() + timedelta(days=2)).isoformat(),
            "estimated_hours": "4", "done_hours": "0", "priority": "normal",
            "owner": ""}
    form.update(changes)
    return form


def test_existing_five_fields_still_load_without_rewriting(isolated):
    row = task()
    del row["priority"]
    del row["details"]
    storage.save([row])
    before = storage.load()
    for path in ("/", "/page1", "/page2", "/page3", "/team"):
        response = isolated.get(path)
        assert response.status_code == 200
        assert "ยังไม่พร้อม" not in response.get_data(as_text=True)
    assert storage.load() == before


def test_add_owner_priority_and_subtasks_keeps_seven_fields(isolated):
    owner = models.team_data()["members"][0]["id"]
    form = add_form(owner=owner, priority="high", subtasks="วิเคราะห์\nออกแบบ\nทดสอบ")
    response = isolated.post("/page2", data=form, follow_redirects=True)
    assert "เพิ่มงานแล้ว" in response.get_data(as_text=True)
    row = storage.load()[0]
    assert len(row) == 7
    assert row["details"]["owner"] == owner
    assert row["priority"] == "high"
    assert len(row["details"]["subtasks"]) == 3
    assert not row["details"]["history"]


@pytest.mark.parametrize("changes", [
    {"title": "   "}, {"course": ""}, {"title": "ก" * 81}, {"course": "ก" * 41},
    {"due_date": "2026-02-30"}, {"due_date": "20260930"},
    {"estimated_hours": "0"}, {"estimated_hours": "-1"},
    {"estimated_hours": "200.1"}, {"estimated_hours": "nan"},
    {"estimated_hours": "inf"}, {"done_hours": "-1"}, {"done_hours": "5"},
    {"priority": "unknown"}, {"owner": "999999"},
])
def test_invalid_add_does_not_mutate_data(isolated, changes):
    storage.save([task()])
    before = storage.load()
    message = page2.handle(add_form(**changes))
    assert message.startswith("✗")
    assert storage.load() == before


def test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated(isolated):
    form = add_form(due_date=(date.today() - timedelta(days=1)).isoformat())
    assert page2.handle(form).startswith("✗")
    assert storage.load() == []
    form["acknowledge_past"] = "yes"
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    form.update(fields(row, action="update"))
    del form["acknowledge_past"]
    form["title"] = "อัปเดตงานค้าง"
    assert page2.handle(form).startswith("✓")
    assert storage.load()[0]["title"] == "อัปเดตงานค้าง"


def test_start_complete_reopen_updates_all_pages_and_preserves_real_hours(isolated):
    row = task(done=1)
    row["details"]["subtasks"] = [{"title": "ออกแบบ", "done": True},
                                 {"title": "ทดสอบ", "done": False}]
    storage.save([row])
    assert page1.handle(fields(row, action="start")).startswith("✓")
    row = storage.load()[0]
    assert page1.handle(fields(row)).startswith("✓")
    saved = storage.load()[0]
    assert saved["done_hours"] == 4
    assert all(subtask["done"] for subtask in saved["details"]["subtasks"])
    assert page1.build()["open_count"] == 0
    assert page1.build()["completed_count"] == 1
    assert page3.build({})["risk_count"] == 0
    history, actual = models.work_history(page2.build()["items"])
    assert actual == 0
    assert history[0]["kind"] == "complete"
    assert page1.handle(fields(saved, action="reopen")).startswith("✓")
    saved = storage.load()[0]
    assert saved["done_hours"] == 1
    assert [subtask["done"] for subtask in saved["details"]["subtasks"]] == [True, False]


def test_work_logs_accumulate_real_hours_and_subtasks_are_independent(isolated):
    row = task()
    row["details"]["subtasks"] = [{"title": "ทดสอบ", "done": False}]
    storage.save([row])
    form = fields(row, action="log_time")
    form.update(hours="1.5", work_date=date.today().isoformat(), note="ทำส่วนแรก")
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    assert row["done_hours"] == 1.5
    assert page1.build()["items"][0]["progress"] == 37
    form = fields(row, action="toggle_subtask")
    form["subtask_no"] = "0"
    assert page2.handle(form).startswith("✓")
    row = storage.load()[0]
    assert row["details"]["subtasks"][0]["done"]
    assert row["done_hours"] == 1.5
    form = fields(row, action="log_time")
    form.update(hours="2.5", work_date=date.today().isoformat())
    assert page2.handle(form).startswith("✓")
    assert page1.build()["open_count"] == 0
    assert page2.build()["actual_total"] == 4


def test_overlogging_and_future_work_date_are_rejected(isolated):
    row = task()
    storage.save([row])
    form = fields(row, action="log_time")
    form.update(hours="5", work_date=date.today().isoformat())
    assert page2.handle(form).startswith("✗")
    form.update(hours="1", work_date=(date.today() + timedelta(days=1)).isoformat())
    assert page2.handle(form).startswith("✗")
    assert storage.load()[0]["done_hours"] == 0


def test_stale_row_cannot_modify_a_shifted_or_updated_task(isolated):
    first, second = task("ก่อน"), task("หลัง")
    storage.save([first, second])
    stale_form = fields(second, 1)
    assert page2.handle(fields(first, action="delete")).startswith("✓")
    assert page1.handle(stale_form).startswith("✗")
    assert storage.load()[0]["title"] == "หลัง"
    assert storage.load()[0]["done_hours"] == 0
    stale_form = fields(storage.load()[0], action="complete")
    row = storage.load()[0]
    row["title"] = "ชื่อใหม่"
    storage.save([row])
    assert page1.handle(stale_form).startswith("✗")


@pytest.mark.parametrize("number", ["²", "-1", "", "99999999999999999999"])
def test_bad_indices_do_not_crash_or_save(isolated, number):
    row = task()
    storage.save([row])
    form = fields(row)
    form["no"] = number
    assert page1.handle(form).startswith("✗")
    assert storage.load()[0]["done_hours"] == 0


def test_plan_uses_daily_capacity_and_groups_identical_deadlines(isolated):
    storage.save([task("วันนี้", 0, 3), task("พรุ่งนี้", 1, 4)])
    plan = page3.build({"hours": "2"})
    assert [row["gap"] for row in plan["tasks"]] == [1, 3]
    assert plan["risk_count"] == 2
    assert page3.build({"hours": "4"})["risk_count"] == 0
    storage.save([task("งานแรก", 0, 3), task("งานสอง", 0, 4)])
    plan = page3.build({"hours": "4"})
    assert [row["gap"] for row in plan["tasks"]] == [3, 3]
    assert [row["cumulative_hours"] for row in plan["tasks"]] == [7, 7]
    assert plan["risk_count"] == 2


def test_plan_example_nine_required_four_available_and_five_short(isolated):
    storage.save([task(estimate=18, days=1)])
    plan = page3.build({"hours": "4"})
    row = plan["tasks"][0]
    assert row["hours_per_day"] == 9
    assert row["shortfall_per_day"] == 5
    assert row["gap"] == 10
    assert plan["required_daily"] == 9
    assert plan["daily_shortfall"] == 5


def test_overdue_included_and_tiny_shortfall_never_looks_on_track(isolated):
    storage.save([task("ค้าง", -1, 2), task("อนาคต", 1, 3)])
    plan = page3.build({"hours": "2"})
    assert plan["tasks"][1]["cumulative_hours"] == 5
    assert plan["tasks"][1]["gap"] == 1
    storage.save([task(estimate=2.01, days=0)])
    row = page3.build({"hours": "2"})["tasks"][0]
    assert row["at_risk"]
    assert row["gap"] == 0.1


def test_daily_hours_saved_and_used_across_pages(isolated):
    assert page3.handle({"action": "save_hours", "hours": "4"}).startswith("✓")
    assert page1.build()["daily_hours"] == 4
    assert page3.build({})["daily_hours"] == 4
    assert team.build()["daily_hours"] == 4
    for value in ("0", "12.1", "abc", "nan", "inf"):
        assert page3.handle({"action": "save_hours", "hours": value}).startswith("✗")
        assert page3.build({"hours": value})["daily_hours"] == 4


def test_recommendations_never_overbook_today_and_use_priority_tiebreak(isolated):
    storage.save([task("ไกล", 7, 10), task("ใกล้", 1, 1), task("ค้าง", -1, 1)])
    overview = page1.build()
    assert overview["focus"]["title"] == "ค้าง"
    assert [row["title"] for row in overview["recommendations"]] == ["ค้าง", "ใกล้"]
    assert sum(row["today_hours"] for row in overview["recommendations"]) <= 2
    storage.save([task("ต่ำ", 2, 2, priority="low"), task("สูง", 2, 2, priority="high")])
    assert page1.build()["focus"]["title"] == "สูง"


def test_team_counts_progress_and_unassigned_tasks(isolated):
    owner = models.team_data()["members"][0]["id"]
    storage.save([task("ของสมาชิก", 2, 4, 1, owner=owner), task("ไม่มอบหมาย")])
    summary = team.build()
    member = summary["members"][0]
    assert member["assignment_count"] == 1
    assert member["open_count"] == 1
    assert member["progress"] == 25
    assert len(summary["unassigned"]) == 1
    storage.save([task("ภาระมาก", 2, 20, owner=owner)])
    assert team.build()["members"][0]["overloaded"]


def test_empty_and_completed_only_data_have_no_focus(isolated):
    assert page1.build()["focus"] is None
    assert page3.build({})["tasks"] == []
    storage.save([task(estimate=4, done=4)])
    assert page3.build({})["tasks"] == []
    assert len(page1.build()["completed"]) == 1


def test_all_forms_have_versions_and_templates_escape_user_input(isolated):
    storage.save([task(title='<script>alert("x")</script>')])
    for path in ("/page1", "/page2", "/page3", "/team"):
        html = isolated.get(path).get_data(as_text=True)
        assert "ยังไม่พร้อม" not in html
        assert '<script>alert("x")</script>' not in html
        if path != "/team":
            assert 'name="version"' in html
    row = storage.load()[0]
    response = isolated.post("/page1", data=fields(row), follow_redirects=True)
    assert "งานที่เสร็จแล้ว" in response.get_data(as_text=True)
    assert storage.load()[0]["done_hours"] == 4


def test_today_work_reduces_recommendation_budget_and_capacity(isolated):
    done = task("เสร็จแล้ว", days=0, estimate=1, done=1)
    done["details"]["history"] = [{"date": date.today().isoformat(),
                                    "hours": 1, "kind": "work", "note": ""}]
    pending = task("วันนี้", days=0, estimate=2)
    storage.save([done, pending])
    result = page1.build()
    assert result["actual_today"] == 1
    assert result["today_remaining"] == 1
    assert result["recommendations"][0]["today_hours"] == 1
    plan = page3.build({})["tasks"][0]
    assert plan["available_hours"] == 1
    assert plan["hours_per_day"] == 3
    assert plan["gap"] == 1
    done["details"]["history"][0]["hours"] = 2
    storage.save([done, pending])
    assert page1.build()["recommendations"] == []
    assert page1.build()["open_count"] == 1


def test_past_logs_and_estimated_completion_do_not_consume_today(isolated):
    row = task("ก่อนหน้า", done=1)
    row["details"]["history"] = [
        {"date": (date.today() - timedelta(days=1)).isoformat(),
         "hours": 1, "kind": "work", "note": ""}]
    storage.save([row, task("วันนี้", days=0)])
    assert page1.handle(fields(row)).startswith("✓")
    assert page1.build()["actual_today"] == 0
    assert page1.build()["today_remaining"] == 2
    assert page2.build()["daily_history"][0]["hours"] == 1
    assert page2.build()["actual_total"] == 1


def test_reopen_requires_prior_manual_completion(isolated):
    for row in (task(), task(estimate=4, done=4)):
        storage.save([row])
        assert page1.handle(fields(row, action="reopen")).startswith("✗")
        assert storage.load() == [row]


def test_daily_summary_groups_actual_work_only(isolated):
    row = task()
    today = date.today().isoformat()
    row["details"]["history"] = [
        {"date": today, "hours": 1, "kind": "work", "note": "ส่วนแรก"},
        {"date": today, "hours": 1.5, "kind": "work", "note": "ส่วนสอง"},
        {"date": today, "hours": 8, "kind": "complete", "note": ""}]
    storage.save([row])
    summary = page2.build()
    assert summary["daily_history"] == [{"date": today, "hours": 2.5, "count": 2}]
    assert summary["actual_total"] == 2.5
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```python
"""Business tests for the upgraded planner; all mutations use temporary files."""
```

- ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน

### L2

```python
from datetime import date, timedelta
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from datetime import date, timedelta`
- เครื่องหมาย: `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง

### L3

```python
import json
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import json`
- ชื่อที่ต้องรู้: `json` = standard library serialize/parse JSON

### L4

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L5

```python
import pytest
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import pytest`
- ชื่อที่ต้องรู้: `pytest` = เครื่องมือทดสอบที่ environment โครงการมีอยู่

### L6

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L7

```python
import app
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import app`
- ชื่อที่ต้องรู้: `app` = module Flask router ที่อาจารย์ให้

### L8

```python
import models
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import models`
- ชื่อที่ต้องรู้: `models` = module คลาสและฟังก์ชันกลาง

### L9

```python
import storage
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `import storage`
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้

### L10

```python
from pages import page1, page2, page3, team
```

- นำเข้าชื่อ/module ที่ใช้ในไฟล์: `from pages import page1, page2, page3, team`
- เครื่องหมาย: `,` คั่นสมาชิก/argument

### L11

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L12

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L13

```python
def task(title="งาน A", days=1, estimate=4, done=0, priority="normal", owner=""):
```

- ประกาศฟังก์ชัน `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `priority` = ระดับ high/normal/low; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง

### L14

```python
    return {"title": title, "course": "การเขียนโปรแกรม",
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L15

```python
            "due_date": (date.today() + timedelta(days=days)).isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L14: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `+` บวกเลข/ต่อข้อความตามชนิด; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L16

```python
            "estimated_hours": estimate, "done_hours": done, "priority": priority,
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L14: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `priority` = ระดับ high/normal/low
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L17

```python
            "details": {"owner": owner, "started": done > 0, "subtasks": [],
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L14: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `{` เปิด dict/set ตามบริบท; `,` คั่นสมาชิก/argument; `>` มากกว่า; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L18

```python
                        "history": [], "created_on": date.today().isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L14: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 24 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L19

```python
                        "progress_on": ""}}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L14: คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'details'`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set
- ย่อหน้า 24 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L20

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L21

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L22

```python
@pytest.fixture
```

- decorator ของ pytest; fixture/parametrize จัดการข้อมูลชั่วคราวหรือขยายกรณีทดสอบ ไม่ใช่ route ของแอป
- เครื่องหมาย: `@` เริ่ม decorator ในชุดทดสอบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย
- ชื่อที่ต้องรู้: `pytest` = เครื่องมือทดสอบที่ environment โครงการมีอยู่

### L23

```python
def isolated(tmp_path, monkeypatch):
```

- ประกาศฟังก์ชัน `isolated`: pytest fixture เปลี่ยน path data/sample/settings ไป tmp_path ผ่าน monkeypatch แล้วคืน Flask test client
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `tmp_path` = พื้นที่ชั่วคราวของ pytest; `monkeypatch` = pytest helper เปลี่ยนตัวแปรและคืนเมื่อจบ test

### L24

```python
    data_file = tmp_path / "data.json"
```

- เก็บผล (`tmp_path` หาร/ต่อ Path `'data.json'`) ลง `data_file`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `tmp_path` = พื้นที่ชั่วคราวของ pytest
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L25

```python
    sample_file = tmp_path / "data.sample.json"
```

- เก็บผล (`tmp_path` หาร/ต่อ Path `'data.sample.json'`) ลง `sample_file`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `/` หาร; กับ pathlib.Path เป็นการต่อ path
- ชื่อที่ต้องรู้: `tmp_path` = พื้นที่ชั่วคราวของ pytest
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L26

```python
    data_file.write_text("[]", encoding="utf-8")
```

- เรียก `data_file.write_text` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L27

```python
    sample_file.write_text("[]", encoding="utf-8")
```

- เรียก `sample_file.write_text` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L28

```python
    monkeypatch.setattr(storage, "DATA_FILE", str(data_file))
```

- เรียก `monkeypatch.setattr` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `monkeypatch` = pytest helper เปลี่ยนตัวแปรและคืนเมื่อจบ test; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `str` = แปลงเป็นข้อความ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L29

```python
    monkeypatch.setattr(storage, "SAMPLE_FILE", str(sample_file))
```

- เรียก `monkeypatch.setattr` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `monkeypatch` = pytest helper เปลี่ยนตัวแปรและคืนเมื่อจบ test; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `str` = แปลงเป็นข้อความ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L30

```python
    monkeypatch.setattr(models, "SETTINGS_FILE", str(tmp_path / "settings.json"))
```

- เรียก `monkeypatch.setattr` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `/` หาร; กับ pathlib.Path เป็นการต่อ path; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `monkeypatch` = pytest helper เปลี่ยนตัวแปรและคืนเมื่อจบ test; `models` = module คลาสและฟังก์ชันกลาง; `str` = แปลงเป็นข้อความ; `tmp_path` = พื้นที่ชั่วคราวของ pytest
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L31

```python
    return app.app.test_client()
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: เรียก `app.app.test_client` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `app` = module Flask router ที่อาจารย์ให้
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L32

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L33

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L34

```python
def fields(row, index=0, action="complete"):
```

- ประกาศฟังก์ชัน `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต

### L35

```python
    return {"action": action, "no": str(index), "version": models.version_of(row)}
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: dict ที่มี key `'action'`, `'no'`, `'version'`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `str` = แปลงเป็นข้อความ; `index` = ตำแหน่งที่ผ่านตรวจขอบเขต; `models` = module คลาสและฟังก์ชันกลาง; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L36

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L37

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L38

```python
def add_form(**changes):
```

- ประกาศฟังก์ชัน `add_form`: สร้างค่าฟอร์มเพิ่มงานที่ถูกต้องแล้ว update ด้วย changes เพื่อทดลองค่าผิดเป็นรายกรณี
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `**` ขยาย keyword arguments หรือยกกำลังตามบริบท; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `changes` = ค่า override สำหรับสร้างข้อมูลทดลอง

### L39

```python
    form = {"action": "add", "title": "งานใหม่", "course": "ฟิสิกส์",
```

- เก็บผล dict ที่มี key `'action'`, `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'owner'` ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L40

```python
            "due_date": (date.today() + timedelta(days=2)).isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L39: เก็บผล dict ที่มี key `'action'`, `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'owner'` ลง `form`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `+` บวกเลข/ต่อข้อความตามชนิด; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L41

```python
            "estimated_hours": "4", "done_hours": "0", "priority": "normal",
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L39: เก็บผล dict ที่มี key `'action'`, `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'owner'` ลง `form`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L42

```python
            "owner": ""}
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L39: เก็บผล dict ที่มี key `'action'`, `'title'`, `'course'`, `'due_date'`, `'estimated_hours'`, `'done_hours'`, `'priority'`, `'owner'` ลง `form`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L43

```python
    form.update(changes)
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `changes` = ค่า override สำหรับสร้างข้อมูลทดลอง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L44

```python
    return form
```

- คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: `form`
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L45

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L46

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L47

```python
def test_existing_five_fields_still_load_without_rewriting(isolated):
```

- ประกาศฟังก์ชัน `test_existing_five_fields_still_load_without_rewriting`: ตรวจทุกหน้าอ่านข้อมูล 5 field ได้ และ GET ไม่ rewrite รายการ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L48

```python
    row = task()
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L49

```python
    del row["priority"]
```

- ลบ key/รายการ `row['priority']` (อ่าน key/index) ในข้อมูลทดสอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L50

```python
    del row["details"]
```

- ลบ key/รายการ `row['details']` (อ่าน key/index) ในข้อมูลทดสอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L51

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L52

```python
    before = storage.load()
```

- เก็บผล อ่านรายการงานล่าสุดผ่าน storage.load() ลง `before`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `before` = ข้อมูลก่อนการกระทำเพื่อเทียบใน test; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L53

```python
    for path in ("/", "/page1", "/page2", "/page3", "/team"):
```

- วน tuple จำนวน 5 สมาชิกตามโค้ด ให้ `path` รับสมาชิกทีละรอบ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L54

```python
        response = isolated.get(path)
```

- เก็บผล อ่าน `path` จาก `isolated` พร้อม default เมื่อไม่มี ลง `response`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L55

```python
        assert response.status_code == 200
```

- ตรวจคำตอบใน test: ต้องให้ `response.status_code` เท่ากับ `200` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L56

```python
        assert "ยังไม่พร้อม" not in response.get_data(as_text=True)
```

- ตรวจคำตอบใน test: ต้องให้ `'ยังไม่พร้อม'` ไม่อยู่ใน เรียก `response.get_data` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `True` = boolean จริง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L57

```python
    assert storage.load() == before
```

- ตรวจคำตอบใน test: ต้องให้ อ่านรายการงานล่าสุดผ่าน storage.load() เท่ากับ `before` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `before` = ข้อมูลก่อนการกระทำเพื่อเทียบใน test
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L58

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L59

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L60

```python
def test_add_owner_priority_and_subtasks_keeps_seven_fields(isolated):
```

- ประกาศฟังก์ชัน `test_add_owner_priority_and_subtasks_keeps_seven_fields`: ตรวจ POST add พร้อม owner/high/งานย่อย มี 7 field และไม่มี work ปลอม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L61

```python
    owner = models.team_data()["members"][0]["id"]
```

- เก็บผล `models.team_data()['members'][0]['id']` (อ่าน key/index) ลง `owner`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L62

```python
    form = add_form(owner=owner, priority="high", subtasks="วิเคราะห์\nออกแบบ\nทดสอบ")
```

- เก็บผล เรียก `add_form`: สร้างค่าฟอร์มเพิ่มงานที่ถูกต้องแล้ว update ด้วย changes เพื่อทดลองค่าผิดเป็นรายกรณี ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `priority` = ระดับ high/normal/low; `subtasks` = list ขั้นตอนย่อย
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L63

```python
    response = isolated.post("/page2", data=form, follow_redirects=True)
```

- เก็บผล เรียก `isolated.post` ด้วย argument ที่แสดงในโค้ด ลง `response`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `form` = dict ของข้อมูลฟอร์ม POST; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L64

```python
    assert "เพิ่มงานแล้ว" in response.get_data(as_text=True)
```

- ตรวจคำตอบใน test: ต้องให้ `'เพิ่มงานแล้ว'` อยู่ใน เรียก `response.get_data` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L65

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L66

```python
    assert len(row) == 7
```

- ตรวจคำตอบใน test: ต้องให้ `len`(`row`) เท่ากับ `7` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L67

```python
    assert row["details"]["owner"] == owner
```

- ตรวจคำตอบใน test: ต้องให้ `row['details']['owner']` (อ่าน key/index) เท่ากับ `owner` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L68

```python
    assert row["priority"] == "high"
```

- ตรวจคำตอบใน test: ต้องให้ `row['priority']` (อ่าน key/index) เท่ากับ `'high'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L69

```python
    assert len(row["details"]["subtasks"]) == 3
```

- ตรวจคำตอบใน test: ต้องให้ `len`(`row['details']['subtasks']` (อ่าน key/index)) เท่ากับ `3` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L70

```python
    assert not row["details"]["history"]
```

- ตรวจคำตอบใน test: ต้องให้ ไม่เป็นจริง: `row['details']['history']` (อ่าน key/index) เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L71

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L72

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L73

```python
@pytest.mark.parametrize("changes", [
```

- decorator ของ pytest; fixture/parametrize จัดการข้อมูลชั่วคราวหรือขยายกรณีทดสอบ ไม่ใช่ route ของแอป
- เครื่องหมาย: `@` เริ่ม decorator ในชุดทดสอบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key
- ชื่อที่ต้องรู้: `pytest` = เครื่องมือทดสอบที่ environment โครงการมีอยู่

### L74

```python
    {"title": "   "}, {"course": ""}, {"title": "ก" * 81}, {"course": "ก" * 41},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument; `*` คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L75

```python
    {"due_date": "2026-02-30"}, {"due_date": "20260930"},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L76

```python
    {"estimated_hours": "0"}, {"estimated_hours": "-1"},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L77

```python
    {"estimated_hours": "200.1"}, {"estimated_hours": "nan"},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L78

```python
    {"estimated_hours": "inf"}, {"done_hours": "-1"}, {"done_hours": "5"},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L79

```python
    {"priority": "unknown"}, {"owner": "999999"},
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `,` คั่นสมาชิก/argument
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L80

```python
])
```

- ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว
- เครื่องหมาย: `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (

### L81

```python
def test_invalid_add_does_not_mutate_data(isolated, changes):
```

- ประกาศฟังก์ชัน `test_invalid_add_does_not_mutate_data`: ใช้ parameter ค่าผิด 15 แบบ ตรวจข้อความผิดและข้อมูลเดิมอยู่ครบ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `changes` = ค่า override สำหรับสร้างข้อมูลทดลอง

### L82

```python
    storage.save([task()])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L83

```python
    before = storage.load()
```

- เก็บผล อ่านรายการงานล่าสุดผ่าน storage.load() ลง `before`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `before` = ข้อมูลก่อนการกระทำเพื่อเทียบใน test; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L84

```python
    message = page2.handle(add_form(**changes))
```

- เก็บผล เรียก `page2.handle` ด้วย argument ที่แสดงในโค้ด ลง `message`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `**` ขยาย keyword arguments หรือยกกำลังตามบริบท; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner; `changes` = ค่า override สำหรับสร้างข้อมูลทดลอง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L85

```python
    assert message.startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `message.startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `message` = ข้อความคืนให้ app แสดง banner; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L86

```python
    assert storage.load() == before
```

- ตรวจคำตอบใน test: ต้องให้ อ่านรายการงานล่าสุดผ่าน storage.load() เท่ากับ `before` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `before` = ข้อมูลก่อนการกระทำเพื่อเทียบใน test
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L87

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L88

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L89

```python
def test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated(isolated):
```

- ประกาศฟังก์ชัน `test_past_deadline_requires_confirmation_but_old_overdue_can_be_updated`: ตรวจเพิ่มวันอดีตต้องยืนยัน แต่ update วันที่อดีตเดิมแก้ชื่อได้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L90

```python
    form = add_form(due_date=(date.today() - timedelta(days=1)).isoformat())
```

- เก็บผล เรียก `add_form`: สร้างค่าฟอร์มเพิ่มงานที่ถูกต้องแล้ว update ด้วย changes เพื่อทดลองค่าผิดเป็นรายกรณี ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `-` ลบ/เครื่องหมายติดลบ
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `due_date` = วันส่งมาตรฐาน YYYY-MM-DD; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L91

```python
    assert page2.handle(form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L92

```python
    assert storage.load() == []
```

- ตรวจคำตอบใน test: ต้องให้ อ่านรายการงานล่าสุดผ่าน storage.load() เท่ากับ list [] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L93

```python
    form["acknowledge_past"] = "yes"
```

- เก็บผล `'yes'` ลง `form['acknowledge_past']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L94

```python
    assert page2.handle(form).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L95

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L96

```python
    form.update(fields(row, action="update"))
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L97

```python
    del form["acknowledge_past"]
```

- ลบ key/รายการ `form['acknowledge_past']` (อ่าน key/index) ในข้อมูลทดสอบ
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L98

```python
    form["title"] = "อัปเดตงานค้าง"
```

- เก็บผล `'อัปเดตงานค้าง'` ลง `form['title']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L99

```python
    assert page2.handle(form).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L100

```python
    assert storage.load()[0]["title"] == "อัปเดตงานค้าง"
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['title']` (อ่าน key/index) เท่ากับ `'อัปเดตงานค้าง'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L101

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L102

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L103

```python
def test_start_complete_reopen_updates_all_pages_and_preserves_real_hours(isolated):
```

- ประกาศฟังก์ชัน `test_start_complete_reopen_updates_all_pages_and_preserves_real_hours`: ตรวจ start→complete→reopen งานย่อยคืนค่า สถิติเปลี่ยน และ complete ไม่เพิ่ม actual_total
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L104

```python
    row = task(done=1)
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L105

```python
    row["details"]["subtasks"] = [{"title": "ออกแบบ", "done": True},
```

- เก็บผล list [dict ที่มี key `'title'`, `'done'`, dict ที่มี key `'title'`, `'done'`] ลง `row['details']['subtasks']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L106

```python
                                 {"title": "ทดสอบ", "done": False}]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L105: เก็บผล list [dict ที่มี key `'title'`, `'done'`, dict ที่มี key `'title'`, `'done'`] ลง `row['details']['subtasks']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `False` = boolean เท็จ
- ย่อหน้า 33 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L107

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L108

```python
    assert page1.handle(fields(row, action="start")).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(fields(row, action='start')).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L109

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L110

```python
    assert page1.handle(fields(row)).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(fields(row)).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L111

```python
    saved = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `saved`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L112

```python
    assert saved["done_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `saved['done_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L113

```python
    assert all(subtask["done"] for subtask in saved["details"]["subtasks"])
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `all` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L114

```python
    assert page1.build()["open_count"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['open_count']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L115

```python
    assert page1.build()["completed_count"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['completed_count']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L116

```python
    assert page3.build({})["risk_count"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({})['risk_count']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L117

```python
    history, actual = models.work_history(page2.build()["items"])
```

- เก็บผล เรียก `models.work_history`: รวมประวัติทุกงาน เติมชื่อ/เจ้าของ/ประเภท เรียงวันที่ใหม่ก่อน และรวมจริงเฉพาะ work ลง `(history, actual)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L118

```python
    assert actual == 0
```

- ตรวจคำตอบใน test: ต้องให้ `actual` เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L119

```python
    assert history[0]["kind"] == "complete"
```

- ตรวจคำตอบใน test: ต้องให้ `history[0]['kind']` (อ่าน key/index) เท่ากับ `'complete'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `history` = ประวัติหลายรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L120

```python
    assert page1.handle(fields(saved, action="reopen")).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(fields(saved, action='reopen')).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L121

```python
    saved = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `saved`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L122

```python
    assert saved["done_hours"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `saved['done_hours']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L123

```python
    assert [subtask["done"] for subtask in saved["details"]["subtasks"]] == [True, False]
```

- ตรวจคำตอบใน test: ต้องให้ `[subtask['done'] for subtask in saved['details']['subtasks']]` เท่ากับ list [`True`, `False`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `True` = boolean จริง; `False` = boolean เท็จ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L124

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L125

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L126

```python
def test_work_logs_accumulate_real_hours_and_subtasks_are_independent(isolated):
```

- ประกาศฟังก์ชัน `test_work_logs_accumulate_real_hours_and_subtasks_are_independent`: ตรวจ work 1.5+2.5=4, progress 37%, ติ๊กงานย่อยไม่เปลี่ยนชั่วโมง และครบงาน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L127

```python
    row = task()
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L128

```python
    row["details"]["subtasks"] = [{"title": "ทดสอบ", "done": False}]
```

- เก็บผล list [dict ที่มี key `'title'`, `'done'`] ลง `row['details']['subtasks']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `False` = boolean เท็จ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L129

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L130

```python
    form = fields(row, action="log_time")
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L131

```python
    form.update(hours="1.5", work_date=date.today().isoformat(), note="ทำส่วนแรก")
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD; `note` = หมายเหตุของประวัติ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L132

```python
    assert page2.handle(form).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L133

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L134

```python
    assert row["done_hours"] == 1.5
```

- ตรวจคำตอบใน test: ต้องให้ `row['done_hours']` (อ่าน key/index) เท่ากับ `1.5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L135

```python
    assert page1.build()["items"][0]["progress"] == 37
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['items'][0]['progress']` (อ่าน key/index) เท่ากับ `37` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L136

```python
    form = fields(row, action="toggle_subtask")
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L137

```python
    form["subtask_no"] = "0"
```

- เก็บผล `'0'` ลง `form['subtask_no']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L138

```python
    assert page2.handle(form).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L139

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L140

```python
    assert row["details"]["subtasks"][0]["done"]
```

- ตรวจคำตอบใน test: ต้องให้ `row['details']['subtasks'][0]['done']` (อ่าน key/index) เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L141

```python
    assert row["done_hours"] == 1.5
```

- ตรวจคำตอบใน test: ต้องให้ `row['done_hours']` (อ่าน key/index) เท่ากับ `1.5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L142

```python
    form = fields(row, action="log_time")
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L143

```python
    form.update(hours="2.5", work_date=date.today().isoformat())
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L144

```python
    assert page2.handle(form).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L145

```python
    assert page1.build()["open_count"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['open_count']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L146

```python
    assert page2.build()["actual_total"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `page2.build()['actual_total']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L147

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L148

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L149

```python
def test_overlogging_and_future_work_date_are_rejected(isolated):
```

- ประกาศฟังก์ชัน `test_overlogging_and_future_work_date_are_rejected`: ปฏิเสธบันทึกเกิน remaining และ work_date อนาคตโดยยอดเดิมไม่เปลี่ยน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L150

```python
    row = task()
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L151

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L152

```python
    form = fields(row, action="log_time")
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L153

```python
    form.update(hours="5", work_date=date.today().isoformat())
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L154

```python
    assert page2.handle(form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L155

```python
    form.update(hours="1", work_date=(date.today() + timedelta(days=1)).isoformat())
```

- เรียก `form.update` ด้วย argument ที่แสดงในโค้ด
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `+` บวกเลข/ต่อข้อความตามชนิด
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `hours` = จำนวนชั่วโมง; อ่านหน่วยรายวันหรือครั้งนี้ตามฟังก์ชัน; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L156

```python
    assert page2.handle(form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L157

```python
    assert storage.load()[0]["done_hours"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['done_hours']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L158

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L159

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L160

```python
def test_stale_row_cannot_modify_a_shifted_or_updated_task(isolated):
```

- ประกาศฟังก์ชัน `test_stale_row_cannot_modify_a_shifted_or_updated_task`: ตรวจ form เก่าหลังลบ row ก่อนหน้าหรือเปลี่ยนชื่อไม่ไปแก้งานใหม่
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L161

```python
    first, second = task("ก่อน"), task("หลัง")
```

- เก็บผล tuple [เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้, เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้] ลง `(first, second)`
- เครื่องหมาย: `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `first` = รายการที่มี key น้อยที่สุดในรอบเลือก; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L162

```python
    storage.save([first, second])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `first` = รายการที่มี key น้อยที่สุดในรอบเลือก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L163

```python
    stale_form = fields(second, 1)
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `stale_form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L164

```python
    assert page2.handle(fields(first, action="delete")).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page2.handle(fields(first, action='delete')).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `first` = รายการที่มี key น้อยที่สุดในรอบเลือก; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L165

```python
    assert page1.handle(stale_form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(stale_form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L166

```python
    assert storage.load()[0]["title"] == "หลัง"
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['title']` (อ่าน key/index) เท่ากับ `'หลัง'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L167

```python
    assert storage.load()[0]["done_hours"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['done_hours']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L168

```python
    stale_form = fields(storage.load()[0], action="complete")
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `stale_form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L169

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L170

```python
    row["title"] = "ชื่อใหม่"
```

- เก็บผล `'ชื่อใหม่'` ลง `row['title']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L171

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L172

```python
    assert page1.handle(stale_form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(stale_form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L173

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L174

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L175

```python
@pytest.mark.parametrize("number", ["²", "-1", "", "99999999999999999999"])
```

- decorator ของ pytest; fixture/parametrize จัดการข้อมูลชั่วคราวหรือขยายกรณีทดสอบ ไม่ใช่ route ของแอป
- เครื่องหมาย: `@` เริ่ม decorator ในชุดทดสอบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `pytest` = เครื่องมือทดสอบที่ environment โครงการมีอยู่

### L176

```python
def test_bad_indices_do_not_crash_or_save(isolated, number):
```

- ประกาศฟังก์ชัน `test_bad_indices_do_not_crash_or_save`: ตรวจ unicode digit, ติดลบ, ว่าง, และเลขยาวไม่ทำให้พัง/บันทึก
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L177

```python
    row = task()
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L178

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L179

```python
    form = fields(row)
```

- เก็บผล เรียก `fields`: สร้าง form action/no/version จาก row ที่กำหนดสำหรับทดสอบฟอร์ม ลง `form`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L180

```python
    form["no"] = number
```

- เก็บผล `number` ลง `form['no']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L181

```python
    assert page1.handle(form).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(form).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `form` = dict ของข้อมูลฟอร์ม POST; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L182

```python
    assert storage.load()[0]["done_hours"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['done_hours']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L183

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L184

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L185

```python
def test_plan_uses_daily_capacity_and_groups_identical_deadlines(isolated):
```

- ประกาศฟังก์ชัน `test_plan_uses_daily_capacity_and_groups_identical_deadlines`: เทียบส่วนขาดที่งบ 2/4 และงานวันเดียวกันมี cumulative/gap เท่ากัน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L186

```python
    storage.save([task("วันนี้", 0, 3), task("พรุ่งนี้", 1, 4)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L187

```python
    plan = page3.build({"hours": "2"})
```

- เก็บผล เรียก `page3.build` ด้วย argument ที่แสดงในโค้ด ลง `plan`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L188

```python
    assert [row["gap"] for row in plan["tasks"]] == [1, 3]
```

- ตรวจคำตอบใน test: ต้องให้ `[row['gap'] for row in plan['tasks']]` เท่ากับ list [`1`, `3`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L189

```python
    assert plan["risk_count"] == 2
```

- ตรวจคำตอบใน test: ต้องให้ `plan['risk_count']` (อ่าน key/index) เท่ากับ `2` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L190

```python
    assert page3.build({"hours": "4"})["risk_count"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({'hours': '4'})['risk_count']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L191

```python
    storage.save([task("งานแรก", 0, 3), task("งานสอง", 0, 4)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L192

```python
    plan = page3.build({"hours": "4"})
```

- เก็บผล เรียก `page3.build` ด้วย argument ที่แสดงในโค้ด ลง `plan`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L193

```python
    assert [row["gap"] for row in plan["tasks"]] == [3, 3]
```

- ตรวจคำตอบใน test: ต้องให้ `[row['gap'] for row in plan['tasks']]` เท่ากับ list [`3`, `3`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L194

```python
    assert [row["cumulative_hours"] for row in plan["tasks"]] == [7, 7]
```

- ตรวจคำตอบใน test: ต้องให้ `[row['cumulative_hours'] for row in plan['tasks']]` เท่ากับ list [`7`, `7`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L195

```python
    assert plan["risk_count"] == 2
```

- ตรวจคำตอบใน test: ต้องให้ `plan['risk_count']` (อ่าน key/index) เท่ากับ `2` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L196

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L197

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L198

```python
def test_plan_example_nine_required_four_available_and_five_short(isolated):
```

- ประกาศฟังก์ชัน `test_plan_example_nine_required_four_available_and_five_short`: ตรวจตัวอย่าง 18 ชั่วโมง/2 วัน ต้อง 9 มี 4 ขาด 5 ต่อวันและ 10 รวม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L199

```python
    storage.save([task(estimate=18, days=1)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `estimate` = ชั่วโมงประมาณของงาน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L200

```python
    plan = page3.build({"hours": "4"})
```

- เก็บผล เรียก `page3.build` ด้วย argument ที่แสดงในโค้ด ลง `plan`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L201

```python
    row = plan["tasks"][0]
```

- เก็บผล `plan['tasks'][0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L202

```python
    assert row["hours_per_day"] == 9
```

- ตรวจคำตอบใน test: ต้องให้ `row['hours_per_day']` (อ่าน key/index) เท่ากับ `9` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L203

```python
    assert row["shortfall_per_day"] == 5
```

- ตรวจคำตอบใน test: ต้องให้ `row['shortfall_per_day']` (อ่าน key/index) เท่ากับ `5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L204

```python
    assert row["gap"] == 10
```

- ตรวจคำตอบใน test: ต้องให้ `row['gap']` (อ่าน key/index) เท่ากับ `10` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L205

```python
    assert plan["required_daily"] == 9
```

- ตรวจคำตอบใน test: ต้องให้ `plan['required_daily']` (อ่าน key/index) เท่ากับ `9` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L206

```python
    assert plan["daily_shortfall"] == 5
```

- ตรวจคำตอบใน test: ต้องให้ `plan['daily_shortfall']` (อ่าน key/index) เท่ากับ `5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L207

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L208

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L209

```python
def test_overdue_included_and_tiny_shortfall_never_looks_on_track(isolated):
```

- ประกาศฟังก์ชัน `test_overdue_included_and_tiny_shortfall_never_looks_on_track`: ตรวจงานค้างรวมในภาระอนาคต และส่วนขาด 0.01 ยังขึ้นเสี่ยง
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L210

```python
    storage.save([task("ค้าง", -1, 2), task("อนาคต", 1, 3)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `-` ลบ/เครื่องหมายติดลบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L211

```python
    plan = page3.build({"hours": "2"})
```

- เก็บผล เรียก `page3.build` ด้วย argument ที่แสดงในโค้ด ลง `plan`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L212

```python
    assert plan["tasks"][1]["cumulative_hours"] == 5
```

- ตรวจคำตอบใน test: ต้องให้ `plan['tasks'][1]['cumulative_hours']` (อ่าน key/index) เท่ากับ `5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L213

```python
    assert plan["tasks"][1]["gap"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `plan['tasks'][1]['gap']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L214

```python
    storage.save([task(estimate=2.01, days=0)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `estimate` = ชั่วโมงประมาณของงาน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L215

```python
    row = page3.build({"hours": "2"})["tasks"][0]
```

- เก็บผล `page3.build({'hours': '2'})['tasks'][0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L216

```python
    assert row["at_risk"]
```

- ตรวจคำตอบใน test: ต้องให้ `row['at_risk']` (อ่าน key/index) เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L217

```python
    assert row["gap"] == 0.1
```

- ตรวจคำตอบใน test: ต้องให้ `row['gap']` (อ่าน key/index) เท่ากับ `0.1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L218

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L219

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L220

```python
def test_daily_hours_saved_and_used_across_pages(isolated):
```

- ประกาศฟังก์ชัน `test_daily_hours_saved_and_used_across_pages`: ตรวจบันทึก settings ใช้ร่วมทุกหน้า และค่าผิดไม่เปลี่ยนค่าที่บันทึก
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L221

```python
    assert page3.handle({"action": "save_hours", "hours": "4"}).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page3.handle({'action': 'save_hours', 'hours': '4'}).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L222

```python
    assert page1.build()["daily_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['daily_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L223

```python
    assert page3.build({})["daily_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({})['daily_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L224

```python
    assert team.build()["daily_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `team.build()['daily_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L225

```python
    for value in ("0", "12.1", "abc", "nan", "inf"):
```

- วน tuple จำนวน 5 สมาชิกตามโค้ด ให้ `value` รับสมาชิกทีละรอบ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L226

```python
        assert page3.handle({"action": "save_hours", "hours": value}).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page3.handle({'action': 'save_hours', 'hours': value}).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L227

```python
        assert page3.build({"hours": value})["daily_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({'hours': value})['daily_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `value` = ค่าที่อ่าน/ตรวจอยู่ในฟังก์ชัน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L228

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L229

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L230

```python
def test_recommendations_never_overbook_today_and_use_priority_tiebreak(isolated):
```

- ประกาศฟังก์ชัน `test_recommendations_never_overbook_today_and_use_priority_tiebreak`: ตรวจค้างก่อน ใกล้ก่อน รวม today_hours ไม่เกินงบ และ high ชนะเมื่อเกณฑ์อื่นเท่ากัน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L231

```python
    storage.save([task("ไกล", 7, 10), task("ใกล้", 1, 1), task("ค้าง", -1, 1)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `-` ลบ/เครื่องหมายติดลบ; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L232

```python
    overview = page1.build()
```

- เก็บผล เรียก `page1.build` ด้วย argument ที่แสดงในโค้ด ลง `overview`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L233

```python
    assert overview["focus"]["title"] == "ค้าง"
```

- ตรวจคำตอบใน test: ต้องให้ `overview['focus']['title']` (อ่าน key/index) เท่ากับ `'ค้าง'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L234

```python
    assert [row["title"] for row in overview["recommendations"]] == ["ค้าง", "ใกล้"]
```

- ตรวจคำตอบใน test: ต้องให้ `[row['title'] for row in overview['recommendations']]` เท่ากับ list [`'ค้าง'`, `'ใกล้'`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L235

```python
    assert sum(row["today_hours"] for row in overview["recommendations"]) <= 2
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `sum` ด้วย argument ที่แสดงในโค้ด ไม่เกิน `2` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `<=` น้อยกว่าหรือเท่ากับ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L236

```python
    storage.save([task("ต่ำ", 2, 2, priority="low"), task("สูง", 2, 2, priority="high")])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `priority` = ระดับ high/normal/low
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L237

```python
    assert page1.build()["focus"]["title"] == "สูง"
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['focus']['title']` (อ่าน key/index) เท่ากับ `'สูง'` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L238

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L239

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L240

```python
def test_team_counts_progress_and_unassigned_tasks(isolated):
```

- ประกาศฟังก์ชัน `test_team_counts_progress_and_unassigned_tasks`: ตรวจ owner/count/progress/unassigned และเกณฑ์ overloaded
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L241

```python
    owner = models.team_data()["members"][0]["id"]
```

- เก็บผล `models.team_data()['members'][0]['id']` (อ่าน key/index) ลง `owner`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง; `models` = module คลาสและฟังก์ชันกลาง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L242

```python
    storage.save([task("ของสมาชิก", 2, 4, 1, owner=owner), task("ไม่มอบหมาย")])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L243

```python
    summary = team.build()
```

- เก็บผล เรียก `team.build` ด้วย argument ที่แสดงในโค้ด ลง `summary`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L244

```python
    member = summary["members"][0]
```

- เก็บผล `summary['members'][0]` (อ่าน key/index) ลง `member`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L245

```python
    assert member["assignment_count"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `member['assignment_count']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L246

```python
    assert member["open_count"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `member['open_count']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L247

```python
    assert member["progress"] == 25
```

- ตรวจคำตอบใน test: ต้องให้ `member['progress']` (อ่าน key/index) เท่ากับ `25` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `member` = สมาชิกหนึ่งคน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L248

```python
    assert len(summary["unassigned"]) == 1
```

- ตรวจคำตอบใน test: ต้องให้ `len`(`summary['unassigned']` (อ่าน key/index)) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L249

```python
    storage.save([task("ภาระมาก", 2, 20, owner=owner)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `owner` = string รหัสสมาชิกที่รับงาน หรือว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L250

```python
    assert team.build()["members"][0]["overloaded"]
```

- ตรวจคำตอบใน test: ต้องให้ `team.build()['members'][0]['overloaded']` (อ่าน key/index) เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L251

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L252

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L253

```python
def test_empty_and_completed_only_data_have_no_focus(isolated):
```

- ประกาศฟังก์ชัน `test_empty_and_completed_only_data_have_no_focus`: ตรวจข้อมูลว่าง/เสร็จหมดไม่มี focus และแผนไม่มี pending
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L254

```python
    assert page1.build()["focus"] is None
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['focus']` (อ่าน key/index) เป็น object เดียวกับ None (ไม่มีค่าที่ใช้ได้) เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `None` = ไม่มีค่าที่ใช้ได้ ไม่ใช่ 0 หรือ string ว่าง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L255

```python
    assert page3.build({})["tasks"] == []
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({})['tasks']` (อ่าน key/index) เท่ากับ list [] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L256

```python
    storage.save([task(estimate=4, done=4)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L257

```python
    assert page3.build({})["tasks"] == []
```

- ตรวจคำตอบใน test: ต้องให้ `page3.build({})['tasks']` (อ่าน key/index) เท่ากับ list [] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L258

```python
    assert len(page1.build()["completed"]) == 1
```

- ตรวจคำตอบใน test: ต้องให้ `len`(`page1.build()['completed']` (อ่าน key/index)) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `len` = จำนวนสมาชิก/อักขระ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L259

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L260

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L261

```python
def test_all_forms_have_versions_and_templates_escape_user_input(isolated):
```

- ประกาศฟังก์ชัน `test_all_forms_have_versions_and_templates_escape_user_input`: ตรวจไม่มีหน้าข้อผิดพลาด ชื่อ script escape hidden version และ POST ปิดได้
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L262

```python
    storage.save([task(title='<script>alert("x")</script>')])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `title` = ชื่องาน/ชื่อหัวข้อขึ้นกับ dict
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L263

```python
    for path in ("/page1", "/page2", "/page3", "/team"):
```

- วน tuple [`'/page1'`, `'/page2'`, `'/page3'`, `'/team'`] ให้ `path` รับสมาชิกทีละรอบ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L264

```python
        html = isolated.get(path).get_data(as_text=True)
```

- เก็บผล เรียก `isolated.get(path).get_data` ด้วย argument ที่แสดงในโค้ด ลง `html`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `get` = อ่านค่า dict พร้อม default เมื่อไม่มี key; `True` = boolean จริง
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L265

```python
        assert "ยังไม่พร้อม" not in html
```

- ตรวจคำตอบใน test: ต้องให้ `'ยังไม่พร้อม'` ไม่อยู่ใน `html` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L266

```python
        assert '<script>alert("x")</script>' not in html
```

- ตรวจคำตอบใน test: ต้องให้ `'<script>alert("x")</script>'` ไม่อยู่ใน `html` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L267

```python
        if path != "/team":
```

- ตรวจเงื่อนไข: `path` ไม่เท่ากับ `'/team'`; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป
- เครื่องหมาย: `!=` เปรียบเทียบไม่เท่ากัน; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L268

```python
            assert 'name="version"' in html
```

- ตรวจคำตอบใน test: ต้องให้ `'name="version"'` อยู่ใน `html` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- ย่อหน้า 12 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L269

```python
    row = storage.load()[0]
```

- เก็บผล `storage.load()[0]` (อ่าน key/index) ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L270

```python
    response = isolated.post("/page1", data=fields(row), follow_redirects=True)
```

- เก็บผล เรียก `isolated.post` ด้วย argument ที่แสดงในโค้ด ลง `response`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว; `row` = dict ข้อมูลงานหนึ่งรายการ; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L271

```python
    assert "งานที่เสร็จแล้ว" in response.get_data(as_text=True)
```

- ตรวจคำตอบใน test: ต้องให้ `'งานที่เสร็จแล้ว'` อยู่ใน เรียก `response.get_data` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `response` = ผล HTTP จาก test client หรือ fetch ตามภาษา; `True` = boolean จริง
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L272

```python
    assert storage.load()[0]["done_hours"] == 4
```

- ตรวจคำตอบใน test: ต้องให้ `storage.load()[0]['done_hours']` (อ่าน key/index) เท่ากับ `4` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L273

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L274

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L275

```python
def test_today_work_reduces_recommendation_budget_and_capacity(isolated):
```

- ประกาศฟังก์ชัน `test_today_work_reduces_recommendation_budget_and_capacity`: ตรวจ work วันนี้จากงานเสร็จลดทั้งงบคำแนะนำและความจุ และเมื่อครบไม่มีจัดสรรเพิ่ม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L276

```python
    done = task("เสร็จแล้ว", days=0, estimate=1, done=1)
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `done`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `estimate` = ชั่วโมงประมาณของงาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L277

```python
    done["details"]["history"] = [{"date": date.today().isoformat(),
```

- เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `done['details']['history']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L278

```python
                                    "hours": 1, "kind": "work", "note": ""}]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L277: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `done['details']['history']`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `]` ปิด list/การอ้าง index/key
- ย่อหน้า 36 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L279

```python
    pending = task("วันนี้", days=0, estimate=2)
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `pending`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `pending` = รายการงานที่ remaining>0; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `estimate` = ชั่วโมงประมาณของงาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L280

```python
    storage.save([done, pending])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `pending` = รายการงานที่ remaining>0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L281

```python
    result = page1.build()
```

- เก็บผล เรียก `page1.build` ด้วย argument ที่แสดงในโค้ด ลง `result`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L282

```python
    assert result["actual_today"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `result['actual_today']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L283

```python
    assert result["today_remaining"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `result['today_remaining']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L284

```python
    assert result["recommendations"][0]["today_hours"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `result['recommendations'][0]['today_hours']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L285

```python
    plan = page3.build({})["tasks"][0]
```

- เก็บผล `page3.build({})['tasks'][0]` (อ่าน key/index) ลง `plan`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `{` เปิด dict/set ตามบริบท; `}` ปิด dict/set; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L286

```python
    assert plan["available_hours"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `plan['available_hours']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L287

```python
    assert plan["hours_per_day"] == 3
```

- ตรวจคำตอบใน test: ต้องให้ `plan['hours_per_day']` (อ่าน key/index) เท่ากับ `3` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L288

```python
    assert plan["gap"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `plan['gap']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L289

```python
    done["details"]["history"][0]["hours"] = 2
```

- เก็บผล `2` ลง `done['details']['history'][0]['hours']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L290

```python
    storage.save([done, pending])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น; `pending` = รายการงานที่ remaining>0
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L291

```python
    assert page1.build()["recommendations"] == []
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['recommendations']` (อ่าน key/index) เท่ากับ list [] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L292

```python
    assert page1.build()["open_count"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['open_count']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L293

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L294

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L295

```python
def test_past_logs_and_estimated_completion_do_not_consume_today(isolated):
```

- ประกาศฟังก์ชัน `test_past_logs_and_estimated_completion_do_not_consume_today`: ตรวจ work วันก่อนกับ complete วันนี้ไม่ลดงบวันนี้ และ summary นับจริงวันเดิม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L296

```python
    row = task("ก่อนหน้า", done=1)
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L297

```python
    row["details"]["history"] = [
```

- เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L298

```python
        {"date": (date.today() - timedelta(days=1)).isoformat(),
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L297: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `(` เปิดกลุ่มนิพจน์/argument/tuple; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `)` ปิดกลุ่มที่เปิดด้วย (; `-` ลบ/เครื่องหมายติดลบ; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `,` คั่นสมาชิก/argument
- ชื่อที่ต้องรู้: `date` = ชนิดวันที่ระดับวันจาก datetime; `today` = วันที่ปัจจุบันจากเครื่อง Python; `timedelta` = ส่วนต่างเวลาที่ใช้สร้างวันที่ทดลอง; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L299

```python
         "hours": 1, "kind": "work", "note": ""}]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L297: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `]` ปิด list/การอ้าง index/key
- ย่อหน้า 9 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L300

```python
    storage.save([row, task("วันนี้", days=0)])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `days` = จำนวนวันรวมวันนี้ หรือ list สรุปวันตามบริบท
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L301

```python
    assert page1.handle(fields(row)).startswith("✓")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(fields(row)).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L302

```python
    assert page1.build()["actual_today"] == 0
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['actual_today']` (อ่าน key/index) เท่ากับ `0` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L303

```python
    assert page1.build()["today_remaining"] == 2
```

- ตรวจคำตอบใน test: ต้องให้ `page1.build()['today_remaining']` (อ่าน key/index) เท่ากับ `2` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L304

```python
    assert page2.build()["daily_history"][0]["hours"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `page2.build()['daily_history'][0]['hours']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L305

```python
    assert page2.build()["actual_total"] == 1
```

- ตรวจคำตอบใน test: ต้องให้ `page2.build()['actual_total']` (อ่าน key/index) เท่ากับ `1` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L306

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L307

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L308

```python
def test_reopen_requires_prior_manual_completion(isolated):
```

- ประกาศฟังก์ชัน `test_reopen_requires_prior_manual_completion`: ตรวจ reopen ของงานค้างหรือเสร็จจากชั่วโมงโดยไม่มี snapshot ถูกปฏิเสธ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L309

```python
    for row in (task(), task(estimate=4, done=4)):
```

- วน tuple [เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้, เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้] ให้ `row` รับสมาชิกทีละรอบ
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน; `estimate` = ชั่วโมงประมาณของงาน; `done` = ชั่วโมงที่ทำแล้ว/ยอดรวม done ในบริบทนั้น
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L310

```python
        storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L311

```python
        assert page1.handle(fields(row, action="reopen")).startswith("✗")
```

- ตรวจคำตอบใน test: ต้องให้ เรียก `page1.handle(fields(row, action='reopen')).startswith` ด้วย argument ที่แสดงในโค้ด เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `,` คั่นสมาชิก/argument; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `startswith` = ตรวจว่าข้อความขึ้นต้นตามที่กำหนด
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L312

```python
        assert storage.load() == [row]
```

- ตรวจคำตอบใน test: ต้องให้ อ่านรายการงานล่าสุดผ่าน storage.load() เท่ากับ list [`row`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `==` เปรียบเทียบเท่ากัน; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `load` = อ่าน/parse JSON หรือ storage.load ตาม module ที่เรียก; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L313

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L314

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน

### L315

```python
def test_daily_summary_groups_actual_work_only(isolated):
```

- ประกาศฟังก์ชัน `test_daily_summary_groups_actual_work_only`: ตรวจ work 1+1.5 วันเดียวรวม 2.5/2 ครั้ง โดย complete 8 ไม่รวม
- เครื่องหมาย: `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท
- ชื่อที่ต้องรู้: `isolated` = Flask test client ที่ใช้ storage/settings ชั่วคราว

### L316

```python
    row = task()
```

- เก็บผล เรียก `task`: สร้าง row จำลองสำหรับ pytest โดย due_date สัมพันธ์กับวันนี้ ลง `row`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ; `task` = Assignment หรือ dict ของงานตามฟังก์ชันที่ใช้งาน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L317

```python
    today = date.today().isoformat()
```

- เก็บผล เรียก `date.today().isoformat` ด้วย argument ที่แสดงในโค้ด ลง `today`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `today` = วันที่ปัจจุบันจากเครื่อง Python; `date` = ชนิดวันที่ระดับวันจาก datetime; `isoformat` = แปลง date เป็น YYYY-MM-DD
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L318

```python
    row["details"]["history"] = [
```

- เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ
- ชื่อที่ต้องรู้: `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L319

```python
        {"date": today, "hours": 1, "kind": "work", "note": "ส่วนแรก"},
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L318: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `today` = วันที่ปัจจุบันจากเครื่อง Python
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L320

```python
        {"date": today, "hours": 1.5, "kind": "work", "note": "ส่วนสอง"},
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L318: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `today` = วันที่ปัจจุบันจากเครื่อง Python
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L321

```python
        {"date": today, "hours": 8, "kind": "complete", "note": ""}]
```

- ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L318: เก็บผล list [dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`, dict ที่มี key `'date'`, `'hours'`, `'kind'`, `'note'`] ลง `row['details']['history']`
- เครื่องหมาย: `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set; `]` ปิด list/การอ้าง index/key
- ชื่อที่ต้องรู้: `today` = วันที่ปัจจุบันจากเครื่อง Python
- ย่อหน้า 8 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L322

```python
    storage.save([row])
```

- เขียนรายการงานทั้งไฟล์ผ่าน storage.save()
- เครื่องหมาย: `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `)` ปิดกลุ่มที่เปิดด้วย (
- ชื่อที่ต้องรู้: `storage` = module อ่าน/เขียนงานที่อาจารย์ให้; `save` = เขียนทั้งรายการงานผ่าน storage; `row` = dict ข้อมูลงานหนึ่งรายการ
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L323

```python
    summary = page2.build()
```

- เก็บผล เรียก `page2.build` ด้วย argument ที่แสดงในโค้ด ลง `summary`
- เครื่องหมาย: `=` กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ; `.` เข้าถึง attribute/method ของชื่อด้านซ้าย; `(` เปิดกลุ่มนิพจน์/argument/tuple; `)` ปิดกลุ่มที่เปิดด้วย (
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L324

```python
    assert summary["daily_history"] == [{"date": today, "hours": 2.5, "count": 2}]
```

- ตรวจคำตอบใน test: ต้องให้ `summary['daily_history']` (อ่าน key/index) เท่ากับ list [dict ที่มี key `'date'`, `'hours'`, `'count'`] เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน; `{` เปิด dict/set ตามบริบท; `:` เริ่ม block หรือคั่น key:value ใน dict ตามบริบท; `,` คั่นสมาชิก/argument; `}` ปิด dict/set
- ชื่อที่ต้องรู้: `today` = วันที่ปัจจุบันจากเครื่อง Python
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง

### L325

```python
    assert summary["actual_total"] == 2.5
```

- ตรวจคำตอบใน test: ต้องให้ `summary['actual_total']` (อ่าน key/index) เท่ากับ `2.5` เป็นจริง มิฉะนั้น test ไม่ผ่าน
- เครื่องหมาย: `[` เปิด list หรือการอ้าง index/key; `]` ปิด list/การอ้าง index/key; `==` เปรียบเทียบเท่ากัน
- ย่อหน้า 4 ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง
