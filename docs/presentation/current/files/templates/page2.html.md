# templates/page2.html — HTML/Jinja ของ Manage

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 134 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `cba2da48f428606fc70cc26285b3ae4179b1a7513c1f3d3eb4e8781249f479d5`

**ผู้ศึกษา/บทบาท:** นายไกรวิชญ์ บุ้งทอง · Page 2

## 1. หน้าที่และการเชื่อมต่อ

จัดฟอร์มงาน ชี้ความหมายชั่วโมง ทำงานย่อย และแสดงประวัติที่แยกประเภท

- **รับเข้า:** items, members, today, history, actual_total และ daily_history จาก page2.build
- **ผลลัพธ์:** ฟอร์ม add/update/delete/log_time/add_subtask/toggle_subtask และแสดงข้อมูล

**เกี่ยวข้องกับ:** base.html; _task_card.html: row_fields/quick_actions; static/js/forms.js; static/style.css

## 2. ลำดับทำงาน

1. ฟอร์มเพิ่มงานพร้อม help, priority, owner และงานย่อย
2. วนงานและใช้ no สร้าง id ของการ์ด/ช่อง
3. details ยุบส่วนบันทึกเวลา งานย่อย และแก้ข้อมูล
4. ทุกการกระทำรายการเดิมมี hidden no/version/action
5. วนสรุปวันและตาราง history พร้อมกรอบเลื่อน
6. โหลด forms.js เพื่อช่วยตรวจและเปิดการ์ดตาม hash

## 3. จุดที่ต้องอธิบายให้ถูก

- name คือ key ใน form; id ใช้ label/JavaScript และต้องไม่ซ้ำ
- hidden เป็นข้อมูลที่ยังแก้จากผู้ใช้ได้ จึงต้องตรวจฝั่ง Python
- required/min/max/step เป็นการตรวจเบราว์เซอร์ ไม่แทน backend
- งานเสร็จจากการบันทึกชั่วโมงจนครบอาจมีงานย่อยไม่ถูกติ๊ก จึงแสดงค่าจริง
- ฟอร์ม edit ปรับยอดรวม; log_time เพิ่มยอดครั้งนี้

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q004: Frontend และ Backend ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q004)
- [Q007: ผู้ใช้กดบันทึกแล้วข้อมูลเดินทางอย่างไร?](../../TEACHER_QUESTIONS.md#q007)
- [Q041: ฟอร์มเพิ่มงานบังคับข้อมูลใด?](../../TEACHER_QUESTIONS.md#q041)
- [Q043: ชั่วโมงทั้งหมด ชั่วโมงที่ทำแล้ว และชั่วโมงครั้งนี้ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q043)
- [Q046: ติ๊กงานย่อยแล้ว progress เพิ่มเองหรือไม่?](../../TEACHER_QUESTIONS.md#q046)
- [Q048: ทำไมประวัติจริงไม่สร้างจาก done_hours เดิมทั้งหมด?](../../TEACHER_QUESTIONS.md#q048)
- [Q065: input name กับ id ต่างกันอย่างไร?](../../TEACHER_QUESTIONS.md#q065)
- [Q067: ทำไมไม่ใช้สีบอกสถานะอย่างเดียว?](../../TEACHER_QUESTIONS.md#q067)
- [Q069: ตารางประวัติยาวกว่าจอจะทำอย่างไร?](../../TEACHER_QUESTIONS.md#q069)
- [Q072: defer ที่ script หมายถึงอะไรในโครงการ?](../../TEACHER_QUESTIONS.md#q072)

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```html
{% extends "base.html" %}
{% from "_task_card.html" import row_fields, quick_actions %}
{% block content %}
<div class="deadline-page-title">
  <span class="deadline-eyebrow">จัดการงาน</span><h1>งานใหญ่เริ่มจากก้าวเล็ก ๆ</h1>
  <p class="lead">กำหนดผู้รับผิดชอบ แบ่งงานย่อย และบันทึกเวลาที่ทำจริงในแต่ละวัน</p>
</div>
<div class="two-col deadline-form-layout">
  <form method="post" class="panel deadline-add-form" data-assignment-form data-today="{{ today }}">
    <h2>+ งานใหม่</h2><input type="hidden" name="action" value="add">
    <p class="deadline-form-error" role="alert" hidden></p>
    <div class="field">
      <label for="new-title">ชื่องาน</label><input id="new-title" name="title" maxlength="80" placeholder="เช่น โครงงานเขียนโปรแกรม" aria-describedby="new-title-help" required>
      <small id="new-title-help" class="deadline-help">ชื่อสั้นและชัดเจน ไม่เกิน 80 ตัวอักษร</small>
    </div>
    <div class="field">
      <label for="new-course">วิชาที่เกี่ยวข้อง</label><input id="new-course" name="course" maxlength="40" placeholder="เช่น การเขียนโปรแกรม" aria-describedby="new-course-help" required>
      <small id="new-course-help" class="deadline-help">ระบุชื่อวิชาเพื่อแยกงานแต่ละรายวิชา</small>
    </div>
    <div class="field">
      <label for="new-date">วันส่งงาน</label><input id="new-date" name="due_date" type="date" aria-describedby="new-date-help" required>
      <small id="new-date-help" class="deadline-help">วันที่ต้องส่งงาน หากผ่านไปแล้วต้องยืนยันว่าเป็นงานค้าง</small>
    </div>
    <label class="deadline-past-confirm" data-past-warning hidden><input type="checkbox" name="acknowledge_past" value="yes"> วันส่งผ่านไปแล้ว ยืนยันบันทึกเพื่อติดตามงานค้าง</label>
    <div class="field">
      <label for="new-hours">เวลาที่คาดว่าจะใช้ทั้งหมด (ชั่วโมง)</label><input id="new-hours" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" placeholder="เช่น 4" aria-describedby="new-hours-help" required>
      <small id="new-hours-help" class="deadline-help">เวลารวมทั้งงาน เช่น 4 ชั่วโมง รวมส่วนที่ทำไปแล้วด้วย</small>
    </div>
    <div class="field">
      <label for="new-done">เวลาที่ทำไปแล้ว (ชั่วโมง)</label><input id="new-done" name="done_hours" type="number" min="0" max="200" step="0.1" value="0" aria-describedby="new-done-help" required>
      <small id="new-done-help" class="deadline-help">ยอดรวมเดิม เช่น 1.5 ชั่วโมง หากยังไม่เริ่มให้ใส่ 0</small>
    </div>
    <div class="field">
      <label for="new-priority">ความสำคัญ</label><select id="new-priority" name="priority"><option value="normal">ปกติ</option><option value="high">สูง</option><option value="low">ต่ำ</option></select>
    </div>
    <div class="field">
      <label for="new-owner">ผู้รับผิดชอบ</label><select id="new-owner" name="owner"><option value="">ยังไม่มอบหมาย</option>{% for member in members %}<option value="{{ member.id }}">{{ member.name }}</option>{% endfor %}</select>
    </div>
    <details class="deadline-subtask-setup">
      <summary>แบ่งเป็นงานย่อย (ไม่บังคับ)</summary>
      <div class="field"><label for="new-subtasks">งานย่อย หนึ่งบรรทัดต่อหนึ่งรายการ</label><textarea id="new-subtasks" name="subtasks" rows="6" aria-describedby="new-subtasks-help" placeholder="วิเคราะห์ปัญหา&#10;ออกแบบระบบ&#10;เขียนโปรแกรม"></textarea><small id="new-subtasks-help" class="deadline-help">สูงสุด 30 รายการ ติ๊กงานย่อยแยกจากยอดชั่วโมง</small></div>
      <button type="button" class="btn ghost" data-subtask-template="new-subtasks">ใช้ขั้นตอนโครงงาน 6 ข้อ</button>
    </details>
    <button class="btn full" type="submit">บันทึกงาน</button>
  </form>
  <section aria-labelledby="saved-heading">
    <div class="deadline-section-head"><div><h2 id="saved-heading">รายการที่บันทึก</h2><p class="note">{{ count }} งาน · เปิดการ์ดเพื่อบันทึกเวลา แก้ไข และจัดการงานย่อย</p></div></div>
    {% for item in items %}
    <article class="panel deadline-edit-card" id="task-{{ item.no }}">
      <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
      <h3>{{ item.title }}</h3>
      <p class="deadline-meta">ส่ง {{ item.due_date }} · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}</p>
      <div class="deadline-badge-row"><span class="badge {{ item.tone }}"><span aria-hidden="true">{{ item.status_icon }}</span> {{ item.status }}</span>{% if item.remaining_hours > 0 %}<span class="badge {{ item.deadline_tone }}">{{ item.deadline_icon }} {{ item.deadline_label }}</span>{% endif %}<span class="badge">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</span></div>
      {{ quick_actions(item, 'page2') }}
      <details class="deadline-work-details">
        <summary>บันทึกเวลา / งานย่อย / แก้ไขข้อมูล</summary>
        {% if item.remaining_hours > 0 %}
        <section class="deadline-work-section" aria-labelledby="log-heading-{{ item.no }}">
          <h4 id="log-heading-{{ item.no }}">บันทึกเวลาที่ทำจริง</h4>
          <form method="post" class="deadline-log-form">
            {{ row_fields(item) }}<input type="hidden" name="action" value="log_time">
            <div class="field-row">
              <div class="field"><label for="work-date-{{ item.no }}">วันที่ทำงาน</label><input id="work-date-{{ item.no }}" name="work_date" type="date" value="{{ today }}" max="{{ today }}" required></div>
              <div class="field"><label for="log-hours-{{ item.no }}">ชั่วโมงที่ทำในครั้งนี้</label><input id="log-hours-{{ item.no }}" name="hours" type="number" min="0.1" max="{{ item.remaining_hours }}" step="0.1" placeholder="เช่น 1.5" required></div>
            </div>
            <div class="field"><label for="log-note-{{ item.no }}">ทำอะไรไปบ้าง (ไม่บังคับ)</label><input id="log-note-{{ item.no }}" name="note" maxlength="120" placeholder="เช่น เขียนส่วนรับข้อมูลเสร็จแล้ว"></div>
            <p class="note">เพิ่มจากยอดเดิม {{ item.done_hours }} ชั่วโมง ไม่ต้องกรอกยอดสะสมใหม่</p>
            <button class="btn" type="submit">+ บันทึกเวลาครั้งนี้</button>
          </form>
        </section>
        {% endif %}
        <section class="deadline-work-section" aria-labelledby="subtask-heading-{{ item.no }}">
          <h4 id="subtask-heading-{{ item.no }}">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</h4>
          <ul class="deadline-subtask-list">
            {% for subtask in item.details.subtasks %}
            <li>
              {% if item.remaining_hours > 0 %}
              <form method="post">
                {{ row_fields(item) }}<input type="hidden" name="action" value="toggle_subtask"><input type="hidden" name="subtask_no" value="{{ loop.index0 }}">
                <button class="deadline-subtask-toggle {{ 'is-done' if subtask.done }}" type="submit" aria-pressed="{{ 'true' if subtask.done else 'false' }}"><span aria-hidden="true">{{ '✓' if subtask.done else '○' }}</span> {{ subtask.title }}</button>
              </form>
              {% else %}<span>{{ '✓' if subtask.done else '○' }} {{ subtask.title }}{% if not subtask.done %} · ยังไม่ได้ทำเครื่องหมาย{% endif %}</span>{% endif %}
            </li>
            {% else %}<li class="note">ยังไม่มีงานย่อย แบ่งขั้นตอนเล็ก ๆ เพื่อเริ่มได้ง่ายขึ้น</li>{% endfor %}
          </ul>
          {% if item.remaining_hours > 0 %}
          <form method="post" class="deadline-subtask-add">
            {{ row_fields(item) }}<input type="hidden" name="action" value="add_subtask">
            <div class="field"><label for="subtask-{{ item.no }}">เพิ่มงานย่อย</label><input id="subtask-{{ item.no }}" name="subtask_title" maxlength="100" placeholder="เช่น ทดสอบระบบ" required></div>
            <button class="btn ghost" type="submit">+ เพิ่มขั้นตอน</button>
          </form>
          {% endif %}
          <p class="note">ติ๊กงานย่อยแล้วให้บันทึกเวลาที่ใช้แยกกัน เปอร์เซ็นต์หลักคำนวณจากชั่วโมง</p>
        </section>
        <section class="deadline-work-section" aria-labelledby="edit-heading-{{ item.no }}">
          <h4 id="edit-heading-{{ item.no }}">แก้ไขข้อมูลงาน</h4>
          <form method="post" class="deadline-edit-form" data-assignment-form data-today="{{ today }}" data-original-date="{{ item.due_date }}">
            {{ row_fields(item) }}<input type="hidden" name="action" value="update">
            <p class="deadline-form-error" role="alert" hidden></p>
            <div class="field"><label for="title-{{ item.no }}">ชื่องาน</label><input id="title-{{ item.no }}" name="title" value="{{ item.title }}" maxlength="80" required></div>
            <div class="field"><label for="course-{{ item.no }}">วิชาที่เกี่ยวข้อง</label><input id="course-{{ item.no }}" name="course" value="{{ item.course }}" maxlength="40" required></div>
            <div class="field"><label for="date-{{ item.no }}">วันส่งงาน</label><input id="date-{{ item.no }}" name="due_date" type="date" value="{{ item.due_date }}" required></div>
            <label class="deadline-past-confirm" data-past-warning hidden><input type="checkbox" name="acknowledge_past" value="yes"> ยืนยันเปลี่ยนวันส่งเป็นวันที่ผ่านไปแล้ว</label>
            <div class="field-row">
              <div class="field"><label for="hours-{{ item.no }}">เวลาที่คาดว่าจะใช้ทั้งหมด</label><input id="hours-{{ item.no }}" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" value="{{ item.estimated_hours }}" aria-describedby="hours-help-{{ item.no }}" required><small id="hours-help-{{ item.no }}" class="deadline-help">ชั่วโมงรวมทั้งงาน รวมส่วนที่ทำแล้ว</small></div>
              <div class="field"><label for="done-{{ item.no }}">เวลาที่ทำไปแล้วทั้งหมด</label><input id="done-{{ item.no }}" name="done_hours" type="number" min="0" max="{{ item.estimated_hours }}" step="0.1" value="{{ item.done_hours }}" aria-describedby="done-help-{{ item.no }}" required><small id="done-help-{{ item.no }}" class="deadline-help">ปรับยอดสะสมเดิม ใช้ “บันทึกเวลา” ด้านบนสำหรับการทำงานครั้งใหม่</small></div>
            </div>
            <div class="field-row">
              <div class="field"><label for="priority-{{ item.no }}">ความสำคัญ</label><select id="priority-{{ item.no }}" name="priority">{% for value, label in [('high','สูง'),('normal','ปกติ'),('low','ต่ำ')] %}<option value="{{ value }}" {{ 'selected' if item.priority == value }}>{{ label }}</option>{% endfor %}</select></div>
              <div class="field"><label for="owner-{{ item.no }}">ผู้รับผิดชอบ</label><select id="owner-{{ item.no }}" name="owner"><option value="">ยังไม่มอบหมาย</option>{% for member in members %}<option value="{{ member.id }}" {{ 'selected' if item.details.owner == member.id }}>{{ member.name }}</option>{% endfor %}</select></div>
            </div>
            <button class="btn" type="submit">บันทึกการแก้ไข</button>
          </form>
        </section>
        <form method="post" class="deadline-delete-form" onsubmit="return confirm('ลบงานนี้พร้อมงานย่อยและประวัติหรือไม่?')">{{ row_fields(item) }}<input type="hidden" name="action" value="delete"><button class="btn danger" type="submit">ลบงานนี้</button></form>
      </details>
    </article>
    {% else %}<div class="empty">ยังไม่มีงานที่บันทึกไว้</div>{% endfor %}
  </section>
</div>

<section class="deadline-history-section" aria-labelledby="history-heading">
  <div class="deadline-section-head"><div><h2 id="history-heading">ประวัติการทำงาน</h2><p class="note">ชั่วโมงทำจริงที่บันทึก {{ actual_total }} ชั่วโมง · การปรับยอดและการกดปิดงานแสดงแยกประเภท</p></div></div>
  {% if history %}
  {% if daily_history %}<div class="deadline-daily-history">{% for day in daily_history %}<div class="panel"><time datetime="{{ day.date }}">{{ day.date }}</time><strong>{{ day.hours }} ชั่วโมง</strong><span class="note">บันทึกเวลาจริง {{ day.count }} ครั้ง</span></div>{% endfor %}</div>{% endif %}
  <div class="deadline-table-scroll" tabindex="0" role="region" aria-label="ประวัติการทำงาน เลื่อนแนวนอนเพื่อดูครบ">
    <table><thead><tr><th>วันที่</th><th>งาน / ผู้รับผิดชอบ</th><th class="num">ชั่วโมง</th><th>ประเภท / หมายเหตุ</th></tr></thead><tbody>
      {% for entry in history %}<tr><td><time datetime="{{ entry.date }}">{{ entry.date }}</time></td><td>{{ entry.title }}<br><small>{{ entry.owner_name }}</small></td><td class="num">{{ "{:,.1f}".format(entry.hours) }}</td><td>{{ entry.label }}{% if entry.note %}<br><small>{{ entry.note }}</small>{% endif %}</td></tr>{% endfor %}
    </tbody></table>
  </div>
  {% else %}<div class="empty">เริ่มบันทึกเวลาของงาน แล้วประวัติรายวันจะแสดงที่นี่ ยอดเดิมที่ไม่มีวันที่จะไม่ถูกสร้างเป็นประวัติย้อนหลัง</div>{% endif %}
</section>
{% endblock %}
{% block scripts %}<script src="{{ url_for('static', filename='js/forms.js') }}" defer></script>{% endblock %}
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
{% from "_task_card.html" import row_fields, quick_actions %}
```

- นำเข้า macro ย่อย: `from "_task_card.html" import row_fields, quick_actions`

### L3

```html
{% block content %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block content`

### L4

```html
<div class="deadline-page-title">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-page-title`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L5

```html
  <span class="deadline-eyebrow">จัดการงาน</span><h1>งานใหญ่เริ่มจากก้าวเล็ก ๆ</h1>
```

- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-eyebrow`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `จัดการงาน`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- เปิด `<h1>`: หัวข้อหลักหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานใหญ่เริ่มจากก้าวเล็ก ๆ`
- ปิด `</h1>` ที่เปิดไว้ก่อนหน้า

### L6

```html
  <p class="lead">กำหนดผู้รับผิดชอบ แบ่งงานย่อย และบันทึกเวลาที่ทำจริงในแต่ละวัน</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`lead`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `กำหนดผู้รับผิดชอบ แบ่งงานย่อย และบันทึกเวลาที่ทำจริงในแต่ละวัน`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L7

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L8

```html
<div class="two-col deadline-form-layout">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`two-col deadline-form-layout`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L9

```html
  <form method="post" class="panel deadline-add-form" data-assignment-form data-today="{{ today }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `today`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `class`=`panel deadline-add-form`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `data-assignment-form`: marker ให้ forms.js ผูก validation
- `data-today`=`{{ today }}`: วันที่อ้างอิงจาก Python ให้ forms.js

### L10

```html
    <h2>+ งานใหม่</h2><input type="hidden" name="action" value="add">
```

- เปิด `<h2>`: หัวข้อส่วน
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `+ งานใหม่`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`add`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L11

```html
    <p class="deadline-form-error" role="alert" hidden></p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-form-error`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`alert`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- `hidden`: ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L12

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L13

```html
      <label for="new-title">ชื่องาน</label><input id="new-title" name="title" maxlength="80" placeholder="เช่น โครงงานเขียนโปรแกรม" aria-describedby="new-title-help" required>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-title`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชื่องาน`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`new-title`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`title`: key ที่ส่งไปใน form
- `maxlength`=`80`: จำนวนอักขระสูงสุดในช่อง
- `placeholder`=`เช่น โครงงานเขียนโปรแกรม`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- `aria-describedby`=`new-title-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด

### L14

```html
      <small id="new-title-help" class="deadline-help">ชื่อสั้นและชัดเจน ไม่เกิน 80 ตัวอักษร</small>
```

- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-title-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชื่อสั้นและชัดเจน ไม่เกิน 80 ตัวอักษร`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า

### L15

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L16

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L17

```html
      <label for="new-course">วิชาที่เกี่ยวข้อง</label><input id="new-course" name="course" maxlength="40" placeholder="เช่น การเขียนโปรแกรม" aria-describedby="new-course-help" required>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-course`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วิชาที่เกี่ยวข้อง`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`new-course`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`course`: key ที่ส่งไปใน form
- `maxlength`=`40`: จำนวนอักขระสูงสุดในช่อง
- `placeholder`=`เช่น การเขียนโปรแกรม`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- `aria-describedby`=`new-course-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด

### L18

```html
      <small id="new-course-help" class="deadline-help">ระบุชื่อวิชาเพื่อแยกงานแต่ละรายวิชา</small>
```

- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-course-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ระบุชื่อวิชาเพื่อแยกงานแต่ละรายวิชา`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า

### L19

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L20

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L21

```html
      <label for="new-date">วันส่งงาน</label><input id="new-date" name="due_date" type="date" aria-describedby="new-date-help" required>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-date`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันส่งงาน`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`new-date`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`due_date`: key ที่ส่งไปใน form
- `type`=`date`: ชนิดช่องหรือปุ่ม
- `aria-describedby`=`new-date-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด

### L22

```html
      <small id="new-date-help" class="deadline-help">วันที่ต้องส่งงาน หากผ่านไปแล้วต้องยืนยันว่าเป็นงานค้าง</small>
```

- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-date-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันที่ต้องส่งงาน หากผ่านไปแล้วต้องยืนยันว่าเป็นงานค้าง`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า

### L23

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L24

```html
    <label class="deadline-past-confirm" data-past-warning hidden><input type="checkbox" name="acknowledge_past" value="yes"> วันส่งผ่านไปแล้ว ยืนยันบันทึกเพื่อติดตามงานค้าง</label>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `class`=`deadline-past-confirm`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `data-past-warning`: marker กล่องยืนยันวันที่อดีต
- `hidden`: ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`checkbox`: ชนิดช่องหรือปุ่ม
- `name`=`acknowledge_past`: key ที่ส่งไปใน form
- `value`=`yes`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันส่งผ่านไปแล้ว ยืนยันบันทึกเพื่อติดตามงานค้าง`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า

### L25

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L26

```html
      <label for="new-hours">เวลาที่คาดว่าจะใช้ทั้งหมด (ชั่วโมง)</label><input id="new-hours" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" placeholder="เช่น 4" aria-describedby="new-hours-help" required>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-hours`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาที่คาดว่าจะใช้ทั้งหมด (ชั่วโมง)`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`new-hours`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`estimated_hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0.1`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`200`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `placeholder`=`เช่น 4`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- `aria-describedby`=`new-hours-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด

### L27

```html
      <small id="new-hours-help" class="deadline-help">เวลารวมทั้งงาน เช่น 4 ชั่วโมง รวมส่วนที่ทำไปแล้วด้วย</small>
```

- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-hours-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลารวมทั้งงาน เช่น 4 ชั่วโมง รวมส่วนที่ทำไปแล้วด้วย`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า

### L28

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L29

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L30

```html
      <label for="new-done">เวลาที่ทำไปแล้ว (ชั่วโมง)</label><input id="new-done" name="done_hours" type="number" min="0" max="200" step="0.1" value="0" aria-describedby="new-done-help" required>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-done`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาที่ทำไปแล้ว (ชั่วโมง)`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`new-done`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`done_hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`200`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `value`=`0`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `aria-describedby`=`new-done-help`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด

### L31

```html
      <small id="new-done-help" class="deadline-help">ยอดรวมเดิม เช่น 1.5 ชั่วโมง หากยังไม่เริ่มให้ใส่ 0</small>
```

- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-done-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยอดรวมเดิม เช่น 1.5 ชั่วโมง หากยังไม่เริ่มให้ใส่ 0`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า

### L32

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L33

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L34

```html
      <label for="new-priority">ความสำคัญ</label><select id="new-priority" name="priority"><option value="normal">ปกติ</option><option value="high">สูง</option><option value="low">ต่ำ</option></select>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-priority`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ความสำคัญ`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<select>`: ตัวเลือก
- `id`=`new-priority`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`priority`: key ที่ส่งไปใน form
- เปิด `<option>`: ตัวเลือกหนึ่งค่า
- `value`=`normal`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ปกติ`
- ปิด `</option>` ที่เปิดไว้ก่อนหน้า
- `value`=`high`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `สูง`
- `value`=`low`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ต่ำ`
- ปิด `</select>` ที่เปิดไว้ก่อนหน้า

### L35

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L36

```html
    <div class="field">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L37

```html
      <label for="new-owner">ผู้รับผิดชอบ</label><select id="new-owner" name="owner"><option value="">ยังไม่มอบหมาย</option>{% for member in members %}<option value="{{ member.id }}">{{ member.name }}</option>{% endfor %}</select>
```

- วน list จาก context: `for member in members`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.id`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.name`
- จบ for: `endfor`
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-owner`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ผู้รับผิดชอบ`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<select>`: ตัวเลือก
- `id`=`new-owner`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`owner`: key ที่ส่งไปใน form
- เปิด `<option>`: ตัวเลือกหนึ่งค่า
- `value`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยังไม่มอบหมาย`
- ปิด `</option>` ที่เปิดไว้ก่อนหน้า
- `value`=`{{ member.id }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ปิด `</select>` ที่เปิดไว้ก่อนหน้า

### L38

```html
    </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L39

```html
    <details class="deadline-subtask-setup">
```

- เปิด `<details>`: ส่วนยุบ/เปิดได้
- `class`=`deadline-subtask-setup`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L40

```html
      <summary>แบ่งเป็นงานย่อย (ไม่บังคับ)</summary>
```

- เปิด `<summary>`: ตัวควบคุมเปิดรายละเอียด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `แบ่งเป็นงานย่อย (ไม่บังคับ)`
- ปิด `</summary>` ที่เปิดไว้ก่อนหน้า

### L41

```html
      <div class="field"><label for="new-subtasks">งานย่อย หนึ่งบรรทัดต่อหนึ่งรายการ</label><textarea id="new-subtasks" name="subtasks" rows="6" aria-describedby="new-subtasks-help" placeholder="วิเคราะห์ปัญหา&#10;ออกแบบระบบ&#10;เขียนโปรแกรม"></textarea><small id="new-subtasks-help" class="deadline-help">สูงสุด 30 รายการ ติ๊กงานย่อยแยกจากยอดชั่วโมง</small></div>
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`new-subtasks`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานย่อย หนึ่งบรรทัดต่อหนึ่งรายการ`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<textarea>`: ข้อความหลายบรรทัด
- `id`=`new-subtasks`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`subtasks`: key ที่ส่งไปใน form
- `rows`=`6`: ความสูง textarea เป็นบรรทัด
- `aria-describedby`=`new-subtasks-help`: id ของข้อความช่วยอธิบาย
- `placeholder`=`วิเคราะห์ปัญหา\nออกแบบระบบ\nเขียนโปรแกรม`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- ปิด `</textarea>` ที่เปิดไว้ก่อนหน้า
- เปิด `<small>`: ข้อความประกอบ
- `id`=`new-subtasks-help`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `สูงสุด 30 รายการ ติ๊กงานย่อยแยกจากยอดชั่วโมง`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L42

```html
      <button type="button" class="btn ghost" data-subtask-template="new-subtasks">ใช้ขั้นตอนโครงงาน 6 ข้อ</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `type`=`button`: ชนิดช่องหรือปุ่ม
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `data-subtask-template`=`new-subtasks`: id textarea เป้าหมายของขั้นตอนตัวอย่าง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ใช้ขั้นตอนโครงงาน 6 ข้อ`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L43

```html
    </details>
```

- ปิด `</details>` ที่เปิดไว้ก่อนหน้า

### L44

```html
    <button class="btn full" type="submit">บันทึกงาน</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn full`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกงาน`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L45

```html
  </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L46

```html
  <section aria-labelledby="saved-heading">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `aria-labelledby`=`saved-heading`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L47

```html
    <div class="deadline-section-head"><div><h2 id="saved-heading">รายการที่บันทึก</h2><p class="note">{{ count }} งาน · เปิดการ์ดเพื่อบันทึกเวลา แก้ไข และจัดการงานย่อย</p></div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-section-head`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<h2>`: หัวข้อส่วน
- `id`=`saved-heading`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `รายการที่บันทึก`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L48

```html
    {% for item in items %}
```

- วน list จาก context: `for item in items`

### L49

```html
    <article class="panel deadline-edit-card" id="task-{{ item.no }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<article>`: การ์ดงาน/สมาชิกหนึ่งรายการ
- `class`=`panel deadline-edit-card`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `id`=`task-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label

### L50

```html
      <span class="deadline-course">{{ item.course }} · ความสำคัญ{{ item.priority_label }}</span>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.course`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.priority_label`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`deadline-course`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L51

```html
      <h3>{{ item.title }}</h3>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- เปิด `<h3>`: หัวข้องาน/การ์ด
- ปิด `</h3>` ที่เปิดไว้ก่อนหน้า

### L52

```html
      <p class="deadline-meta">ส่ง {{ item.due_date }} · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.due_date`
- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(item.remaining_hours)`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.owner_name`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-meta`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ส่ง {{ item.due_date }} · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง · {{ item.owner_name }}`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L53

```html
      <div class="deadline-badge-row"><span class="badge {{ item.tone }}"><span aria-hidden="true">{{ item.status_icon }}</span> {{ item.status }}</span>{% if item.remaining_hours > 0 %}<span class="badge {{ item.deadline_tone }}">{{ item.deadline_icon }} {{ item.deadline_label }}</span>{% endif %}<span class="badge">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</span></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.status_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.status`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_tone`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_icon`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.deadline_label`
- จบเงื่อนไข: `endif`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_done`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_count`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-badge-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`badge {{ item.tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- `class`=`badge {{ item.deadline_tone }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`badge`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L54

```html
      {{ quick_actions(item, 'page2') }}
```

- เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: `quick_actions(item, 'page2')`

### L55

```html
      <details class="deadline-work-details">
```

- เปิด `<details>`: ส่วนยุบ/เปิดได้
- `class`=`deadline-work-details`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L56

```html
        <summary>บันทึกเวลา / งานย่อย / แก้ไขข้อมูล</summary>
```

- เปิด `<summary>`: ตัวควบคุมเปิดรายละเอียด
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกเวลา / งานย่อย / แก้ไขข้อมูล`
- ปิด `</summary>` ที่เปิดไว้ก่อนหน้า

### L57

```html
        {% if item.remaining_hours > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`

### L58

```html
        <section class="deadline-work-section" aria-labelledby="log-heading-{{ item.no }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-work-section`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-labelledby`=`log-heading-{{ item.no }}`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L59

```html
          <h4 id="log-heading-{{ item.no }}">บันทึกเวลาที่ทำจริง</h4>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<h4>`: หัวข้อย่อยในรายละเอียด
- `id`=`log-heading-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกเวลาที่ทำจริง`
- ปิด `</h4>` ที่เปิดไว้ก่อนหน้า

### L60

```html
          <form method="post" class="deadline-log-form">
```

- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `class`=`deadline-log-form`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L61

```html
            {{ row_fields(item) }}<input type="hidden" name="action" value="log_time">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`log_time`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L62

```html
            <div class="field-row">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L63

```html
              <div class="field"><label for="work-date-{{ item.no }}">วันที่ทำงาน</label><input id="work-date-{{ item.no }}" name="work_date" type="date" value="{{ today }}" max="{{ today }}" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `today`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`work-date-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันที่ทำงาน`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`work-date-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`work_date`: key ที่ส่งไปใน form
- `type`=`date`: ชนิดช่องหรือปุ่ม
- `value`=`{{ today }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `max`=`{{ today }}`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L64

```html
              <div class="field"><label for="log-hours-{{ item.no }}">ชั่วโมงที่ทำในครั้งนี้</label><input id="log-hours-{{ item.no }}" name="hours" type="number" min="0.1" max="{{ item.remaining_hours }}" step="0.1" placeholder="เช่น 1.5" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.remaining_hours`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`log-hours-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมงที่ทำในครั้งนี้`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`log-hours-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0.1`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`{{ item.remaining_hours }}`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `placeholder`=`เช่น 1.5`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L65

```html
            </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L66

```html
            <div class="field"><label for="log-note-{{ item.no }}">ทำอะไรไปบ้าง (ไม่บังคับ)</label><input id="log-note-{{ item.no }}" name="note" maxlength="120" placeholder="เช่น เขียนส่วนรับข้อมูลเสร็จแล้ว"></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`log-note-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ทำอะไรไปบ้าง (ไม่บังคับ)`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`log-note-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`note`: key ที่ส่งไปใน form
- `maxlength`=`120`: จำนวนอักขระสูงสุดในช่อง
- `placeholder`=`เช่น เขียนส่วนรับข้อมูลเสร็จแล้ว`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L67

```html
            <p class="note">เพิ่มจากยอดเดิม {{ item.done_hours }} ชั่วโมง ไม่ต้องกรอกยอดสะสมใหม่</p>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.done_hours`
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เพิ่มจากยอดเดิม {{ item.done_hours }} ชั่วโมง ไม่ต้องกรอกยอดสะสมใหม่`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L68

```html
            <button class="btn" type="submit">+ บันทึกเวลาครั้งนี้</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `+ บันทึกเวลาครั้งนี้`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L69

```html
          </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L70

```html
        </section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L71

```html
        {% endif %}
```

- จบเงื่อนไข: `endif`

### L72

```html
        <section class="deadline-work-section" aria-labelledby="subtask-heading-{{ item.no }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-work-section`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-labelledby`=`subtask-heading-{{ item.no }}`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L73

```html
          <h4 id="subtask-heading-{{ item.no }}">งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}</h4>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_done`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.subtask_count`
- เปิด `<h4>`: หัวข้อย่อยในรายละเอียด
- `id`=`subtask-heading-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งานย่อย {{ item.subtask_done }}/{{ item.subtask_count }}`
- ปิด `</h4>` ที่เปิดไว้ก่อนหน้า

### L74

```html
          <ul class="deadline-subtask-list">
```

- เปิด `<ul>`: รายการแบบไม่มีเลข
- `class`=`deadline-subtask-list`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L75

```html
            {% for subtask in item.details.subtasks %}
```

- วน list จาก context: `for subtask in item.details.subtasks`

### L76

```html
            <li>
```

- เปิด `<li>`: สมาชิกในรายการ

### L77

```html
              {% if item.remaining_hours > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`

### L78

```html
              <form method="post">
```

- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)

### L79

```html
                {{ row_fields(item) }}<input type="hidden" name="action" value="toggle_subtask"><input type="hidden" name="subtask_no" value="{{ loop.index0 }}">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- แสดงค่าจาก context/นิพจน์ Jinja: `loop.index0`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`toggle_subtask`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `name`=`subtask_no`: key ที่ส่งไปใน form
- `value`=`{{ loop.index0 }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L80

```html
                <button class="deadline-subtask-toggle {{ 'is-done' if subtask.done }}" type="submit" aria-pressed="{{ 'true' if subtask.done else 'false' }}"><span aria-hidden="true">{{ '✓' if subtask.done else '○' }}</span> {{ subtask.title }}</button>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `'is-done' if subtask.done`
- แสดงค่าจาก context/นิพจน์ Jinja: `'true' if subtask.done else 'false'`
- แสดงค่าจาก context/นิพจน์ Jinja: `'✓' if subtask.done else '○'`
- แสดงค่าจาก context/นิพจน์ Jinja: `subtask.title`
- เปิด `<button>`: ปุ่มกระทำ
- `class`=`deadline-subtask-toggle {{ 'is-done' if subtask.done }}`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- `aria-pressed`=`{{ 'true' if subtask.done else 'false' }}`: สถานะกดของปุ่ม toggle ไม่ใช่ชั่วโมงทำงาน
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `aria-hidden`=`true`: กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L81

```html
              </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L82

```html
              {% else %}<span>{{ '✓' if subtask.done else '○' }} {{ subtask.title }}{% if not subtask.done %} · ยังไม่ได้ทำเครื่องหมาย{% endif %}</span>{% endif %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- แสดงค่าจาก context/นิพจน์ Jinja: `'✓' if subtask.done else '○'`
- แสดงค่าจาก context/นิพจน์ Jinja: `subtask.title`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if not subtask.done`
- จบเงื่อนไข: `endif`
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า

### L83

```html
            </li>
```

- ปิด `</li>` ที่เปิดไว้ก่อนหน้า

### L84

```html
            {% else %}<li class="note">ยังไม่มีงานย่อย แบ่งขั้นตอนเล็ก ๆ เพื่อเริ่มได้ง่ายขึ้น</li>{% endfor %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบ for: `endfor`
- เปิด `<li>`: สมาชิกในรายการ
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยังไม่มีงานย่อย แบ่งขั้นตอนเล็ก ๆ เพื่อเริ่มได้ง่ายขึ้น`
- ปิด `</li>` ที่เปิดไว้ก่อนหน้า

### L85

```html
          </ul>
```

- ปิด `</ul>` ที่เปิดไว้ก่อนหน้า

### L86

```html
          {% if item.remaining_hours > 0 %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if item.remaining_hours > 0`

### L87

```html
          <form method="post" class="deadline-subtask-add">
```

- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `class`=`deadline-subtask-add`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L88

```html
            {{ row_fields(item) }}<input type="hidden" name="action" value="add_subtask">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`add_subtask`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L89

```html
            <div class="field"><label for="subtask-{{ item.no }}">เพิ่มงานย่อย</label><input id="subtask-{{ item.no }}" name="subtask_title" maxlength="100" placeholder="เช่น ทดสอบระบบ" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`subtask-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เพิ่มงานย่อย`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`subtask-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`subtask_title`: key ที่ส่งไปใน form
- `maxlength`=`100`: จำนวนอักขระสูงสุดในช่อง
- `placeholder`=`เช่น ทดสอบระบบ`: ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L90

```html
            <button class="btn ghost" type="submit">+ เพิ่มขั้นตอน</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn ghost`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `+ เพิ่มขั้นตอน`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L91

```html
          </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L92

```html
          {% endif %}
```

- จบเงื่อนไข: `endif`

### L93

```html
          <p class="note">ติ๊กงานย่อยแล้วให้บันทึกเวลาที่ใช้แยกกัน เปอร์เซ็นต์หลักคำนวณจากชั่วโมง</p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ติ๊กงานย่อยแล้วให้บันทึกเวลาที่ใช้แยกกัน เปอร์เซ็นต์หลักคำนวณจากชั่วโมง`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L94

```html
        </section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L95

```html
        <section class="deadline-work-section" aria-labelledby="edit-heading-{{ item.no }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-work-section`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-labelledby`=`edit-heading-{{ item.no }}`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L96

```html
          <h4 id="edit-heading-{{ item.no }}">แก้ไขข้อมูลงาน</h4>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- เปิด `<h4>`: หัวข้อย่อยในรายละเอียด
- `id`=`edit-heading-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `แก้ไขข้อมูลงาน`
- ปิด `</h4>` ที่เปิดไว้ก่อนหน้า

### L97

```html
          <form method="post" class="deadline-edit-form" data-assignment-form data-today="{{ today }}" data-original-date="{{ item.due_date }}">
```

- แสดงค่าจาก context/นิพจน์ Jinja: `today`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.due_date`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `class`=`deadline-edit-form`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `data-assignment-form`: marker ให้ forms.js ผูก validation
- `data-today`=`{{ today }}`: วันที่อ้างอิงจาก Python ให้ forms.js
- `data-original-date`=`{{ item.due_date }}`: วันเดิมเพื่อไม่ยืนยันอดีตเดิมซ้ำ

### L98

```html
            {{ row_fields(item) }}<input type="hidden" name="action" value="update">
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`update`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key

### L99

```html
            <p class="deadline-form-error" role="alert" hidden></p>
```

- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`deadline-form-error`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `role`=`alert`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- `hidden`: ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า

### L100

```html
            <div class="field"><label for="title-{{ item.no }}">ชื่องาน</label><input id="title-{{ item.no }}" name="title" value="{{ item.title }}" maxlength="80" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.title`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`title-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชื่องาน`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`title-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`title`: key ที่ส่งไปใน form
- `value`=`{{ item.title }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `maxlength`=`80`: จำนวนอักขระสูงสุดในช่อง
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L101

```html
            <div class="field"><label for="course-{{ item.no }}">วิชาที่เกี่ยวข้อง</label><input id="course-{{ item.no }}" name="course" value="{{ item.course }}" maxlength="40" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.course`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`course-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วิชาที่เกี่ยวข้อง`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`course-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`course`: key ที่ส่งไปใน form
- `value`=`{{ item.course }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `maxlength`=`40`: จำนวนอักขระสูงสุดในช่อง
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L102

```html
            <div class="field"><label for="date-{{ item.no }}">วันส่งงาน</label><input id="date-{{ item.no }}" name="due_date" type="date" value="{{ item.due_date }}" required></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.due_date`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`date-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันส่งงาน`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`date-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`due_date`: key ที่ส่งไปใน form
- `type`=`date`: ชนิดช่องหรือปุ่ม
- `value`=`{{ item.due_date }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L103

```html
            <label class="deadline-past-confirm" data-past-warning hidden><input type="checkbox" name="acknowledge_past" value="yes"> ยืนยันเปลี่ยนวันส่งเป็นวันที่ผ่านไปแล้ว</label>
```

- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `class`=`deadline-past-confirm`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `data-past-warning`: marker กล่องยืนยันวันที่อดีต
- `hidden`: ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`checkbox`: ชนิดช่องหรือปุ่ม
- `name`=`acknowledge_past`: key ที่ส่งไปใน form
- `value`=`yes`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยืนยันเปลี่ยนวันส่งเป็นวันที่ผ่านไปแล้ว`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า

### L104

```html
            <div class="field-row">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L105

```html
              <div class="field"><label for="hours-{{ item.no }}">เวลาที่คาดว่าจะใช้ทั้งหมด</label><input id="hours-{{ item.no }}" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" value="{{ item.estimated_hours }}" aria-describedby="hours-help-{{ item.no }}" required><small id="hours-help-{{ item.no }}" class="deadline-help">ชั่วโมงรวมทั้งงาน รวมส่วนที่ทำแล้ว</small></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.estimated_hours`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`hours-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาที่คาดว่าจะใช้ทั้งหมด`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`hours-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`estimated_hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0.1`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`200`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `value`=`{{ item.estimated_hours }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `aria-describedby`=`hours-help-{{ item.no }}`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- เปิด `<small>`: ข้อความประกอบ
- `id`=`hours-help-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมงรวมทั้งงาน รวมส่วนที่ทำแล้ว`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L106

```html
              <div class="field"><label for="done-{{ item.no }}">เวลาที่ทำไปแล้วทั้งหมด</label><input id="done-{{ item.no }}" name="done_hours" type="number" min="0" max="{{ item.estimated_hours }}" step="0.1" value="{{ item.done_hours }}" aria-describedby="done-help-{{ item.no }}" required><small id="done-help-{{ item.no }}" class="deadline-help">ปรับยอดสะสมเดิม ใช้ “บันทึกเวลา” ด้านบนสำหรับการทำงานครั้งใหม่</small></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.estimated_hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `item.done_hours`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`done-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เวลาที่ทำไปแล้วทั้งหมด`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `id`=`done-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`done_hours`: key ที่ส่งไปใน form
- `type`=`number`: ชนิดช่องหรือปุ่ม
- `min`=`0`: ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์
- `max`=`{{ item.estimated_hours }}`: ค่าสูงสุดที่ช่องรับในเบราว์เซอร์
- `step`=`0.1`: ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข
- `value`=`{{ item.done_hours }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `aria-describedby`=`done-help-{{ item.no }}`: id ของข้อความช่วยอธิบาย
- `required`: ให้เบราว์เซอร์บังคับค่าตามชนิด
- เปิด `<small>`: ข้อความประกอบ
- `id`=`done-help-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `class`=`deadline-help`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ปรับยอดสะสมเดิม ใช้ “บันทึกเวลา” ด้านบนสำหรับการทำงานครั้งใหม่`
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L107

```html
            </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L108

```html
            <div class="field-row">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`field-row`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง

### L109

```html
              <div class="field"><label for="priority-{{ item.no }}">ความสำคัญ</label><select id="priority-{{ item.no }}" name="priority">{% for value, label in [('high','สูง'),('normal','ปกติ'),('low','ต่ำ')] %}<option value="{{ value }}" {{ 'selected' if item.priority == value }}>{{ label }}</option>{% endfor %}</select></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- วน list จาก context: `for value, label in [('high','สูง'),('normal','ปกติ'),('low','ต่ำ')]`
- แสดงค่าจาก context/นิพจน์ Jinja: `value`
- แสดงค่าจาก context/นิพจน์ Jinja: `'selected' if item.priority == value`
- แสดงค่าจาก context/นิพจน์ Jinja: `label`
- จบ for: `endfor`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`priority-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ความสำคัญ`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<select>`: ตัวเลือก
- `id`=`priority-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`priority`: key ที่ส่งไปใน form
- เปิด `<option>`: ตัวเลือกหนึ่งค่า
- `value`=`{{ value }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `jinja_mark_97_end`: attribute ตาม HTML/DOM ที่ส่วนนี้ใช้งาน
- ปิด `</option>` ที่เปิดไว้ก่อนหน้า
- ปิด `</select>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L110

```html
              <div class="field"><label for="owner-{{ item.no }}">ผู้รับผิดชอบ</label><select id="owner-{{ item.no }}" name="owner"><option value="">ยังไม่มอบหมาย</option>{% for member in members %}<option value="{{ member.id }}" {{ 'selected' if item.details.owner == member.id }}>{{ member.name }}</option>{% endfor %}</select></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `item.no`
- วน list จาก context: `for member in members`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.id`
- แสดงค่าจาก context/นิพจน์ Jinja: `'selected' if item.details.owner == member.id`
- แสดงค่าจาก context/นิพจน์ Jinja: `member.name`
- จบ for: `endfor`
- เปิด `<div>`: กลุ่ม layout
- `class`=`field`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<label>`: ชื่อ/คำอธิบายของช่อง
- `for`=`owner-{{ item.no }}`: id ของช่องที่ label อธิบาย
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ผู้รับผิดชอบ`
- ปิด `</label>` ที่เปิดไว้ก่อนหน้า
- เปิด `<select>`: ตัวเลือก
- `id`=`owner-{{ item.no }}`: ชื่อเฉพาะ DOM/anchor/label
- `name`=`owner`: key ที่ส่งไปใน form
- เปิด `<option>`: ตัวเลือกหนึ่งค่า
- `value`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยังไม่มอบหมาย`
- ปิด `</option>` ที่เปิดไว้ก่อนหน้า
- `value`=`{{ member.id }}`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- `jinja_mark_104_end`: attribute ตาม HTML/DOM ที่ส่วนนี้ใช้งาน
- ปิด `</select>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L111

```html
            </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L112

```html
            <button class="btn" type="submit">บันทึกการแก้ไข</button>
```

- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกการแก้ไข`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า

### L113

```html
          </form>
```

- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L114

```html
        </section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L115

```html
        <form method="post" class="deadline-delete-form" onsubmit="return confirm('ลบงานนี้พร้อมงานย่อยและประวัติหรือไม่?')">{{ row_fields(item) }}<input type="hidden" name="action" value="delete"><button class="btn danger" type="submit">ลบงานนี้</button></form>
```

- เรียก macro ใส่ no/version ซ่อนใน form: `row_fields(item)`
- เปิด `<form>`: ชุดข้อมูลที่จะส่ง
- `method`=`post`: วิธีส่ง form (post ไป handle)
- `class`=`deadline-delete-form`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `onsubmit`=`return confirm('ลบงานนี้พร้อมงานย่อยและประวัติหรือไม่?')`: JavaScript เมื่อส่ง form; confirm ลบข้อมูล
- เปิด `<input>`: ช่องรับ/ค่าซ่อน
- `type`=`hidden`: ชนิดช่องหรือปุ่ม
- `name`=`action`: key ที่ส่งไปใน form
- `value`=`delete`: ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key
- เปิด `<button>`: ปุ่มกระทำ
- `class`=`btn danger`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `type`=`submit`: ชนิดช่องหรือปุ่ม
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ลบงานนี้`
- ปิด `</button>` ที่เปิดไว้ก่อนหน้า
- ปิด `</form>` ที่เปิดไว้ก่อนหน้า

### L116

```html
      </details>
```

- ปิด `</details>` ที่เปิดไว้ก่อนหน้า

### L117

```html
    </article>
```

- ปิด `</article>` ที่เปิดไว้ก่อนหน้า

### L118

```html
    {% else %}<div class="empty">ยังไม่มีงานที่บันทึกไว้</div>{% endfor %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบ for: `endfor`
- เปิด `<div>`: กลุ่ม layout
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ยังไม่มีงานที่บันทึกไว้`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L119

```html
  </section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L120

```html
</div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L121

(บรรทัดว่าง)

- บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม

### L122

```html
<section class="deadline-history-section" aria-labelledby="history-heading">
```

- เปิด `<section>`: ส่วนเนื้อหาที่มีหัวข้อ
- `class`=`deadline-history-section`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `aria-labelledby`=`history-heading`: id ของข้อความที่ตั้งชื่อส่วนนี้

### L123

```html
  <div class="deadline-section-head"><div><h2 id="history-heading">ประวัติการทำงาน</h2><p class="note">ชั่วโมงทำจริงที่บันทึก {{ actual_total }} ชั่วโมง · การปรับยอดและการกดปิดงานแสดงแยกประเภท</p></div></div>
```

- แสดงค่าจาก context/นิพจน์ Jinja: `actual_total`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-section-head`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<h2>`: หัวข้อส่วน
- `id`=`history-heading`: ชื่อเฉพาะ DOM/anchor/label
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ประวัติการทำงาน`
- ปิด `</h2>` ที่เปิดไว้ก่อนหน้า
- เปิด `<p>`: ย่อหน้าหรือคำอธิบาย
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมงทำจริงที่บันทึก {{ actual_total }} ชั่วโมง · การปรับยอดและการกดปิดงานแสดงแยกประเภท`
- ปิด `</p>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L124

```html
  {% if history %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if history`

### L125

```html
  {% if daily_history %}<div class="deadline-daily-history">{% for day in daily_history %}<div class="panel"><time datetime="{{ day.date }}">{{ day.date }}</time><strong>{{ day.hours }} ชั่วโมง</strong><span class="note">บันทึกเวลาจริง {{ day.count }} ครั้ง</span></div>{% endfor %}</div>{% endif %}
```

- ตรวจเงื่อนไขก่อนแสดง HTML: `if daily_history`
- วน list จาก context: `for day in daily_history`
- แสดงค่าจาก context/นิพจน์ Jinja: `day.date`
- แสดงค่าจาก context/นิพจน์ Jinja: `day.hours`
- แสดงค่าจาก context/นิพจน์ Jinja: `day.count`
- จบ for: `endfor`
- จบเงื่อนไข: `endif`
- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-daily-history`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `class`=`panel`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- เปิด `<time>`: ข้อมูลวันที่ที่มีความหมาย
- `datetime`=`{{ day.date }}`: วันที่มาตรฐานของ time
- ปิด `</time>` ที่เปิดไว้ก่อนหน้า
- เปิด `<strong>`: ข้อความที่เน้น
- ปิด `</strong>` ที่เปิดไว้ก่อนหน้า
- เปิด `<span>`: ข้อความย่อยในบรรทัด
- `class`=`note`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `บันทึกเวลาจริง {{ day.count }} ครั้ง`
- ปิด `</span>` ที่เปิดไว้ก่อนหน้า
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L126

```html
  <div class="deadline-table-scroll" tabindex="0" role="region" aria-label="ประวัติการทำงาน เลื่อนแนวนอนเพื่อดูครบ">
```

- เปิด `<div>`: กลุ่ม layout
- `class`=`deadline-table-scroll`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- `tabindex`=`0`: ลำดับ/ความสามารถรับ focus จากคีย์บอร์ด
- `role`=`region`: บทบาทเชิงความหมายให้เครื่องมือเข้าถึง
- `aria-label`=`ประวัติการทำงาน เลื่อนแนวนอนเพื่อดูครบ`: คำอธิบายสำหรับเครื่องมืออ่านหน้าจอ

### L127

```html
    <table><thead><tr><th>วันที่</th><th>งาน / ผู้รับผิดชอบ</th><th class="num">ชั่วโมง</th><th>ประเภท / หมายเหตุ</th></tr></thead><tbody>
```

- เปิด `<table>`: ตาราง
- เปิด `<thead>`: หัวตาราง
- เปิด `<tr>`: แถว
- เปิด `<th>`: ชื่อคอลัมน์
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `วันที่`
- ปิด `</th>` ที่เปิดไว้ก่อนหน้า
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `งาน / ผู้รับผิดชอบ`
- `class`=`num`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ชั่วโมง`
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `ประเภท / หมายเหตุ`
- ปิด `</tr>` ที่เปิดไว้ก่อนหน้า
- ปิด `</thead>` ที่เปิดไว้ก่อนหน้า
- เปิด `<tbody>`: เนื้อตาราง

### L128

```html
      {% for entry in history %}<tr><td><time datetime="{{ entry.date }}">{{ entry.date }}</time></td><td>{{ entry.title }}<br><small>{{ entry.owner_name }}</small></td><td class="num">{{ "{:,.1f}".format(entry.hours) }}</td><td>{{ entry.label }}{% if entry.note %}<br><small>{{ entry.note }}</small>{% endif %}</td></tr>{% endfor %}
```

- วน list จาก context: `for entry in history`
- แสดงค่าจาก context/นิพจน์ Jinja: `entry.date`
- แสดงค่าจาก context/นิพจน์ Jinja: `entry.title`
- แสดงค่าจาก context/นิพจน์ Jinja: `entry.owner_name`
- แสดงค่าจาก context/นิพจน์ Jinja: `"{:,.1f}".format(entry.hours)`
- แสดงค่าจาก context/นิพจน์ Jinja: `entry.label`
- ตรวจเงื่อนไขก่อนแสดง HTML: `if entry.note`
- แสดงค่าจาก context/นิพจน์ Jinja: `entry.note`
- จบเงื่อนไข: `endif`
- จบ for: `endfor`
- เปิด `<tr>`: แถว
- เปิด `<td>`: ช่องข้อมูล
- เปิด `<time>`: ข้อมูลวันที่ที่มีความหมาย
- `datetime`=`{{ entry.date }}`: วันที่มาตรฐานของ time
- ปิด `</time>` ที่เปิดไว้ก่อนหน้า
- ปิด `</td>` ที่เปิดไว้ก่อนหน้า
- เปิด `<br>`: ขึ้นบรรทัดใน HTML
- เปิด `<small>`: ข้อความประกอบ
- ปิด `</small>` ที่เปิดไว้ก่อนหน้า
- `class`=`num`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ปิด `</tr>` ที่เปิดไว้ก่อนหน้า

### L129

```html
    </tbody></table>
```

- ปิด `</tbody>` ที่เปิดไว้ก่อนหน้า
- ปิด `</table>` ที่เปิดไว้ก่อนหน้า

### L130

```html
  </div>
```

- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L131

```html
  {% else %}<div class="empty">เริ่มบันทึกเวลาของงาน แล้วประวัติรายวันจะแสดงที่นี่ ยอดเดิมที่ไม่มีวันที่จะไม่ถูกสร้างเป็นประวัติย้อนหลัง</div>{% endif %}
```

- ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ: `else`
- จบเงื่อนไข: `endif`
- เปิด `<div>`: กลุ่ม layout
- `class`=`empty`: ชื่อ class ที่ CSS ใช้เลือกตกแต่ง
- ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: `เริ่มบันทึกเวลาของงาน แล้วประวัติรายวันจะแสดงที่นี่ ยอดเดิมที่ไม่มีวันที่จะไม่ถูกสร้างเป็นประวัติย้อนหลัง`
- ปิด `</div>` ที่เปิดไว้ก่อนหน้า

### L132

```html
</section>
```

- ปิด `</section>` ที่เปิดไว้ก่อนหน้า

### L133

```html
{% endblock %}
```

- จบ block content/scripts: `endblock`

### L134

```html
{% block scripts %}<script src="{{ url_for('static', filename='js/forms.js') }}" defer></script>{% endblock %}
```

- เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน: `block scripts`
- สร้าง URL ผ่าน route เดิม: `url_for('static', filename='js/forms.js')`
- จบ block content/scripts: `endblock`
- เปิด `<script>`: script/JSON ตาม type
- `src`=`{{ url_for('static', filename='js/forms.js') }}`: ไฟล์ script ที่โหลด
- `defer`: รัน script ภายนอกหลังแยก HTML เสร็จ
- ปิด `</script>` ที่เปิดไว้ก่อนหน้า
