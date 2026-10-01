# templates/page3.html — HTML/Jinja ของ Plan

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 55 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `16565dde747686bc4a663447c945273e084967e32bf806027bec3034b7646755`

**ผู้ศึกษา/บทบาท:** นายธีรเดช ฤทธิ์คำรพ · Page 3

## 1. หน้าที่และการเชื่อมต่อ

ทำให้ผู้ใช้เทียบเวลาที่ต้องทำ มีจริง และขาดได้โดยไม่คำนวณเอง

- **รับเข้า:** tasks, focus, required_daily, daily_shortfall, daily_hours และสถิติจาก page3.build
- **ผลลัพธ์:** แบบบันทึกเวลาว่าง สรุปความเสี่ยง และการ์ดแผนตามวันส่ง

**เกี่ยวข้องกับ:** base.html; _task_card.html: quick_actions; pages/page3.py; static/style.css

## 2. ลำดับทำงาน

1. POST save_hours ไป /page3 ชัดเจน
2. แสดงสถิติและคำแนะนำจาก daily_shortfall
3. แสดง focus พร้อมปุ่มเริ่ม/ปิด
4. วน tasks และแยกกำหนดยังไม่ผ่านกับเกินกำหนด
5. แสดง 3 ตัวเลขต่อวันและข้อมูลสะสม/ความจุ/ขาดรวม
6. อธิบายสมมติฐานรวมวันนี้และหักชั่วโมงจริงแล้ว

## 3. จุดที่ต้องอธิบายให้ถูก

- Jinja ใช้ตัวเลขที่ Python คำนวณ ไม่เขียนสูตรภาระสะสมใหม่ใน template
- focus อาจมี today_hours=0 หากงบวันนี้หมด ต้องอ่านงบร่วม
- ค่าเฉลี่ยสรุปอนาคตไม่ใช่คำแนะนำให้ทำเกินเวลาว่างโดยอัตโนมัติ

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- อธิบายว่าไฟล์นี้เป็นข้อมูล/เครื่องมือประกอบอะไร และถูกอ่านที่ใด

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% extends "base.html" %}
{% from "_task_card.html" import quick_actions %}
{% block content %}
<div class="deadline-page-title"><span class="deadline-eyebrow">วางแผนก่อนวันส่ง</span><h1>เห็นเวลาที่ขาด แล้วปรับแผนให้ทัน</h1><p class="lead">รวมงานที่ต้องเสร็จภายในแต่ละวัน และเปรียบเทียบกับเวลาว่างจริงของคุณ</p></div>
<form method="post" action="{{ url_for('page', name='page3') }}" class="panel deadline-hours-form">
  <input type="hidden" name="action" value="save_hours">
  <div class="field"><label for="daily-hours">มีเวลาว่างจริงวันละกี่ชั่วโมง</label><input id="daily-hours" name="hours" type="number" min="0.1" max="12" step="0.1" value="{{ daily_hours }}" aria-describedby="daily-help" required><small id="daily-help" class="deadline-help">เช่น 4 ชั่วโมง · บันทึกแล้วใช้ร่วมกับหน้าภาพรวม</small></div>
  <button class="btn" type="submit">บันทึกและคำนวณแผน</button>
</form>
<div class="stat-grid deadline-summary">
  <div class="stat {{ 'bad' if risk_count else 'good' }}"><div class="label">งานที่เสี่ยงไม่ทัน</div><div class="value">{{ risk_count }}</div><div class="unit">จาก {{ open_count }} งานค้าง</div></div>
  <div class="stat"><div class="label">ต้องทำเฉลี่ยอย่างน้อย</div><div class="value">{{ required_daily }}</div><div class="unit">ชั่วโมง/วัน ถึงกำหนดงานในอนาคต</div></div>
  <div class="stat gold"><div class="label">มีเวลาว่างจริง</div><div class="value">{{ daily_hours }}</div><div class="unit">ชั่วโมง/วัน</div></div>
</div>
{% if daily_shortfall > 0 %}
<div class="deadline-alert" role="status"><strong>! ต้องทำประมาณ {{ required_daily }} ชั่วโมง/วัน แต่มีเวลา {{ daily_hours }} ชั่วโมง/วัน</strong><p>จึงขาดอย่างน้อย {{ daily_shortfall }} ชั่วโมง/วัน ในช่วงที่แน่นที่สุด ควรแบ่งงาน ลดขอบเขต หรือปรึกษาผู้สอนเรื่องกำหนดส่ง</p></div>
{% elif tasks %}
<p class="deadline-insight">✓ เวลาสำหรับกำหนดส่งในอนาคตอยู่ในแผน{% if overdue_count %} แต่ยังมี {{ overdue_count }} งานเกินกำหนดที่ต้องจัดการ{% endif %}</p>
{% endif %}
{% if overdue_count %}<p class="deadline-insight">! งานเกินกำหนด {{ overdue_count }} รายการยังรวมในภาระสะสม ควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่</p>{% endif %}
{% if soon_count > 1 %}<p class="note">◷ มี {{ soon_count }} งานใกล้ถึงกำหนด ควรเริ่มตามลำดับในภาพรวมวันนี้</p>{% endif %}

{% if focus %}
<section class="deadline-focus" aria-label="งานที่ควรเริ่มก่อน">
  <span class="deadline-eyebrow">ควรเริ่มงานนี้ก่อน</span><strong>{{ focus.title }}</strong><span>{{ focus.course }} · {{ focus.deadline_label }} · วันนี้แบ่งให้ {{ focus.today_hours }} ชั่วโมง</span>
  <div class="deadline-focus-actions">{{ quick_actions(focus, 'page3') }}</div>
</section>
{% endif %}

<div class="deadline-section-head"><div><h2>แผนตามวันส่ง</h2><p class="note">งานวันเดียวกันใช้ภาระรวมเดียวกัน ตัวเลขเป็นการประมาณจากเวลาที่กรอก</p></div></div>
<div class="deadline-task-list">
  {% for task in tasks %}
  <article class="panel deadline-plan-card">
    <div class="deadline-edit-heading">
      <div><span class="deadline-course">{{ task.course }} · {{ task.owner_name }}</span><h3>{{ task.title }}</h3><p class="deadline-meta">ส่ง <time datetime="{{ task.due_date }}">{{ task.due_date }}</time> · งานนี้เหลือ {{ task.remaining_hours }} ชั่วโมง</p></div>
      <span class="badge {{ task.plan_tone }}"><span aria-hidden="true">{{ task.plan_icon }}</span> {{ task.plan_status }}</span>
    </div>
    <div class="deadline-badge-row"><span class="badge {{ task.tone }}">{{ task.status_icon }} {{ task.status }}</span><span class="badge {{ task.deadline_tone }}">{{ task.deadline_icon }} {{ task.deadline_label }}</span></div>
    {% if task.days_left >= 0 %}
    <div class="deadline-time-comparison">
      <div><span>ต้องทำเฉลี่ย</span><strong>{{ task.hours_per_day }} <small>ชม./วัน</small></strong></div>
      <div><span>มีเวลาว่างจริง</span><strong>{{ daily_hours }} <small>ชม./วัน</small></strong></div>
      <div class="{{ 'deadline-time-bad' if task.at_risk }}"><span>ขาดเวลาเฉลี่ย</span><strong>{{ task.shortfall_per_day }} <small>ชม./วัน</small></strong></div>
    </div>
    <p class="deadline-plan-detail">งานสะสมถึงวันส่งนี้ <strong>{{ task.cumulative_hours }} ชั่วโมง</strong> · ทำได้ <strong>{{ task.available_hours }} ชั่วโมง</strong>{% if task.gap > 0 %} · ขาดรวม <strong>{{ task.gap }} ชั่วโมง</strong>{% endif %}</p>
    {% else %}
    <p class="deadline-plan-detail"><strong>เกินกำหนด {{ -task.days_left }} วัน</strong> · ควรติดต่อผู้สอนและจัดการก่อน{% if task.today_hours > 0 %} วันนี้แบ่งให้ {{ task.today_hours }} ชั่วโมง{% else %} เวลาวันนี้ถูกแบ่งให้งานก่อนหน้าแล้ว{% endif %}</p>
    {% endif %}
    <ul class="deadline-reasons">{% for reason in task.reasons %}<li>{{ reason }}</li>{% endfor %}</ul>
    {{ quick_actions(task, 'page3') }}
  </article>
  {% else %}<div class="empty">✓ งานทั้งหมดเสร็จแล้ว หรือยังไม่ได้เพิ่มงาน</div>{% endfor %}
</div>
<p class="note deadline-footnote">วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง เหลือเวลาว่าง {{ today_remaining }} ชั่วโมง การคำนวณนับวันนี้และหักเวลาที่ใช้แล้วออกจากความจุ ส่วนค่าเฉลี่ยรวมเวลาที่ใช้ไปวันนี้ไม่เกินเวลาว่างที่ตั้งไว้ สมมติว่ามีเวลาว่างเท่ากันทุกวันและปัดส่วนขาดขึ้นเป็นทศนิยม 1 ตำแหน่ง</p>
{% endblock %}
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
{% from "_task_card.html" import quick_actions %}
```

- นำเข้า macro ย่อย: `from "_task_card.html" import quick_actions`

### L3

```html
{% block content %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block content`

### L4

```html
<div class="deadline-page-title"><span class="deadline-eyebrow">วางแผนก่อนวันส่ง</span><h1>เห็นเวลาที่ขาด แล้วปรับแผนให้ทัน</h1><p class="lead">รวมงานที่ต้องเสร็จภายในแต่ละวัน และเปรียบเทียบกับเวลาว่างจริงของคุณ</p></div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-page-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วางแผนก่อนวันส่ง`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h1>`: หัวข้อหลักหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เห็นเวลาที่ขาด แล้วปรับแผนให้ทัน`
- ปิด `</h1>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`lead`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รวมงานที่ต้องเสร็จภายในแต่ละวัน และเปรียบเทียบกับเวลาว่างจริงของคุณ`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L5

```html
<form method="post" action="{{ url_for('page', name='page3') }}" class="panel deadline-hours-form">
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page3')`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `action`=`{{ url_for('page', name='page3') }}`: URL ปลายทาง form
- `class`=`panel deadline-hours-form`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L6

```html
  <input type="hidden" name="action" value="save_hours">
```

- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`save_hours`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L7

```html
  <div class="field"><label for="daily-hours">มีเวลาว่างจริงวันละกี่ชั่วโมง</label><input id="daily-hours" name="hours" type="number" min="0.1" max="12" step="0.1" value="{{ daily_hours }}" aria-describedby="daily-help" required><small id="daily-help" class="deadline-help">เช่น 4 ชั่วโมง · บันทึกแล้วใช้ร่วมกับหน้าภาพรวม</small></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`daily-hours`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `มีเวลาว่างจริงวันละกี่ชั่วโมง`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`daily-hours`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0.1`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`12`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `value`=`{{ daily_hours }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `aria-describedby`=`daily-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- เปิด `<small>`: ข้อความประกอบ
- `id`=`daily-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เช่น 4 ชั่วโมง · บันทึกแล้วใช้ร่วมกับหน้าภาพรวม`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L8

```html
  <button class="btn" type="submit">บันทึกและคำนวณแผน</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกและคำนวณแผน`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L9

```html
</form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L10

```html
<div class="stat-grid deadline-summary">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`stat-grid deadline-summary`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L11

```html
  <div class="stat {{ 'bad' if risk_count else 'good' }}"><div class="label">งานที่เสี่ยงไม่ทัน</div><div class="value">{{ risk_count }}</div><div class="unit">จาก {{ open_count }} งานค้าง</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `'bad' if risk_count else 'good'`
- แสดงค่าจาก context/นิพจน์ Jinja: `risk_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `open_count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat {{ 'bad' if risk_count else 'good' }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานที่เสี่ยงไม่ทัน`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `จาก {{ open_count }} งานค้าง`

### L12

```html
  <div class="stat"><div class="label">ต้องทำเฉลี่ยอย่างน้อย</div><div class="value">{{ required_daily }}</div><div class="unit">ชั่วโมง/วัน ถึงกำหนดงานในอนาคต</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `required_daily`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ต้องทำเฉลี่ยอย่างน้อย`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมง/วัน ถึงกำหนดงานในอนาคต`

### L13

```html
  <div class="stat gold"><div class="label">มีเวลาว่างจริง</div><div class="value">{{ daily_hours }}</div><div class="unit">ชั่วโมง/วัน</div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- เปิด `<div>`: กลุ่ม layout
- `class`=`stat gold`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`label`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `มีเวลาว่างจริง`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- `class`=`value`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`unit`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมง/วัน`

### L14

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L15

```html
{% if daily_shortfall > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if daily_shortfall > 0`

### L16

```html
<div class="deadline-alert" role="status"><strong>! ต้องทำประมาณ {{ required_daily }} ชั่วโมง/วัน แต่มีเวลา {{ daily_hours }} ชั่วโมง/วัน</strong><p>จึงขาดอย่างน้อย {{ daily_shortfall }} ชั่วโมง/วัน ในช่วงที่แน่นที่สุด ควรแบ่งงาน ลดขอบเขต หรือปรึกษาผู้สอนเรื่องกำหนดส่ง</p></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `required_daily`
- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `daily_shortfall`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-alert`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`status`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- เปิด `<strong>`: ข้อความที่เน้น
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `! ต้องทำประมาณ {{ required_daily }} ชั่วโมง/วัน แต่มีเวลา {{ daily_hours }} ชั่วโมง/วัน`
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `จึงขาดอย่างน้อย {{ daily_shortfall }} ชั่วโมง/วัน ในช่วงที่แน่นที่สุด ควรแบ่งงาน ลดขอบเขต หรือปรึกษาผู้สอนเรื่องกำหนดส่ง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L17

```html
{% elif tasks %}
```

- ตรวจเงื่อนไขทางเลือก: `elif tasks`

### L18

```html
<p class="deadline-insight">✓ เวลาสำหรับกำหนดส่งในอนาคตอยู่ในแผน{% if overdue_count %} แต่ยังมี {{ overdue_count }} งานเกินกำหนดที่ต้องจัดการ{% endif %}</p>
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if overdue_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `overdue_count`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-insight`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ เวลาสำหรับกำหนดส่งในอนาคตอยู่ในแผน{% if overdue_count %} แต่ยังมี {{ overdue_count }} งานเกินกำหนดที่ต้องจัดการ{% endif %}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L19

```html
{% endif %}
```

- จบเงื่อนไข: `endif`

### L20

```html
{% if overdue_count %}<p class="deadline-insight">! งานเกินกำหนด {{ overdue_count }} รายการยังรวมในภาระสะสม ควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่</p>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if overdue_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `overdue_count`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-insight`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `! งานเกินกำหนด {{ overdue_count }} รายการยังรวมในภาระสะสม ควรติดต่อผู้สอนเพื่อยืนยันวันส่งใหม่`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L21

```html
{% if soon_count > 1 %}<p class="note">◷ มี {{ soon_count }} งานใกล้ถึงกำหนด ควรเริ่มตามลำดับในภาพรวมวันนี้</p>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if soon_count > 1`
- แสดงค่าจาก context/นิพจน์ Jinja: `soon_count`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `◷ มี {{ soon_count }} งานใกล้ถึงกำหนด ควรเริ่มตามลำดับในภาพรวมวันนี้`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L22

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L23

```html
{% if focus %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if focus`

### L24

```html
<section class="deadline-focus" aria-label="งานที่ควรเริ่มก่อน">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-focus`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-label`=`งานที่ควรเริ่มก่อน`: คำอธิบายสำหรับเครื่องมืออ่านหน้าจอ

### L25

```html
  <span class="deadline-eyebrow">ควรเริ่มงานนี้ก่อน</span><strong>{{ focus.title }}</strong><span>{{ focus.course }} · {{ focus.deadline_label }} · วันนี้แบ่งให้ {{ focus.today_hours }} ชั่วโมง</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `focus.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `focus.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `focus.deadline_label`
- แสดงค่าจาก context/นิพจน์ Jinja: `focus.today_hours`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ควรเริ่มงานนี้ก่อน`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า

### L26

```html
  <div class="deadline-focus-actions">{{ quick_actions(focus, 'page3') }}</div>
```

- เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: `quick_actions(focus, 'page3')`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-focus-actions`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L27

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L28

```html
{% endif %}
```

- จบเงื่อนไข: `endif`

### L29

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L30

```html
<div class="deadline-section-head"><div><h2>แผนตามวันส่ง</h2><p class="note">งานวันเดียวกันใช้ภาระรวมเดียวกัน ตัวเลขเป็นการประมาณจากเวลาที่กรอก</p></div></div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-section-head`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<h2>`: หัวข้อส่วน
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `แผนตามวันส่ง`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานวันเดียวกันใช้ภาระรวมเดียวกัน ตัวเลขเป็นการประมาณจากเวลาที่กรอก`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L31

```html
<div class="deadline-task-list">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-list`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L32

```html
  {% for task in tasks %}
```

- วน list จาก context: `for task in tasks`

### L33

```html
  <article class="panel deadline-plan-card">
```

- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`panel deadline-plan-card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L34

```html
    <div class="deadline-edit-heading">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-edit-heading`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L35

```html
      <div><span class="deadline-course">{{ task.course }} · {{ task.owner_name }}</span><h3>{{ task.title }}</h3><p class="deadline-meta">ส่ง <time datetime="{{ task.due_date }}">{{ task.due_date }}</time> · งานนี้เหลือ {{ task.remaining_hours }} ชั่วโมง</p></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.owner_name`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.due_date`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.remaining_hours`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-course`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h3>`: หัวข้องาน/การ์ด
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-meta`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ส่ง`
- เปิด `<time>`: ข้อมูลวันที่ที่มีความหมาย
- `datetime`=`{{ task.due_date }}`: วันที่มาตรฐานของ time
- ปิด `</time>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `· งานนี้เหลือ {{ task.remaining_hours }} ชั่วโมง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L36

```html
      <span class="badge {{ task.plan_tone }}"><span aria-hidden="true">{{ task.plan_icon }}</span> {{ task.plan_status }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.plan_tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.plan_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.plan_status`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ task.plan_tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L37

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L38

```html
    <div class="deadline-badge-row"><span class="badge {{ task.tone }}">{{ task.status_icon }} {{ task.status }}</span><span class="badge {{ task.deadline_tone }}">{{ task.deadline_icon }} {{ task.deadline_label }}</span></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.status_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.status`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.deadline_tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.deadline_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.deadline_label`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-badge-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ task.tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- `class`=`badge {{ task.deadline_tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L39

```html
    {% if task.days_left >= 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if task.days_left >= 0`

### L40

```html
    <div class="deadline-time-comparison">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-time-comparison`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L41

```html
      <div><span>ต้องทำเฉลี่ย</span><strong>{{ task.hours_per_day }} <small>ชม./วัน</small></strong></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.hours_per_day`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ต้องทำเฉลี่ย`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<strong>`: ข้อความที่เน้น
- เปิด `<small>`: ข้อความประกอบ
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชม./วัน`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L42

```html
      <div><span>มีเวลาว่างจริง</span><strong>{{ daily_hours }} <small>ชม./วัน</small></strong></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `มีเวลาว่างจริง`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<strong>`: ข้อความที่เน้น
- เปิด `<small>`: ข้อความประกอบ
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชม./วัน`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L43

```html
      <div class="{{ 'deadline-time-bad' if task.at_risk }}"><span>ขาดเวลาเฉลี่ย</span><strong>{{ task.shortfall_per_day }} <small>ชม./วัน</small></strong></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `'deadline-time-bad' if task.at_risk`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.shortfall_per_day`
- เปิด `<div>`: กลุ่ม layout
- `class`=`{{ 'deadline-time-bad' if task.at_risk }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ขาดเวลาเฉลี่ย`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<strong>`: ข้อความที่เน้น
- เปิด `<small>`: ข้อความประกอบ
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชม./วัน`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L44

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L45

```html
    <p class="deadline-plan-detail">งานสะสมถึงวันส่งนี้ <strong>{{ task.cumulative_hours }} ชั่วโมง</strong> · ทำได้ <strong>{{ task.available_hours }} ชั่วโมง</strong>{% if task.gap > 0 %} · ขาดรวม <strong>{{ task.gap }} ชั่วโมง</strong>{% endif %}</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.cumulative_hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.available_hours`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if task.gap > 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.gap`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-plan-detail`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานสะสมถึงวันส่งนี้`
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `· ทำได้`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L46

```html
    {% else %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`

### L47

```html
    <p class="deadline-plan-detail"><strong>เกินกำหนด {{ -task.days_left }} วัน</strong> · ควรติดต่อผู้สอนและจัดการก่อน{% if task.today_hours > 0 %} วันนี้แบ่งให้ {{ task.today_hours }} ชั่วโมง{% else %} เวลาวันนี้ถูกแบ่งให้งานก่อนหน้าแล้ว{% endif %}</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `-task.days_left`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if task.today_hours > 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.today_hours`
- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-plan-detail`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<strong>`: ข้อความที่เน้น
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เกินกำหนด {{ -task.days_left }} วัน`
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `· ควรติดต่อผู้สอนและจัดการก่อน{% if task.today_hours > 0 %} วันนี้แบ่งให้ {{ task.today_hours }} ชั่วโมง{% else %} เวลาวันนี้ถูกแบ่งให้งานก่อนหน้าแล้ว{% endif %}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L48

```html
    {% endif %}
```

- จบเงื่อนไข: `endif`

### L49

```html
    <ul class="deadline-reasons">{% for reason in task.reasons %}<li>{{ reason }}</li>{% endfor %}</ul>
```

- วน list จาก context: `for reason in task.reasons`
- แสดงค่าจาก context/นิพจน์ Jinja: `reason`
- จบ for: `endfor`
- เปิด `<ul>`: รายการแบบไม่มีเลข
- `class`=`deadline-reasons`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<li>`: สมาชิกในรายการ
- ปิด `</li>` ที่เปิดไว้ก่อนหน้า
- ปิด `</ul>` ที่เปิดไว้ก่อนหน้า

### L50

```html
    {{ quick_actions(task, 'page3') }}
```

- เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: `quick_actions(task, 'page3')`

### L51

```html
  </article>
```

- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L52

```html
  {% else %}<div class="empty">✓ งานทั้งหมดเสร็จแล้ว หรือยังไม่ได้เพิ่มงาน</div>{% endfor %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบ for: `endfor`
- เปิด `<div>`: กลุ่ม layout
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ งานทั้งหมดเสร็จแล้ว หรือยังไม่ได้เพิ่มงาน`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L53

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L54

```html
<p class="note deadline-footnote">วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง เหลือเวลาว่าง {{ today_remaining }} ชั่วโมง การคำนวณนับวันนี้และหักเวลาที่ใช้แล้วออกจากความจุ ส่วนค่าเฉลี่ยรวมเวลาที่ใช้ไปวันนี้ไม่เกินเวลาว่างที่ตั้งไว้ สมมติว่ามีเวลาว่างเท่ากันทุกวันและปัดส่วนขาดขึ้นเป็นทศนิยม 1 ตำแหน่ง</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `actual_today`
- แสดงค่าจาก context/นิพจน์ Jinja: `today_remaining`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note deadline-footnote`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันนี้บันทึกเวลาทำจริงแล้ว {{ actual_today }} ชั่วโมง เหลือเวลาว่าง {{ today_remaining }} ชั่วโมง การคำนวณนับวันนี้และหักเวลาที่ใช้แล้วออกจากความจุ ส่วนค่าเฉลี่ยรวมเวลาที่ใช้ไปวันนี้ไม่เกินเวลาว่างที่ตั้งไว้ สมมติว่ามีเวลาว่างเท่ากันทุกวันและปัดส่วนขาดขึ้นเป็นทศนิยม 1 ตำแหน่ง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L55

```html
{% endblock %}
```

- จบ block content/scripts: `endblock`
