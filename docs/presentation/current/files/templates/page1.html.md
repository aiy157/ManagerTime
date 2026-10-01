# templates/page1.html — HTML/Jinja ของ Overview

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 82 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `62df0224f14886762ac6143ed521ce346474d917d8795ad4fea8c33fdf707a65`

**ผู้ศึกษา/บทบาท:** นางสาวลักขณา ศรีโพธิ์ · Page 1

## 1. หน้าที่และการเชื่อมต่อ

แสดงงานวันนี้ เหตุผล สถิติ งานค้าง งานเสร็จ และจุดควบคุมการเตือน

- **รับเข้า:** context จาก pages/page1.py และ macro _task_card.html
- **ผลลัพธ์:** หน้า Overview ที่มีฟอร์ม POST และ JSON สำหรับ JavaScript

**เกี่ยวข้องกับ:** base.html; _task_card.html: task_card/quick_actions; static/js/reminders.js; static/style.css

## 2. ลำดับทำงาน

1. แสดงเวลาที่ตั้ง ทำจริงวันนี้ และงบเหลือ
2. แสดงสถิติและเตือนงานเกินกำหนด/หลายงานใกล้ส่ง
3. วน recommendations เป็นการ์ดแนะนำ
4. วน items เป็นงานค้าง และ completed เป็นหมวดเสร็จ
5. ฝัง reminder_tasks ผ่าน tojson และโหลด reminders.js ด้วย defer

## 3. จุดที่ต้องอธิบายให้ถูก

- tojson เปลี่ยนข้อมูลเป็น JSON ที่เหมาะกับการฝังใน HTML; ไม่ใช้ safe กับชื่อผู้ใช้
- else ของ for ใช้เมื่อรายการว่าง แตกต่างจาก else ของ if
- กรณีงบวันนี้หมดแต่ยัง pending ต้องอ่านคำอธิบายให้ตรง ไม่ใช่งานเสร็จหมด
- การดึงข้อมูลเตือนใหม่ยังไม่แทนการ์ดทั้งหน้าทันที

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q005: ทำไมหนึ่งหน้ามีทั้ง .py และ .html?](../../TEACHER_QUESTIONS.md#q005)
- [Q031: Overview ตอบคำถามสำคัญอะไร?](../../TEACHER_QUESTIONS.md#q031)
- [Q038: ทำวันนี้ 1.5 ชั่วโมง จากงบ 4 ระบบควรแนะนำเพิ่มเท่าไร?](../../TEACHER_QUESTIONS.md#q038)
- [Q039: ถ้าวันนี้ครบงบแต่ยังมีงานค้าง ทำอย่างไร?](../../TEACHER_QUESTIONS.md#q039)
- [Q040: กดเสร็จแล้วตัวเลข Overview เปลี่ยนอย่างไร?](../../TEACHER_QUESTIONS.md#q040)
- [Q061: extends base.html ทำอะไร?](../../TEACHER_QUESTIONS.md#q061)
- [Q062: {{ }} กับ {% %} ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q062)
- [Q072: defer ที่ script หมายถึงอะไรในโครงการ?](../../TEACHER_QUESTIONS.md#q072)
- [Q076: ข้อมูลในอีกแท็บเปลี่ยน ระบบเตือนรู้ได้อย่างไร?](../../TEACHER_QUESTIONS.md#q076)
- [Q096: ป้องกัน XSS อย่างไร?](../../TEACHER_QUESTIONS.md#q096)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% extends "base.html" %}
{% from "_task_card.html" import task_card, quick_actions %}
{% block content %}
<section class="deadline-hero deadline-overview-hero">
  <div>
    <span class="deadline-eyebrow">DEADLINE COMPASS · วันนี้</span>
    <h1>เริ่มจากงานสำคัญ แล้วค่อยไปต่อ</h1>
    <p>เวลาว่าง {{ daily_hours }} ชั่วโมง/วัน · วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง · เหลือแบ่ง {{ today_remaining }} ชั่วโมง</p>
    <a class="btn" href="{{ url_for('page', name='page2') }}">+ เพิ่มงาน</a>
    <a class="btn ghost" href="{{ url_for('page', name='page3') }}">ปรับเวลาว่างและดูแผน →</a>
  </div>
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>GO</span></div>
</section>

<div class="stat-grid deadline-summary">
  <div class="stat"><div class="label">งานค้าง</div><div class="value">{{ open_count }}</div><div class="unit">รายการ</div></div>
  <div class="stat gold"><div class="label">ส่งวันนี้ถึงอีก 3 วัน</div><div class="value">{{ soon_count }}</div><div class="unit">รายการ</div></div>
  <div class="stat"><div class="label">เวลาที่ยังต้องใช้</div><div class="value">{{ "{:,.1f}".format(remaining_total) }}</div><div class="unit">ชั่วโมง</div></div>
  <div class="stat good"><div class="label">เสร็จแล้ว</div><div class="value">{{ completed_count }}</div><div class="unit">รายการ</div></div>
</div>

{% if overdue_count %}
<div class="deadline-alert" role="status">
  <strong>! มีงานเกินกำหนด {{ overdue_count }} รายการ</strong>
  <p>เริ่มจัดการงานค้างตามลำดับด้านล่าง หากส่งไม่ทันควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่</p>
</div>
{% endif %}
{% if soon_count > 1 %}
<p class="deadline-insight">◷ มีงานหลายชิ้นใกล้ถึงกำหนด แบ่งเวลาวันนี้ก่อนเริ่มงานอื่น</p>
{% endif %}

<section aria-labelledby="today-heading">
  <div class="deadline-section-head">
    <div><span class="deadline-eyebrow">ก้าวแรกของวันนี้</span><h2 id="today-heading">งานที่ควรเริ่มวันนี้</h2><p class="note">แบ่งเวลาเพิ่มรวมไม่เกิน {{ today_remaining }} ชั่วโมง หลังหักเวลาทำจริงที่บันทึกวันนี้แล้ว</p></div>
  </div>
  <div class="deadline-today-grid">
    {% for item in recommendations %}
    <article class="panel deadline-today-card">
      <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
      <h3>{{ item.title }}</h3>
      <span class="badge {{ item.deadline_tone }}"><span aria-hidden="true">{{ item.deadline_icon }}</span> {{ item.deadline_label }}</span>
      <p class="deadline-today-time">วันนี้แบ่งให้ <strong>{{ "{:,.1f}".format(item.today_hours) }}</strong> ชั่วโมง</p>
      <ul class="deadline-reasons">{% for reason in item.reasons %}<li>{{ reason }}</li>{% endfor %}</ul>
      {{ quick_actions(item, 'page1') }}
    </article>
    {% else %}
    <div class="empty">{% if open_count and today_remaining == 0 %}บันทึกเวลาทำจริงครบเวลาว่างวันนี้แล้ว ✓ ยังมีงานค้าง {{ open_count }} รายการ ตรวจหน้าแผนเพื่อจัดเวลาวันถัดไป{% else %}ยังไม่มีงานค้างที่ต้องทำวันนี้ เพิ่มงานใหม่หรือพักเมื่อทำเสร็จครบแล้ว{% endif %}</div>
    {% endfor %}
  </div>
</section>

<div class="deadline-section-head">
  <div><h2>งานค้างตามความเร่งด่วน</h2><p class="note">สถานะการทำงานและกำหนดส่งมีทั้งไอคอน ข้อความ และสี</p></div>
  <div class="deadline-reminder-control">
    <button id="enable-reminders" class="btn ghost" type="button">🔔 เปิดการแจ้งเตือน</button>
    <span id="reminder-status" class="note" aria-live="polite"></span>
  </div>
</div>
<p class="deadline-refresh-notice" id="reminder-refresh" hidden>ข้อมูลมีการเปลี่ยนแปลง <a href="{{ url_for('page', name='page1') }}">โหลดภาพรวมใหม่</a></p>
{% if stale_count %}<p class="note">↻ มี {{ stale_count }} งานที่ยังไม่มีบันทึกความคืบหน้า หรือไม่ได้อัปเดตตั้งแต่ 2 วันขึ้นไป</p>{% endif %}
<div class="deadline-task-list">
  {% for item in items %}
    {{ task_card(item, 'page1') }}
  {% else %}
    <div class="empty">ไม่มีงานค้างแล้ว ✓</div>
  {% endfor %}
</div>

<section class="deadline-completed-section" aria-labelledby="completed-heading">
  <h2 id="completed-heading">✓ งานที่เสร็จแล้ว <small class="muted">({{ completed_count }})</small></h2>
  <div class="deadline-task-list">
    {% for item in completed %}
      {{ task_card(item, 'page1') }}
    {% else %}
      <p class="note">งานที่ทำเครื่องหมายว่าเสร็จแล้วจะอยู่ในหมวดนี้</p>
    {% endfor %}
  </div>
</section>
<p class="note deadline-footnote">การแจ้งเตือนทำงานขณะเปิดหน้าภาพรวม หากต้องการเตือนภายหลัง ให้ดาวน์โหลดไฟล์จาก “เพิ่มลงปฏิทิน” แล้วนำเข้าแอปปฏิทิน</p>
<script id="reminder-data" type="application/json">{{ reminder_tasks|tojson }}</script>
{% endblock %}
{% block scripts %}<script src="{{ url_for('static', filename='js/reminders.js') }}" defer></script>{% endblock %}
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```html
{% extends "base.html" %}
```

- ใช้โครงแม่ base.html: `extends "base.html"`

### L2

```html
{% from "_task_card.html" import task_card, quick_actions %}
```

- นำเข้า macro ย่อย: `from "_task_card.html" import task_card, quick_actions`

### L3

```html
{% block content %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block content`

### L4

```html
<section class="deadline-hero deadline-overview-hero">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-hero deadline-overview-hero`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L5

```html
  <div>
```

- เปิด `<div>`: กลุ่ม layout

### L6

```html
    <span class="deadline-eyebrow">DEADLINE COMPASS · วันนี้</span>
```

- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `DEADLINE COMPASS · วันนี้`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L7

```html
    <h1>เริ่มจากงานสำคัญ แล้วค่อยไปต่อ</h1>
```

- เปิด `<h1>`: หัวข้อหลักหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เริ่มจากงานสำคัญ แล้วค่อยไปต่อ`
- ปิด `</h1>` ที่เปิดไว้ก่อนหน้า

### L8

```html
    <p>เวลาว่าง {{ daily_hours }} ชั่วโมง/วัน · วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง · เหลือแบ่ง {{ today_remaining }} ชั่วโมง</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `actual_today`
- แสดงค่าจาก context/นิพจน์ Jinja: `today_remaining`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาว่าง {{ daily_hours }} ชั่วโมง/วัน · วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง · เหลือแบ่ง {{ today_remaining }} ชั่วโมง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L9

```html
    <a class="btn" href="{{ url_for('page', name='page2') }}">+ เพิ่มงาน</a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- เปิด `<a>`: ลิงก์
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page2') }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `+ เพิ่มงาน`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L10

```html
    <a class="btn ghost" href="{{ url_for('page', name='page3') }}">ปรับเวลาว่างและดูแผน →</a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page3')`
- เปิด `<a>`: ลิงก์
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page3') }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ปรับเวลาว่างและดูแผน →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L11

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L12

```html
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>GO</span></div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-hero-mark`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `GO`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L13

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L14

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L15

```html
<div class="stat-grid deadline-summary">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`stat-grid deadline-summary`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L16

```html
  <div class="stat"><div class="label">งานค้าง</div><div class="value">{{ open_count }}</div><div class="unit">รายการ</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `open_count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานค้าง`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รายการ`

### L17

```html
  <div class="stat gold"><div class="label">ส่งวันนี้ถึงอีก 3 วัน</div><div class="value">{{ soon_count }}</div><div class="unit">รายการ</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `soon_count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat gold`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ส่งวันนี้ถึงอีก 3 วัน`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รายการ`

### L18

```html
  <div class="stat"><div class="label">เวลาที่ยังต้องใช้</div><div class="value">{{ "{:,.1f}".format(remaining_total) }}</div><div class="unit">ชั่วโมง</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(remaining_total)`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาที่ยังต้องใช้`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมง`

### L19

```html
  <div class="stat good"><div class="label">เสร็จแล้ว</div><div class="value">{{ completed_count }}</div><div class="unit">รายการ</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `completed_count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat good`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เสร็จแล้ว`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รายการ`

### L20

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L21

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L22

```html
{% if overdue_count %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if overdue_count`

### L23

```html
<div class="deadline-alert" role="status">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-alert`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`status`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง

### L24

```html
  <strong>! มีงานเกินกำหนด {{ overdue_count }} รายการ</strong>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `overdue_count`
- เปิด `<strong>`: ข้อความที่เน้น
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `! มีงานเกินกำหนด {{ overdue_count }} รายการ`
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า

### L25

```html
  <p>เริ่มจัดการงานค้างตามลำดับด้านล่าง หากส่งไม่ทันควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เริ่มจัดการงานค้างตามลำดับด้านล่าง หากส่งไม่ทันควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L26

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L27

```html
{% endif %}
```

- จบเงื่อนไข: `endif`

### L28

```html
{% if soon_count > 1 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if soon_count > 1`

### L29

```html
<p class="deadline-insight">◷ มีงานหลายชิ้นใกล้ถึงกำหนด แบ่งเวลาวันนี้ก่อนเริ่มงานอื่น</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-insight`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `◷ มีงานหลายชิ้นใกล้ถึงกำหนด แบ่งเวลาวันนี้ก่อนเริ่มงานอื่น`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L30

```html
{% endif %}
```

- จบเงื่อนไข: `endif`

### L31

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L32

```html
<section aria-labelledby="today-heading">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `aria-labelledby`=`today-heading`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L33

```html
  <div class="deadline-section-head">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-section-head`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L34

```html
    <div><span class="deadline-eyebrow">ก้าวแรกของวันนี้</span><h2 id="today-heading">งานที่ควรเริ่มวันนี้</h2><p class="note">แบ่งเวลาเพิ่มรวมไม่เกิน {{ today_remaining }} ชั่วโมง หลังหักเวลาทำจริงที่บันทึกวันนี้แล้ว</p></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `today_remaining`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ก้าวแรกของวันนี้`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h2>`: หัวข้อส่วน
- `id`=`today-heading`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานที่ควรเริ่มวันนี้`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `แบ่งเวลาเพิ่มรวมไม่เกิน {{ today_remaining }} ชั่วโมง หลังหักเวลาทำจริงที่บันทึกวันนี้แล้ว`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L35

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L36

```html
  <div class="deadline-today-grid">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-today-grid`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L37

```html
    {% for item in recommendations %}
```

- วน list จาก context: `for item in recommendations`

### L38

```html
    <article class="panel deadline-today-card">
```

- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`panel deadline-today-card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L39

```html
      <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.priority_label`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-course`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L40

```html
      <h3>{{ item.title }}</h3>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- เปิด `<h3>`: หัวข้องาน/การ์ด
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า

### L41

```html
      <span class="badge {{ item.deadline_tone }}"><span aria-hidden="true">{{ item.deadline_icon }}</span> {{ item.deadline_label }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_label`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ item.deadline_tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L42

```html
      <p class="deadline-today-time">วันนี้แบ่งให้ <strong>{{ "{:,.1f}".format(item.today_hours) }}</strong> ชั่วโมง</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(item.today_hours)`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-today-time`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันนี้แบ่งให้`
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L43

```html
      <ul class="deadline-reasons">{% for reason in item.reasons %}<li>{{ reason }}</li>{% endfor %}</ul>
```

- วน list จาก context: `for reason in item.reasons`
- แสดงค่าจาก context/นิพจน์ Jinja: `reason`
- จบ for: `endfor`
- เปิด `<ul>`: รายการแบบไม่มีเลข
- `class`=`deadline-reasons`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<li>`: สมาชิกในรายการ
- ปิด `</li>` ที่เปิดไว้ก่อนหน้า
- ปิด `</ul>` ที่เปิดไว้ก่อนหน้า

### L44

```html
      {{ quick_actions(item, 'page1') }}
```

- เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: `quick_actions(item, 'page1')`

### L45

```html
    </article>
```

- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L46

```html
    {% else %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`

### L47

```html
    <div class="empty">{% if open_count and today_remaining == 0 %}บันทึกเวลาทำจริงครบเวลาว่างวันนี้แล้ว ✓ ยังมีงานค้าง {{ open_count }} รายการ ตรวจหน้าแผนเพื่อจัดเวลาวันถัดไป{% else %}ยังไม่มีงานค้างที่ต้องทำวันนี้ เพิ่มงานใหม่หรือพักเมื่อทำเสร็จครบแล้ว{% endif %}</div>
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if open_count and today_remaining == 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `open_count`
- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบเงื่อนไข: `endif`
- เปิด `<div>`: กลุ่ม layout
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L48

```html
    {% endfor %}
```

- จบ for: `endfor`

### L49

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L50

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L51

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L52

```html
<div class="deadline-section-head">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-section-head`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L53

```html
  <div><h2>งานค้างตามความเร่งด่วน</h2><p class="note">สถานะการทำงานและกำหนดส่งมีทั้งไอคอน ข้อความ และสี</p></div>
```

- เปิด `<div>`: กลุ่ม layout
- เปิด `<h2>`: หัวข้อส่วน
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานค้างตามความเร่งด่วน`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `สถานะการทำงานและกำหนดส่งมีทั้งไอคอน ข้อความ และสี`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L54

```html
  <div class="deadline-reminder-control">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-reminder-control`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L55

```html
    <button id="enable-reminders" class="btn ghost" type="button">🔔 เปิดการแจ้งเตือน</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `id`=`enable-reminders`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`button`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `🔔 เปิดการแจ้งเตือน`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L56

```html
    <span id="reminder-status" class="note" aria-live="polite"></span>
```

- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `id`=`reminder-status`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-live`=`polite`: ให้แจ้งข้อความที่เปลี่ยนอย่างสุภาพตามค่าที่กำหนด
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L57

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L58

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L59

```html
<p class="deadline-refresh-notice" id="reminder-refresh" hidden>ข้อมูลมีการเปลี่ยนแปลง <a href="{{ url_for('page', name='page1') }}">โหลดภาพรวมใหม่</a></p>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page1')`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-refresh-notice`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `id`=`reminder-refresh`: ชื่อเฉพาะ DOM/anchor/label
- `hidden`: ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ข้อมูลมีการเปลี่ยนแปลง`
- เปิด `<a>`: ลิงก์
- `href`=`{{ url_for('page', name='page1') }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `โหลดภาพรวมใหม่`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L60

```html
{% if stale_count %}<p class="note">↻ มี {{ stale_count }} งานที่ยังไม่มีบันทึกความคืบหน้า หรือไม่ได้อัปเดตตั้งแต่ 2 วันขึ้นไป</p>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if stale_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `stale_count`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `↻ มี {{ stale_count }} งานที่ยังไม่มีบันทึกความคืบหน้า หรือไม่ได้อัปเดตตั้งแต่ 2 วันขึ้นไป`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L61

```html
<div class="deadline-task-list">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-list`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L62

```html
  {% for item in items %}
```

- วน list จาก context: `for item in items`

### L63

```html
    {{ task_card(item, 'page1') }}
```

- เรียก macro การ์ดงานร่วม: `task_card(item, 'page1')`

### L64

```html
  {% else %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`

### L65

```html
    <div class="empty">ไม่มีงานค้างแล้ว ✓</div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ไม่มีงานค้างแล้ว ✓`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L66

```html
  {% endfor %}
```

- จบ for: `endfor`

### L67

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L68

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L69

```html
<section class="deadline-completed-section" aria-labelledby="completed-heading">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-completed-section`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-labelledby`=`completed-heading`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L70

```html
  <h2 id="completed-heading">✓ งานที่เสร็จแล้ว <small class="muted">({{ completed_count }})</small></h2>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `completed_count`
- เปิด `<h2>`: หัวข้อส่วน
- `id`=`completed-heading`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ งานที่เสร็จแล้ว`
- เปิด `<small>`: ข้อความประกอบ
- `class`=`muted`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `({{ completed_count }})`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า

### L71

```html
  <div class="deadline-task-list">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-list`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L72

```html
    {% for item in completed %}
```

- วน list จาก context: `for item in completed`

### L73

```html
      {{ task_card(item, 'page1') }}
```

- เรียก macro การ์ดงานร่วม: `task_card(item, 'page1')`

### L74

```html
    {% else %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`

### L75

```html
      <p class="note">งานที่ทำเครื่องหมายว่าเสร็จแล้วจะอยู่ในหมวดนี้</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานที่ทำเครื่องหมายว่าเสร็จแล้วจะอยู่ในหมวดนี้`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L76

```html
    {% endfor %}
```

- จบ for: `endfor`

### L77

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L78

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L79

```html
<p class="note deadline-footnote">การแจ้งเตือนทำงานขณะเปิดหน้าภาพรวม หากต้องการเตือนภายหลัง ให้ดาวน์โหลดไฟล์จาก “เพิ่มลงปฏิทิน” แล้วนำเข้าแอปปฏิทิน</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note deadline-footnote`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `การแจ้งเตือนทำงานขณะเปิดหน้าภาพรวม หากต้องการเตือนภายหลัง ให้ดาวน์โหลดไฟล์จาก “เพิ่มลงปฏิทิน” แล้วนำเข้าแอปปฏิทิน`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L80

```html
<script id="reminder-data" type="application/json">{{ reminder_tasks|tojson }}</script>
```

- serialize ข้อมูลเป็น JSON สำหรับ script data: `reminder_tasks|tojson`
- เปิด `<script>`: script/JSON ตาม type
- `id`=`reminder-data`: ชื่อเฉพาะ DOM/anchor/label
- `type`=`application/json`: ชนิดช่องหรือปุ่ม
- ปิด `</script>` ที่เปิดไว้ก่อนหน้า

### L81

```html
{% endblock %}
```

- จบ block content/scripts: `endblock`

### L82

```html
{% block scripts %}<script src="{{ url_for('static', filename='js/reminders.js') }}" defer></script>{% endblock %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block scripts`
- สร้าง URL ผ่าน route เดิม: `url_for('static', filename='js/reminders.js')`
- จบ block content/scripts: `endblock`
- เปิด `<script>`: script/JSON ตาม type
- `src`=`{{ url_for('static', filename='js/reminders.js') }}`: ไฟล์ script ที่โหลด
- `defer`: รัน script ภายนอกหลังแยก HTML เสร็จ
- ปิด `</script>` ที่เปิดไว้ก่อนหน้า
