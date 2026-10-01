# static/js/forms.js — JavaScript ช่วยตรวจและใช้งานฟอร์ม

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 62 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `1e11f533d5c27e2e88eab61acb3c8b2b2dc83487e39e7ce33c2bd0a430db2bc2`

**ผู้ศึกษา/บทบาท:** ส่วนติดต่อผู้ใช้ของ Manage

## 1. หน้าที่และการเชื่อมต่อ

แจ้งช่องผิดทันที ช่วยยืนยันวันส่งอดีต เติมงานย่อย และเปิดการ์ดจากลิงก์

- **รับเข้า:** DOM ของ form, dataset.today/originalDate, ค่าช่อง และ location.hash
- **ผลลัพธ์:** สถานะ validation, aria-invalid, ข้อความเตือน และการเปิด details ในเบราว์เซอร์

**เกี่ยวข้องกับ:** templates/page2.html; Browser DOM/Constraint Validation API; ไม่มี package ภายนอก

## 2. ลำดับทำงาน

1. ผูกแต่ละ data-assignment-form กับ validate
2. ตรวจ trim ชื่อ/วิชา ยอดชั่วโมง และวันส่งที่เปลี่ยนเป็นอดีต
3. ผูก input/invalid/submit กับข้อความและการตรวจ
4. เติมขั้นตอนตัวอย่าง 6 ข้อเมื่อกดปุ่ม
5. openLinkedTask เปิดรายละเอียดการ์ดจาก #task-no และเลื่อนถึง

## 3. จุดที่ต้องอธิบายให้ถูก

- JavaScript ไม่เขียน JSON ของงาน และปิด JS แล้วยังมี Python ตรวจ
- ฟอร์มมีชื่อ input ที่โค้ดคาดไว้ เปลี่ยน name ต้องแก้ทั้งสองส่วน
- focus/scrollIntoView เปลี่ยนตำแหน่งอ่าน ไม่ใช่เปลี่ยนงานในไฟล์

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q044: เลือกวันส่งอดีตแล้วทำไมยังบันทึกได้?](../../../TEACHER_QUESTIONS.md#q044)
- [Q045: ถ้าปิด JavaScript จะข้าม validation ได้หรือไม่?](../../../TEACHER_QUESTIONS.md#q045)
- [Q047: งานย่อยมีข้อจำกัดอะไร?](../../../TEACHER_QUESTIONS.md#q047)
- [Q071: forms.js มีหน้าที่อะไร?](../../../TEACHER_QUESTIONS.md#q071)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `validate` | เริ่ม L11 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `openLinkedTask` | เริ่ม L54 | ฟังก์ชัน JavaScript ตามส่วนนี้ |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```javascript
// Browser hints complement Python validation; they do not replace it.
document.querySelectorAll("[data-assignment-form]").forEach((form) => {
  const due = form.elements.due_date;
  const estimate = form.elements.estimated_hours;
  const done = form.elements.done_hours;
  const confirmation = form.querySelector("[data-past-warning]");
  const checkbox = form.elements.acknowledge_past;
  const message = form.querySelector(".deadline-form-error");
  const today = form.dataset.today;

  function validate() {
    form.elements.title.setCustomValidity(form.elements.title.value.trim() ? "" : "กรุณากรอกชื่องาน");
    form.elements.course.setCustomValidity(form.elements.course.value.trim() ? "" : "กรุณากรอกวิชา");
    if (estimate.value !== "") done.max = estimate.value;
    done.setCustomValidity(Number(done.value) > Number(estimate.value)
      ? "เวลาที่ทำแล้วต้องไม่เกินเวลาทั้งหมด" : "");
    const changedPast = due.value && due.value < today && due.value !== form.dataset.originalDate;
    confirmation.hidden = !changedPast;
    checkbox.required = Boolean(changedPast);
    if (!changedPast) checkbox.checked = false;
    form.querySelectorAll("input").forEach((input) => {
      input.setAttribute("aria-invalid", input.validity.valid ? "false" : "true");
    });
  }

  form.addEventListener("input", () => {
    validate();
    message.hidden = true;
  });
  form.addEventListener("invalid", (event) => {
    message.hidden = false;
    message.textContent = event.target.validationMessage || "กรุณาตรวจช่องที่ยังไม่ถูกต้อง";
  }, true);
  form.addEventListener("submit", (event) => {
    validate();
    if (!form.checkValidity()) {
      event.preventDefault();
      form.reportValidity();
    }
  });
  validate();
});

document.querySelectorAll("[data-subtask-template]").forEach((button) => {
  button.addEventListener("click", () => {
    const input = document.getElementById(button.dataset.subtaskTemplate);
    if (input.value.trim() && !window.confirm("แทนรายการงานย่อยเดิมด้วยขั้นตอนตัวอย่างหรือไม่?")) return;
    input.value = ["วิเคราะห์ปัญหา", "ออกแบบระบบ", "เขียนโปรแกรม",
      "ทดสอบระบบ", "แก้ไขข้อผิดพลาด", "เตรียมส่งงาน"].join("\n");
    input.focus();
  });
});

function openLinkedTask() {
  const target = document.getElementById(window.location.hash.slice(1));
  if (!target || !target.classList.contains("deadline-edit-card")) return;
  const details = target.querySelector(".deadline-work-details");
  if (details) details.open = true;
  target.scrollIntoView({ block: "start" });
}
openLinkedTask();
window.addEventListener("hashchange", openLinkedTask);
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```javascript
// Browser hints complement Python validation; they do not replace it.
```

- comment สำหรับคนอ่าน: // Browser hints complement Python validation; they do not replace it.

### L2

```javascript
document.querySelectorAll("[data-assignment-form]").forEach((form) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `querySelectorAll()`: เลือก DOM ที่ตรง selector ทั้งชุด
- `forEach()`: ทำ callback ต่อสมาชิก
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L3

```javascript
  const due = form.elements.due_date;
```

- สร้างตัวแปร `due` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L4

```javascript
  const estimate = form.elements.estimated_hours;
```

- สร้างตัวแปร `estimate` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L5

```javascript
  const done = form.elements.done_hours;
```

- สร้างตัวแปร `done` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L6

```javascript
  const confirmation = form.querySelector("[data-past-warning]");
```

- สร้างตัวแปร `confirmation` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `querySelector()`: เลือก DOM ที่ตรง selectorหนึ่ง element
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L7

```javascript
  const checkbox = form.elements.acknowledge_past;
```

- สร้างตัวแปร `checkbox` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L8

```javascript
  const message = form.querySelector(".deadline-form-error");
```

- สร้างตัวแปร `message` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `querySelector()`: เลือก DOM ที่ตรง selectorหนึ่ง element
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L9

```javascript
  const today = form.dataset.today;
```

- สร้างตัวแปร `today` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L10

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L11

```javascript
  function validate() {
```

- ประกาศ `validate` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L12

```javascript
    form.elements.title.setCustomValidity(form.elements.title.value.trim() ? "" : "กรุณากรอกชื่องาน");
```

- `setCustomValidity()`: ตั้ง/ล้างข้อความ validation ของช่อง
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L13

```javascript
    form.elements.course.setCustomValidity(form.elements.course.value.trim() ? "" : "กรุณากรอกวิชา");
```

- `setCustomValidity()`: ตั้ง/ล้างข้อความ validation ของช่อง
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L14

```javascript
    if (estimate.value !== "") done.max = estimate.value;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `!==`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L15

```javascript
    done.setCustomValidity(Number(done.value) > Number(estimate.value)
```

- `setCustomValidity()`: ตั้ง/ล้างข้อความ validation ของช่อง
- เครื่องหมายที่พบ: `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L16

```javascript
      ? "เวลาที่ทำแล้วต้องไม่เกินเวลาทั้งหมด" : "");
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L17

```javascript
    const changedPast = due.value && due.value < today && due.value !== form.dataset.originalDate;
```

- สร้างตัวแปร `changedPast` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `&&`, `!==`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L18

```javascript
    confirmation.hidden = !changedPast;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L19

```javascript
    checkbox.required = Boolean(changedPast);
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L20

```javascript
    if (!changedPast) checkbox.checked = false;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L21

```javascript
    form.querySelectorAll("input").forEach((input) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `querySelectorAll()`: เลือก DOM ที่ตรง selector ทั้งชุด
- `forEach()`: ทำ callback ต่อสมาชิก
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L22

```javascript
      input.setAttribute("aria-invalid", input.validity.valid ? "false" : "true");
```

- `setAttribute()`: เปลี่ยน attribute ใน DOM
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L23

```javascript
    });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L24

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L25

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L26

```javascript
  form.addEventListener("input", () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L27

```javascript
    validate();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L28

```javascript
    message.hidden = true;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L29

```javascript
  });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L30

```javascript
  form.addEventListener("invalid", (event) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L31

```javascript
    message.hidden = false;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L32

```javascript
    message.textContent = event.target.validationMessage || "กรุณาตรวจช่องที่ยังไม่ถูกต้อง";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `||`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L33

```javascript
  }, true);
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L34

```javascript
  form.addEventListener("submit", (event) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L35

```javascript
    validate();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L36

```javascript
    if (!form.checkValidity()) {
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- `checkValidity()`: ตรวจ form ตาม constraint
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L37

```javascript
      event.preventDefault();
```

- `preventDefault()`: หยุดการส่ง form ปกติ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L38

```javascript
      form.reportValidity();
```

- `reportValidity()`: ให้ browser แสดงจุดผิด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L39

```javascript
    }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L40

```javascript
  });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L41

```javascript
  validate();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L42

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L43

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L44

```javascript
document.querySelectorAll("[data-subtask-template]").forEach((button) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `querySelectorAll()`: เลือก DOM ที่ตรง selector ทั้งชุด
- `forEach()`: ทำ callback ต่อสมาชิก
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L45

```javascript
  button.addEventListener("click", () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L46

```javascript
    const input = document.getElementById(button.dataset.subtaskTemplate);
```

- สร้างตัวแปร `input` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L47

```javascript
    if (input.value.trim() && !window.confirm("แทนรายการงานย่อยเดิมด้วยขั้นตอนตัวอย่างหรือไม่?")) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `&&`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L48

```javascript
    input.value = ["วิเคราะห์ปัญหา", "ออกแบบระบบ", "เขียนโปรแกรม",
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `[`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L49

```javascript
      "ทดสอบระบบ", "แก้ไขข้อผิดพลาด", "เตรียมส่งงาน"].join("\n");
```

- `join()`: ต่อรายการเป็นข้อความ
- เครื่องหมายที่พบ: `]`, `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L50

```javascript
    input.focus();
```

- `focus()`: ย้าย focus ไป element/หน้าต่าง
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L51

```javascript
  });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L52

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L53

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L54

```javascript
function openLinkedTask() {
```

- ประกาศ `openLinkedTask` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L55

```javascript
  const target = document.getElementById(window.location.hash.slice(1));
```

- สร้างตัวแปร `target` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- `slice()`: ตัดช่วงข้อความ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L56

```javascript
  if (!target || !target.classList.contains("deadline-edit-card")) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `||`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L57

```javascript
  const details = target.querySelector(".deadline-work-details");
```

- สร้างตัวแปร `details` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `querySelector()`: เลือก DOM ที่ตรง selectorหนึ่ง element
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L58

```javascript
  if (details) details.open = true;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L59

```javascript
  target.scrollIntoView({ block: "start" });
```

- `scrollIntoView()`: เลื่อนให้เห็นการ์ด
- เครื่องหมายที่พบ: `(`, `{`, `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L60

```javascript
}
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L61

```javascript
openLinkedTask();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L62

```javascript
window.addEventListener("hashchange", openLinkedTask);
```

- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม
