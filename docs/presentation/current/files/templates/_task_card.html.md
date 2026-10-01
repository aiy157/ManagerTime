# templates/_task_card.html — Macro ฟอร์มและการ์ดร่วม

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 60 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `2c89502a22de0f2c61e5c53fe434a939fd6e3d1661564d0ed13500d6039ff92f`

**ผู้ศึกษา/บทบาท:** ส่วนร่วมของทุกหน้า

## 1. หน้าที่และการเชื่อมต่อ

ลดโค้ดปุ่มและการ์ดที่ซ้ำ พร้อมให้ทุกหน้าส่ง no/version ด้วยกติกาเดียวกัน

- **รับเข้า:** item ข้อมูล view และ page_name หน้าเป้าหมาย
- **ผลลัพธ์:** ชิ้น HTML ของ row_fields, quick_actions และ task_card

**เกี่ยวข้องกับ:** models.task_view/overview; url_for; CSS ของการ์ดและปุ่ม

## 2. ลำดับทำงาน

1. row_fields สร้าง hidden no และ version
2. quick_actions แสดงเริ่มเฉพาะยังไม่เริ่ม ปิดสำหรับ pending และเปิดกลับเฉพาะเคยกดปิด
3. task_card แสดงชื่อ เจ้าของ ชั่วโมง ป้าย progress เหตุผล และปุ่มปฏิทิน

## 3. จุดที่ต้องอธิบายให้ถูก

- เป็นส่วนที่ import ใช้ ไม่ใช่หน้า route จึงไม่ extends base
- item ของ task_card ต้องมี today_hours/reasons ในกรณี pending ซึ่ง overview เตรียมไว้
- ปุ่มปฏิทินมี dataset ต้องมี reminders.js ในหน้าที่ใช้งานจึงดาวน์โหลดได้

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q027: no กับ version ใช้เพื่ออะไร?](../../TEACHER_QUESTIONS.md#q027)
- [Q035: งานกำลังทำและเกินกำหนดพร้อมกันได้หรือไม่?](../../TEACHER_QUESTIONS.md#q035)
- [Q049: กดเปิดกลับคืนอะไร และทุกงานเสร็จเปิดกลับได้หรือไม่?](../../TEACHER_QUESTIONS.md#q049)
- [Q063: macro ใน _task_card.html คืออะไร?](../../TEACHER_QUESTIONS.md#q063)
- [Q064: ทำไมไฟล์ macro ไม่ extends base?](../../TEACHER_QUESTIONS.md#q064)
- [Q066: hidden ป้องกันผู้ใช้แก้ค่าได้หรือไม่?](../../TEACHER_QUESTIONS.md#q066)
- [Q067: ทำไมไม่ใช้สีบอกสถานะอย่างเดียว?](../../TEACHER_QUESTIONS.md#q067)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% macro row_fields(item) %}
<input type="hidden" name="no" value="{{ item.no }}">
<input type="hidden" name="version" value="{{ item.version }}">
{% endmacro %}

{% macro quick_actions(item, page_name) %}
<div class="deadline-quick-actions">
  {% if item.remaining_hours > 0 %}
    {% if item.status == 'ยังไม่เริ่ม' %}
    <form method="post" action="{{ url_for('page', name=page_name) }}">
      {{ row_fields(item) }}<input type="hidden" name="action" value="start">
      <button class="btn" type="submit">▶ เริ่มงานนี้</button>
    </form>
    {% endif %}
    <form method="post" action="{{ url_for('page', name=page_name) }}">
      {{ row_fields(item) }}<input type="hidden" name="action" value="complete">
      <button class="btn ghost" type="submit">✓ ทำเครื่องหมายว่าเสร็จแล้ว</button>
    </form>
    <a class="deadline-action-link" href="{{ url_for('page', name='page2') }}#task-{{ item.no }}">บันทึกเวลา / งานย่อย →</a>
  {% else %}
    {% if item.details.before_complete is defined %}
    <form method="post" action="{{ url_for('page', name=page_name) }}">
      {{ row_fields(item) }}<input type="hidden" name="action" value="reopen">
      <button class="btn ghost" type="submit">↻ เปิดกลับมาทำต่อ</button>
    </form>
    {% endif %}
    <a class="deadline-action-link" href="{{ url_for('page', name='page2') }}#task-{{ item.no }}">ดูงานย่อย / แก้ไขข้อมูล →</a>
  {% endif %}
</div>
{% endmacro %}

{% macro task_card(item, page_name) %}
<article class="deadline-task">
  <div class="deadline-task-main">
    <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
    <h3>{{ item.title }}</h3>
    <p class="deadline-meta">ส่ง <time datetime="{{ item.due_date }}">{{ item.due_date }}</time> · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}</p>
    <div class="deadline-badge-row">
      <span class="badge {{ item.tone }}"><span aria-hidden="true">{{ item.status_icon }}</span> {{ item.status }}</span>
      {% if item.remaining_hours > 0 %}<span class="badge {{ item.deadline_tone }}"><span aria-hidden="true">{{ item.deadline_icon }}</span> {{ item.deadline_label }}</span>{% endif %}
      {% if item.subtask_count %}<span class="badge">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</span>{% endif %}
    </div>
    <div class="progress deadline-progress" role="progressbar" aria-label="ความคืบหน้า {{ item.title }}" aria-valuenow="{{ item.progress }}" aria-valuemin="0" aria-valuemax="100"><div style="width: {{ item.progress }}%"></div></div>
    <p class="note">{{ item.progress }}% จากชั่วโมงที่ทำแล้ว</p>
    {% if item.remaining_hours > 0 %}
    <p class="deadline-plan-detail">
      {% if item.today_hours > 0 %}วันนี้ควรแบ่งให้ <strong>{{ "{:,.1f}".format(item.today_hours) }} ชั่วโมง</strong>
      {% else %}เวลาที่แบ่งวันนี้ครบแล้ว ควรปรับเวลาว่างหรือเลื่อนงานลำดับถัดไป{% endif %}
    </p>
    <ul class="deadline-reasons">{% for reason in item.reasons %}<li>{{ reason }}</li>{% endfor %}</ul>
    {% endif %}
  </div>
  <div class="deadline-task-actions">
    {{ quick_actions(item, page_name) }}
    {% if item.remaining_hours > 0 and item.days_left >= 0 %}
    <button class="deadline-text-button" type="button" data-calendar-title="{{ item.title }}" data-calendar-course="{{ item.course }}" data-calendar-date="{{ item.due_date }}">▣ เพิ่มลงปฏิทิน</button>
    {% endif %}
  </div>
</article>
{% endmacro %}
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```html
{% macro row_fields(item) %}
```

- นิยาม macro รับ argument แล้วสร้างชิ้น HTML: `macro row_fields(item)`

### L2

```html
<input type="hidden" name="no" value="{{ item.no }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`no`: key ที่ส่งไปใน form
- `value`=`{{ item.no }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L3

```html
<input type="hidden" name="version" value="{{ item.version }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.version`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`version`: key ที่ส่งไปใน form
- `value`=`{{ item.version }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L4

```html
{% endmacro %}
```

- จบ macro: `endmacro`

### L5

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L6

```html
{% macro quick_actions(item, page_name) %}
```

- นิยาม macro รับ argument แล้วสร้างชิ้น HTML: `macro quick_actions(item, page_name)`

### L7

```html
<div class="deadline-quick-actions">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-quick-actions`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L8

```html
  {% if item.remaining_hours > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`

### L9

```html
    {% if item.status == 'ยังไม่เริ่ม' %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.status == 'ยังไม่เริ่ม'`

### L10

```html
    <form method="post" action="{{ url_for('page', name=page_name) }}">
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name=page_name)`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `action`=`{{ url_for('page', name=page_name) }}`: URL ปลายทาง form

### L11

```html
      {{ row_fields(item) }}<input type="hidden" name="action" value="start">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`start`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L12

```html
      <button class="btn" type="submit">▶ เริ่มงานนี้</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `▶ เริ่มงานนี้`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L13

```html
    </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L14

```html
    {% endif %}
```

- จบเงื่อนไข: `endif`

### L15

```html
    <form method="post" action="{{ url_for('page', name=page_name) }}">
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name=page_name)`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `action`=`{{ url_for('page', name=page_name) }}`: URL ปลายทาง form

### L16

```html
      {{ row_fields(item) }}<input type="hidden" name="action" value="complete">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`complete`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L17

```html
      <button class="btn ghost" type="submit">✓ ทำเครื่องหมายว่าเสร็จแล้ว</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `✓ ทำเครื่องหมายว่าเสร็จแล้ว`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L18

```html
    </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L19

```html
    <a class="deadline-action-link" href="{{ url_for('page', name='page2') }}#task-{{ item.no }}">บันทึกเวลา / งานย่อย →</a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<a>`: ลิงก์
- `class`=`deadline-action-link`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page2') }}#task-{{ item.no }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกเวลา / งานย่อย →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L20

```html
  {% else %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`

### L21

```html
    {% if item.details.before_complete is defined %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.details.before_complete is defined`

### L22

```html
    <form method="post" action="{{ url_for('page', name=page_name) }}">
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name=page_name)`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `action`=`{{ url_for('page', name=page_name) }}`: URL ปลายทาง form

### L23

```html
      {{ row_fields(item) }}<input type="hidden" name="action" value="reopen">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`reopen`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L24

```html
      <button class="btn ghost" type="submit">↻ เปิดกลับมาทำต่อ</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `↻ เปิดกลับมาทำต่อ`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L25

```html
    </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L26

```html
    {% endif %}
```

- จบเงื่อนไข: `endif`

### L27

```html
    <a class="deadline-action-link" href="{{ url_for('page', name='page2') }}#task-{{ item.no }}">ดูงานย่อย / แก้ไขข้อมูล →</a>
```

- สร้าง URL ผ่าน route เดิม: `url_for('page', name='page2')`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<a>`: ลิงก์
- `class`=`deadline-action-link`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `href`=`{{ url_for('page', name='page2') }}#task-{{ item.no }}`: ปลายทางลิงก์/anchor
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ดูงานย่อย / แก้ไขข้อมูล →`
- ปิด `</a>` ที่เปิดไว้ก่อนหน้า

### L28

```html
  {% endif %}
```

- จบเงื่อนไข: `endif`

### L29

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L30

```html
{% endmacro %}
```

- จบ macro: `endmacro`

### L31

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L32

```html
{% macro task_card(item, page_name) %}
```

- นิยาม macro รับ argument แล้วสร้างชิ้น HTML: `macro task_card(item, page_name)`

### L33

```html
<article class="deadline-task">
```

- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`deadline-task`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L34

```html
  <div class="deadline-task-main">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-main`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L35

```html
    <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.priority_label`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-course`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L36

```html
    <h3>{{ item.title }}</h3>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- เปิด `<h3>`: หัวข้องาน/การ์ด
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า

### L37

```html
    <p class="deadline-meta">ส่ง <time datetime="{{ item.due_date }}">{{ item.due_date }}</time> · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.due_date`
- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(item.remaining_hours)`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.owner_name`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-meta`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ส่ง`
- เปิด `<time>`: ข้อมูลวันที่ที่มีความหมาย
- `datetime`=`{{ item.due_date }}`: วันที่มาตรฐานของ time
- ปิด `</time>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `· เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L38

```html
    <div class="deadline-badge-row">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-badge-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L39

```html
      <span class="badge {{ item.tone }}"><span aria-hidden="true">{{ item.status_icon }}</span> {{ item.status }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.status_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.status`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ item.tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L40

```html
      {% if item.remaining_hours > 0 %}<span class="badge {{ item.deadline_tone }}"><span aria-hidden="true">{{ item.deadline_icon }}</span> {{ item.deadline_label }}</span>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_label`
- จบเงื่อนไข: `endif`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ item.deadline_tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L41

```html
      {% if item.subtask_count %}<span class="badge">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</span>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.subtask_count`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_done`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_count`
- จบเงื่อนไข: `endif`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L42

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L43

```html
    <div class="progress deadline-progress" role="progressbar" aria-label="ความคืบหน้า {{ item.title }}" aria-valuenow="{{ item.progress }}" aria-valuemin="0" aria-valuemax="100"><div style="width: {{ item.progress }}%"></div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.progress`
- เปิด `<div>`: กลุ่ม layout
- `class`=`progress deadline-progress`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`progressbar`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- `aria-label`=`ความคืบหน้า {{ item.title }}`: คำอธิบายสำหรับเครื่องมืออ่านหน้าจอ
- `aria-valuenow`=`{{ item.progress }}`: ค่าปัจจุบันของ progressbar
- `aria-valuemin`=`0`: ขอบล่าง progressbar
- `aria-valuemax`=`100`: ขอบบน progressbar
- `style`=`width: {{ item.progress }}%`: CSS เฉพาะ element; progress เป็นเปอร์เซ็นต์ที่ Python คำนวณ
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L44

```html
    <p class="note">{{ item.progress }}% จากชั่วโมงที่ทำแล้ว</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.progress`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L45

```html
    {% if item.remaining_hours > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`

### L46

```html
    <p class="deadline-plan-detail">
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-plan-detail`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L47

```html
      {% if item.today_hours > 0 %}วันนี้ควรแบ่งให้ <strong>{{ "{:,.1f}".format(item.today_hours) }} ชั่วโมง</strong>
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.today_hours > 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(item.today_hours)`
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า

### L48

```html
      {% else %}เวลาที่แบ่งวันนี้ครบแล้ว ควรปรับเวลาว่างหรือเลื่อนงานลำดับถัดไป{% endif %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบเงื่อนไข: `endif`

### L49

```html
    </p>
```

- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L50

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

### L51

```html
    {% endif %}
```

- จบเงื่อนไข: `endif`

### L52

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L53

```html
  <div class="deadline-task-actions">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-task-actions`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L54

```html
    {{ quick_actions(item, page_name) }}
```

- เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: `quick_actions(item, page_name)`

### L55

```html
    {% if item.remaining_hours > 0 and item.days_left >= 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0 and item.days_left >= 0`

### L56

```html
    <button class="deadline-text-button" type="button" data-calendar-title="{{ item.title }}" data-calendar-course="{{ item.course }}" data-calendar-date="{{ item.due_date }}">▣ เพิ่มลงปฏิทิน</button>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.due_date`
- เปิด `<button>`: ปุ่มกระทำ
- `class`=`deadline-text-button`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`button`: ชนิดช่องหรือปุ่ม
- `data-calendar-title`=`{{ item.title }}`: ชื่อสำหรับไฟล์ปฏิทิน
- `data-calendar-course`=`{{ item.course }}`: วิชาสำหรับไฟล์ปฏิทิน
- `data-calendar-date`=`{{ item.due_date }}`: วันส่งสำหรับไฟล์ปฏิทิน
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `▣ เพิ่มลงปฏิทิน`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L57

```html
    {% endif %}
```

- จบเงื่อนไข: `endif`

### L58

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L59

```html
</article>
```

- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L60

```html
{% endmacro %}
```

- จบ macro: `endmacro`
