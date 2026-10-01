# docs/qa/test_reminders.cjs — ชุดทดสอบ JavaScript ด้วยส่วนจำลอง

อ้างอิงไฟล์ปัจจุบัน 1 ตุลาคม 2569 (2026-10-01); 97 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `02975c5a1427c25a0eb222d4a035477bcd2746b494d6d5591f2b91b020aa7b57`

**ผู้ศึกษา/บทบาท:** QA

## 1. หน้าที่และการเชื่อมต่อ

ตรวจเกณฑ์เตือน การดึงข้อมูลใหม่ การไม่ซ้ำ ข้อจำกัดสิทธิ์ และข้อความ ICS

- **รับเข้า:** reminders.js และ DOM/Notification/fetch จำลองใน vm
- **ผลลัพธ์:** Node test ผ่าน/ไม่ผ่าน 4 กรณี

**เกี่ยวข้องกับ:** node:test/node:assert/node:vm/node:fs/node:path (built-in)

## 2. ลำดับทำงาน

1. อ่าน source แล้วสร้าง harness ที่ใช้เวลาอ้างอิงคงที่
2. จำลอง window/document/localStorage/fetch และ Notification
3. รัน source ใน context จำลอง
4. assert เกณฑ์ pending และ signature เมื่อ polling
5. assert DTSTART/DTEND ข้ามเดือนและ escape ข้อความ

## 3. จุดที่ต้องอธิบายให้ถูก

- ไม่เปิด browser และไม่ขอสิทธิ์ OS จริง
- ใช้ Node ที่มีอยู่แล้ว ไม่ติดตั้ง dependency เพื่อรันแอป
- FixedDate ใน test เป็นวันที่ควบคุม ไม่ใช่วันที่ของแอปจริง

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q095: ชุด Node พิสูจน์ว่าแจ้งเตือนเด้งจริงหรือไม่?](../../../TEACHER_QUESTIONS.md#q095)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `harness` | เริ่ม L9 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `task` | เริ่ม L49 | ฟังก์ชัน JavaScript ตามส่วนนี้ |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```javascript
// Unit tests for reminder decisions; no browser or OS permission is changed.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');
const source = fs.readFileSync(path.join(__dirname, '../../static/js/reminders.js'), 'utf8');

function harness(tasks, permission = 'granted', supported = true) {
  const result = { notifications: [], stored: new Map(), events: {}, next: tasks };
  const elements = {
    'reminder-data': { textContent: JSON.stringify(tasks) },
    'enable-reminders': { addEventListener: (name, action) => { result.click = action; } },
    'reminder-status': {}, 'reminder-refresh': { hidden: true }
  };
  class FixedDate extends Date {
    constructor(...args) { super(...(args.length ? args : ['2026-09-30T06:00:00Z'])); }
  }
  class Notice {
    static permission = permission;
    static async requestPermission() { Notice.permission = 'granted'; return 'granted'; }
    constructor(title, options) { result.notifications.push({ title, ...options }); }
  }
  const context = {
    Date: FixedDate, Blob, AbortController, console,
    document: {
      getElementById: id => elements[id], hidden: false,
      addEventListener: (name, action) => { result.events[name] = action; },
      body: { appendChild() {} },
      createElement: () => ({ click() { result.download = this.download; }, remove() {} })
    },
    window: { isSecureContext: true, location: { pathname: '/page1' }, focus() {},
      setInterval: fn => { result.interval = fn; }, setTimeout: () => 1, clearTimeout() {} },
    localStorage: { getItem: key => result.stored.get(key),
      setItem: (key, value) => result.stored.set(key, value) },
    fetch: async () => ({ ok: true, text: async () => JSON.stringify(result.next) }),
    DOMParser: class {
      parseFromString(text) { return { getElementById: () => ({ textContent: text }) }; }
    },
    URL: { createObjectURL: blob => { result.calendar = blob; return 'blob:test'; },
      revokeObjectURL() {} }
  };
  if (supported) { context.Notification = Notice; context.window.Notification = Notice; }
  vm.runInNewContext(source, context);
  result.elements = elements;
  return result;
}

function task(changes = {}) {
  return { title: 'งานทดสอบ', due_date: '2026-10-20', remaining_hours: 4,
    at_risk: false, stale: false, today_hours: 0, ...changes };
}

test('each requested reminder condition qualifies; completed tasks never qualify', () => {
  for (const changes of [{ due_date: '2026-10-02' }, { due_date: '2026-09-29' },
    { at_risk: true }, { today_hours: 2 }, { stale: true }]) {
    assert.equal(harness([task(changes)]).notifications.length, 1);
    assert.equal(harness([task({ ...changes, remaining_hours: 0 })]).notifications.length, 0);
  }
  assert.equal(harness([task()]).notifications.length, 0);
});

test('polling deduplicates unchanged data and picks up new tasks', async () => {
  const state = harness([task({ today_hours: 2 })]);
  await state.interval();
  assert.equal(state.notifications.length, 1);
  state.next = [task({ title: 'งานใหม่เกินกำหนด', due_date: '2026-09-29', at_risk: true })];
  await state.interval();
  assert.equal(state.notifications.length, 2);
  assert.match(state.notifications[1].body, /งานใหม่เกินกำหนด/);
  assert.match(state.notifications[1].body, /เกินกำหนด 1 งาน/);
  assert.equal(state.elements['reminder-refresh'].hidden, false);
  await state.interval();
  assert.equal(state.notifications.length, 2);
});

test('denied or unsupported notifications show a usable fallback', () => {
  const denied = harness([task({ stale: true })], 'denied');
  assert.equal(denied.notifications.length, 0);
  assert.equal(denied.elements['enable-reminders'].disabled, true);
  const missing = harness([], 'default', false);
  assert.equal(missing.elements['enable-reminders'].disabled, true);
  assert.match(missing.elements['reminder-status'].textContent, /ไฟล์ปฏิทิน/);
});

test('calendar spans one all-day date across month boundaries and escapes text', async () => {
  const state = harness([]);
  state.events.click({ target: { closest: () => ({ dataset: {
    calendarDate: '2026-01-31', calendarTitle: 'งาน, A; B\nC', calendarCourse: 'วิชาทดสอบ'
  } }) } });
  const text = await state.calendar.text();
  assert.match(text, /DTSTART;VALUE=DATE:20260131\r\n/);
  assert.match(text, /DTEND;VALUE=DATE:20260201\r\n/);
  assert.ok(text.includes('SUMMARY:ส่งงาน: งาน\\, A\\; B\\nC'));
  assert.match(text, /TRIGGER:-P1D/);
  assert.equal(state.download, 'deadline-2026-01-31.ics');
});
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```javascript
// Unit tests for reminder decisions; no browser or OS permission is changed.
```

- comment สำหรับคนอ่าน: // Unit tests for reminder decisions; no browser or OS permission is changed.

### L2

```javascript
const assert = require('node:assert/strict');
```

- สร้างตัวแปร `assert` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L3

```javascript
const fs = require('node:fs');
```

- สร้างตัวแปร `fs` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L4

```javascript
const path = require('node:path');
```

- สร้างตัวแปร `path` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L5

```javascript
const test = require('node:test');
```

- สร้างตัวแปร `test` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L6

```javascript
const vm = require('node:vm');
```

- สร้างตัวแปร `vm` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L7

```javascript
const source = fs.readFileSync(path.join(__dirname, '../../static/js/reminders.js'), 'utf8');
```

- สร้างตัวแปร `source` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `readFileSync()`: อ่าน reminders.js สำหรับ Node test
- `join()`: ต่อรายการเป็นข้อความ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L8

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L9

```javascript
function harness(tasks, permission = 'granted', supported = true) {
```

- ประกาศ `harness` รับ `tasks, permission = 'granted', supported = true`; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L10

```javascript
  const result = { notifications: [], stored: new Map(), events: {}, next: tasks };
```

- สร้างตัวแปร `result` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `{`, `[`, `]`, `(`, `)`, `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L11

```javascript
  const elements = {
```

- สร้างตัวแปร `elements` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L12

```javascript
    'reminder-data': { textContent: JSON.stringify(tasks) },
```

- serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ
- เครื่องหมายที่พบ: `{`, `(`, `)`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L13

```javascript
    'enable-reminders': { addEventListener: (name, action) => { result.click = action; } },
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `{`, `(`, `)`, `=>`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L14

```javascript
    'reminder-status': {}, 'reminder-refresh': { hidden: true }
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L15

```javascript
  };
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L16

```javascript
  class FixedDate extends Date {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L17

```javascript
    constructor(...args) { super(...(args.length ? args : ['2026-09-30T06:00:00Z'])); }
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `{`, `[`, `]`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L18

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L19

```javascript
  class Notice {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L20

```javascript
    static permission = permission;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L21

```javascript
    static async requestPermission() { Notice.permission = 'granted'; return 'granted'; }
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `{`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L22

```javascript
    constructor(title, options) { result.notifications.push({ title, ...options }); }
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `{`, `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L23

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L24

```javascript
  const context = {
```

- สร้างตัวแปร `context` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L25

```javascript
    Date: FixedDate, Blob, AbortController, console,
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ

### L26

```javascript
    document: {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L27

```javascript
      getElementById: id => elements[id], hidden: false,
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `=>`, `[`, `]`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L28

```javascript
      addEventListener: (name, action) => { result.events[name] = action; },
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`, `[`, `]`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L29

```javascript
      body: { appendChild() {} },
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`, `(`, `)`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L30

```javascript
      createElement: () => ({ click() { result.download = this.download; }, remove() {} })
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L31

```javascript
    },
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L32

```javascript
    window: { isSecureContext: true, location: { pathname: '/page1' }, focus() {},
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`, `}`, `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L33

```javascript
      setInterval: fn => { result.interval = fn; }, setTimeout: () => 1, clearTimeout() {} },
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `=>`, `{`, `;`, `}`, `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L34

```javascript
    localStorage: { getItem: key => result.stored.get(key),
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `{`, `=>`, `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L35

```javascript
      setItem: (key, value) => result.stored.set(key, value) },
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L36

```javascript
    fetch: async () => ({ ok: true, text: async () => JSON.stringify(result.next) }),
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L37

```javascript
    DOMParser: class {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L38

```javascript
      parseFromString(text) { return { getElementById: () => ({ textContent: text }) }; }
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `{`, `=>`, `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L39

```javascript
    },
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L40

```javascript
    URL: { createObjectURL: blob => { result.calendar = blob; return 'blob:test'; },
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `{`, `=>`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L41

```javascript
      revokeObjectURL() {} }
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `{`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L42

```javascript
  };
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L43

```javascript
  if (supported) { context.Notification = Notice; context.window.Notification = Notice; }
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `{`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L44

```javascript
  vm.runInNewContext(source, context);
```

- `runInNewContext()`: รัน source ในส่วนจำลอง Node vm ไม่ใช่ browser จริง
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L45

```javascript
  result.elements = elements;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L46

```javascript
  return result;
```

- คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L47

```javascript
}
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L48

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L49

```javascript
function task(changes = {}) {
```

- ประกาศ `task` รับ `changes = {}`; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `{`, `}`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L50

```javascript
  return { title: 'งานทดสอบ', due_date: '2026-10-20', remaining_hours: 4,
```

- คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L51

```javascript
    at_risk: false, stale: false, today_hours: 0, ...changes };
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L52

```javascript
}
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L53

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L54

```javascript
test('each requested reminder condition qualifies; completed tasks never qualify', () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `;`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L55

```javascript
  for (const changes of [{ due_date: '2026-10-02' }, { due_date: '2026-09-29' },
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `[`, `{`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L56

```javascript
    { at_risk: true }, { today_hours: 2 }, { stale: true }]) {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `{`, `}`, `]`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L57

```javascript
    assert.equal(harness([task(changes)]).notifications.length, 1);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L58

```javascript
    assert.equal(harness([task({ ...changes, remaining_hours: 0 })]).notifications.length, 0);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `{`, `}`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L59

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L60

```javascript
  assert.equal(harness([task()]).notifications.length, 0);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L61

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L62

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L63

```javascript
test('polling deduplicates unchanged data and picks up new tasks', async () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L64

```javascript
  const state = harness([task({ today_hours: 2 })]);
```

- สร้างตัวแปร `state` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `[`, `{`, `}`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L65

```javascript
  await state.interval();
```

- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L66

```javascript
  assert.equal(state.notifications.length, 1);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L67

```javascript
  state.next = [task({ title: 'งานใหม่เกินกำหนด', due_date: '2026-09-29', at_risk: true })];
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `[`, `(`, `{`, `}`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L68

```javascript
  await state.interval();
```

- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L69

```javascript
  assert.equal(state.notifications.length, 2);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L70

```javascript
  assert.match(state.notifications[1].body, /งานใหม่เกินกำหนด/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L71

```javascript
  assert.match(state.notifications[1].body, /เกินกำหนด 1 งาน/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L72

```javascript
  assert.equal(state.elements['reminder-refresh'].hidden, false);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L73

```javascript
  await state.interval();
```

- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L74

```javascript
  assert.equal(state.notifications.length, 2);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L75

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L76

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L77

```javascript
test('denied or unsupported notifications show a usable fallback', () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L78

```javascript
  const denied = harness([task({ stale: true })], 'denied');
```

- สร้างตัวแปร `denied` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `[`, `{`, `}`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L79

```javascript
  assert.equal(denied.notifications.length, 0);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L80

```javascript
  assert.equal(denied.elements['enable-reminders'].disabled, true);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L81

```javascript
  const missing = harness([], 'default', false);
```

- สร้างตัวแปร `missing` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L82

```javascript
  assert.equal(missing.elements['enable-reminders'].disabled, true);
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L83

```javascript
  assert.match(missing.elements['reminder-status'].textContent, /ไฟล์ปฏิทิน/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L84

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L85

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L86

```javascript
test('calendar spans one all-day date across month boundaries and escapes text', async () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L87

```javascript
  const state = harness([]);
```

- สร้างตัวแปร `state` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L88

```javascript
  state.events.click({ target: { closest: () => ({ dataset: {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `click()`: กระตุ้นดาวน์โหลดตามลิงก์
- เครื่องหมายที่พบ: `(`, `{`, `)`, `=>`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L89

```javascript
    calendarDate: '2026-01-31', calendarTitle: 'งาน, A; B\nC', calendarCourse: 'วิชาทดสอบ'
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L90

```javascript
  } }) } });
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L91

```javascript
  const text = await state.calendar.text();
```

- สร้างตัวแปร `text` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L92

```javascript
  assert.match(text, /DTSTART;VALUE=DATE:20260131\r\n/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `;`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L93

```javascript
  assert.match(text, /DTEND;VALUE=DATE:20260201\r\n/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `;`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L94

```javascript
  assert.ok(text.includes('SUMMARY:ส่งงาน: งาน\\, A\\; B\\nC'));
```

- `ok()`: assert เป็นจริง
- เครื่องหมายที่พบ: `(`, `;`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L95

```javascript
  assert.match(text, /TRIGGER:-P1D/);
```

- `match()`: assert ข้อความตรง regex
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L96

```javascript
  assert.equal(state.download, 'deadline-2026-01-31.ics');
```

- `equal()`: assert ค่าเท่ากันใน test
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L97

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม
