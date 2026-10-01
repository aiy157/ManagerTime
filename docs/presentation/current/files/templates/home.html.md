# templates/home.html — HTML/Jinja ของหน้าแรก

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 17 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `7f0f5c8caedfe79704fcdcafb3fe1066a3c978d9a2f93e929452751bba0edb97`

**ผู้ศึกษา/บทบาท:** ภาพรวมโครงการ

## 1. หน้าที่และการเชื่อมต่อ

แนะนำหัวข้อและทางลัดไปภาพรวม จัดการงาน และแผน

- **รับเข้า:** context กลางจาก app.py และแม่แบบ base.html
- **ผลลัพธ์:** หน้าแรกเมื่อเปิด /

**เกี่ยวข้องกับ:** templates/base.html (เดิม ห้ามแก้); static/style.css; url_for('page', name=...)

## 2. ลำดับทำงาน

1. extends base และเปิด block content
2. แสดงหัวข้อ คำอธิบาย และปุ่มเข้า Overview
3. แสดงการ์ดทางลัด 3 หน้า
4. ปิด block เพื่อให้ base ประกอบหน้าเต็ม

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่มี index.html ในโครงการ; route / ใช้ home.html จริง
- เลข 28 ในภาพปฏิทินเป็นข้อความตกแต่ง ไม่ใช่วันที่หรือจำนวนงาน
- ไม่มี build ของ home และไม่มีการคำนวณงานในไฟล์นี้

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q001: โครงการนี้แก้ปัญหาอะไร?](../../TEACHER_QUESTIONS.md#q001)
- [Q006: หน้าแรกคือ index.html หรือไม่?](../../TEACHER_QUESTIONS.md#q006)
- [Q061: extends base.html ทำอะไร?](../../TEACHER_QUESTIONS.md#q061)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% extends "base.html" %}
{% block content %}
<section class="deadline-hero deadline-home-hero">
  <div>
    <span class="deadline-eyebrow">DEADLINE COMPASS</span>
    <h1>เดดไลน์ไม่ชนกัน</h1>
    <p>เห็นงานทั้งหมด วางเวลาที่มี และเริ่มงานสำคัญก่อนถึงวันส่ง</p>
    <a class="btn" href="{{ url_for('page', name='page1') }}">เปิดภาพรวมงาน →</a>
  </div>
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>28</span></div>
</section>
<section class="cards deadline-home-cards">
  <a class="card" href="{{ url_for('page', name='page1') }}"><span class="card-kicker">01 · ภาพรวม</span><span class="card-title">วันนี้มีอะไรต้องทำ</span><span class="note">ดูงานและสถานะในที่เดียว</span></a>
  <a class="card" href="{{ url_for('page', name='page2') }}"><span class="card-kicker">02 · จัดการ</span><span class="card-title">บันทึกงานให้ครบ</span><span class="note">เพิ่ม แก้ไข และติดตามชั่วโมง</span></a>
  <a class="card" href="{{ url_for('page', name='page3') }}"><span class="card-kicker">03 · วางแผน</span><span class="card-title">รู้ทันงานที่ชนกัน</span><span class="note">เทียบงานค้างกับเวลาที่มีจริง</span></a>
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
<section class="deadline-hero deadline-home-hero">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-hero deadline-home-hero`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L4

```html
  <div>
```

- เปิด `<div>`: กลุ่ม layout

### L5

```html
    <span class="deadline-eyebrow">DEADLINE COMPASS</span>
```

- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `DEADLINE COMPASS`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L6

```html
    <h1>เดดไลน์ไม่ชนกัน</h1>
```

- เปิด `<h1>`: หัวข้อหลักหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เดดไลน์ไม่ชนกัน`
- ปิด `</h1>` ที่เปิดไว้ก่อนหน้า

### L7

```html
    <p>เห็นงานทั้งหมด วางเวลาที่มี และเริ่มงานสำคัญก่อนถึงวันส่ง</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เห็นงานทั้งหมด วางเวลาที่มี และเริ่มงานสำคัญก่อนถึงวันส่ง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L8

```html
    <a class="btn" href="{{ url_for('page', name='page1') }}">เปิดภาพรวมงาน →</a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page1')`
- เปิด `<a>`: ลิงก์
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page1') }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เปิดภาพรวมงาน →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L9

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L10

```html
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>28</span></div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-hero-mark`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `28`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L11

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L12

```html
<section class="cards deadline-home-cards">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`cards deadline-home-cards`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L13

```html
  <a class="card" href="{{ url_for('page', name='page1') }}"><span class="card-kicker">01 · ภาพรวม</span><span class="card-title">วันนี้มีอะไรต้องทำ</span><span class="note">ดูงานและสถานะในที่เดียว</span></a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page1')`
- เปิด `<a>`: ลิงก์
- `class`=`card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page1') }}`: ปลายทางลิงก์/anchor
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`card-kicker`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `01 · ภาพรวม`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- `class`=`card-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันนี้มีอะไรต้องทำ`
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ดูงานและสถานะในที่เดียว`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L14

```html
  <a class="card" href="{{ url_for('page', name='page2') }}"><span class="card-kicker">02 · จัดการ</span><span class="card-title">บันทึกงานให้ครบ</span><span class="note">เพิ่ม แก้ไข และติดตามชั่วโมง</span></a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- เปิด `<a>`: ลิงก์
- `class`=`card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page2') }}`: ปลายทางลิงก์/anchor
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`card-kicker`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `02 · จัดการ`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- `class`=`card-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกงานให้ครบ`
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เพิ่ม แก้ไข และติดตามชั่วโมง`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L15

```html
  <a class="card" href="{{ url_for('page', name='page3') }}"><span class="card-kicker">03 · วางแผน</span><span class="card-title">รู้ทันงานที่ชนกัน</span><span class="note">เทียบงานค้างกับเวลาที่มีจริง</span></a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page3')`
- เปิด `<a>`: ลิงก์
- `class`=`card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page3') }}`: ปลายทางลิงก์/anchor
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`card-kicker`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `03 · วางแผน`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- `class`=`card-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รู้ทันงานที่ชนกัน`
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เทียบงานค้างกับเวลาที่มีจริง`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L16

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L17

```html
{% endblock %}
```

- จบ block content/scripts: `endblock`
