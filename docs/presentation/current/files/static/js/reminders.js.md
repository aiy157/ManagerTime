# static/js/reminders.js — JavaScript แจ้งเตือนและไฟล์ปฏิทิน

อ้างอิงไฟล์ปัจจุบัน 30 กันยายน 2569 (2026-09-30); 153 physical lines (รวมบรรทัดว่าง)

**SHA-256 ของไฟล์จริง:** `c55778563e6d78cc648e1cdb08c5323d3d5072100ea5ae670773af7d94fecc4a`

**ผู้ศึกษา/บทบาท:** Overview / ระบบเตือน

## 1. หน้าที่และการเชื่อมต่อ

เลือกงานที่ต้องเตือน ดึงข้อมูลใหม่ ลดการซ้ำ และสร้าง .ics

- **รับเข้า:** JSON reminder-data, สิทธิ์ Notification, localStorage, หน้า Overview และ dataset ปุ่มปฏิทิน
- **ผลลัพธ์:** Notification/ข้อความสถานะ/ลิงก์โหลดข้อมูลใหม่ และไฟล์ .ics

**เกี่ยวข้องกับ:** templates/page1.html; Browser Notification, fetch, DOMParser, AbortController, Blob, URL

## 2. ลำดับทำงาน

1. อ่าน JSON และตรวจความสามารถ/สิทธิ์
2. filter pending ที่ใกล้ส่ง/ค้าง/เสี่ยง/ทำวันนี้/ไม่อัปเดต
3. จำ signature ตามวันและสร้าง Notification เมื่อควรเตือน
4. poll ทุก 60000 ms และ visibilitychange; ตัด fetch ที่ 10000 ms
5. สร้าง VCALENDAR/VEVENT/VALARM กิจกรรมทั้งวันและดาวน์โหลด
6. ล้าง object URL หลังดาวน์โหลด

## 3. จุดที่ต้องอธิบายให้ถูก

- เมื่อปิดหน้า/โปรแกรม Python ไม่มีการเตือนเว็บต่อ ไม่ใช่ service worker/push
- daysUntil ใช้ปี/เดือน/วันของเบราว์เซอร์แล้วแปลง UTC เพื่อเปรียบเทียบระดับวัน
- signature ไม่ใช่ SHA/รหัสผ่าน และไม่รวมชั่วโมงทศนิยมทุกครั้ง
- เมื่อดึงใหม่ข้อมูลเตือนเปลี่ยน แต่รายการ DOM เดิมไม่ถูกแทนเอง
- ICS เตือนก่อน 1 วันเป็นคำขอที่แอปนำเข้าต้องรองรับ; กดซ้ำอาจสร้างกิจกรรมซ้ำ

## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์

- [Q073: ระบบเตือนงานประเภทใด?](../../../TEACHER_QUESTIONS.md#q073)
- [Q074: ผู้ใช้ต้องอนุญาตอะไร?](../../../TEACHER_QUESTIONS.md#q074)
- [Q075: ทำไมไม่เตือนซ้ำทุกนาที?](../../../TEACHER_QUESTIONS.md#q075)
- [Q076: ข้อมูลในอีกแท็บเปลี่ยน ระบบเตือนรู้ได้อย่างไร?](../../../TEACHER_QUESTIONS.md#q076)
- [Q077: ปิดเว็บแล้วแจ้งเตือนต่อหรือไม่?](../../../TEACHER_QUESTIONS.md#q077)
- [Q078: ถ้า server ไม่ตอบ การเตือนทำให้หน้าพังหรือไม่?](../../../TEACHER_QUESTIONS.md#q078)
- [Q079: ไฟล์ .ics สร้างกิจกรรมลักษณะใด?](../../../TEACHER_QUESTIONS.md#q079)
- [Q080: ทำไมต้อง escapeCalendarText และ revokeObjectURL?](../../../TEACHER_QUESTIONS.md#q080)

## 5. ฟังก์ชัน/คลาสและตำแหน่ง

| ชื่อ | บรรทัดจริง | หน้าที่ |
|---|---|---|
| `daysUntil` | เริ่ม L13 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `todayKey` | เริ่ม L21 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `updateStatus` | เริ่ม L27 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `checkReminders` | เริ่ม L43 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `refreshTasks` | เริ่ม L75 | ฟังก์ชัน JavaScript ตามส่วนนี้ |
| `escapeCalendarText` | เริ่ม L121 | ฟังก์ชัน JavaScript ตามส่วนนี้ |

## 7. โค้ดปัจจุบันครบทั้งไฟล์

คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง

```javascript
// Reminders refresh from the existing Overview page while it remains open.
const reminderData = document.getElementById("reminder-data");
const reminderButton = document.getElementById("enable-reminders");
const reminderStatus = document.getElementById("reminder-status");
const refreshNotice = document.getElementById("reminder-refresh");

if (reminderData && reminderButton && reminderStatus) {
  let tasks = JSON.parse(reminderData.textContent);
  let lastShownKey = "";
  let refreshing = false;
  const originalData = JSON.stringify(tasks);

  function daysUntil(dateText) {
    const parts = dateText.split("-").map(Number);
    const now = new Date();
    const due = Date.UTC(parts[0], parts[1] - 1, parts[2]);
    const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
    return Math.round((due - today) / 86400000);
  }

  function todayKey() {
    const now = new Date();
    return [now.getFullYear(), String(now.getMonth() + 1).padStart(2, "0"),
      String(now.getDate()).padStart(2, "0")].join("-");
  }

  function updateStatus() {
    reminderButton.disabled = false;
    if (!("Notification" in window) || !window.isSecureContext) {
      reminderStatus.textContent = "หน้านี้ไม่รองรับการแจ้งเตือน ใช้ไฟล์ปฏิทินได้";
      reminderButton.disabled = true;
    } else if (Notification.permission === "granted") {
      reminderStatus.textContent = "เปิดแล้ว · ตรวจงานใหม่ทุกนาทีขณะเปิดหน้านี้";
      reminderButton.textContent = "🔔 เปิดการแจ้งเตือนแล้ว";
    } else if (Notification.permission === "denied") {
      reminderStatus.textContent = "สิทธิ์ถูกปิดกั้น เปลี่ยนได้ในการตั้งค่าเว็บไซต์";
      reminderButton.disabled = true;
    } else {
      reminderStatus.textContent = "อนุญาตเพื่อเตือนงานวันนี้ งานใกล้ส่ง และแผนเสี่ยง";
    }
  }

  function checkReminders() {
    if (!("Notification" in window) || Notification.permission !== "granted") return;
    const urgent = tasks.filter((task) => task.remaining_hours > 0 &&
      (daysUntil(task.due_date) <= 3 || task.at_risk || task.today_hours > 0 || task.stale));
    if (!urgent.length) return;
    const signature = JSON.stringify(urgent.map((task) => [task.title, task.due_date,
      Boolean(task.at_risk), Boolean(task.stale), task.today_hours > 0]));
    const key = "deadline-reminder-" + todayKey();
    if (lastShownKey === key + signature) return;
    try {
      if (localStorage.getItem(key) === signature) return;
    } catch (_) { /* Daily reminders still work in this tab without storage. */ }

    const overdue = urgent.filter((task) => daysUntil(task.due_date) < 0).length;
    const risk = urgent.filter((task) => task.at_risk).length;
    const stale = urgent.filter((task) => task.stale).length;
    const reasons = [];
    if (overdue) reasons.push("เกินกำหนด " + overdue + " งาน");
    if (risk) reasons.push("แผนเสี่ยง " + risk + " งาน");
    if (stale) reasons.push("ยังไม่ได้อัปเดต " + stale + " งาน");
    const body = "วันนี้เริ่มจาก " + urgent[0].title +
      (reasons.length ? " · " + reasons.join(" · ") : " · มีงานใกล้ส่งหรือแบ่งไว้ทำวันนี้");
    try {
      const notification = new Notification("ตรวจแผนงานวันนี้", { body });
      notification.onclick = () => window.focus();
      lastShownKey = key + signature;
      try { localStorage.setItem(key, signature); } catch (_) { /* optional */ }
    } catch (_) {
      reminderStatus.textContent = "แสดงการเตือนไม่ได้ โปรดตรวจสิทธิ์และการตั้งค่าอุปกรณ์";
    }
  }

  async function refreshTasks() {
    if (refreshing) return;
    refreshing = true;
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 10000);
    try {
      const response = await fetch(window.location.pathname, {
        cache: "no-store", signal: controller.signal
      });
      if (!response.ok) return;
      const html = new DOMParser().parseFromString(await response.text(), "text/html");
      const data = html.getElementById("reminder-data");
      if (!data) return;
      const next = JSON.parse(data.textContent);
      if (!Array.isArray(next)) return;
      tasks = next;
      if (refreshNotice) refreshNotice.hidden = JSON.stringify(tasks) === originalData;
      updateStatus();
      checkReminders();
    } catch (_) {
      // Keep the last data if the local server is temporarily unavailable.
    } finally {
      window.clearTimeout(timeout);
      refreshing = false;
    }
  }

  reminderButton.addEventListener("click", async () => {
    if (!("Notification" in window) || !window.isSecureContext) return;
    try {
      await Notification.requestPermission();
      updateStatus();
      await refreshTasks();
      checkReminders();
    } catch (_) {
      reminderStatus.textContent = "ไม่สามารถขอสิทธิ์ได้ ใช้ไฟล์ปฏิทินแทน";
    }
  });
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) refreshTasks();
  });
  updateStatus();
  checkReminders();
  window.setInterval(refreshTasks, 60000);
}

function escapeCalendarText(value) {
  return value.replace(/\\/g, "\\\\").replace(/\n/g, "\\n")
    .replace(/,/g, "\\,").replace(/;/g, "\\;");
}

document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-calendar-date]");
  if (!button) return;

  const dateText = button.dataset.calendarDate;
  const start = dateText.replace(/-/g, "");
  const next = new Date(dateText + "T00:00:00Z");
  next.setUTCDate(next.getUTCDate() + 1);
  const end = next.toISOString().slice(0, 10).replace(/-/g, "");
  const stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
  const title = escapeCalendarText("ส่งงาน: " + button.dataset.calendarTitle);
  const detail = escapeCalendarText("วิชา " + button.dataset.calendarCourse + " · เปิดเว็บเดดไลน์ไม่ชนกันเพื่อดูแผน");
  const lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Deadline Compass//TH",
    "BEGIN:VEVENT", "UID:" + Date.now() + "@deadline-compass.local", "DTSTAMP:" + stamp,
    "DTSTART;VALUE=DATE:" + start, "DTEND;VALUE=DATE:" + end,
    "SUMMARY:" + title, "DESCRIPTION:" + detail,
    "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + title,
    "TRIGGER:-P1D", "END:VALARM", "END:VEVENT", "END:VCALENDAR"];
  const file = new Blob([lines.join("\r\n") + "\r\n"], { type: "text/calendar;charset=utf-8" });
  const url = URL.createObjectURL(file);
  const link = document.createElement("a");
  link.href = url;
  link.download = "deadline-" + dateText + ".ics";
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
});
```

## 8. คำอธิบายทุกบรรทัด

สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ

### L1

```javascript
// Reminders refresh from the existing Overview page while it remains open.
```

- comment สำหรับคนอ่าน: // Reminders refresh from the existing Overview page while it remains open.

### L2

```javascript
const reminderData = document.getElementById("reminder-data");
```

- สร้างตัวแปร `reminderData` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L3

```javascript
const reminderButton = document.getElementById("enable-reminders");
```

- สร้างตัวแปร `reminderButton` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L4

```javascript
const reminderStatus = document.getElementById("reminder-status");
```

- สร้างตัวแปร `reminderStatus` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L5

```javascript
const refreshNotice = document.getElementById("reminder-refresh");
```

- สร้างตัวแปร `refreshNotice` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L6

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L7

```javascript
if (reminderData && reminderButton && reminderStatus) {
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `&&`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L8

```javascript
  let tasks = JSON.parse(reminderData.textContent);
```

- สร้างตัวแปร `tasks` ด้วย let (เปลี่ยนค่าภายหลังได้)
- parse ข้อความ JSON เป็นค่าข้อมูล ไม่ใช่การรันโค้ดผู้ใช้
- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L9

```javascript
  let lastShownKey = "";
```

- สร้างตัวแปร `lastShownKey` ด้วย let (เปลี่ยนค่าภายหลังได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L10

```javascript
  let refreshing = false;
```

- สร้างตัวแปร `refreshing` ด้วย let (เปลี่ยนค่าภายหลังได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L11

```javascript
  const originalData = JSON.stringify(tasks);
```

- สร้างตัวแปร `originalData` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L12

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L13

```javascript
  function daysUntil(dateText) {
```

- ประกาศ `daysUntil` รับ `dateText`; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L14

```javascript
    const parts = dateText.split("-").map(Number);
```

- สร้างตัวแปร `parts` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `split()`: แยกข้อความ
- `map()`: สร้าง array ใหม่จากสมาชิก
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L15

```javascript
    const now = new Date();
```

- สร้างตัวแปร `now` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L16

```javascript
    const due = Date.UTC(parts[0], parts[1] - 1, parts[2]);
```

- สร้างตัวแปร `due` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L17

```javascript
    const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
```

- สร้างตัวแปร `today` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L18

```javascript
    return Math.round((due - today) / 86400000);
```

- คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด
- 86400000 ms = หนึ่งวัน; หารผล UTC ของวันเพื่อเทียบ deadline
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L19

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L20

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L21

```javascript
  function todayKey() {
```

- ประกาศ `todayKey` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L22

```javascript
    const now = new Date();
```

- สร้างตัวแปร `now` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L23

```javascript
    return [now.getFullYear(), String(now.getMonth() + 1).padStart(2, "0"),
```

- คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด
- `padStart()`: เติมอักขระข้างหน้าให้ความยาวครบ
- เครื่องหมายที่พบ: `[`, `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L24

```javascript
      String(now.getDate()).padStart(2, "0")].join("-");
```

- `padStart()`: เติมอักขระข้างหน้าให้ความยาวครบ
- `join()`: ต่อรายการเป็นข้อความ
- เครื่องหมายที่พบ: `(`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L25

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L26

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L27

```javascript
  function updateStatus() {
```

- ประกาศ `updateStatus` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L28

```javascript
    reminderButton.disabled = false;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L29

```javascript
    if (!("Notification" in window) || !window.isSecureContext) {
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `||`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L30

```javascript
      reminderStatus.textContent = "หน้านี้ไม่รองรับการแจ้งเตือน ใช้ไฟล์ปฏิทินได้";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L31

```javascript
      reminderButton.disabled = true;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L32

```javascript
    } else if (Notification.permission === "granted") {
```

- ทำทางเลือกของเงื่อนไขก่อนหน้า
- เครื่องหมายที่พบ: `}`, `(`, `===`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L33

```javascript
      reminderStatus.textContent = "เปิดแล้ว · ตรวจงานใหม่ทุกนาทีขณะเปิดหน้านี้";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L34

```javascript
      reminderButton.textContent = "🔔 เปิดการแจ้งเตือนแล้ว";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L35

```javascript
    } else if (Notification.permission === "denied") {
```

- ทำทางเลือกของเงื่อนไขก่อนหน้า
- เครื่องหมายที่พบ: `}`, `(`, `===`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L36

```javascript
      reminderStatus.textContent = "สิทธิ์ถูกปิดกั้น เปลี่ยนได้ในการตั้งค่าเว็บไซต์";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L37

```javascript
      reminderButton.disabled = true;
```

- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L38

```javascript
    } else {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `}`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L39

```javascript
      reminderStatus.textContent = "อนุญาตเพื่อเตือนงานวันนี้ งานใกล้ส่ง และแผนเสี่ยง";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L40

```javascript
    }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L41

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L42

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L43

```javascript
  function checkReminders() {
```

- ประกาศ `checkReminders` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L44

```javascript
    if (!("Notification" in window) || Notification.permission !== "granted") return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `||`, `!==`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L45

```javascript
    const urgent = tasks.filter((task) => task.remaining_hours > 0 &&
```

- สร้างตัวแปร `urgent` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `filter()`: เลือกสมาชิกที่เงื่อนไขจริง
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `&&`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L46

```javascript
      (daysUntil(task.due_date) <= 3 || task.at_risk || task.today_hours > 0 || task.stale));
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `||`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L47

```javascript
    if (!urgent.length) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L48

```javascript
    const signature = JSON.stringify(urgent.map((task) => [task.title, task.due_date,
```

- สร้างตัวแปร `signature` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `map()`: สร้าง array ใหม่จากสมาชิก
- serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `[`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L49

```javascript
      Boolean(task.at_risk), Boolean(task.stale), task.today_hours > 0]));
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L50

```javascript
    const key = "deadline-reminder-" + todayKey();
```

- สร้างตัวแปร `key` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L51

```javascript
    if (lastShownKey === key + signature) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `===`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L52

```javascript
    try {
```

- ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L53

```javascript
      if (localStorage.getItem(key) === signature) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- `getItem()`: อ่าน signature จาก localStorage
- เครื่องหมายที่พบ: `(`, `)`, `===`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L54

```javascript
    } catch (_) { /* Daily reminders still work in this tab without storage. */ }
```

- รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด
- เครื่องหมายที่พบ: `}`, `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L55

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L56

```javascript
    const overdue = urgent.filter((task) => daysUntil(task.due_date) < 0).length;
```

- สร้างตัวแปร `overdue` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `filter()`: เลือกสมาชิกที่เงื่อนไขจริง
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L57

```javascript
    const risk = urgent.filter((task) => task.at_risk).length;
```

- สร้างตัวแปร `risk` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `filter()`: เลือกสมาชิกที่เงื่อนไขจริง
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L58

```javascript
    const stale = urgent.filter((task) => task.stale).length;
```

- สร้างตัวแปร `stale` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `filter()`: เลือกสมาชิกที่เงื่อนไขจริง
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L59

```javascript
    const reasons = [];
```

- สร้างตัวแปร `reasons` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `[`, `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L60

```javascript
    if (overdue) reasons.push("เกินกำหนด " + overdue + " งาน");
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L61

```javascript
    if (risk) reasons.push("แผนเสี่ยง " + risk + " งาน");
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L62

```javascript
    if (stale) reasons.push("ยังไม่ได้อัปเดต " + stale + " งาน");
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L63

```javascript
    const body = "วันนี้เริ่มจาก " + urgent[0].title +
```

- สร้างตัวแปร `body` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `[`, `]`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L64

```javascript
      (reasons.length ? " · " + reasons.join(" · ") : " · มีงานใกล้ส่งหรือแบ่งไว้ทำวันนี้");
```

- `join()`: ต่อรายการเป็นข้อความ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L65

```javascript
    try {
```

- ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L66

```javascript
      const notification = new Notification("ตรวจแผนงานวันนี้", { body });
```

- สร้างตัวแปร `notification` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- สร้าง Notification เฉพาะเมื่อเงื่อนไขและสิทธิ์ผ่าน; ใน Node harness เป็น class จำลอง
- เครื่องหมายที่พบ: `(`, `{`, `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L67

```javascript
      notification.onclick = () => window.focus();
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `focus()`: ย้าย focus ไป element/หน้าต่าง
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L68

```javascript
      lastShownKey = key + signature;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L69

```javascript
      try { localStorage.setItem(key, signature); } catch (_) { /* optional */ }
```

- ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network
- รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด
- `setItem()`: จำ signature ลง localStorage
- เครื่องหมายที่พบ: `{`, `(`, `)`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L70

```javascript
    } catch (_) {
```

- รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด
- เครื่องหมายที่พบ: `}`, `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L71

```javascript
      reminderStatus.textContent = "แสดงการเตือนไม่ได้ โปรดตรวจสิทธิ์และการตั้งค่าอุปกรณ์";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L72

```javascript
    }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L73

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L74

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L75

```javascript
  async function refreshTasks() {
```

- ประกาศ `refreshTasks` รับ ``; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L76

```javascript
    if (refreshing) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L77

```javascript
    refreshing = true;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L78

```javascript
    const controller = new AbortController();
```

- สร้างตัวแปร `controller` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L79

```javascript
    const timeout = window.setTimeout(() => controller.abort(), 10000);
```

- สร้างตัวแปร `timeout` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `setTimeout()`: ตั้ง timeout สำหรับ fetch/คืน URL
- `abort()`: ยกเลิก fetch ที่ใช้เวลานาน
- 10000 ms = 10 วินาทีสำหรับตัดการดึงข้อมูล
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L80

```javascript
    try {
```

- ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L81

```javascript
      const response = await fetch(window.location.pathname, {
```

- สร้างตัวแปร `response` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- GET หน้า Overview เดิมเพื่ออ่าน reminder-data ล่าสุด; ไม่ส่งการแก้งาน
- เครื่องหมายที่พบ: `(`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L82

```javascript
        cache: "no-store", signal: controller.signal
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ

### L83

```javascript
      });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L84

```javascript
      if (!response.ok) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L85

```javascript
      const html = new DOMParser().parseFromString(await response.text(), "text/html");
```

- สร้างตัวแปร `html` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- `parseFromString()`: อ่าน HTML snapshot ที่ fetch ได้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L86

```javascript
      const data = html.getElementById("reminder-data");
```

- สร้างตัวแปร `data` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `getElementById()`: หา element ด้วย id
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L87

```javascript
      if (!data) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L88

```javascript
      const next = JSON.parse(data.textContent);
```

- สร้างตัวแปร `next` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- parse ข้อความ JSON เป็นค่าข้อมูล ไม่ใช่การรันโค้ดผู้ใช้
- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L89

```javascript
      if (!Array.isArray(next)) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L90

```javascript
      tasks = next;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L91

```javascript
      if (refreshNotice) refreshNotice.hidden = JSON.stringify(tasks) === originalData;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ
- ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json
- เครื่องหมายที่พบ: `(`, `)`, `===`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L92

```javascript
      updateStatus();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L93

```javascript
      checkReminders();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L94

```javascript
    } catch (_) {
```

- รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด
- เครื่องหมายที่พบ: `}`, `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L95

```javascript
      // Keep the last data if the local server is temporarily unavailable.
```

- comment สำหรับคนอ่าน: // Keep the last data if the local server is temporarily unavailable.

### L96

```javascript
    } finally {
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `}`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L97

```javascript
      window.clearTimeout(timeout);
```

- `clearTimeout()`: ยกเลิก timeout ที่เสร็จแล้ว
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L98

```javascript
      refreshing = false;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L99

```javascript
    }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L100

```javascript
  }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L101

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L102

```javascript
  reminderButton.addEventListener("click", async () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L103

```javascript
    if (!("Notification" in window) || !window.isSecureContext) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `||`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L104

```javascript
    try {
```

- ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network
- เครื่องหมายที่พบ: `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L105

```javascript
      await Notification.requestPermission();
```

- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- `requestPermission()`: ขอสิทธิ์ Notification จากการกดของผู้ใช้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L106

```javascript
      updateStatus();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L107

```javascript
      await refreshTasks();
```

- รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L108

```javascript
      checkReminders();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L109

```javascript
    } catch (_) {
```

- รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด
- เครื่องหมายที่พบ: `}`, `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L110

```javascript
      reminderStatus.textContent = "ไม่สามารถขอสิทธิ์ได้ ใช้ไฟล์ปฏิทินแทน";
```

- อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L111

```javascript
    }
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L112

```javascript
  });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L113

```javascript
  document.addEventListener("visibilitychange", () => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L114

```javascript
    if (!document.hidden) refreshTasks();
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L115

```javascript
  });
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L116

```javascript
  updateStatus();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L117

```javascript
  checkReminders();
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L118

```javascript
  window.setInterval(refreshTasks, 60000);
```

- `setInterval()`: ตั้งงานตรวจข้อมูลซ้ำ 60000 ms
- 60000 ms = 60 วินาที; browser อาจหน่วง timer เมื่อแท็บพัก
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L119

```javascript
}
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L120

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L121

```javascript
function escapeCalendarText(value) {
```

- ประกาศ `escapeCalendarText` รับ `value`; body ทำงานเมื่อเรียก
- เครื่องหมายที่พบ: `(`, `)`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L122

```javascript
  return value.replace(/\\/g, "\\\\").replace(/\n/g, "\\n")
```

- คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด
- `replace()`: แทนข้อความตามรูปแบบ
- เครื่องหมายที่พบ: `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L123

```javascript
    .replace(/,/g, "\\,").replace(/;/g, "\\;");
```

- `replace()`: แทนข้อความตามรูปแบบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L124

```javascript
}
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L125

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L126

```javascript
document.addEventListener("click", (event) => {
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `addEventListener()`: ผูกฟังก์ชันกับ event
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `{`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L127

```javascript
  const button = event.target.closest("[data-calendar-date]");
```

- สร้างตัวแปร `button` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `closest()`: หา element นี้หรือบรรพบุรุษที่ตรง marker
- เครื่องหมายที่พบ: `(`, `[`, `]`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L128

```javascript
  if (!button) return;
```

- ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L129

(บรรทัดว่าง)

- บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง

### L130

```javascript
  const dateText = button.dataset.calendarDate;
```

- สร้างตัวแปร `dateText` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L131

```javascript
  const start = dateText.replace(/-/g, "");
```

- สร้างตัวแปร `start` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `replace()`: แทนข้อความตามรูปแบบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L132

```javascript
  const next = new Date(dateText + "T00:00:00Z");
```

- สร้างตัวแปร `next` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L133

```javascript
  next.setUTCDate(next.getUTCDate() + 1);
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L134

```javascript
  const end = next.toISOString().slice(0, 10).replace(/-/g, "");
```

- สร้างตัวแปร `end` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `slice()`: ตัดช่วงข้อความ
- `replace()`: แทนข้อความตามรูปแบบ
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L135

```javascript
  const stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
```

- สร้างตัวแปร `stamp` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `replace()`: แทนข้อความตามรูปแบบ
- เครื่องหมายที่พบ: `(`, `)`, `[`, `]`, `{`, `}`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L136

```javascript
  const title = escapeCalendarText("ส่งงาน: " + button.dataset.calendarTitle);
```

- สร้างตัวแปร `title` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L137

```javascript
  const detail = escapeCalendarText("วิชา " + button.dataset.calendarCourse + " · เปิดเว็บเดดไลน์ไม่ชนกันเพื่อดูแผน");
```

- สร้างตัวแปร `detail` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L138

```javascript
  const lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Deadline Compass//TH",
```

- สร้างตัวแปร `lines` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `[`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L139

```javascript
    "BEGIN:VEVENT", "UID:" + Date.now() + "@deadline-compass.local", "DTSTAMP:" + stamp,
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `(`, `)`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L140

```javascript
    "DTSTART;VALUE=DATE:" + start, "DTEND;VALUE=DATE:" + end,
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L141

```javascript
    "SUMMARY:" + title, "DESCRIPTION:" + detail,
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ

### L142

```javascript
    "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + title,
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ

### L143

```javascript
    "TRIGGER:-P1D", "END:VALARM", "END:VEVENT", "END:VCALENDAR"];
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `]`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L144

```javascript
  const file = new Blob([lines.join("\r\n") + "\r\n"], { type: "text/calendar;charset=utf-8" });
```

- สร้างตัวแปร `file` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `join()`: ต่อรายการเป็นข้อความ
- รวมข้อความ ICS เป็นไฟล์ text/calendar UTF-8 ในหน่วยความจำ
- เครื่องหมายที่พบ: `(`, `[`, `)`, `]`, `{`, `;`, `}`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L145

```javascript
  const url = URL.createObjectURL(file);
```

- สร้างตัวแปร `url` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- `createObjectURL()`: สร้าง URL ชั่วคราวของ Blob
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L146

```javascript
  const link = document.createElement("a");
```

- สร้างตัวแปร `link` ด้วย const (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L147

```javascript
  link.href = url;
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L148

```javascript
  link.download = "deadline-" + dateText + ".ics";
```

- ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ
- เครื่องหมายที่พบ: `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L149

```javascript
  document.body.appendChild(link);
```

- `appendChild()`: เพิ่มลิงก์ดาวน์โหลดชั่วคราวใน DOM
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L150

```javascript
  link.click();
```

- `click()`: กระตุ้นดาวน์โหลดตามลิงก์
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L151

```javascript
  link.remove();
```

- `remove()`: เอาลิงก์ดาวน์โหลดชั่วคราวออกจาก DOM
- เครื่องหมายที่พบ: `(`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L152

```javascript
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
```

- arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที
- `setTimeout()`: ตั้ง timeout สำหรับ fetch/คืน URL
- `revokeObjectURL()`: คืนทรัพยากร URL หลังใช้
- เครื่องหมายที่พบ: `(`, `)`, `=>`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม

### L153

```javascript
});
```

- ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย
- เครื่องหมายที่พบ: `}`, `)`, `;`; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม
