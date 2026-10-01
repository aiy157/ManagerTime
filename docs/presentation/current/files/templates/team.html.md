# templates/team.html — HTML/Jinja ของ Team

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 38 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `65c0629dd1dce44dfa6582a8dd8c70dc77c99e8107cbef10d882dc1489a0bba1`

**ผู้ศึกษา/บทบาท:** ทีม CodeMind

## 1. หน้าที่และการเชื่อมต่อ

แสดงสมาชิกตามข้อมูลจริงพร้อมจำนวนงาน ความคืบหน้า และสิ่งที่ต้องช่วยแบ่ง

- **รับเข้า:** group, members, count, unassigned, daily_hours, weekly_capacity
- **ผลลัพธ์:** การ์ดสมาชิกและรายการงานที่ยังไม่มอบหมาย

**เกี่ยวข้องกับ:** pages/team.py; base.html; static/style.css; ลิงก์ไป page2#task-no

## 2. ลำดับทำงาน

1. แสดงชื่อกลุ่มและอธิบายเกณฑ์ภาระ
2. วนสมาชิกพร้อม role/task ตามรายวิชา
3. แสดงสถิติ progress และป้ายช่วยแบ่งงาน
4. details แสดงงานที่แต่ละคนรับผิดชอบ
5. วน unassigned พร้อมปุ่มมอบหมายไป Manage

## 3. จุดที่ต้องอธิบายให้ถูก

- ปุ่มมอบหมายเป็นทางลัด ไม่บันทึกผู้รับผิดชอบทันที
- บทบาทในรายวิชาจาก team.json ต่างจาก owner ของงานแต่ละชิ้น
- progressbar ใช้ตัวเลข 0–100 ที่ Python เตรียมแล้ว

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q089: อะไรทำให้ขึ้นควรช่วยแบ่งงาน?](../../TEACHER_QUESTIONS.md#q089)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% extends "base.html" %}
{% block content %}
<div class="deadline-page-title"><span class="deadline-eyebrow">ทีมและภาระงาน</span><h1>{{ group.name }} <small class="muted">· {{ group.section }}</small></h1><p class="lead">{{ group.topic }} — {{ group.description }}</p></div>
<div class="deadline-insight">ดูความคืบหน้าตามชั่วโมงของแต่ละคน และมอบหมายงานจากหน้าจัดการงาน <a href="{{ url_for('page', name='page2') }}">จัดผู้รับผิดชอบ →</a></div>
<p class="note">ใช้เวลาว่าง {{ daily_hours }} ชั่วโมง/วันเป็นเกณฑ์เดียวกันสำหรับสมาชิกทุกคน เกณฑ์ให้ช่วยแบ่งงาน: มีงานเสี่ยงตามกำหนด หรือชั่วโมงค้างมากกว่า {{ weekly_capacity }} ชั่วโมงใน 7 วัน</p>
<h2>สมาชิก {{ count }} คน</h2>
<div class="member-grid deadline-member-grid">
  {% for member in members %}
  <article class="member deadline-member">
    <div class="avatar" aria-hidden="true">{{ member.initial }}</div>
    <h3 class="member-name">{{ member.name }}</h3><div class="muted">{{ member.id }}</div>
    <div class="role">{{ member.role }}</div><p class="task">หน้าที่รายวิชา: {{ member.task }}</p>
    <div class="deadline-member-stats">
      <div><strong>{{ member.assignment_count }}</strong><span>งานทั้งหมด</span></div>
      <div><strong>{{ member.open_count }}</strong><span>งานค้าง</span></div>
      <div><strong>{{ member.remaining_hours }}</strong><span>ชม.ที่เหลือ</span></div>
    </div>
    <div class="progress deadline-progress" role="progressbar" aria-label="ความคืบหน้า {{ member.name }}" aria-valuenow="{{ member.progress }}" aria-valuemin="0" aria-valuemax="100"><div style="width: {{ member.progress }}%"></div></div>
    <p class="note">ความคืบหน้า {{ member.progress }}% ตามชั่วโมงทั้งหมด</p>
    {% if member.overloaded %}<p class="deadline-member-warning">! ควรช่วยแบ่งงาน{% if member.risk_count %} · มี {{ member.risk_count }} งานเสี่ยง{% endif %}</p>
    {% elif member.open_count %}<span class="badge good">✓ ภาระงานอยู่ในเกณฑ์</span>
    {% else %}<span class="badge">○ ไม่มีงานค้างที่มอบหมาย</span>{% endif %}
    <details><summary>งานที่รับผิดชอบ ({{ member.assignment_count }})</summary><ul class="deadline-member-tasks">
      {% for task in member.assignments %}<li><a href="{{ url_for('page', name='page2') }}#task-{{ task.no }}">{{ task.title }}</a><small>{{ task.status_icon }} {{ task.status }} · {{ task.progress }}%</small></li>
      {% else %}<li class="note">ยังไม่มีงานที่มอบหมาย</li>{% endfor %}
    </ul></details>
  </article>
  {% endfor %}
</div>
<section aria-labelledby="unassigned-heading">
  <h2 id="unassigned-heading">○ งานที่ยังไม่มีผู้รับผิดชอบ ({{ unassigned|length }})</h2>
  <div class="deadline-task-list">
    {% for task in unassigned %}
    <article class="deadline-task"><div class="deadline-task-main"><span class="deadline-course">{{ task.course }}</span><h3>{{ task.title }}</h3><p class="deadline-meta">ส่ง {{ task.due_date }} · เหลือ {{ task.remaining_hours }} ชั่วโมง</p></div><a class="btn ghost" href="{{ url_for('page', name='page2') }}#task-{{ task.no }}">มอบหมายงาน →</a></article>
    {% else %}<p class="empty">✓ งานค้างทุกชิ้นมีผู้รับผิดชอบแล้ว</p>{% endfor %}
  </div>
</section>
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
{% block content %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block content`

### L3

```html
<div class="deadline-page-title"><span class="deadline-eyebrow">ทีมและภาระงาน</span><h1>{{ group.name }} <small class="muted">· {{ group.section }}</small></h1><p class="lead">{{ group.topic }} — {{ group.description }}</p></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `group.name`
- แสดงค่าจาก context/นิพจน์ Jinja: `group.section`
- แสดงค่าจาก context/นิพจน์ Jinja: `group.topic`
- แสดงค่าจาก context/นิพจน์ Jinja: `group.description`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-page-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ทีมและภาระงาน`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h1>`: หัวข้อหลักหน้า
- เปิด `<small>`: ข้อความประกอบ
- `class`=`muted`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `· {{ group.section }}`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</h1>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`lead`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L4

```html
<div class="deadline-insight">ดูความคืบหน้าตามชั่วโมงของแต่ละคน และมอบหมายงานจากหน้าจัดการงาน <a href="{{ url_for('page', name='page2') }}">จัดผู้รับผิดชอบ →</a></div>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-insight`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ดูความคืบหน้าตามชั่วโมงของแต่ละคน และมอบหมายงานจากหน้าจัดการงาน`
- เปิด `<a>`: ลิงก์
- `href`=`{{ url_for('page', name='page2') }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `จัดผู้รับผิดชอบ →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L5

```html
<p class="note">ใช้เวลาว่าง {{ daily_hours }} ชั่วโมง/วันเป็นเกณฑ์เดียวกันสำหรับสมาชิกทุกคน เกณฑ์ให้ช่วยแบ่งงาน: มีงานเสี่ยงตามกำหนด หรือชั่วโมงค้างมากกว่า {{ weekly_capacity }} ชั่วโมงใน 7 วัน</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `daily_hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `weekly_capacity`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ใช้เวลาว่าง {{ daily_hours }} ชั่วโมง/วันเป็นเกณฑ์เดียวกันสำหรับสมาชิกทุกคน เกณฑ์ให้ช่วยแบ่งงาน: มีงานเสี่ยงตามกำหนด หรือชั่วโมงค้างมากกว่า {{ weekly_capacity }} ชั่วโมงใน 7 วัน`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L6

```html
<h2>สมาชิก {{ count }} คน</h2>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `count`
- เปิด `<h2>`: หัวข้อส่วน
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `สมาชิก {{ count }} คน`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า

### L7

```html
<div class="member-grid deadline-member-grid">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`member-grid deadline-member-grid`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L8

```html
  {% for member in members %}
```

- วน list จาก context: `for member in members`

### L9

```html
  <article class="member deadline-member">
```

- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`member deadline-member`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L10

```html
    <div class="avatar" aria-hidden="true">{{ member.initial }}</div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.initial`
- เปิด `<div>`: กลุ่ม layout
- `class`=`avatar`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L11

```html
    <h3 class="member-name">{{ member.name }}</h3><div class="muted">{{ member.id }}</div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.name`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.id`
- เปิด `<h3>`: หัวข้องาน/การ์ด
- `class`=`member-name`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า
- เปิด `<div>`: กลุ่ม layout
- `class`=`muted`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L12

```html
    <div class="role">{{ member.role }}</div><p class="task">หน้าที่รายวิชา: {{ member.task }}</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.role`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.task`
- เปิด `<div>`: กลุ่ม layout
- `class`=`role`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`task`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `หน้าที่รายวิชา: {{ member.task }}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L13

```html
    <div class="deadline-member-stats">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-member-stats`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L14

```html
      <div><strong>{{ member.assignment_count }}</strong><span>งานทั้งหมด</span></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.assignment_count`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานทั้งหมด`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L15

```html
      <div><strong>{{ member.open_count }}</strong><span>งานค้าง</span></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.open_count`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานค้าง`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L16

```html
      <div><strong>{{ member.remaining_hours }}</strong><span>ชม.ที่เหลือ</span></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.remaining_hours`
- เปิด `<div>`: กลุ่ม layout
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชม.ที่เหลือ`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L17

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L18

```html
    <div class="progress deadline-progress" role="progressbar" aria-label="ความคืบหน้า {{ member.name }}" aria-valuenow="{{ member.progress }}" aria-valuemin="0" aria-valuemax="100"><div style="width: {{ member.progress }}%"></div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.name`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.progress`
- เปิด `<div>`: กลุ่ม layout
- `class`=`progress deadline-progress`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`progressbar`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- `aria-label`=`ความคืบหน้า {{ member.name }}`: คำอธิบายสำหรับเครื่องมืออ่านหน้าจอ
- `aria-valuenow`=`{{ member.progress }}`: ค่าปัจจุบันของ progressbar
- `aria-valuemin`=`0`: ขอบล่าง progressbar
- `aria-valuemax`=`100`: ขอบบน progressbar
- `style`=`width: {{ member.progress }}%`: CSS เฉพาะ element; progress เป็นเปอร์เซ็นต์ที่ Python คำนวณ
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L19

```html
    <p class="note">ความคืบหน้า {{ member.progress }}% ตามชั่วโมงทั้งหมด</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.progress`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ความคืบหน้า {{ member.progress }}% ตามชั่วโมงทั้งหมด`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L20

```html
    {% if member.overloaded %}<p class="deadline-member-warning">! ควรช่วยแบ่งงาน{% if member.risk_count %} · มี {{ member.risk_count }} งานเสี่ยง{% endif %}</p>
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if member.overloaded`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if member.risk_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.risk_count`
- จบเงื่อนไข: `endif`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-member-warning`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `! ควรช่วยแบ่งงาน{% if member.risk_count %} · มี {{ member.risk_count }} งานเสี่ยง{% endif %}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L21

```html
    {% elif member.open_count %}<span class="badge good">✓ ภาระงานอยู่ในเกณฑ์</span>
```

- ตรวจเงื่อนไขทางเลือก: `elif member.open_count`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge good`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ ภาระงานอยู่ในเกณฑ์`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L22

```html
    {% else %}<span class="badge">○ ไม่มีงานค้างที่มอบหมาย</span>{% endif %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบเงื่อนไข: `endif`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `○ ไม่มีงานค้างที่มอบหมาย`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L23

```html
    <details><summary>งานที่รับผิดชอบ ({{ member.assignment_count }})</summary><ul class="deadline-member-tasks">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `member.assignment_count`
- เปิด `<details>`: ส่วนยุบ/เปิดได้
- เปิด `<summary>`: ตัวควบคุมเปิดรายละเอียด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานที่รับผิดชอบ ({{ member.assignment_count }})`
- ปิด `</summary>` ที่เปิดไว้ก่อนหน้า
- เปิด `<ul>`: รายการแบบไม่มีเลข
- `class`=`deadline-member-tasks`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L24

```html
      {% for task in member.assignments %}<li><a href="{{ url_for('page', name='page2') }}#task-{{ task.no }}">{{ task.title }}</a><small>{{ task.status_icon }} {{ task.status }} · {{ task.progress }}%</small></li>
```

- วน list จาก context: `for task in member.assignments`
- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.status_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.status`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.progress`
- เปิด `<li>`: สมาชิกในรายการ
- เปิด `<a>`: ลิงก์
- `href`=`{{ url_for('page', name='page2') }}#task-{{ task.no }}`: ปลายทางลิงก์/anchor
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า
- เปิด `<small>`: ข้อความประกอบ
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</li>` ที่เปิดไว้ก่อนหน้า

### L25

```html
      {% else %}<li class="note">ยังไม่มีงานที่มอบหมาย</li>{% endfor %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบ for: `endfor`
- เปิด `<li>`: สมาชิกในรายการ
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยังไม่มีงานที่มอบหมาย`
- ปิด `</li>` ที่เปิดไว้ก่อนหน้า

### L26

```html
    </ul></details>
```

- ปิด `</ul>` ที่เปิดไว้ก่อนหน้า
- ปิด `</details>` ที่เปิดไว้ก่อนหน้า

### L27

```html
  </article>
```

- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L28

```html
  {% endfor %}
```

- จบ for: `endfor`

### L29

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L30

```html
<section aria-labelledby="unassigned-heading">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `aria-labelledby`=`unassigned-heading`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L31

```html
  <h2 id="unassigned-heading">○ งานที่ยังไม่มีผู้รับผิดชอบ ({{ unassigned|length }})</h2>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `unassigned|length`
- เปิด `<h2>`: หัวข้อส่วน
- `id`=`unassigned-heading`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `○ งานที่ยังไม่มีผู้รับผิดชอบ ({{ unassigned|length }})`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า

### L32

```html
  <div class="deadline-task-list">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-list`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L33

```html
    {% for task in unassigned %}
```

- วน list จาก context: `for task in unassigned`

### L34

```html
    <article class="deadline-task"><div class="deadline-task-main"><span class="deadline-course">{{ task.course }}</span><h3>{{ task.title }}</h3><p class="deadline-meta">ส่ง {{ task.due_date }} · เหลือ {{ task.remaining_hours }} ชั่วโมง</p></div><a class="btn ghost" href="{{ url_for('page', name='page2') }}#task-{{ task.no }}">มอบหมายงาน →</a></article>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `task.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.due_date`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.remaining_hours`
- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- แสดงค่าจาก context/นิพจน์ Jinja: `task.no`
- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`deadline-task`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-main`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-course`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h3>`: หัวข้องาน/การ์ด
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-meta`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ส่ง {{ task.due_date }} · เหลือ {{ task.remaining_hours }} ชั่วโมง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า
- เปิด `<a>`: ลิงก์
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page2') }}#task-{{ task.no }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `มอบหมายงาน →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า
- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L35

```html
    {% else %}<p class="empty">✓ งานค้างทุกชิ้นมีผู้รับผิดชอบแล้ว</p>{% endfor %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบ for: `endfor`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ งานค้างทุกชิ้นมีผู้รับผิดชอบแล้ว`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L36

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L37

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L38

```html
{% endblock %}
```

- จบ block content/scripts: `endblock`
