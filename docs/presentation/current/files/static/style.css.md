# static/style.css — CSS เดิมและส่วนที่เพิ่มสำหรับโครงการ

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 359 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `f4b7b6ab83f12222136d98a7cd12e25e9e7325c25c3999dda531d488b6070084`

**ผู้ศึกษา/บทบาท:** นายไกรวิชญ์ บุ้งทอง · Frontend / ส่วนร่วม

## 1. หน้าที่และการเชื่อมต่อ

กำหนดสี ฟอนต์ การ์ด ฟอร์ม ปุ่ม การเปรียบเทียบเวลา และหน้าจอมือถือ

- **รับเข้า:** element/class/attribute ใน HTML และขนาด viewport
- **ผลลัพธ์:** รูปแบบการแสดงผล ไม่แก้ data.json หรือสูตร

**เกี่ยวข้องกับ:** HTML ทุกหน้า; CSS custom properties ใน :root

## 2. ลำดับทำงาน

1. ส่วนเดิมกำหนดสีและ component ของ skeleton
2. ส่วนหลัง marker your own styles below เพิ่มรูปแบบ Deadline Compass
3. ชุด v2 เพิ่มงานวันนี้ quick actions งานย่อย ประวัติ และภาระทีม
4. @media 720/640 ปรับจากหลายคอลัมน์เป็นแนวตั้ง
5. กำหนด focus-visible และขนาดสัมผัสขั้นต่ำ 44px

## 3. จุดที่ต้องอธิบายให้ถูก

- อธิบายทุกบรรทัดเพื่ออ่านภาพรวม แต่ส่วนก่อน marker เป็นของเดิม ไม่อ้างว่าเราเขียนทั้งหมด
- CSS ซ้ำ selector เดิมอาจ override เฉพาะ property ตามลำดับและ specificity
- Sarabun/Noto Sans Thai ใน font stack ไม่รับประกันว่าติดตั้งจริง; ไม่มีการโหลดฟอนต์ภายนอก
- [hidden] มี display:none เฉพาะข้อความบางกลุ่มเพื่อไม่ให้รูปแบบ flex ทำให้แสดงโดยไม่ตั้งใจ
- ตารางเลื่อนเฉพาะกรอบ ไม่ซ่อน overflow ทั้งหน้าเพื่อกลบปัญหา

**ขอบเขตส่วนเดิม:** marker `your own styles below` อยู่ L171 ส่วนก่อน marker เป็น component ที่อาจารย์ให้ ส่วนหลังเป็นกฎโครงการ การอธิบายทุกบรรทัดไม่ได้อ้างว่าแก้ส่วนเดิม

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q004: Frontend และ Backend ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q004)
- [Q010: ทำงานโดยไม่ต่ออินเทอร์เน็ตได้หรือไม่?](../../TEACHER_QUESTIONS.md#q010)
- [Q068: ทำอย่างไรให้เมนูและการ์ดเหมาะกับมือถือ?](../../TEACHER_QUESTIONS.md#q068)
- [Q069: ตารางประวัติยาวกว่าจอจะทำอย่างไร?](../../TEACHER_QUESTIONS.md#q069)
- [Q070: มี Tailwind หรือโหลด Google Fonts หรือไม่?](../../TEACHER_QUESTIONS.md#q070)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```css
/* style.css — given, but you may ADD your own rules at the bottom. */
:root {
  --maroon: #7a1f2b;
  --maroon-dark: #5c1620;
  --gold: #e6b422;
  --ink: #1f2933;
  --muted: #6b7280;
  --line: #e5e7eb;
  --bg: #f7f5f2;
  --card: #ffffff;
}
* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  font-family: "Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.55;
  display: flex; flex-direction: column; min-height: 100vh;
}
.wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; width: 100%; }

/* ---------- header ---------- */
.site-header { background: linear-gradient(180deg, var(--maroon), var(--maroon-dark)); color: #fff; }
.header-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 12px 20px; }
.brand { display: flex; align-items: center; gap: 14px; color: #fff; text-decoration: none; }
.brand img { height: 56px; width: 56px; border-radius: 50%; background: #fff; padding: 2px; }
.brand-text { display: flex; flex-direction: column; }
.brand-line1 { font-weight: 700; font-size: 17px; letter-spacing: .2px; }
.brand-line2 { font-size: 12.5px; opacity: .85; }
.group-badge { font-size: 13px; background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.3); padding: 4px 12px; border-radius: 999px; white-space: nowrap; }
.site-nav { display: flex; gap: 4px; flex-wrap: wrap; padding: 0 20px 0; border-top: 1px solid rgba(255,255,255,.15); }
.site-nav a { color: #fff; text-decoration: none; padding: 10px 14px; font-size: 14px; border-bottom: 3px solid transparent; opacity: .85; }
.site-nav a:hover { opacity: 1; }
.site-nav a.active { border-bottom-color: var(--gold); opacity: 1; font-weight: 600; }

/* ---------- main ---------- */
main { flex: 1; padding: 28px 20px 48px; }
h1 { font-size: 26px; margin: 0 0 8px; }
h2 { font-size: 19px; margin: 28px 0 10px; }
.lead { color: var(--muted); margin-top: 0; }
.muted { color: var(--muted); font-weight: normal; font-size: 14px; }
small.muted { font-size: 15px; }
.banner { background: #fff8e1; border: 1px solid #f6d46a; color: #6b4d00; padding: 10px 14px; border-radius: 8px; margin-bottom: 18px; }

table { width: 100%; border-collapse: collapse; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); font-size: 14.5px; }
th { background: #f1ede8; color: var(--muted); font-weight: 600; font-size: 13px; }
tr:last-child td { border-bottom: none; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }

.btn { display: inline-block; padding: 8px 16px; border-radius: 8px; border: 1px solid var(--maroon); background: var(--maroon); color: #fff; font-size: 14px; text-decoration: none; cursor: pointer; }
.btn.ghost { background: #fff; color: var(--maroon); }
.field { margin-bottom: 14px; }
.field label { display: block; font-size: 13px; color: var(--muted); margin-bottom: 4px; }
.field input, .field select, .field textarea { width: 100%; max-width: 380px; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; font-family: inherit; }

.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }
.stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; }
.stat .label { color: var(--muted); font-size: 13px; }
.stat .value { font-size: 26px; font-weight: 700; color: var(--maroon); }

.empty { color: var(--muted); padding: 32px; text-align: center; background: var(--card); border: 1px dashed var(--line); border-radius: 10px; }

/* home */
.hero { padding: 8px 0 20px; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-decoration: none; color: var(--ink); display: flex; flex-direction: column; gap: 4px; transition: transform .1s, box-shadow .1s; }
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.07); }
.card-kicker { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; }
.card-title { font-size: 17px; font-weight: 600; color: var(--maroon); }

/* team */
.member-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 8px; }
.member { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-align: center; }
.avatar { width: 56px; height: 56px; border-radius: 50%; background: var(--maroon); color: #fff; font-size: 24px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; }
.member-name { font-weight: 600; }
.role { color: var(--maroon); font-size: 13px; margin-top: 4px; }
.task { color: var(--muted); font-size: 13px; }

/* gallery */
.gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 14px; }
.gallery figure { margin: 0; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
.gallery img { width: 100%; height: 140px; object-fit: cover; display: block; }
.gallery figcaption { padding: 8px 10px; font-size: 13.5px; }

/* not built */
.notbuilt { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 28px; }
.notbuilt .reason { font-size: 16px; }
.notbuilt pre { background: #1f2933; color: #f8fafc; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 12.5px; }
.notbuilt code { background: #f1ede8; padding: 1px 6px; border-radius: 4px; }
.hint { color: var(--muted); font-size: 14px; }

/* footer */
.site-footer { border-top: 1px solid var(--line); color: var(--muted); font-size: 13px; padding: 12px 0; background: #fff; }
.site-footer .wrap { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }

@media (max-width: 640px) {
  .brand-line1 { font-size: 14px; }
  .brand-line2 { display: none; }
  .group-badge { display: none; }
}


/* ---------- components you can use on any page ---------- */
/* panel / card */
.panel { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; }
.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: 18px; align-items: start; }
@media (max-width: 720px) { .two-col { grid-template-columns: 1fr; } }
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
.item-card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; }
.item-card img { width: 100%; height: 140px; object-fit: cover; background: #f1ede8; }
.item-card .body { padding: 12px 14px; display: flex; flex-direction: column; gap: 4px; flex: 1; }
.item-card .price { font-weight: 700; color: var(--maroon); font-size: 18px; margin-top: auto; }
/* badges & pills */
.badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 12px; font-weight: 600; background: #f1ede8; color: var(--muted); }
.badge.good { background: #e6f5ec; color: #1b6b3a; }
.badge.bad { background: #fdecec; color: #9b1c1c; }
.badge.gold { background: #fff5d6; color: #8a6100; }
.pills { display: flex; gap: 6px; flex-wrap: wrap; margin: 10px 0; }
.pills a { padding: 5px 12px; border-radius: 999px; border: 1px solid var(--line); background: #fff; color: var(--ink); text-decoration: none; font-size: 13px; }
.pills a.active { background: var(--maroon); border-color: var(--maroon); color: #fff; }
/* stat card variants */
.stat.good .value { color: #1b6b3a; }
.stat.bad .value { color: #9b1c1c; }
.stat.gold { background: #fffbe8; border-color: #f2df9a; }
.stat .unit { color: var(--muted); font-size: 12px; }
/* horizontal bars: width = percent of the biggest value (compute the % in Python) */
.bar-row { display: grid; grid-template-columns: 120px 1fr 90px; align-items: center; gap: 10px; padding: 6px 0; }
.bar-track { background: #efeae4; border-radius: 6px; height: 14px; overflow: hidden; }
.bar-fill { background: var(--maroon); height: 100%; border-radius: 6px; }
.bar-fill.gold { background: var(--gold); }
.bar-fill.green { background: #2e8b57; }
.bar-row .num { text-align: right; font-variant-numeric: tabular-nums; }
/* progress bar */
.progress { background: #efeae4; border-radius: 999px; height: 12px; overflow: hidden; }
.progress > div { background: var(--gold); height: 100%; border-radius: 999px; }
/* vertical columns chart: height = percent (compute the % in Python) */
.chart { display: flex; align-items: flex-end; gap: 8px; height: 180px; padding: 8px 0; border-bottom: 1px solid var(--line); }
.chart .col { flex: 1; display: flex; flex-direction: column; justify-content: flex-end; height: 100%; }
.chart .col > div { background: var(--maroon); border-radius: 4px 4px 0 0; }
.chart .col > div.gold { background: var(--gold); }
.chart-labels { display: flex; gap: 8px; }
.chart-labels span { flex: 1; text-align: center; font-size: 12px; color: var(--muted); }
/* buttons */
.btn.small { padding: 4px 10px; font-size: 13px; }
.btn.full { display: block; width: 100%; text-align: center; }
.btn.danger { background: #fff; color: #9b1c1c; border-color: #f3b4b4; }
form.inline { display: inline; }
/* misc */
.kbd { display: inline-block; padding: 2px 8px; border: 1px solid #cbd5e1; border-bottom-width: 3px; border-radius: 6px; background: #fff; font-family: monospace; font-size: 12px; }
.hero-box { background: linear-gradient(135deg, #fff, #f7efe9); border: 1px solid var(--line); border-radius: 14px; padding: 24px; margin-bottom: 18px; }
.note { font-size: 13px; color: var(--muted); }

/* stacked columns: put several <div class="seg"> inside a .col, heights in % of the column */
.chart .col .seg { width: 100%; }
.chart .col .seg.gold { background: var(--gold); }
.chart .col .seg.green { background: #2e8b57; }
/* donut: style="--p: 42" (percent) */
.donut { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0); display: flex; align-items: center; justify-content: center; }
.donut > span { width: 78px; height: 78px; border-radius: 50%; background: var(--card); display: flex; align-items: center; justify-content: center; font-weight: 700; color: var(--maroon); }
/* small things forms and summaries keep needing */
.thumb { width: 56px; height: 56px; object-fit: cover; border-radius: 8px; background: #f1ede8; }
.field-row { display: flex; gap: 14px; flex-wrap: wrap; align-items: flex-end; }
.field-row .field { margin: 0; }
.sum-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--line); }
.sum-row.total { border: 0; font-size: 18px; font-weight: 700; color: var(--maroon); }
.game-board { display: block; margin: 0 auto; background: #1f2933; border: 4px solid var(--maroon); border-radius: 10px; }
.hud { display: flex; gap: 10px; justify-content: center; margin: 10px 0; }

/* ---------- your own styles below ---------- */

/* Deadline Compass: page styles added without changing the given components. */
.deadline-eyebrow { display: inline-block; color: var(--maroon); font-size: 12px; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; }
.deadline-hero { display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 32px; margin-bottom: 20px; border: 1px solid #ead8cf; border-radius: 18px; background: linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%); overflow: hidden; }
.deadline-hero h1 { font-size: clamp(27px, 4vw, 40px); line-height: 1.2; margin: 8px 0 10px; color: var(--maroon-dark); }
.deadline-hero p { max-width: 480px; margin: 0 0 20px; color: #5d5552; }
.deadline-hero .btn { margin: 0 7px 7px 0; }
.deadline-hero-mark { flex: 0 0 170px; width: 170px; height: 170px; transform: rotate(9deg); border: 9px solid var(--maroon); border-radius: 22px; background: #fff; box-shadow: 16px 16px 0 rgba(122,31,43,.11); text-align: center; overflow: hidden; }
.deadline-hero-mark span:first-child { display: block; height: 40px; background: var(--maroon); color: white; font-size: 26px; line-height: 32px; }
.deadline-hero-mark span:last-child { display: block; color: var(--maroon); font-size: 76px; font-weight: 800; line-height: 115px; }
.deadline-summary { margin: 16px 0 24px; }
.deadline-summary .stat { box-shadow: 0 5px 18px rgba(31,41,51,.035); }
.deadline-summary .value { font-variant-numeric: tabular-nums; }
.deadline-alert { background: #fdecec; border: 1px solid #eab4b4; color: #802020; border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; font-weight: 600; }
.deadline-section-head { display: flex; align-items: end; justify-content: space-between; gap: 16px; margin: 22px 0 12px; }
.deadline-section-head h2 { margin: 0 0 2px; }
.deadline-section-head .note { margin: 0; }
.deadline-reminder-control { display: flex; flex-direction: column; align-items: end; gap: 4px; text-align: right; }
.deadline-task-list { display: grid; gap: 10px; }
.deadline-task { display: flex; align-items: center; justify-content: space-between; gap: 20px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px 18px; box-shadow: 0 3px 12px rgba(31,41,51,.025); }
.deadline-task-main { min-width: 0; flex: 1; }
.deadline-course { color: var(--maroon); font-size: 12px; font-weight: 700; letter-spacing: .035em; }
.deadline-task h3, .deadline-edit-card h3 { margin: 2px 0 5px; font-size: 17px; line-height: 1.3; }
.deadline-meta { color: var(--muted); font-size: 13px; margin: 0; }
.deadline-progress { width: min(100%, 360px); margin-top: 12px; height: 8px; }
.deadline-task-actions { display: flex; flex-direction: column; align-items: end; gap: 9px; flex-shrink: 0; }
.deadline-text-button { background: transparent; border: 0; padding: 2px 0; color: var(--maroon); text-decoration: underline; font: inherit; font-size: 12px; cursor: pointer; }
.deadline-footnote { margin-top: 15px; }
.deadline-page-title { margin: 2px 0 22px; }
.deadline-page-title h1 { margin-top: 5px; }
.deadline-form-layout { grid-template-columns: minmax(255px, .85fr) minmax(0, 1.4fr); }
.deadline-add-form { position: sticky; top: 16px; }
.deadline-add-form h2 { margin: 0 0 18px; }
.deadline-add-form .field input { max-width: none; }
.deadline-edit-card { margin-bottom: 10px; }
.deadline-edit-heading { display: flex; justify-content: space-between; align-items: start; gap: 12px; }
.deadline-edit-card details { border-top: 1px solid var(--line); margin-top: 12px; padding-top: 10px; }
.deadline-edit-card summary { color: var(--maroon); cursor: pointer; font-size: 13px; font-weight: 700; }
.deadline-edit-form { margin-top: 16px; }
.deadline-edit-form .field { flex: 1; min-width: 120px; }
.deadline-edit-form .field input { width: 100%; }
.deadline-delete-form { margin-top: 14px; }
.deadline-hours-form { display: flex; flex-wrap: wrap; align-items: end; gap: 12px; }
.deadline-hours-form .field { margin: 0; }
.deadline-hours-form input { max-width: 210px; }
.deadline-focus { display: flex; flex-direction: column; gap: 4px; padding: 20px 22px; border-radius: 12px; background: var(--maroon); color: #fff; }
.deadline-focus .deadline-eyebrow { color: #ffdc75; }
.deadline-focus strong { font-size: 22px; }
.deadline-focus span:last-child { font-size: 13px; opacity: .9; }
.deadline-plan-detail { margin: 9px 0 0; font-size: 13px; color: var(--ink); }
.deadline-home-hero { min-height: 260px; }
.deadline-home-cards .card { min-height: 132px; }
.deadline-home-cards .card-title { line-height: 1.35; }
.deadline-task :focus-visible, .deadline-edit-card :focus-visible, .deadline-hero :focus-visible, .deadline-hours-form :focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
@media (max-width: 720px) {
  .deadline-form-layout { grid-template-columns: 1fr; }
  .deadline-add-form { position: static; }
}
@media (max-width: 640px) {
  .deadline-hero { padding: 24px 20px; }
  .deadline-hero-mark { display: none; }
  .deadline-hero .btn { display: block; width: 100%; text-align: center; }
  .deadline-section-head { align-items: start; flex-direction: column; }
  .deadline-reminder-control { align-items: start; text-align: left; }
  .deadline-task { align-items: start; flex-direction: column; gap: 10px; }
  .deadline-task-actions { align-items: start; flex-direction: row; flex-wrap: wrap; }
  .deadline-edit-heading { flex-direction: column; }
}

/* Deadline Compass v2: daily actions, work logs, and accessible touch layouts. */
.deadline-overview-hero { padding: 26px 30px; }
.deadline-overview-hero .deadline-hero-mark span:last-child { font-size: 64px; }
.deadline-today-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 14px; }
.deadline-today-card { border: 1px solid #ebd4a0; border-top: 4px solid var(--gold); background: #fffdf6; padding: 22px; display: flex; flex-direction: column; }
.deadline-today-card h3 { font-size: 21px; line-height: 1.4; margin: 8px 0 12px; overflow-wrap: anywhere; }
.deadline-today-time { margin: 16px 0 6px; color: var(--maroon-dark); }
.deadline-today-time strong { font-size: 29px; font-variant-numeric: tabular-nums; }
.deadline-reasons { padding-left: 20px; font-size: 14px; line-height: 1.7; color: #514b47; margin: 9px 0 15px; }
.deadline-today-card .deadline-quick-actions { margin-top: auto; padding-top: 12px; }
.deadline-quick-actions { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 12px; }
.deadline-quick-actions form { margin: 0; }
.deadline-quick-actions .btn, .deadline-action-link { min-height: 44px; display: inline-flex; align-items: center; justify-content: center; line-height: 1.4; text-align: center; }
.deadline-action-link { color: var(--maroon); padding: 6px 2px; text-underline-offset: 3px; font-size: 14px; }
.deadline-task-actions { width: 245px; max-width: 100%; }
.deadline-task-actions .deadline-quick-actions { flex-direction: column; align-items: stretch; width: 100%; margin: 0; }
.deadline-task-actions .btn { width: 100%; }
.deadline-text-button { min-height: 44px; padding: 10px 5px; font-size: 14px; }
.deadline-badge-row { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
.deadline-badge-row .badge, .deadline-edit-heading > .badge { font-size: 13px; padding: 5px 10px; }
.deadline-alert p { margin: 6px 0 0; font-weight: 400; font-size: 15px; }
.deadline-insight { background: #fdf8e9; border: 1px solid #ebdfb8; border-radius: 10px; padding: 14px 16px; color: #635022; font-size: 15px; }
.deadline-insight a { color: var(--maroon); }
.deadline-completed-section { border-top: 1px solid var(--line); margin-top: 30px; padding-top: 8px; }
.deadline-completed-section .deadline-task { background: #f5faf6; }
.deadline-refresh-notice { padding: 12px; border: 1px solid #b6d6f2; background: #edf6ff; border-radius: 8px; }
.deadline-refresh-notice[hidden], .deadline-form-error[hidden], .deadline-past-confirm[hidden] { display: none; }
.deadline-help { display: block; font-size: 13px; line-height: 1.6; color: #5f6671; margin-top: 6px; }
.deadline-form-error { color: #9b1c1c; padding: 10px 12px; border-radius: 8px; background: #fdecec; font-size: 14px; }
.deadline-past-confirm { display: flex; align-items: flex-start; gap: 10px; margin: 0 0 16px; padding: 12px; font-size: 14px; line-height: 1.5; background: #fff5d6; border-radius: 8px; color: #6b4d00; }
.deadline-past-confirm input { width: 22px; height: 22px; margin: 0; flex-shrink: 0; accent-color: var(--maroon); }
.deadline-subtask-setup { margin-bottom: 20px; }
.deadline-subtask-setup summary, .deadline-work-details > summary, .deadline-member > details > summary { min-height: 44px; padding: 10px 0; cursor: pointer; color: var(--maroon); font-weight: 600; }
.deadline-subtask-setup textarea { resize: vertical; min-height: 140px; }
.deadline-work-section { padding: 6px 0 18px; border-bottom: 1px solid var(--line); }
.deadline-work-section h4 { font-size: 16px; margin: 16px 0; }
.deadline-log-form .field-row { align-items: start; }
.deadline-log-form .field { flex: 1; min-width: 150px; }
.deadline-subtask-list { list-style: none; margin: 0; padding: 0; }
.deadline-subtask-list li { margin-bottom: 7px; }
.deadline-subtask-toggle { display: flex; align-items: center; gap: 10px; width: 100%; min-height: 44px; padding: 10px 12px; border: 1px solid var(--line); border-radius: 8px; background: #fff; color: var(--ink); font: inherit; font-size: 15px; text-align: left; cursor: pointer; overflow-wrap: anywhere; }
.deadline-subtask-toggle.is-done { color: #1b6b3a; background: #eef8f0; }
.deadline-subtask-toggle.is-done span { color: #1b6b3a; }
.deadline-subtask-add { margin-top: 15px; display: flex; flex-wrap: wrap; gap: 8px; align-items: end; }
.deadline-subtask-add .field { flex: 1; min-width: 150px; margin: 0; }
.deadline-subtask-add .field input { max-width: none; }
.deadline-edit-card { scroll-margin-top: 18px; }
.deadline-edit-card:target { outline: 3px solid var(--gold); outline-offset: 3px; }
.deadline-edit-card .field input, .deadline-edit-card .field select { max-width: none; }
.deadline-plan-card { padding: 22px; }
.deadline-plan-card h3 { font-size: 19px; margin: 5px 0 7px; overflow-wrap: anywhere; }
.deadline-time-comparison { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin: 20px 0 14px; }
.deadline-time-comparison > div { display: flex; flex-direction: column; gap: 6px; padding: 14px; background: #f8f5f1; border: 1px solid var(--line); border-radius: 10px; }
.deadline-time-comparison span { color: #62676d; font-size: 13px; }
.deadline-time-comparison strong { font-size: 25px; font-variant-numeric: tabular-nums; }
.deadline-time-comparison small { font-size: 12px; font-weight: 400; }
.deadline-time-comparison .deadline-time-bad { color: #9b1c1c; background: #fdecec; border-color: #f3b4b4; }
.deadline-focus-actions .btn { border-color: #fff; }
.deadline-focus-actions .deadline-action-link { color: #fff; }
.deadline-history-section { margin-top: 32px; }
.deadline-table-scroll { width: 100%; overflow-x: auto; border-radius: 10px; }
.deadline-table-scroll table { min-width: 580px; }
.deadline-table-scroll td { vertical-align: top; line-height: 1.6; }
.deadline-member-grid { grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); }
.deadline-member { text-align: left; padding: 22px; min-width: 0; }
.deadline-member .avatar { margin: 0 0 12px; }
.deadline-member h3 { font-size: 18px; margin: 4px 0; overflow-wrap: anywhere; }
.deadline-member-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 18px; }
.deadline-member-stats > div { display: flex; flex-direction: column; gap: 3px; background: #f7f5f2; padding: 10px 8px; border-radius: 8px; }
.deadline-member-stats strong { font-size: 23px; color: var(--maroon); }
.deadline-member-stats span { font-size: 12px; color: #62676d; }
.deadline-member-warning { color: #9b1c1c; background: #fdecec; padding: 10px; font-size: 14px; border-radius: 8px; }
.deadline-member-tasks { padding-left: 18px; font-size: 14px; }
.deadline-member-tasks li { margin: 10px 0; }
.deadline-member-tasks a { color: var(--maroon); overflow-wrap: anywhere; }
.deadline-member-tasks small { display: block; color: #62676d; margin-top: 4px; }
.deadline-task h3, .deadline-meta, .deadline-plan-detail, .deadline-section-head h2, .members { overflow-wrap: anywhere; }
input, select, textarea { min-width: 0; }
.deadline-add-form .field input, .deadline-add-form .field select, .deadline-add-form .field textarea { max-width: none; }
.deadline-add-form .field input, .deadline-add-form .field select, .deadline-edit-card .field input, .deadline-edit-card .field select, .deadline-hours-form input { min-height: 44px; }
.deadline-add-form .field label, .deadline-edit-card .field label, .deadline-hours-form label { font-size: 14px; color: #515964; }
.deadline-add-form .btn, .deadline-edit-card .btn, .deadline-hours-form .btn, .deadline-member .btn { min-height: 44px; }
main :focus-visible, .site-nav a:focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
@media (max-width: 720px) {
  .deadline-task { align-items: start; flex-direction: column; }
  .deadline-task-actions { width: 100%; align-items: start; }
  .deadline-task-actions .deadline-quick-actions { flex-direction: row; align-items: center; }
  .deadline-task-actions .btn { width: auto; }
  .deadline-hours-form { align-items: stretch; }
}
@media (max-width: 640px) {
  .wrap { padding-left: 16px; padding-right: 16px; }
  .header-row { flex-direction: column; align-items: start; gap: 10px; }
  .brand { width: 100%; gap: 10px; }
  .brand img { height: 42px; width: 42px; flex-shrink: 0; }
  .brand-text { min-width: 0; }
  .brand-line1 { font-size: 14px; overflow-wrap: anywhere; }
  .brand-line2 { font-size: 11px; overflow-wrap: anywhere; }
  .group-badge { align-self: start; }
  .site-nav { gap: 0; }
  .site-nav a { min-height: 44px; padding: 11px 10px; }
  .deadline-overview-hero { padding: 24px 20px; }
  .deadline-task, .deadline-plan-card, .deadline-today-card, .deadline-member { padding: 18px; }
  .deadline-quick-actions form { flex: 1 1 180px; }
  .deadline-quick-actions .btn { width: 100%; }
  .deadline-action-link { width: 100%; justify-content: start; }
  .deadline-task-actions .btn { width: 100%; }
  .deadline-add-form .field input, .deadline-edit-card .field input, .deadline-hours-form input, .deadline-add-form select, .deadline-edit-card select, .deadline-add-form textarea { font-size: 16px; }
  .deadline-time-comparison { grid-template-columns: 1fr; }
  .deadline-time-comparison > div { flex-direction: row; align-items: center; justify-content: space-between; gap: 8px; }
  .deadline-hours-form .field { flex: 1 1 100%; }
  .deadline-hours-form input { max-width: none; }
  .deadline-hours-form .btn { width: 100%; }
  .deadline-table-scroll table { min-width: 520px; }
}

.deadline-daily-history { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 16px; }
.deadline-daily-history .panel { display: flex; flex-direction: column; gap: 8px; padding: 16px; }
.deadline-daily-history strong { color: var(--maroon); font-size: 1.2rem; }
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```css
/* style.css — given, but you may ADD your own rules at the bottom. */
```

- comment บอกส่วนของ stylesheet: /* style.css — given, but you may ADD your own rules at the bottom. */

### L2

```css
:root {
```

- selector `:root` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย

### L3

```css
  --maroon: #7a1f2b;
```

- `--maroon`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#7a1f2b`

### L4

```css
  --maroon-dark: #5c1620;
```

- `--maroon-dark`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#5c1620`

### L5

```css
  --gold: #e6b422;
```

- `--gold`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#e6b422`

### L6

```css
  --ink: #1f2933;
```

- `--ink`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#1f2933`

### L7

```css
  --muted: #6b7280;
```

- `--muted`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#6b7280`

### L8

```css
  --line: #e5e7eb;
```

- `--line`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#e5e7eb`

### L9

```css
  --bg: #f7f5f2;
```

- `--bg`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#f7f5f2`

### L10

```css
  --card: #ffffff;
```

- `--card`: นิยามตัวแปร CSS ให้ var(...) อ้างใช้ = `#ffffff`

### L11

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `:root`

### L12

```css
* { box-sizing: border-box; }
```

- selector `*` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `box-sizing`: วิธีรวม padding/border ในขนาด = `border-box`
- } จบ block ของกฎ/เงื่อนไข `*`

### L13

```css
html, body { margin: 0; }
```

- selector `html, body` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `html, body`

### L14

```css
body {
```

- selector `body` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย

### L15

```css
  font-family: "Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif;
```

- `font-family`: ชุดฟอนต์ตามลำดับ = `"Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif`

### L16

```css
  color: var(--ink);
```

- `color`: สีตัวอักษร = `var(--ink)`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L17

```css
  background: var(--bg);
```

- `background`: พื้นหลัง/gradient = `var(--bg)`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L18

```css
  line-height: 1.55;
```

- `line-height`: ระยะบรรทัด = `1.55`

### L19

```css
  display: flex; flex-direction: column; min-height: 100vh;
```

- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `min-height`: ความสูงต่ำสุด = `100vh`

### L20

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `body`

### L21

```css
.wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; width: 100%; }
```

- selector `.wrap` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `960px`
- `margin`: ระยะภายนอก = `0 auto`
- `padding`: ระยะภายใน = `0 20px`
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.wrap`

### L22

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L23

```css
/* ---------- header ---------- */
```

- comment บอกส่วนของ stylesheet: /* ---------- header ---------- */

### L24

```css
.site-header { background: linear-gradient(180deg, var(--maroon), var(--maroon-dark)); color: #fff; }
```

- selector `.site-header` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `linear-gradient(180deg, var(--maroon), var(--maroon-dark))`
- `color`: สีตัวอักษร = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.site-header`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L25

```css
.header-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 12px 20px; }
```

- selector `.header-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `gap`: ช่องว่างระหว่าง item = `16px`
- `padding`: ระยะภายใน = `12px 20px`
- } จบ block ของกฎ/เงื่อนไข `.header-row`

### L26

```css
.brand { display: flex; align-items: center; gap: 14px; color: #fff; text-decoration: none; }
```

- selector `.brand` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `gap`: ช่องว่างระหว่าง item = `14px`
- `color`: สีตัวอักษร = `#fff`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `none`
- } จบ block ของกฎ/เงื่อนไข `.brand`

### L27

```css
.brand img { height: 56px; width: 56px; border-radius: 50%; background: #fff; padding: 2px; }
```

- selector `.brand img` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `height`: ความสูง = `56px`
- `width`: ความกว้าง = `56px`
- `border-radius`: ความโค้งมุม = `50%`
- `background`: พื้นหลัง/gradient = `#fff`
- `padding`: ระยะภายใน = `2px`
- } จบ block ของกฎ/เงื่อนไข `.brand img`

### L28

```css
.brand-text { display: flex; flex-direction: column; }
```

- selector `.brand-text` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.brand-text`

### L29

```css
.brand-line1 { font-weight: 700; font-size: 17px; letter-spacing: .2px; }
```

- selector `.brand-line1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-weight`: น้ำหนักอักษร = `700`
- `font-size`: ขนาดอักษร = `17px`
- `letter-spacing`: ช่องห่างอักขระ = `.2px`
- } จบ block ของกฎ/เงื่อนไข `.brand-line1`

### L30

```css
.brand-line2 { font-size: 12.5px; opacity: .85; }
```

- selector `.brand-line2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `12.5px`
- `opacity`: ความทึบ = `.85`
- } จบ block ของกฎ/เงื่อนไข `.brand-line2`

### L31

```css
.group-badge { font-size: 13px; background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.3); padding: 4px 12px; border-radius: 999px; white-space: nowrap; }
```

- selector `.group-badge` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `13px`
- `background`: พื้นหลัง/gradient = `rgba(255,255,255,.14)`
- `border`: เส้นขอบแบบย่อ = `1px solid rgba(255,255,255,.3)`
- `padding`: ระยะภายใน = `4px 12px`
- `border-radius`: ความโค้งมุม = `999px`
- `white-space`: การรักษา/ตัดช่องว่างและบรรทัด = `nowrap`
- } จบ block ของกฎ/เงื่อนไข `.group-badge`

### L32

```css
.site-nav { display: flex; gap: 4px; flex-wrap: wrap; padding: 0 20px 0; border-top: 1px solid rgba(255,255,255,.15); }
```

- selector `.site-nav` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `gap`: ช่องว่างระหว่าง item = `4px`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `padding`: ระยะภายใน = `0 20px 0`
- `border-top`: เส้นขอบบน = `1px solid rgba(255,255,255,.15)`
- } จบ block ของกฎ/เงื่อนไข `.site-nav`

### L33

```css
.site-nav a { color: #fff; text-decoration: none; padding: 10px 14px; font-size: 14px; border-bottom: 3px solid transparent; opacity: .85; }
```

- selector `.site-nav a` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#fff`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `none`
- `padding`: ระยะภายใน = `10px 14px`
- `font-size`: ขนาดอักษร = `14px`
- `border-bottom`: เส้นขอบล่าง = `3px solid transparent`
- `opacity`: ความทึบ = `.85`
- } จบ block ของกฎ/เงื่อนไข `.site-nav a`

### L34

```css
.site-nav a:hover { opacity: 1; }
```

- selector `.site-nav a:hover` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `opacity`: ความทึบ = `1`
- } จบ block ของกฎ/เงื่อนไข `.site-nav a:hover`

### L35

```css
.site-nav a.active { border-bottom-color: var(--gold); opacity: 1; font-weight: 600; }
```

- selector `.site-nav a.active` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border-bottom-color`: สีขอบล่าง = `var(--gold)`
- `opacity`: ความทึบ = `1`
- `font-weight`: น้ำหนักอักษร = `600`
- } จบ block ของกฎ/เงื่อนไข `.site-nav a.active`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L36

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L37

```css
/* ---------- main ---------- */
```

- comment บอกส่วนของ stylesheet: /* ---------- main ---------- */

### L38

```css
main { flex: 1; padding: 28px 20px 48px; }
```

- selector `main` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `padding`: ระยะภายใน = `28px 20px 48px`
- } จบ block ของกฎ/เงื่อนไข `main`

### L39

```css
h1 { font-size: 26px; margin: 0 0 8px; }
```

- selector `h1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `26px`
- `margin`: ระยะภายนอก = `0 0 8px`
- } จบ block ของกฎ/เงื่อนไข `h1`

### L40

```css
h2 { font-size: 19px; margin: 28px 0 10px; }
```

- selector `h2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `19px`
- `margin`: ระยะภายนอก = `28px 0 10px`
- } จบ block ของกฎ/เงื่อนไข `h2`

### L41

```css
.lead { color: var(--muted); margin-top: 0; }
```

- selector `.lead` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `margin-top`: ระยะนอกด้านบน = `0`
- } จบ block ของกฎ/เงื่อนไข `.lead`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L42

```css
.muted { color: var(--muted); font-weight: normal; font-size: 14px; }
```

- selector `.muted` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-weight`: น้ำหนักอักษร = `normal`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.muted`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L43

```css
small.muted { font-size: 15px; }
```

- selector `small.muted` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `15px`
- } จบ block ของกฎ/เงื่อนไข `small.muted`

### L44

```css
.banner { background: #fff8e1; border: 1px solid #f6d46a; color: #6b4d00; padding: 10px 14px; border-radius: 8px; margin-bottom: 18px; }
```

- selector `.banner` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fff8e1`
- `border`: เส้นขอบแบบย่อ = `1px solid #f6d46a`
- `color`: สีตัวอักษร = `#6b4d00`
- `padding`: ระยะภายใน = `10px 14px`
- `border-radius`: ความโค้งมุม = `8px`
- `margin-bottom`: ระยะนอกด้านล่าง = `18px`
- } จบ block ของกฎ/เงื่อนไข `.banner`

### L45

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L46

```css
table { width: 100%; border-collapse: collapse; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
```

- selector `table` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `border-collapse`: การรวมเส้นขอบตาราง = `collapse`
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `10px`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `table`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L47

```css
th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); font-size: 14.5px; }
```

- selector `th, td` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `text-align`: แนวข้อความ = `left`
- `padding`: ระยะภายใน = `10px 12px`
- `border-bottom`: เส้นขอบล่าง = `1px solid var(--line)`
- `font-size`: ขนาดอักษร = `14.5px`
- } จบ block ของกฎ/เงื่อนไข `th, td`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L48

```css
th { background: #f1ede8; color: var(--muted); font-weight: 600; font-size: 13px; }
```

- selector `th` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#f1ede8`
- `color`: สีตัวอักษร = `var(--muted)`
- `font-weight`: น้ำหนักอักษร = `600`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `th`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L49

```css
tr:last-child td { border-bottom: none; }
```

- selector `tr:last-child td` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `tr`: property CSS ของกฎที่เลือก = `last-child td`
- `border-bottom`: เส้นขอบล่าง = `none`
- } จบ block ของกฎ/เงื่อนไข `tr:last-child td`

### L50

```css
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
```

- selector `td.num, th.num` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `text-align`: แนวข้อความ = `right`
- `font-variant-numeric`: รูปแบบตัวเลข เช่นกว้างเท่ากัน = `tabular-nums`
- } จบ block ของกฎ/เงื่อนไข `td.num, th.num`

### L51

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L52

```css
.btn { display: inline-block; padding: 8px 16px; border-radius: 8px; border: 1px solid var(--maroon); background: var(--maroon); color: #fff; font-size: 14px; text-decoration: none; cursor: pointer; }
```

- selector `.btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `inline-block`
- `padding`: ระยะภายใน = `8px 16px`
- `border-radius`: ความโค้งมุม = `8px`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--maroon)`
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `color`: สีตัวอักษร = `#fff`
- `font-size`: ขนาดอักษร = `14px`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `none`
- `cursor`: รูปตัวชี้ = `pointer`
- } จบ block ของกฎ/เงื่อนไข `.btn`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L53

```css
.btn.ghost { background: #fff; color: var(--maroon); }
```

- selector `.btn.ghost` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fff`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.btn.ghost`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L54

```css
.field { margin-bottom: 14px; }
```

- selector `.field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-bottom`: ระยะนอกด้านล่าง = `14px`
- } จบ block ของกฎ/เงื่อนไข `.field`

### L55

```css
.field label { display: block; font-size: 13px; color: var(--muted); margin-bottom: 4px; }
```

- selector `.field label` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `font-size`: ขนาดอักษร = `13px`
- `color`: สีตัวอักษร = `var(--muted)`
- `margin-bottom`: ระยะนอกด้านล่าง = `4px`
- } จบ block ของกฎ/เงื่อนไข `.field label`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L56

```css
.field input, .field select, .field textarea { width: 100%; max-width: 380px; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; font-family: inherit; }
```

- selector `.field input, .field select, .field textarea` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `max-width`: ความกว้างสูงสุด = `380px`
- `padding`: ระยะภายใน = `8px 10px`
- `border`: เส้นขอบแบบย่อ = `1px solid #cbd5e1`
- `border-radius`: ความโค้งมุม = `8px`
- `font-size`: ขนาดอักษร = `14px`
- `font-family`: ชุดฟอนต์ตามลำดับ = `inherit`
- } จบ block ของกฎ/เงื่อนไข `.field input, .field select, .field textarea`

### L57

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L58

```css
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }
```

- selector `.stat-grid` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(180px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `12px`
- } จบ block ของกฎ/เงื่อนไข `.stat-grid`

### L59

```css
.stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; }
```

- selector `.stat` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `10px`
- `padding`: ระยะภายใน = `14px 16px`
- } จบ block ของกฎ/เงื่อนไข `.stat`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L60

```css
.stat .label { color: var(--muted); font-size: 13px; }
```

- selector `.stat .label` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `.stat .label`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L61

```css
.stat .value { font-size: 26px; font-weight: 700; color: var(--maroon); }
```

- selector `.stat .value` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `26px`
- `font-weight`: น้ำหนักอักษร = `700`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.stat .value`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L62

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L63

```css
.empty { color: var(--muted); padding: 32px; text-align: center; background: var(--card); border: 1px dashed var(--line); border-radius: 10px; }
```

- selector `.empty` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `padding`: ระยะภายใน = `32px`
- `text-align`: แนวข้อความ = `center`
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px dashed var(--line)`
- `border-radius`: ความโค้งมุม = `10px`
- } จบ block ของกฎ/เงื่อนไข `.empty`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L64

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L65

```css
/* home */
```

- comment บอกส่วนของ stylesheet: /* home */

### L66

```css
.hero { padding: 8px 0 20px; }
```

- selector `.hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `8px 0 20px`
- } จบ block ของกฎ/เงื่อนไข `.hero`

### L67

```css
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
```

- selector `.cards` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(200px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `14px`
- } จบ block ของกฎ/เงื่อนไข `.cards`

### L68

```css
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-decoration: none; color: var(--ink); display: flex; flex-direction: column; gap: 4px; transition: transform .1s, box-shadow .1s; }
```

- selector `.card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `padding`: ระยะภายใน = `18px`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `none`
- `color`: สีตัวอักษร = `var(--ink)`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `4px`
- `transition`: การเปลี่ยนลักษณะระหว่างสถานะ = `transform .1s, box-shadow .1s`
- } จบ block ของกฎ/เงื่อนไข `.card`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L69

```css
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.07); }
```

- selector `.card:hover` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `transform`: แปลงตำแหน่ง/หมุน = `translateY(-2px)`
- `box-shadow`: เงา = `0 6px 18px rgba(0,0,0,.07)`
- } จบ block ของกฎ/เงื่อนไข `.card:hover`

### L70

```css
.card-kicker { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; }
```

- selector `.card-kicker` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `12px`
- `color`: สีตัวอักษร = `var(--muted)`
- `text-transform`: รูปแบบตัวพิมพ์ = `uppercase`
- `letter-spacing`: ช่องห่างอักขระ = `.5px`
- } จบ block ของกฎ/เงื่อนไข `.card-kicker`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L71

```css
.card-title { font-size: 17px; font-weight: 600; color: var(--maroon); }
```

- selector `.card-title` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `17px`
- `font-weight`: น้ำหนักอักษร = `600`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.card-title`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L72

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L73

```css
/* team */
```

- comment บอกส่วนของ stylesheet: /* team */

### L74

```css
.member-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 8px; }
```

- selector `.member-grid` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(200px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `14px`
- `margin-bottom`: ระยะนอกด้านล่าง = `8px`
- } จบ block ของกฎ/เงื่อนไข `.member-grid`

### L75

```css
.member { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-align: center; }
```

- selector `.member` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `padding`: ระยะภายใน = `18px`
- `text-align`: แนวข้อความ = `center`
- } จบ block ของกฎ/เงื่อนไข `.member`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L76

```css
.avatar { width: 56px; height: 56px; border-radius: 50%; background: var(--maroon); color: #fff; font-size: 24px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; }
```

- selector `.avatar` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `56px`
- `height`: ความสูง = `56px`
- `border-radius`: ความโค้งมุม = `50%`
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `color`: สีตัวอักษร = `#fff`
- `font-size`: ขนาดอักษร = `24px`
- `font-weight`: น้ำหนักอักษร = `700`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `center`
- `margin`: ระยะภายนอก = `0 auto 10px`
- } จบ block ของกฎ/เงื่อนไข `.avatar`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L77

```css
.member-name { font-weight: 600; }
```

- selector `.member-name` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-weight`: น้ำหนักอักษร = `600`
- } จบ block ของกฎ/เงื่อนไข `.member-name`

### L78

```css
.role { color: var(--maroon); font-size: 13px; margin-top: 4px; }
```

- selector `.role` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `13px`
- `margin-top`: ระยะนอกด้านบน = `4px`
- } จบ block ของกฎ/เงื่อนไข `.role`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L79

```css
.task { color: var(--muted); font-size: 13px; }
```

- selector `.task` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `.task`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L80

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L81

```css
/* gallery */
```

- comment บอกส่วนของ stylesheet: /* gallery */

### L82

```css
.gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 14px; }
```

- selector `.gallery` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fill, minmax(180px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `14px`
- } จบ block ของกฎ/เงื่อนไข `.gallery`

### L83

```css
.gallery figure { margin: 0; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
```

- selector `.gallery figure` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `10px`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `.gallery figure`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L84

```css
.gallery img { width: 100%; height: 140px; object-fit: cover; display: block; }
```

- selector `.gallery img` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `height`: ความสูง = `140px`
- `object-fit`: วิธีวางภาพในกรอบ = `cover`
- `display`: วิธีจัดวาง/การแสดง = `block`
- } จบ block ของกฎ/เงื่อนไข `.gallery img`

### L85

```css
.gallery figcaption { padding: 8px 10px; font-size: 13.5px; }
```

- selector `.gallery figcaption` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `8px 10px`
- `font-size`: ขนาดอักษร = `13.5px`
- } จบ block ของกฎ/เงื่อนไข `.gallery figcaption`

### L86

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L87

```css
/* not built */
```

- comment บอกส่วนของ stylesheet: /* not built */

### L88

```css
.notbuilt { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 28px; }
```

- selector `.notbuilt` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `padding`: ระยะภายใน = `28px`
- } จบ block ของกฎ/เงื่อนไข `.notbuilt`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L89

```css
.notbuilt .reason { font-size: 16px; }
```

- selector `.notbuilt .reason` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `16px`
- } จบ block ของกฎ/เงื่อนไข `.notbuilt .reason`

### L90

```css
.notbuilt pre { background: #1f2933; color: #f8fafc; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 12.5px; }
```

- selector `.notbuilt pre` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#1f2933`
- `color`: สีตัวอักษร = `#f8fafc`
- `padding`: ระยะภายใน = `12px`
- `border-radius`: ความโค้งมุม = `8px`
- `overflow-x`: การจัดการส่วนล้นแนวนอน = `auto`
- `font-size`: ขนาดอักษร = `12.5px`
- } จบ block ของกฎ/เงื่อนไข `.notbuilt pre`

### L91

```css
.notbuilt code { background: #f1ede8; padding: 1px 6px; border-radius: 4px; }
```

- selector `.notbuilt code` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#f1ede8`
- `padding`: ระยะภายใน = `1px 6px`
- `border-radius`: ความโค้งมุม = `4px`
- } จบ block ของกฎ/เงื่อนไข `.notbuilt code`

### L92

```css
.hint { color: var(--muted); font-size: 14px; }
```

- selector `.hint` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.hint`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L93

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L94

```css
/* footer */
```

- comment บอกส่วนของ stylesheet: /* footer */

### L95

```css
.site-footer { border-top: 1px solid var(--line); color: var(--muted); font-size: 13px; padding: 12px 0; background: #fff; }
```

- selector `.site-footer` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border-top`: เส้นขอบบน = `1px solid var(--line)`
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `13px`
- `padding`: ระยะภายใน = `12px 0`
- `background`: พื้นหลัง/gradient = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.site-footer`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L96

```css
.site-footer .wrap { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
```

- selector `.site-footer .wrap` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `gap`: ช่องว่างระหว่าง item = `8px`
- } จบ block ของกฎ/เงื่อนไข `.site-footer .wrap`

### L97

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L98

```css
@media (max-width: 640px) {
```

- เงื่อนไขขนาดจอ: `@media (max-width: 640px)` กฎภายในใช้เมื่อเข้าเงื่อนไข

### L99

```css
  .brand-line1 { font-size: 14px; }
```

- selector `.brand-line1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.brand-line1`

### L100

```css
  .brand-line2 { display: none; }
```

- selector `.brand-line2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `none`
- } จบ block ของกฎ/เงื่อนไข `.brand-line2`

### L101

```css
  .group-badge { display: none; }
```

- selector `.group-badge` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `none`
- } จบ block ของกฎ/เงื่อนไข `.group-badge`

### L102

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 640px)`

### L103

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L104

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L105

```css
/* ---------- components you can use on any page ---------- */
```

- comment บอกส่วนของ stylesheet: /* ---------- components you can use on any page ---------- */

### L106

```css
/* panel / card */
```

- comment บอกส่วนของ stylesheet: /* panel / card */

### L107

```css
.panel { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; }
```

- selector `.panel` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `padding`: ระยะภายใน = `18px`
- } จบ block ของกฎ/เงื่อนไข `.panel`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L108

```css
.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: 18px; align-items: start; }
```

- selector `.two-col` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `2fr 1fr`
- `gap`: ช่องว่างระหว่าง item = `18px`
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- } จบ block ของกฎ/เงื่อนไข `.two-col`

### L109

```css
@media (max-width: 720px) { .two-col { grid-template-columns: 1fr; } }
```

- เงื่อนไขขนาดจอ: `@media (max-width: 720px)` กฎภายในใช้เมื่อเข้าเงื่อนไข
- selector `.two-col` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `1fr`
- } จบ block ของกฎ/เงื่อนไข `.two-col`
- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 720px)`

### L110

```css
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
```

- selector `.card-grid` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fill, minmax(200px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `14px`
- } จบ block ของกฎ/เงื่อนไข `.card-grid`

### L111

```css
.item-card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; }
```

- selector `.item-card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `overflow`: การจัดการส่วนล้น = `hidden`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.item-card`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L112

```css
.item-card img { width: 100%; height: 140px; object-fit: cover; background: #f1ede8; }
```

- selector `.item-card img` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `height`: ความสูง = `140px`
- `object-fit`: วิธีวางภาพในกรอบ = `cover`
- `background`: พื้นหลัง/gradient = `#f1ede8`
- } จบ block ของกฎ/เงื่อนไข `.item-card img`

### L113

```css
.item-card .body { padding: 12px 14px; display: flex; flex-direction: column; gap: 4px; flex: 1; }
```

- selector `.item-card .body` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `12px 14px`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `4px`
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- } จบ block ของกฎ/เงื่อนไข `.item-card .body`

### L114

```css
.item-card .price { font-weight: 700; color: var(--maroon); font-size: 18px; margin-top: auto; }
```

- selector `.item-card .price` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-weight`: น้ำหนักอักษร = `700`
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `18px`
- `margin-top`: ระยะนอกด้านบน = `auto`
- } จบ block ของกฎ/เงื่อนไข `.item-card .price`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L115

```css
/* badges & pills */
```

- comment บอกส่วนของ stylesheet: /* badges & pills */

### L116

```css
.badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 12px; font-weight: 600; background: #f1ede8; color: var(--muted); }
```

- selector `.badge` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `inline-block`
- `padding`: ระยะภายใน = `2px 9px`
- `border-radius`: ความโค้งมุม = `999px`
- `font-size`: ขนาดอักษร = `12px`
- `font-weight`: น้ำหนักอักษร = `600`
- `background`: พื้นหลัง/gradient = `#f1ede8`
- `color`: สีตัวอักษร = `var(--muted)`
- } จบ block ของกฎ/เงื่อนไข `.badge`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L117

```css
.badge.good { background: #e6f5ec; color: #1b6b3a; }
```

- selector `.badge.good` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#e6f5ec`
- `color`: สีตัวอักษร = `#1b6b3a`
- } จบ block ของกฎ/เงื่อนไข `.badge.good`

### L118

```css
.badge.bad { background: #fdecec; color: #9b1c1c; }
```

- selector `.badge.bad` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fdecec`
- `color`: สีตัวอักษร = `#9b1c1c`
- } จบ block ของกฎ/เงื่อนไข `.badge.bad`

### L119

```css
.badge.gold { background: #fff5d6; color: #8a6100; }
```

- selector `.badge.gold` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fff5d6`
- `color`: สีตัวอักษร = `#8a6100`
- } จบ block ของกฎ/เงื่อนไข `.badge.gold`

### L120

```css
.pills { display: flex; gap: 6px; flex-wrap: wrap; margin: 10px 0; }
```

- selector `.pills` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `gap`: ช่องว่างระหว่าง item = `6px`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `margin`: ระยะภายนอก = `10px 0`
- } จบ block ของกฎ/เงื่อนไข `.pills`

### L121

```css
.pills a { padding: 5px 12px; border-radius: 999px; border: 1px solid var(--line); background: #fff; color: var(--ink); text-decoration: none; font-size: 13px; }
```

- selector `.pills a` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `5px 12px`
- `border-radius`: ความโค้งมุม = `999px`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `background`: พื้นหลัง/gradient = `#fff`
- `color`: สีตัวอักษร = `var(--ink)`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `none`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `.pills a`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L122

```css
.pills a.active { background: var(--maroon); border-color: var(--maroon); color: #fff; }
```

- selector `.pills a.active` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `border-color`: สีเส้นขอบ = `var(--maroon)`
- `color`: สีตัวอักษร = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.pills a.active`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L123

```css
/* stat card variants */
```

- comment บอกส่วนของ stylesheet: /* stat card variants */

### L124

```css
.stat.good .value { color: #1b6b3a; }
```

- selector `.stat.good .value` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#1b6b3a`
- } จบ block ของกฎ/เงื่อนไข `.stat.good .value`

### L125

```css
.stat.bad .value { color: #9b1c1c; }
```

- selector `.stat.bad .value` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#9b1c1c`
- } จบ block ของกฎ/เงื่อนไข `.stat.bad .value`

### L126

```css
.stat.gold { background: #fffbe8; border-color: #f2df9a; }
```

- selector `.stat.gold` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fffbe8`
- `border-color`: สีเส้นขอบ = `#f2df9a`
- } จบ block ของกฎ/เงื่อนไข `.stat.gold`

### L127

```css
.stat .unit { color: var(--muted); font-size: 12px; }
```

- selector `.stat .unit` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `12px`
- } จบ block ของกฎ/เงื่อนไข `.stat .unit`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L128

```css
/* horizontal bars: width = percent of the biggest value (compute the % in Python) */
```

- comment บอกส่วนของ stylesheet: /* horizontal bars: width = percent of the biggest value (compute the % in Python) */

### L129

```css
.bar-row { display: grid; grid-template-columns: 120px 1fr 90px; align-items: center; gap: 10px; padding: 6px 0; }
```

- selector `.bar-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `120px 1fr 90px`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `gap`: ช่องว่างระหว่าง item = `10px`
- `padding`: ระยะภายใน = `6px 0`
- } จบ block ของกฎ/เงื่อนไข `.bar-row`

### L130

```css
.bar-track { background: #efeae4; border-radius: 6px; height: 14px; overflow: hidden; }
```

- selector `.bar-track` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#efeae4`
- `border-radius`: ความโค้งมุม = `6px`
- `height`: ความสูง = `14px`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `.bar-track`

### L131

```css
.bar-fill { background: var(--maroon); height: 100%; border-radius: 6px; }
```

- selector `.bar-fill` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `height`: ความสูง = `100%`
- `border-radius`: ความโค้งมุม = `6px`
- } จบ block ของกฎ/เงื่อนไข `.bar-fill`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L132

```css
.bar-fill.gold { background: var(--gold); }
```

- selector `.bar-fill.gold` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--gold)`
- } จบ block ของกฎ/เงื่อนไข `.bar-fill.gold`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L133

```css
.bar-fill.green { background: #2e8b57; }
```

- selector `.bar-fill.green` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#2e8b57`
- } จบ block ของกฎ/เงื่อนไข `.bar-fill.green`

### L134

```css
.bar-row .num { text-align: right; font-variant-numeric: tabular-nums; }
```

- selector `.bar-row .num` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `text-align`: แนวข้อความ = `right`
- `font-variant-numeric`: รูปแบบตัวเลข เช่นกว้างเท่ากัน = `tabular-nums`
- } จบ block ของกฎ/เงื่อนไข `.bar-row .num`

### L135

```css
/* progress bar */
```

- comment บอกส่วนของ stylesheet: /* progress bar */

### L136

```css
.progress { background: #efeae4; border-radius: 999px; height: 12px; overflow: hidden; }
```

- selector `.progress` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#efeae4`
- `border-radius`: ความโค้งมุม = `999px`
- `height`: ความสูง = `12px`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `.progress`

### L137

```css
.progress > div { background: var(--gold); height: 100%; border-radius: 999px; }
```

- selector `.progress > div` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--gold)`
- `height`: ความสูง = `100%`
- `border-radius`: ความโค้งมุม = `999px`
- } จบ block ของกฎ/เงื่อนไข `.progress > div`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L138

```css
/* vertical columns chart: height = percent (compute the % in Python) */
```

- comment บอกส่วนของ stylesheet: /* vertical columns chart: height = percent (compute the % in Python) */

### L139

```css
.chart { display: flex; align-items: flex-end; gap: 8px; height: 180px; padding: 8px 0; border-bottom: 1px solid var(--line); }
```

- selector `.chart` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `flex-end`
- `gap`: ช่องว่างระหว่าง item = `8px`
- `height`: ความสูง = `180px`
- `padding`: ระยะภายใน = `8px 0`
- `border-bottom`: เส้นขอบล่าง = `1px solid var(--line)`
- } จบ block ของกฎ/เงื่อนไข `.chart`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L140

```css
.chart .col { flex: 1; display: flex; flex-direction: column; justify-content: flex-end; height: 100%; }
```

- selector `.chart .col` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `flex-end`
- `height`: ความสูง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.chart .col`

### L141

```css
.chart .col > div { background: var(--maroon); border-radius: 4px 4px 0 0; }
```

- selector `.chart .col > div` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `border-radius`: ความโค้งมุม = `4px 4px 0 0`
- } จบ block ของกฎ/เงื่อนไข `.chart .col > div`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L142

```css
.chart .col > div.gold { background: var(--gold); }
```

- selector `.chart .col > div.gold` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--gold)`
- } จบ block ของกฎ/เงื่อนไข `.chart .col > div.gold`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L143

```css
.chart-labels { display: flex; gap: 8px; }
```

- selector `.chart-labels` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `gap`: ช่องว่างระหว่าง item = `8px`
- } จบ block ของกฎ/เงื่อนไข `.chart-labels`

### L144

```css
.chart-labels span { flex: 1; text-align: center; font-size: 12px; color: var(--muted); }
```

- selector `.chart-labels span` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `text-align`: แนวข้อความ = `center`
- `font-size`: ขนาดอักษร = `12px`
- `color`: สีตัวอักษร = `var(--muted)`
- } จบ block ของกฎ/เงื่อนไข `.chart-labels span`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L145

```css
/* buttons */
```

- comment บอกส่วนของ stylesheet: /* buttons */

### L146

```css
.btn.small { padding: 4px 10px; font-size: 13px; }
```

- selector `.btn.small` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `4px 10px`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `.btn.small`

### L147

```css
.btn.full { display: block; width: 100%; text-align: center; }
```

- selector `.btn.full` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `width`: ความกว้าง = `100%`
- `text-align`: แนวข้อความ = `center`
- } จบ block ของกฎ/เงื่อนไข `.btn.full`

### L148

```css
.btn.danger { background: #fff; color: #9b1c1c; border-color: #f3b4b4; }
```

- selector `.btn.danger` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fff`
- `color`: สีตัวอักษร = `#9b1c1c`
- `border-color`: สีเส้นขอบ = `#f3b4b4`
- } จบ block ของกฎ/เงื่อนไข `.btn.danger`

### L149

```css
form.inline { display: inline; }
```

- selector `form.inline` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `inline`
- } จบ block ของกฎ/เงื่อนไข `form.inline`

### L150

```css
/* misc */
```

- comment บอกส่วนของ stylesheet: /* misc */

### L151

```css
.kbd { display: inline-block; padding: 2px 8px; border: 1px solid #cbd5e1; border-bottom-width: 3px; border-radius: 6px; background: #fff; font-family: monospace; font-size: 12px; }
```

- selector `.kbd` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `inline-block`
- `padding`: ระยะภายใน = `2px 8px`
- `border`: เส้นขอบแบบย่อ = `1px solid #cbd5e1`
- `border-bottom-width`: ความหนาขอบล่าง = `3px`
- `border-radius`: ความโค้งมุม = `6px`
- `background`: พื้นหลัง/gradient = `#fff`
- `font-family`: ชุดฟอนต์ตามลำดับ = `monospace`
- `font-size`: ขนาดอักษร = `12px`
- } จบ block ของกฎ/เงื่อนไข `.kbd`

### L152

```css
.hero-box { background: linear-gradient(135deg, #fff, #f7efe9); border: 1px solid var(--line); border-radius: 14px; padding: 24px; margin-bottom: 18px; }
```

- selector `.hero-box` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `linear-gradient(135deg, #fff, #f7efe9)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `14px`
- `padding`: ระยะภายใน = `24px`
- `margin-bottom`: ระยะนอกด้านล่าง = `18px`
- } จบ block ของกฎ/เงื่อนไข `.hero-box`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L153

```css
.note { font-size: 13px; color: var(--muted); }
```

- selector `.note` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `13px`
- `color`: สีตัวอักษร = `var(--muted)`
- } จบ block ของกฎ/เงื่อนไข `.note`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L154

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L155

```css
/* stacked columns: put several <div class="seg"> inside a .col, heights in % of the column */
```

- comment บอกส่วนของ stylesheet: /* stacked columns: put several <div class="seg"> inside a .col, heights in % of the column */

### L156

```css
.chart .col .seg { width: 100%; }
```

- selector `.chart .col .seg` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.chart .col .seg`

### L157

```css
.chart .col .seg.gold { background: var(--gold); }
```

- selector `.chart .col .seg.gold` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `var(--gold)`
- } จบ block ของกฎ/เงื่อนไข `.chart .col .seg.gold`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L158

```css
.chart .col .seg.green { background: #2e8b57; }
```

- selector `.chart .col .seg.green` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#2e8b57`
- } จบ block ของกฎ/เงื่อนไข `.chart .col .seg.green`

### L159

```css
/* donut: style="--p: 42" (percent) */
```

- comment บอกส่วนของ stylesheet: /* donut: style="--p: 42" (percent) */

### L160

```css
.donut { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0); display: flex; align-items: center; justify-content: center; }
```

- selector `.donut` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `120px`
- `height`: ความสูง = `120px`
- `border-radius`: ความโค้งมุม = `50%`
- `background`: พื้นหลัง/gradient = `conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0)`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `center`
- } จบ block ของกฎ/เงื่อนไข `.donut`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L161

```css
.donut > span { width: 78px; height: 78px; border-radius: 50%; background: var(--card); display: flex; align-items: center; justify-content: center; font-weight: 700; color: var(--maroon); }
```

- selector `.donut > span` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `78px`
- `height`: ความสูง = `78px`
- `border-radius`: ความโค้งมุม = `50%`
- `background`: พื้นหลัง/gradient = `var(--card)`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `center`
- `font-weight`: น้ำหนักอักษร = `700`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.donut > span`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L162

```css
/* small things forms and summaries keep needing */
```

- comment บอกส่วนของ stylesheet: /* small things forms and summaries keep needing */

### L163

```css
.thumb { width: 56px; height: 56px; object-fit: cover; border-radius: 8px; background: #f1ede8; }
```

- selector `.thumb` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `56px`
- `height`: ความสูง = `56px`
- `object-fit`: วิธีวางภาพในกรอบ = `cover`
- `border-radius`: ความโค้งมุม = `8px`
- `background`: พื้นหลัง/gradient = `#f1ede8`
- } จบ block ของกฎ/เงื่อนไข `.thumb`

### L164

```css
.field-row { display: flex; gap: 14px; flex-wrap: wrap; align-items: flex-end; }
```

- selector `.field-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `gap`: ช่องว่างระหว่าง item = `14px`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `align-items`: แนวจัดวางบนแกนขวาง = `flex-end`
- } จบ block ของกฎ/เงื่อนไข `.field-row`

### L165

```css
.field-row .field { margin: 0; }
```

- selector `.field-row .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.field-row .field`

### L166

```css
.sum-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--line); }
```

- selector `.sum-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `padding`: ระยะภายใน = `6px 0`
- `border-bottom`: เส้นขอบล่าง = `1px solid var(--line)`
- } จบ block ของกฎ/เงื่อนไข `.sum-row`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L167

```css
.sum-row.total { border: 0; font-size: 18px; font-weight: 700; color: var(--maroon); }
```

- selector `.sum-row.total` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border`: เส้นขอบแบบย่อ = `0`
- `font-size`: ขนาดอักษร = `18px`
- `font-weight`: น้ำหนักอักษร = `700`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.sum-row.total`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L168

```css
.game-board { display: block; margin: 0 auto; background: #1f2933; border: 4px solid var(--maroon); border-radius: 10px; }
```

- selector `.game-board` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `margin`: ระยะภายนอก = `0 auto`
- `background`: พื้นหลัง/gradient = `#1f2933`
- `border`: เส้นขอบแบบย่อ = `4px solid var(--maroon)`
- `border-radius`: ความโค้งมุม = `10px`
- } จบ block ของกฎ/เงื่อนไข `.game-board`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L169

```css
.hud { display: flex; gap: 10px; justify-content: center; margin: 10px 0; }
```

- selector `.hud` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `gap`: ช่องว่างระหว่าง item = `10px`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `center`
- `margin`: ระยะภายนอก = `10px 0`
- } จบ block ของกฎ/เงื่อนไข `.hud`

### L170

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L171

```css
/* ---------- your own styles below ---------- */
```

- comment บอกส่วนของ stylesheet: /* ---------- your own styles below ---------- */

### L172

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L173

```css
/* Deadline Compass: page styles added without changing the given components. */
```

- comment บอกส่วนของ stylesheet: /* Deadline Compass: page styles added without changing the given components. */

### L174

```css
.deadline-eyebrow { display: inline-block; color: var(--maroon); font-size: 12px; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; }
```

- selector `.deadline-eyebrow` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `inline-block`
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `12px`
- `font-weight`: น้ำหนักอักษร = `800`
- `letter-spacing`: ช่องห่างอักขระ = `.13em`
- `text-transform`: รูปแบบตัวพิมพ์ = `uppercase`
- } จบ block ของกฎ/เงื่อนไข `.deadline-eyebrow`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L175

```css
.deadline-hero { display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 32px; margin-bottom: 20px; border: 1px solid #ead8cf; border-radius: 18px; background: linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%); overflow: hidden; }
```

- selector `.deadline-hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `gap`: ช่องว่างระหว่าง item = `24px`
- `padding`: ระยะภายใน = `32px`
- `margin-bottom`: ระยะนอกด้านล่าง = `20px`
- `border`: เส้นขอบแบบย่อ = `1px solid #ead8cf`
- `border-radius`: ความโค้งมุม = `18px`
- `background`: พื้นหลัง/gradient = `linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%)`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero`

### L176

```css
.deadline-hero h1 { font-size: clamp(27px, 4vw, 40px); line-height: 1.2; margin: 8px 0 10px; color: var(--maroon-dark); }
```

- selector `.deadline-hero h1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `clamp(27px, 4vw, 40px)`
- `line-height`: ระยะบรรทัด = `1.2`
- `margin`: ระยะภายนอก = `8px 0 10px`
- `color`: สีตัวอักษร = `var(--maroon-dark)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero h1`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L177

```css
.deadline-hero p { max-width: 480px; margin: 0 0 20px; color: #5d5552; }
```

- selector `.deadline-hero p` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `480px`
- `margin`: ระยะภายนอก = `0 0 20px`
- `color`: สีตัวอักษร = `#5d5552`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero p`

### L178

```css
.deadline-hero .btn { margin: 0 7px 7px 0; }
```

- selector `.deadline-hero .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0 7px 7px 0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero .btn`

### L179

```css
.deadline-hero-mark { flex: 0 0 170px; width: 170px; height: 170px; transform: rotate(9deg); border: 9px solid var(--maroon); border-radius: 22px; background: #fff; box-shadow: 16px 16px 0 rgba(122,31,43,.11); text-align: center; overflow: hidden; }
```

- selector `.deadline-hero-mark` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `0 0 170px`
- `width`: ความกว้าง = `170px`
- `height`: ความสูง = `170px`
- `transform`: แปลงตำแหน่ง/หมุน = `rotate(9deg)`
- `border`: เส้นขอบแบบย่อ = `9px solid var(--maroon)`
- `border-radius`: ความโค้งมุม = `22px`
- `background`: พื้นหลัง/gradient = `#fff`
- `box-shadow`: เงา = `16px 16px 0 rgba(122,31,43,.11)`
- `text-align`: แนวข้อความ = `center`
- `overflow`: การจัดการส่วนล้น = `hidden`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero-mark`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L180

```css
.deadline-hero-mark span:first-child { display: block; height: 40px; background: var(--maroon); color: white; font-size: 26px; line-height: 32px; }
```

- selector `.deadline-hero-mark span:first-child` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `height`: ความสูง = `40px`
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `color`: สีตัวอักษร = `white`
- `font-size`: ขนาดอักษร = `26px`
- `line-height`: ระยะบรรทัด = `32px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero-mark span:first-child`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L181

```css
.deadline-hero-mark span:last-child { display: block; color: var(--maroon); font-size: 76px; font-weight: 800; line-height: 115px; }
```

- selector `.deadline-hero-mark span:last-child` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `76px`
- `font-weight`: น้ำหนักอักษร = `800`
- `line-height`: ระยะบรรทัด = `115px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero-mark span:last-child`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L182

```css
.deadline-summary { margin: 16px 0 24px; }
```

- selector `.deadline-summary` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `16px 0 24px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-summary`

### L183

```css
.deadline-summary .stat { box-shadow: 0 5px 18px rgba(31,41,51,.035); }
```

- selector `.deadline-summary .stat` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `box-shadow`: เงา = `0 5px 18px rgba(31,41,51,.035)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-summary .stat`

### L184

```css
.deadline-summary .value { font-variant-numeric: tabular-nums; }
```

- selector `.deadline-summary .value` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-variant-numeric`: รูปแบบตัวเลข เช่นกว้างเท่ากัน = `tabular-nums`
- } จบ block ของกฎ/เงื่อนไข `.deadline-summary .value`

### L185

```css
.deadline-alert { background: #fdecec; border: 1px solid #eab4b4; color: #802020; border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; font-weight: 600; }
```

- selector `.deadline-alert` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fdecec`
- `border`: เส้นขอบแบบย่อ = `1px solid #eab4b4`
- `color`: สีตัวอักษร = `#802020`
- `border-radius`: ความโค้งมุม = `10px`
- `padding`: ระยะภายใน = `12px 16px`
- `margin-bottom`: ระยะนอกด้านล่าง = `18px`
- `font-weight`: น้ำหนักอักษร = `600`
- } จบ block ของกฎ/เงื่อนไข `.deadline-alert`

### L186

```css
.deadline-section-head { display: flex; align-items: end; justify-content: space-between; gap: 16px; margin: 22px 0 12px; }
```

- selector `.deadline-section-head` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `end`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `gap`: ช่องว่างระหว่าง item = `16px`
- `margin`: ระยะภายนอก = `22px 0 12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-section-head`

### L187

```css
.deadline-section-head h2 { margin: 0 0 2px; }
```

- selector `.deadline-section-head h2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0 0 2px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-section-head h2`

### L188

```css
.deadline-section-head .note { margin: 0; }
```

- selector `.deadline-section-head .note` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-section-head .note`

### L189

```css
.deadline-reminder-control { display: flex; flex-direction: column; align-items: end; gap: 4px; text-align: right; }
```

- selector `.deadline-reminder-control` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `align-items`: แนวจัดวางบนแกนขวาง = `end`
- `gap`: ช่องว่างระหว่าง item = `4px`
- `text-align`: แนวข้อความ = `right`
- } จบ block ของกฎ/เงื่อนไข `.deadline-reminder-control`

### L190

```css
.deadline-task-list { display: grid; gap: 10px; }
```

- selector `.deadline-task-list` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `gap`: ช่องว่างระหว่าง item = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-list`

### L191

```css
.deadline-task { display: flex; align-items: center; justify-content: space-between; gap: 20px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px 18px; box-shadow: 0 3px 12px rgba(31,41,51,.025); }
```

- selector `.deadline-task` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `gap`: ช่องว่างระหว่าง item = `20px`
- `background`: พื้นหลัง/gradient = `var(--card)`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `12px`
- `padding`: ระยะภายใน = `16px 18px`
- `box-shadow`: เงา = `0 3px 12px rgba(31,41,51,.025)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L192

```css
.deadline-task-main { min-width: 0; flex: 1; }
```

- selector `.deadline-task-main` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-width`: ความกว้างต่ำสุด = `0`
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-main`

### L193

```css
.deadline-course { color: var(--maroon); font-size: 12px; font-weight: 700; letter-spacing: .035em; }
```

- selector `.deadline-course` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `12px`
- `font-weight`: น้ำหนักอักษร = `700`
- `letter-spacing`: ช่องห่างอักขระ = `.035em`
- } จบ block ของกฎ/เงื่อนไข `.deadline-course`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L194

```css
.deadline-task h3, .deadline-edit-card h3 { margin: 2px 0 5px; font-size: 17px; line-height: 1.3; }
```

- selector `.deadline-task h3, .deadline-edit-card h3` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `2px 0 5px`
- `font-size`: ขนาดอักษร = `17px`
- `line-height`: ระยะบรรทัด = `1.3`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task h3, .deadline-edit-card h3`

### L195

```css
.deadline-meta { color: var(--muted); font-size: 13px; margin: 0; }
```

- selector `.deadline-meta` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--muted)`
- `font-size`: ขนาดอักษร = `13px`
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-meta`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L196

```css
.deadline-progress { width: min(100%, 360px); margin-top: 12px; height: 8px; }
```

- selector `.deadline-progress` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `min(100%, 360px)`
- `margin-top`: ระยะนอกด้านบน = `12px`
- `height`: ความสูง = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-progress`

### L197

```css
.deadline-task-actions { display: flex; flex-direction: column; align-items: end; gap: 9px; flex-shrink: 0; }
```

- selector `.deadline-task-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `align-items`: แนวจัดวางบนแกนขวาง = `end`
- `gap`: ช่องว่างระหว่าง item = `9px`
- `flex-shrink`: การหดตัว flex item = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions`

### L198

```css
.deadline-text-button { background: transparent; border: 0; padding: 2px 0; color: var(--maroon); text-decoration: underline; font: inherit; font-size: 12px; cursor: pointer; }
```

- selector `.deadline-text-button` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `transparent`
- `border`: เส้นขอบแบบย่อ = `0`
- `padding`: ระยะภายใน = `2px 0`
- `color`: สีตัวอักษร = `var(--maroon)`
- `text-decoration`: รูปแบบเส้นตกแต่งข้อความ = `underline`
- `font`: รูปแบบฟอนต์แบบย่อ = `inherit`
- `font-size`: ขนาดอักษร = `12px`
- `cursor`: รูปตัวชี้ = `pointer`
- } จบ block ของกฎ/เงื่อนไข `.deadline-text-button`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L199

```css
.deadline-footnote { margin-top: 15px; }
```

- selector `.deadline-footnote` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `15px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-footnote`

### L200

```css
.deadline-page-title { margin: 2px 0 22px; }
```

- selector `.deadline-page-title` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `2px 0 22px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-page-title`

### L201

```css
.deadline-page-title h1 { margin-top: 5px; }
```

- selector `.deadline-page-title h1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `5px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-page-title h1`

### L202

```css
.deadline-form-layout { grid-template-columns: minmax(255px, .85fr) minmax(0, 1.4fr); }
```

- selector `.deadline-form-layout` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `minmax(255px, .85fr) minmax(0, 1.4fr)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-form-layout`

### L203

```css
.deadline-add-form { position: sticky; top: 16px; }
```

- selector `.deadline-add-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `position`: รูปแบบตำแหน่ง = `sticky`
- `top`: ตำแหน่งจากบน = `16px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form`

### L204

```css
.deadline-add-form h2 { margin: 0 0 18px; }
```

- selector `.deadline-add-form h2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0 0 18px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form h2`

### L205

```css
.deadline-add-form .field input { max-width: none; }
```

- selector `.deadline-add-form .field input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .field input`

### L206

```css
.deadline-edit-card { margin-bottom: 10px; }
```

- selector `.deadline-edit-card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-bottom`: ระยะนอกด้านล่าง = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card`

### L207

```css
.deadline-edit-heading { display: flex; justify-content: space-between; align-items: start; gap: 12px; }
```

- selector `.deadline-edit-heading` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `gap`: ช่องว่างระหว่าง item = `12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-heading`

### L208

```css
.deadline-edit-card details { border-top: 1px solid var(--line); margin-top: 12px; padding-top: 10px; }
```

- selector `.deadline-edit-card details` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border-top`: เส้นขอบบน = `1px solid var(--line)`
- `margin-top`: ระยะนอกด้านบน = `12px`
- `padding-top`: ระยะในด้านบน = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card details`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L209

```css
.deadline-edit-card summary { color: var(--maroon); cursor: pointer; font-size: 13px; font-weight: 700; }
```

- selector `.deadline-edit-card summary` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `cursor`: รูปตัวชี้ = `pointer`
- `font-size`: ขนาดอักษร = `13px`
- `font-weight`: น้ำหนักอักษร = `700`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card summary`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L210

```css
.deadline-edit-form { margin-top: 16px; }
```

- selector `.deadline-edit-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `16px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-form`

### L211

```css
.deadline-edit-form .field { flex: 1; min-width: 120px; }
```

- selector `.deadline-edit-form .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `min-width`: ความกว้างต่ำสุด = `120px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-form .field`

### L212

```css
.deadline-edit-form .field input { width: 100%; }
```

- selector `.deadline-edit-form .field input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-form .field input`

### L213

```css
.deadline-delete-form { margin-top: 14px; }
```

- selector `.deadline-delete-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-delete-form`

### L214

```css
.deadline-hours-form { display: flex; flex-wrap: wrap; align-items: end; gap: 12px; }
```

- selector `.deadline-hours-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `align-items`: แนวจัดวางบนแกนขวาง = `end`
- `gap`: ช่องว่างระหว่าง item = `12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form`

### L215

```css
.deadline-hours-form .field { margin: 0; }
```

- selector `.deadline-hours-form .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form .field`

### L216

```css
.deadline-hours-form input { max-width: 210px; }
```

- selector `.deadline-hours-form input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `210px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form input`

### L217

```css
.deadline-focus { display: flex; flex-direction: column; gap: 4px; padding: 20px 22px; border-radius: 12px; background: var(--maroon); color: #fff; }
```

- selector `.deadline-focus` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `4px`
- `padding`: ระยะภายใน = `20px 22px`
- `border-radius`: ความโค้งมุม = `12px`
- `background`: พื้นหลัง/gradient = `var(--maroon)`
- `color`: สีตัวอักษร = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L218

```css
.deadline-focus .deadline-eyebrow { color: #ffdc75; }
```

- selector `.deadline-focus .deadline-eyebrow` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#ffdc75`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus .deadline-eyebrow`

### L219

```css
.deadline-focus strong { font-size: 22px; }
```

- selector `.deadline-focus strong` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `22px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus strong`

### L220

```css
.deadline-focus span:last-child { font-size: 13px; opacity: .9; }
```

- selector `.deadline-focus span:last-child` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `13px`
- `opacity`: ความทึบ = `.9`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus span:last-child`

### L221

```css
.deadline-plan-detail { margin: 9px 0 0; font-size: 13px; color: var(--ink); }
```

- selector `.deadline-plan-detail` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `9px 0 0`
- `font-size`: ขนาดอักษร = `13px`
- `color`: สีตัวอักษร = `var(--ink)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-plan-detail`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L222

```css
.deadline-home-hero { min-height: 260px; }
```

- selector `.deadline-home-hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `260px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-home-hero`

### L223

```css
.deadline-home-cards .card { min-height: 132px; }
```

- selector `.deadline-home-cards .card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `132px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-home-cards .card`

### L224

```css
.deadline-home-cards .card-title { line-height: 1.35; }
```

- selector `.deadline-home-cards .card-title` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `line-height`: ระยะบรรทัด = `1.35`
- } จบ block ของกฎ/เงื่อนไข `.deadline-home-cards .card-title`

### L225

```css
.deadline-task :focus-visible, .deadline-edit-card :focus-visible, .deadline-hero :focus-visible, .deadline-hours-form :focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
```

- selector `.deadline-task :focus-visible, .deadline-edit-card :focus-visible, .deadline-hero :focus-visible, .deadline-hours-form :focus-visible` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `outline`: เส้น focus ที่ไม่ใช้พื้นที่ layout = `3px solid var(--gold)`
- `outline-offset`: ระยะของเส้น focus = `3px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task :focus-visible, .deadline-edit-card :focus-visible, .deadline-hero :focus-visible, .deadline-hours-form :focus-visible`
- focus-visible ช่วยเห็นตำแหน่งคีย์บอร์ด ไม่ใช่สถานะงาน
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L226

```css
@media (max-width: 720px) {
```

- เงื่อนไขขนาดจอ: `@media (max-width: 720px)` กฎภายในใช้เมื่อเข้าเงื่อนไข

### L227

```css
  .deadline-form-layout { grid-template-columns: 1fr; }
```

- selector `.deadline-form-layout` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `1fr`
- } จบ block ของกฎ/เงื่อนไข `.deadline-form-layout`

### L228

```css
  .deadline-add-form { position: static; }
```

- selector `.deadline-add-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `position`: รูปแบบตำแหน่ง = `static`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form`

### L229

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 720px)`

### L230

```css
@media (max-width: 640px) {
```

- เงื่อนไขขนาดจอ: `@media (max-width: 640px)` กฎภายในใช้เมื่อเข้าเงื่อนไข

### L231

```css
  .deadline-hero { padding: 24px 20px; }
```

- selector `.deadline-hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `24px 20px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero`

### L232

```css
  .deadline-hero-mark { display: none; }
```

- selector `.deadline-hero-mark` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero-mark`

### L233

```css
  .deadline-hero .btn { display: block; width: 100%; text-align: center; }
```

- selector `.deadline-hero .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `width`: ความกว้าง = `100%`
- `text-align`: แนวข้อความ = `center`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hero .btn`

### L234

```css
  .deadline-section-head { align-items: start; flex-direction: column; }
```

- selector `.deadline-section-head` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.deadline-section-head`

### L235

```css
  .deadline-reminder-control { align-items: start; text-align: left; }
```

- selector `.deadline-reminder-control` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `text-align`: แนวข้อความ = `left`
- } จบ block ของกฎ/เงื่อนไข `.deadline-reminder-control`

### L236

```css
  .deadline-task { align-items: start; flex-direction: column; gap: 10px; }
```

- selector `.deadline-task` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task`

### L237

```css
  .deadline-task-actions { align-items: start; flex-direction: row; flex-wrap: wrap; }
```

- selector `.deadline-task-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `flex-direction`: ทิศทางของ flex = `row`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions`

### L238

```css
  .deadline-edit-heading { flex-direction: column; }
```

- selector `.deadline-edit-heading` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-heading`

### L239

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 640px)`

### L240

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L241

```css
/* Deadline Compass v2: daily actions, work logs, and accessible touch layouts. */
```

- comment บอกส่วนของ stylesheet: /* Deadline Compass v2: daily actions, work logs, and accessible touch layouts. */

### L242

```css
.deadline-overview-hero { padding: 26px 30px; }
```

- selector `.deadline-overview-hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `26px 30px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-overview-hero`

### L243

```css
.deadline-overview-hero .deadline-hero-mark span:last-child { font-size: 64px; }
```

- selector `.deadline-overview-hero .deadline-hero-mark span:last-child` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `64px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-overview-hero .deadline-hero-mark span:last-child`

### L244

```css
.deadline-today-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr)); gap: 14px; }
```

- selector `.deadline-today-grid` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(min(100%, 260px), 1fr))`
- `gap`: ช่องว่างระหว่าง item = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-grid`

### L245

```css
.deadline-today-card { border: 1px solid #ebd4a0; border-top: 4px solid var(--gold); background: #fffdf6; padding: 22px; display: flex; flex-direction: column; }
```

- selector `.deadline-today-card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border`: เส้นขอบแบบย่อ = `1px solid #ebd4a0`
- `border-top`: เส้นขอบบน = `4px solid var(--gold)`
- `background`: พื้นหลัง/gradient = `#fffdf6`
- `padding`: ระยะภายใน = `22px`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-card`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L246

```css
.deadline-today-card h3 { font-size: 21px; line-height: 1.4; margin: 8px 0 12px; overflow-wrap: anywhere; }
```

- selector `.deadline-today-card h3` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `21px`
- `line-height`: ระยะบรรทัด = `1.4`
- `margin`: ระยะภายนอก = `8px 0 12px`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-card h3`

### L247

```css
.deadline-today-time { margin: 16px 0 6px; color: var(--maroon-dark); }
```

- selector `.deadline-today-time` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `16px 0 6px`
- `color`: สีตัวอักษร = `var(--maroon-dark)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-time`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L248

```css
.deadline-today-time strong { font-size: 29px; font-variant-numeric: tabular-nums; }
```

- selector `.deadline-today-time strong` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `29px`
- `font-variant-numeric`: รูปแบบตัวเลข เช่นกว้างเท่ากัน = `tabular-nums`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-time strong`

### L249

```css
.deadline-reasons { padding-left: 20px; font-size: 14px; line-height: 1.7; color: #514b47; margin: 9px 0 15px; }
```

- selector `.deadline-reasons` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding-left`: ระยะในซ้าย = `20px`
- `font-size`: ขนาดอักษร = `14px`
- `line-height`: ระยะบรรทัด = `1.7`
- `color`: สีตัวอักษร = `#514b47`
- `margin`: ระยะภายนอก = `9px 0 15px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-reasons`

### L250

```css
.deadline-today-card .deadline-quick-actions { margin-top: auto; padding-top: 12px; }
```

- selector `.deadline-today-card .deadline-quick-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `auto`
- `padding-top`: ระยะในด้านบน = `12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-today-card .deadline-quick-actions`

### L251

```css
.deadline-quick-actions { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 12px; }
```

- selector `.deadline-quick-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `gap`: ช่องว่างระหว่าง item = `8px`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `margin-top`: ระยะนอกด้านบน = `12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-quick-actions`

### L252

```css
.deadline-quick-actions form { margin: 0; }
```

- selector `.deadline-quick-actions form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-quick-actions form`

### L253

```css
.deadline-quick-actions .btn, .deadline-action-link { min-height: 44px; display: inline-flex; align-items: center; justify-content: center; line-height: 1.4; text-align: center; }
```

- selector `.deadline-quick-actions .btn, .deadline-action-link` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- `display`: วิธีจัดวาง/การแสดง = `inline-flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `center`
- `line-height`: ระยะบรรทัด = `1.4`
- `text-align`: แนวข้อความ = `center`
- } จบ block ของกฎ/เงื่อนไข `.deadline-quick-actions .btn, .deadline-action-link`

### L254

```css
.deadline-action-link { color: var(--maroon); padding: 6px 2px; text-underline-offset: 3px; font-size: 14px; }
```

- selector `.deadline-action-link` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `padding`: ระยะภายใน = `6px 2px`
- `text-underline-offset`: ระยะเส้นใต้ = `3px`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-action-link`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L255

```css
.deadline-task-actions { width: 245px; max-width: 100%; }
```

- selector `.deadline-task-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `245px`
- `max-width`: ความกว้างสูงสุด = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions`

### L256

```css
.deadline-task-actions .deadline-quick-actions { flex-direction: column; align-items: stretch; width: 100%; margin: 0; }
```

- selector `.deadline-task-actions .deadline-quick-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex-direction`: ทิศทางของ flex = `column`
- `align-items`: แนวจัดวางบนแกนขวาง = `stretch`
- `width`: ความกว้าง = `100%`
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions .deadline-quick-actions`

### L257

```css
.deadline-task-actions .btn { width: 100%; }
```

- selector `.deadline-task-actions .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions .btn`

### L258

```css
.deadline-text-button { min-height: 44px; padding: 10px 5px; font-size: 14px; }
```

- selector `.deadline-text-button` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- `padding`: ระยะภายใน = `10px 5px`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-text-button`

### L259

```css
.deadline-badge-row { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
```

- selector `.deadline-badge-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `gap`: ช่องว่างระหว่าง item = `7px`
- `margin-top`: ระยะนอกด้านบน = `12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-badge-row`

### L260

```css
.deadline-badge-row .badge, .deadline-edit-heading > .badge { font-size: 13px; padding: 5px 10px; }
```

- selector `.deadline-badge-row .badge, .deadline-edit-heading > .badge` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `13px`
- `padding`: ระยะภายใน = `5px 10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-badge-row .badge, .deadline-edit-heading > .badge`

### L261

```css
.deadline-alert p { margin: 6px 0 0; font-weight: 400; font-size: 15px; }
```

- selector `.deadline-alert p` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `6px 0 0`
- `font-weight`: น้ำหนักอักษร = `400`
- `font-size`: ขนาดอักษร = `15px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-alert p`

### L262

```css
.deadline-insight { background: #fdf8e9; border: 1px solid #ebdfb8; border-radius: 10px; padding: 14px 16px; color: #635022; font-size: 15px; }
```

- selector `.deadline-insight` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#fdf8e9`
- `border`: เส้นขอบแบบย่อ = `1px solid #ebdfb8`
- `border-radius`: ความโค้งมุม = `10px`
- `padding`: ระยะภายใน = `14px 16px`
- `color`: สีตัวอักษร = `#635022`
- `font-size`: ขนาดอักษร = `15px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-insight`

### L263

```css
.deadline-insight a { color: var(--maroon); }
```

- selector `.deadline-insight a` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-insight a`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L264

```css
.deadline-completed-section { border-top: 1px solid var(--line); margin-top: 30px; padding-top: 8px; }
```

- selector `.deadline-completed-section` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border-top`: เส้นขอบบน = `1px solid var(--line)`
- `margin-top`: ระยะนอกด้านบน = `30px`
- `padding-top`: ระยะในด้านบน = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-completed-section`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L265

```css
.deadline-completed-section .deadline-task { background: #f5faf6; }
```

- selector `.deadline-completed-section .deadline-task` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `background`: พื้นหลัง/gradient = `#f5faf6`
- } จบ block ของกฎ/เงื่อนไข `.deadline-completed-section .deadline-task`

### L266

```css
.deadline-refresh-notice { padding: 12px; border: 1px solid #b6d6f2; background: #edf6ff; border-radius: 8px; }
```

- selector `.deadline-refresh-notice` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `12px`
- `border`: เส้นขอบแบบย่อ = `1px solid #b6d6f2`
- `background`: พื้นหลัง/gradient = `#edf6ff`
- `border-radius`: ความโค้งมุม = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-refresh-notice`

### L267

```css
.deadline-refresh-notice[hidden], .deadline-form-error[hidden], .deadline-past-confirm[hidden] { display: none; }
```

- selector `.deadline-refresh-notice[hidden], .deadline-form-error[hidden], .deadline-past-confirm[hidden]` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-refresh-notice[hidden], .deadline-form-error[hidden], .deadline-past-confirm[hidden]`
- selector ใช้ attribute hidden ร่วม display:none ของส่วนเตือน

### L268

```css
.deadline-help { display: block; font-size: 13px; line-height: 1.6; color: #5f6671; margin-top: 6px; }
```

- selector `.deadline-help` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `font-size`: ขนาดอักษร = `13px`
- `line-height`: ระยะบรรทัด = `1.6`
- `color`: สีตัวอักษร = `#5f6671`
- `margin-top`: ระยะนอกด้านบน = `6px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-help`

### L269

```css
.deadline-form-error { color: #9b1c1c; padding: 10px 12px; border-radius: 8px; background: #fdecec; font-size: 14px; }
```

- selector `.deadline-form-error` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#9b1c1c`
- `padding`: ระยะภายใน = `10px 12px`
- `border-radius`: ความโค้งมุม = `8px`
- `background`: พื้นหลัง/gradient = `#fdecec`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-form-error`

### L270

```css
.deadline-past-confirm { display: flex; align-items: flex-start; gap: 10px; margin: 0 0 16px; padding: 12px; font-size: 14px; line-height: 1.5; background: #fff5d6; border-radius: 8px; color: #6b4d00; }
```

- selector `.deadline-past-confirm` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `flex-start`
- `gap`: ช่องว่างระหว่าง item = `10px`
- `margin`: ระยะภายนอก = `0 0 16px`
- `padding`: ระยะภายใน = `12px`
- `font-size`: ขนาดอักษร = `14px`
- `line-height`: ระยะบรรทัด = `1.5`
- `background`: พื้นหลัง/gradient = `#fff5d6`
- `border-radius`: ความโค้งมุม = `8px`
- `color`: สีตัวอักษร = `#6b4d00`
- } จบ block ของกฎ/เงื่อนไข `.deadline-past-confirm`

### L271

```css
.deadline-past-confirm input { width: 22px; height: 22px; margin: 0; flex-shrink: 0; accent-color: var(--maroon); }
```

- selector `.deadline-past-confirm input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `22px`
- `height`: ความสูง = `22px`
- `margin`: ระยะภายนอก = `0`
- `flex-shrink`: การหดตัว flex item = `0`
- `accent-color`: สี control ตาม browser = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-past-confirm input`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L272

```css
.deadline-subtask-setup { margin-bottom: 20px; }
```

- selector `.deadline-subtask-setup` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-bottom`: ระยะนอกด้านล่าง = `20px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-setup`

### L273

```css
.deadline-subtask-setup summary, .deadline-work-details > summary, .deadline-member > details > summary { min-height: 44px; padding: 10px 0; cursor: pointer; color: var(--maroon); font-weight: 600; }
```

- selector `.deadline-subtask-setup summary, .deadline-work-details > summary, .deadline-member > details > summary` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- `padding`: ระยะภายใน = `10px 0`
- `cursor`: รูปตัวชี้ = `pointer`
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-weight`: น้ำหนักอักษร = `600`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-setup summary, .deadline-work-details > summary, .deadline-member > details > summary`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L274

```css
.deadline-subtask-setup textarea { resize: vertical; min-height: 140px; }
```

- selector `.deadline-subtask-setup textarea` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `resize`: ทิศที่ผู้ใช้ปรับ textarea ได้ = `vertical`
- `min-height`: ความสูงต่ำสุด = `140px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-setup textarea`

### L275

```css
.deadline-work-section { padding: 6px 0 18px; border-bottom: 1px solid var(--line); }
```

- selector `.deadline-work-section` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `6px 0 18px`
- `border-bottom`: เส้นขอบล่าง = `1px solid var(--line)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-work-section`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L276

```css
.deadline-work-section h4 { font-size: 16px; margin: 16px 0; }
```

- selector `.deadline-work-section h4` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `16px`
- `margin`: ระยะภายนอก = `16px 0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-work-section h4`

### L277

```css
.deadline-log-form .field-row { align-items: start; }
```

- selector `.deadline-log-form .field-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- } จบ block ของกฎ/เงื่อนไข `.deadline-log-form .field-row`

### L278

```css
.deadline-log-form .field { flex: 1; min-width: 150px; }
```

- selector `.deadline-log-form .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `min-width`: ความกว้างต่ำสุด = `150px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-log-form .field`

### L279

```css
.deadline-subtask-list { list-style: none; margin: 0; padding: 0; }
```

- selector `.deadline-subtask-list` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `list-style`: รูป marker ของรายการ = `none`
- `margin`: ระยะภายนอก = `0`
- `padding`: ระยะภายใน = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-list`

### L280

```css
.deadline-subtask-list li { margin-bottom: 7px; }
```

- selector `.deadline-subtask-list li` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-bottom`: ระยะนอกด้านล่าง = `7px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-list li`

### L281

```css
.deadline-subtask-toggle { display: flex; align-items: center; gap: 10px; width: 100%; min-height: 44px; padding: 10px 12px; border: 1px solid var(--line); border-radius: 8px; background: #fff; color: var(--ink); font: inherit; font-size: 15px; text-align: left; cursor: pointer; overflow-wrap: anywhere; }
```

- selector `.deadline-subtask-toggle` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `gap`: ช่องว่างระหว่าง item = `10px`
- `width`: ความกว้าง = `100%`
- `min-height`: ความสูงต่ำสุด = `44px`
- `padding`: ระยะภายใน = `10px 12px`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `8px`
- `background`: พื้นหลัง/gradient = `#fff`
- `color`: สีตัวอักษร = `var(--ink)`
- `font`: รูปแบบฟอนต์แบบย่อ = `inherit`
- `font-size`: ขนาดอักษร = `15px`
- `text-align`: แนวข้อความ = `left`
- `cursor`: รูปตัวชี้ = `pointer`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-toggle`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L282

```css
.deadline-subtask-toggle.is-done { color: #1b6b3a; background: #eef8f0; }
```

- selector `.deadline-subtask-toggle.is-done` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#1b6b3a`
- `background`: พื้นหลัง/gradient = `#eef8f0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-toggle.is-done`

### L283

```css
.deadline-subtask-toggle.is-done span { color: #1b6b3a; }
```

- selector `.deadline-subtask-toggle.is-done span` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#1b6b3a`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-toggle.is-done span`

### L284

```css
.deadline-subtask-add { margin-top: 15px; display: flex; flex-wrap: wrap; gap: 8px; align-items: end; }
```

- selector `.deadline-subtask-add` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `15px`
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-wrap`: ให้ flex ขึ้นบรรทัดใหม่ = `wrap`
- `gap`: ช่องว่างระหว่าง item = `8px`
- `align-items`: แนวจัดวางบนแกนขวาง = `end`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-add`

### L285

```css
.deadline-subtask-add .field { flex: 1; min-width: 150px; margin: 0; }
```

- selector `.deadline-subtask-add .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1`
- `min-width`: ความกว้างต่ำสุด = `150px`
- `margin`: ระยะภายนอก = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-add .field`

### L286

```css
.deadline-subtask-add .field input { max-width: none; }
```

- selector `.deadline-subtask-add .field input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-subtask-add .field input`

### L287

```css
.deadline-edit-card { scroll-margin-top: 18px; }
```

- selector `.deadline-edit-card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `scroll-margin-top`: ระยะเมื่อเลื่อนมาที่ anchor = `18px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card`

### L288

```css
.deadline-edit-card:target { outline: 3px solid var(--gold); outline-offset: 3px; }
```

- selector `.deadline-edit-card:target` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `outline`: เส้น focus ที่ไม่ใช้พื้นที่ layout = `3px solid var(--gold)`
- `outline-offset`: ระยะของเส้น focus = `3px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card:target`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L289

```css
.deadline-edit-card .field input, .deadline-edit-card .field select { max-width: none; }
```

- selector `.deadline-edit-card .field input, .deadline-edit-card .field select` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-edit-card .field input, .deadline-edit-card .field select`

### L290

```css
.deadline-plan-card { padding: 22px; }
```

- selector `.deadline-plan-card` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `22px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-plan-card`

### L291

```css
.deadline-plan-card h3 { font-size: 19px; margin: 5px 0 7px; overflow-wrap: anywhere; }
```

- selector `.deadline-plan-card h3` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `19px`
- `margin`: ระยะภายนอก = `5px 0 7px`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-plan-card h3`

### L292

```css
.deadline-time-comparison { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin: 20px 0 14px; }
```

- selector `.deadline-time-comparison` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(3, minmax(0, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `10px`
- `margin`: ระยะภายนอก = `20px 0 14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison`

### L293

```css
.deadline-time-comparison > div { display: flex; flex-direction: column; gap: 6px; padding: 14px; background: #f8f5f1; border: 1px solid var(--line); border-radius: 10px; }
```

- selector `.deadline-time-comparison > div` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `6px`
- `padding`: ระยะภายใน = `14px`
- `background`: พื้นหลัง/gradient = `#f8f5f1`
- `border`: เส้นขอบแบบย่อ = `1px solid var(--line)`
- `border-radius`: ความโค้งมุม = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison > div`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L294

```css
.deadline-time-comparison span { color: #62676d; font-size: 13px; }
```

- selector `.deadline-time-comparison span` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#62676d`
- `font-size`: ขนาดอักษร = `13px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison span`

### L295

```css
.deadline-time-comparison strong { font-size: 25px; font-variant-numeric: tabular-nums; }
```

- selector `.deadline-time-comparison strong` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `25px`
- `font-variant-numeric`: รูปแบบตัวเลข เช่นกว้างเท่ากัน = `tabular-nums`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison strong`

### L296

```css
.deadline-time-comparison small { font-size: 12px; font-weight: 400; }
```

- selector `.deadline-time-comparison small` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `12px`
- `font-weight`: น้ำหนักอักษร = `400`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison small`

### L297

```css
.deadline-time-comparison .deadline-time-bad { color: #9b1c1c; background: #fdecec; border-color: #f3b4b4; }
```

- selector `.deadline-time-comparison .deadline-time-bad` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#9b1c1c`
- `background`: พื้นหลัง/gradient = `#fdecec`
- `border-color`: สีเส้นขอบ = `#f3b4b4`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison .deadline-time-bad`

### L298

```css
.deadline-focus-actions .btn { border-color: #fff; }
```

- selector `.deadline-focus-actions .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `border-color`: สีเส้นขอบ = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus-actions .btn`

### L299

```css
.deadline-focus-actions .deadline-action-link { color: #fff; }
```

- selector `.deadline-focus-actions .deadline-action-link` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#fff`
- } จบ block ของกฎ/เงื่อนไข `.deadline-focus-actions .deadline-action-link`

### L300

```css
.deadline-history-section { margin-top: 32px; }
```

- selector `.deadline-history-section` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin-top`: ระยะนอกด้านบน = `32px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-history-section`

### L301

```css
.deadline-table-scroll { width: 100%; overflow-x: auto; border-radius: 10px; }
```

- selector `.deadline-table-scroll` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `overflow-x`: การจัดการส่วนล้นแนวนอน = `auto`
- `border-radius`: ความโค้งมุม = `10px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-table-scroll`

### L302

```css
.deadline-table-scroll table { min-width: 580px; }
```

- selector `.deadline-table-scroll table` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-width`: ความกว้างต่ำสุด = `580px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-table-scroll table`

### L303

```css
.deadline-table-scroll td { vertical-align: top; line-height: 1.6; }
```

- selector `.deadline-table-scroll td` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `vertical-align`: แนวข้อมูลใน table = `top`
- `line-height`: ระยะบรรทัด = `1.6`
- } จบ block ของกฎ/เงื่อนไข `.deadline-table-scroll td`

### L304

```css
.deadline-member-grid { grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); }
```

- selector `.deadline-member-grid` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(min(100%, 300px), 1fr))`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-grid`

### L305

```css
.deadline-member { text-align: left; padding: 22px; min-width: 0; }
```

- selector `.deadline-member` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `text-align`: แนวข้อความ = `left`
- `padding`: ระยะภายใน = `22px`
- `min-width`: ความกว้างต่ำสุด = `0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member`

### L306

```css
.deadline-member .avatar { margin: 0 0 12px; }
```

- selector `.deadline-member .avatar` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `0 0 12px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member .avatar`

### L307

```css
.deadline-member h3 { font-size: 18px; margin: 4px 0; overflow-wrap: anywhere; }
```

- selector `.deadline-member h3` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `18px`
- `margin`: ระยะภายนอก = `4px 0`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member h3`

### L308

```css
.deadline-member-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 18px; }
```

- selector `.deadline-member-stats` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(3, minmax(0, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `8px`
- `margin-top`: ระยะนอกด้านบน = `18px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-stats`

### L309

```css
.deadline-member-stats > div { display: flex; flex-direction: column; gap: 3px; background: #f7f5f2; padding: 10px 8px; border-radius: 8px; }
```

- selector `.deadline-member-stats > div` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `3px`
- `background`: พื้นหลัง/gradient = `#f7f5f2`
- `padding`: ระยะภายใน = `10px 8px`
- `border-radius`: ความโค้งมุม = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-stats > div`

### L310

```css
.deadline-member-stats strong { font-size: 23px; color: var(--maroon); }
```

- selector `.deadline-member-stats strong` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `23px`
- `color`: สีตัวอักษร = `var(--maroon)`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-stats strong`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L311

```css
.deadline-member-stats span { font-size: 12px; color: #62676d; }
```

- selector `.deadline-member-stats span` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `12px`
- `color`: สีตัวอักษร = `#62676d`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-stats span`

### L312

```css
.deadline-member-warning { color: #9b1c1c; background: #fdecec; padding: 10px; font-size: 14px; border-radius: 8px; }
```

- selector `.deadline-member-warning` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `#9b1c1c`
- `background`: พื้นหลัง/gradient = `#fdecec`
- `padding`: ระยะภายใน = `10px`
- `font-size`: ขนาดอักษร = `14px`
- `border-radius`: ความโค้งมุม = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-warning`

### L313

```css
.deadline-member-tasks { padding-left: 18px; font-size: 14px; }
```

- selector `.deadline-member-tasks` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding-left`: ระยะในซ้าย = `18px`
- `font-size`: ขนาดอักษร = `14px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-tasks`

### L314

```css
.deadline-member-tasks li { margin: 10px 0; }
```

- selector `.deadline-member-tasks li` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `margin`: ระยะภายนอก = `10px 0`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-tasks li`

### L315

```css
.deadline-member-tasks a { color: var(--maroon); overflow-wrap: anywhere; }
```

- selector `.deadline-member-tasks a` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-tasks a`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L316

```css
.deadline-member-tasks small { display: block; color: #62676d; margin-top: 4px; }
```

- selector `.deadline-member-tasks small` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `block`
- `color`: สีตัวอักษร = `#62676d`
- `margin-top`: ระยะนอกด้านบน = `4px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-member-tasks small`

### L317

```css
.deadline-task h3, .deadline-meta, .deadline-plan-detail, .deadline-section-head h2, .members { overflow-wrap: anywhere; }
```

- selector `.deadline-task h3, .deadline-meta, .deadline-plan-detail, .deadline-section-head h2, .members` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task h3, .deadline-meta, .deadline-plan-detail, .deadline-section-head h2, .members`

### L318

```css
input, select, textarea { min-width: 0; }
```

- selector `input, select, textarea` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-width`: ความกว้างต่ำสุด = `0`
- } จบ block ของกฎ/เงื่อนไข `input, select, textarea`

### L319

```css
.deadline-add-form .field input, .deadline-add-form .field select, .deadline-add-form .field textarea { max-width: none; }
```

- selector `.deadline-add-form .field input, .deadline-add-form .field select, .deadline-add-form .field textarea` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .field input, .deadline-add-form .field select, .deadline-add-form .field textarea`

### L320

```css
.deadline-add-form .field input, .deadline-add-form .field select, .deadline-edit-card .field input, .deadline-edit-card .field select, .deadline-hours-form input { min-height: 44px; }
```

- selector `.deadline-add-form .field input, .deadline-add-form .field select, .deadline-edit-card .field input, .deadline-edit-card .field select, .deadline-hours-form input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .field input, .deadline-add-form .field select, .deadline-edit-card .field input, .deadline-edit-card .field select, .deadline-hours-form input`

### L321

```css
.deadline-add-form .field label, .deadline-edit-card .field label, .deadline-hours-form label { font-size: 14px; color: #515964; }
```

- selector `.deadline-add-form .field label, .deadline-edit-card .field label, .deadline-hours-form label` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `14px`
- `color`: สีตัวอักษร = `#515964`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .field label, .deadline-edit-card .field label, .deadline-hours-form label`

### L322

```css
.deadline-add-form .btn, .deadline-edit-card .btn, .deadline-hours-form .btn, .deadline-member .btn { min-height: 44px; }
```

- selector `.deadline-add-form .btn, .deadline-edit-card .btn, .deadline-hours-form .btn, .deadline-member .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .btn, .deadline-edit-card .btn, .deadline-hours-form .btn, .deadline-member .btn`

### L323

```css
main :focus-visible, .site-nav a:focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
```

- selector `main :focus-visible, .site-nav a:focus-visible` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `main`: property CSS ของกฎที่เลือก = `focus-visible, .site-nav a:focus-visible`
- `outline`: เส้น focus ที่ไม่ใช้พื้นที่ layout = `3px solid var(--gold)`
- `outline-offset`: ระยะของเส้น focus = `3px`
- } จบ block ของกฎ/เงื่อนไข `main :focus-visible, .site-nav a:focus-visible`
- focus-visible ช่วยเห็นตำแหน่งคีย์บอร์ด ไม่ใช่สถานะงาน
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด

### L324

```css
@media (max-width: 720px) {
```

- เงื่อนไขขนาดจอ: `@media (max-width: 720px)` กฎภายในใช้เมื่อเข้าเงื่อนไข

### L325

```css
  .deadline-task { align-items: start; flex-direction: column; }
```

- selector `.deadline-task` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `flex-direction`: ทิศทางของ flex = `column`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task`

### L326

```css
  .deadline-task-actions { width: 100%; align-items: start; }
```

- selector `.deadline-task-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions`

### L327

```css
  .deadline-task-actions .deadline-quick-actions { flex-direction: row; align-items: center; }
```

- selector `.deadline-task-actions .deadline-quick-actions` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex-direction`: ทิศทางของ flex = `row`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions .deadline-quick-actions`

### L328

```css
  .deadline-task-actions .btn { width: auto; }
```

- selector `.deadline-task-actions .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `auto`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions .btn`

### L329

```css
  .deadline-hours-form { align-items: stretch; }
```

- selector `.deadline-hours-form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-items`: แนวจัดวางบนแกนขวาง = `stretch`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form`

### L330

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 720px)`

### L331

```css
@media (max-width: 640px) {
```

- เงื่อนไขขนาดจอ: `@media (max-width: 640px)` กฎภายในใช้เมื่อเข้าเงื่อนไข

### L332

```css
  .wrap { padding-left: 16px; padding-right: 16px; }
```

- selector `.wrap` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding-left`: ระยะในซ้าย = `16px`
- `padding-right`: ระยะในขวา = `16px`
- } จบ block ของกฎ/เงื่อนไข `.wrap`

### L333

```css
  .header-row { flex-direction: column; align-items: start; gap: 10px; }
```

- selector `.header-row` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex-direction`: ทิศทางของ flex = `column`
- `align-items`: แนวจัดวางบนแกนขวาง = `start`
- `gap`: ช่องว่างระหว่าง item = `10px`
- } จบ block ของกฎ/เงื่อนไข `.header-row`

### L334

```css
  .brand { width: 100%; gap: 10px; }
```

- selector `.brand` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `gap`: ช่องว่างระหว่าง item = `10px`
- } จบ block ของกฎ/เงื่อนไข `.brand`

### L335

```css
  .brand img { height: 42px; width: 42px; flex-shrink: 0; }
```

- selector `.brand img` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `height`: ความสูง = `42px`
- `width`: ความกว้าง = `42px`
- `flex-shrink`: การหดตัว flex item = `0`
- } จบ block ของกฎ/เงื่อนไข `.brand img`

### L336

```css
  .brand-text { min-width: 0; }
```

- selector `.brand-text` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-width`: ความกว้างต่ำสุด = `0`
- } จบ block ของกฎ/เงื่อนไข `.brand-text`

### L337

```css
  .brand-line1 { font-size: 14px; overflow-wrap: anywhere; }
```

- selector `.brand-line1` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `14px`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.brand-line1`

### L338

```css
  .brand-line2 { font-size: 11px; overflow-wrap: anywhere; }
```

- selector `.brand-line2` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `11px`
- `overflow-wrap`: การตัดข้อความยาว = `anywhere`
- } จบ block ของกฎ/เงื่อนไข `.brand-line2`

### L339

```css
  .group-badge { align-self: start; }
```

- selector `.group-badge` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `align-self`: แนวจัดวางเฉพาะ item = `start`
- } จบ block ของกฎ/เงื่อนไข `.group-badge`

### L340

```css
  .site-nav { gap: 0; }
```

- selector `.site-nav` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `gap`: ช่องว่างระหว่าง item = `0`
- } จบ block ของกฎ/เงื่อนไข `.site-nav`

### L341

```css
  .site-nav a { min-height: 44px; padding: 11px 10px; }
```

- selector `.site-nav a` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-height`: ความสูงต่ำสุด = `44px`
- `padding`: ระยะภายใน = `11px 10px`
- } จบ block ของกฎ/เงื่อนไข `.site-nav a`

### L342

```css
  .deadline-overview-hero { padding: 24px 20px; }
```

- selector `.deadline-overview-hero` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `24px 20px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-overview-hero`

### L343

```css
  .deadline-task, .deadline-plan-card, .deadline-today-card, .deadline-member { padding: 18px; }
```

- selector `.deadline-task, .deadline-plan-card, .deadline-today-card, .deadline-member` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `padding`: ระยะภายใน = `18px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task, .deadline-plan-card, .deadline-today-card, .deadline-member`

### L344

```css
  .deadline-quick-actions form { flex: 1 1 180px; }
```

- selector `.deadline-quick-actions form` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1 1 180px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-quick-actions form`

### L345

```css
  .deadline-quick-actions .btn { width: 100%; }
```

- selector `.deadline-quick-actions .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-quick-actions .btn`

### L346

```css
  .deadline-action-link { width: 100%; justify-content: start; }
```

- selector `.deadline-action-link` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `start`
- } จบ block ของกฎ/เงื่อนไข `.deadline-action-link`

### L347

```css
  .deadline-task-actions .btn { width: 100%; }
```

- selector `.deadline-task-actions .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-task-actions .btn`

### L348

```css
  .deadline-add-form .field input, .deadline-edit-card .field input, .deadline-hours-form input, .deadline-add-form select, .deadline-edit-card select, .deadline-add-form textarea { font-size: 16px; }
```

- selector `.deadline-add-form .field input, .deadline-edit-card .field input, .deadline-hours-form input, .deadline-add-form select, .deadline-edit-card select, .deadline-add-form textarea` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `font-size`: ขนาดอักษร = `16px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-add-form .field input, .deadline-edit-card .field input, .deadline-hours-form input, .deadline-add-form select, .deadline-edit-card select, .deadline-add-form textarea`

### L349

```css
  .deadline-time-comparison { grid-template-columns: 1fr; }
```

- selector `.deadline-time-comparison` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `1fr`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison`

### L350

```css
  .deadline-time-comparison > div { flex-direction: row; align-items: center; justify-content: space-between; gap: 8px; }
```

- selector `.deadline-time-comparison > div` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex-direction`: ทิศทางของ flex = `row`
- `align-items`: แนวจัดวางบนแกนขวาง = `center`
- `justify-content`: จัดพื้นที่บนแกนหลัก = `space-between`
- `gap`: ช่องว่างระหว่าง item = `8px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-time-comparison > div`

### L351

```css
  .deadline-hours-form .field { flex: 1 1 100%; }
```

- selector `.deadline-hours-form .field` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `flex`: สัดส่วนและพฤติกรรม flex item = `1 1 100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form .field`

### L352

```css
  .deadline-hours-form input { max-width: none; }
```

- selector `.deadline-hours-form input` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `max-width`: ความกว้างสูงสุด = `none`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form input`

### L353

```css
  .deadline-hours-form .btn { width: 100%; }
```

- selector `.deadline-hours-form .btn` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `width`: ความกว้าง = `100%`
- } จบ block ของกฎ/เงื่อนไข `.deadline-hours-form .btn`

### L354

```css
  .deadline-table-scroll table { min-width: 520px; }
```

- selector `.deadline-table-scroll table` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `min-width`: ความกว้างต่ำสุด = `520px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-table-scroll table`

### L355

```css
}
```

- } จบ block ของกฎ/เงื่อนไข `@media (max-width: 640px)`

### L356

(บรรทัดว่าง)

- บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง

### L357

```css
.deadline-daily-history { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 16px; }
```

- selector `.deadline-daily-history` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `grid`
- `grid-template-columns`: จำนวน/สัดส่วนคอลัมน์ grid = `repeat(auto-fit, minmax(160px, 1fr))`
- `gap`: ช่องว่างระหว่าง item = `12px`
- `margin-bottom`: ระยะนอกด้านล่าง = `16px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-daily-history`

### L358

```css
.deadline-daily-history .panel { display: flex; flex-direction: column; gap: 8px; padding: 16px; }
```

- selector `.deadline-daily-history .panel` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `display`: วิธีจัดวาง/การแสดง = `flex`
- `flex-direction`: ทิศทางของ flex = `column`
- `gap`: ช่องว่างระหว่าง item = `8px`
- `padding`: ระยะภายใน = `16px`
- } จบ block ของกฎ/เงื่อนไข `.deadline-daily-history .panel`

### L359

```css
.deadline-daily-history strong { color: var(--maroon); font-size: 1.2rem; }
```

- selector `.deadline-daily-history strong` เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย
- `color`: สีตัวอักษร = `var(--maroon)`
- `font-size`: ขนาดอักษร = `1.2rem`
- } จบ block ของกฎ/เงื่อนไข `.deadline-daily-history strong`
- var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด
