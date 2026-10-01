# รายละเอียด JavaScript ข้อมูล JSON และเอกสารกำกับ

**รายละเอียดปัจจุบัน:** อ่าน [สารบัญแยกรายไฟล์](current/README.md), [forms.js](current/files/static/js/forms.js.md), [reminders.js](current/files/static/js/reminders.js.md), [data.json](current/files/data.json.md), [data.sample.json](current/files/data.sample.json.md), [team.json](current/files/team.json.md) และ [planner_settings.json](current/files/planner_settings.json.md)

> **เอกสารประวัติฉบับแรก:** ปัจจุบันข้อมูลงานมี 7 field และการเตือนดึงข้อมูลใหม่ทุกนาที รายละเอียดด้านล่างเป็น source ก่อนปรับปรุง 30 กันยายน 2569 อ่านโครงสร้างและข้อจำกัดล่าสุดใน [UPGRADE_DETAILS.md](UPGRADE_DETAILS.md)

เอกสารนี้อ้างถึงไฟล์จริง ณ วันที่ 29 กันยายน 2569 เลขบรรทัดนับตามไฟล์บนดิสก์ รวมบรรทัดว่างและ comment หากเปิดเว็บแล้วบันทึกข้อมูล storage.save อาจจัดย่อหน้า JSON ใหม่ ทำให้เลขบรรทัดเปลี่ยนได้ ให้ใช้เนื้อหาและค่า SHA-256 ประกอบการเทียบ

## วิธีอ่านอักขระและเครื่องหมาย

คำว่า “ทุกตัวอักษร” ในการอธิบายโปรแกรมควรอ่านเป็นทั้งหน่วยความหมาย: เช่น remaining_hours เป็นชื่อตัวแปรหนึ่งชื่อ ตัว r ไม่ใช่คำสั่งแยกต่างหาก เอกสารเก็บ source จริงทุกบรรทัด และแจกแจงคำสั่ง ชื่อข้อมูล operator ตัวเลข ข้อความ และเครื่องหมายที่มีผลต่อการตีความ รวมทั้งชี้ว่าช่องว่าง/บรรทัดว่างมีหน้าที่ใด

| เครื่องหมาย/คำ | ความหมายใน JavaScript นี้ | ข้อสังเกต |
|---|---|---|
| const / let | ตัวแปรห้ามกำหนด reference ใหม่ / ตัวแปรกำหนดใหม่ได้ | const ที่เก็บ object ยังแก้ property ได้ |
| = / === / !== | กำหนดค่า / เท่ากันแบบเคร่งครัด / ไม่เท่ากันแบบเคร่งครัด | = ไม่ใช่คำถามเปรียบเทียบ |
| > / <= | มากกว่า / น้อยกว่าหรือเท่ากับ | ขอบ3วันถูกรวมด้วย <= |
| ! / && / `||` | ไม่ / และ / หรือ | มีการประเมินแบบหยุดก่อนเมื่อรู้ผล |
| + / - / / | บวกหรือเชื่อม string / ลบ / หาร | / เมื่อครอบ pattern เป็น regex มีความหมายต่างจากหาร |
| . | เข้าถึง property/method | เช่น task.title, tasks.filter |
| ( ) | argument หรือจัดกลุ่ม expression | function และ if ใช้ตามบริบท |
| [ ] | array หรือ index | แต่ใน string selector เป็น attribute selector |
| { } | block หรือ object | {body} ย่อจาก {body: body} |
| , / ; / : | คั่นรายการ / จบ statement / ผูก key-value หรือกิ่ง ternary | ถ้าอยู่ใน quote ถือเป็นข้อความ |
| ? : | เลือกค่าจากเงื่อนไข | condition ? whenTrue : whenFalse |
| => | arrow function | รับค่าด้านซ้าย ทำงาน/คืนค่าด้านขวา |
| "..." | string literal | ตัวเลขใน quote เป็นข้อความ |
| // และ /* */ | comment ถึงท้ายบรรทัด / comment ครอบช่วง | ไม่ทำงาน |
| async / await | ฟังก์ชันทำงานกับ Promise / รอผลในฟังก์ชันนั้น | ไม่ได้ทำให้ส่วน Python เป็น async |
| try / catch | ลองคำสั่งและรับข้อผิดพลาด | ไม่ได้ซ่อนข้อผิดพลาดทุกจุดทั้งระบบ |
| new | สร้าง instance | Date, Notification, Blob |
| return | คืนผลและจบการเรียกฟังก์ชัน | return เปล่าคืน undefined |

## หลักการ escape: สิ่งที่เห็นใน source กับสิ่งที่อยู่ในไฟล์จริง

| source JavaScript | ค่าหรือความหมายจริง |
|---|---|
| `/\\/g` | regex จับ backslash หนึ่งตัวทุกตำแหน่ง |
| `"\\\\"` | string ที่มี backslash สองตัว |
| `/\n/g` | regex จับอักขระขึ้นบรรทัดใหม่ LF |
| `"\\n"` | string ที่มี backslash ตามด้วยตัว n สองตัวอักษร ไม่ใช่การขึ้นบรรทัด |
| `"\\,"` / `"\\;"` | backslash ตามด้วย comma / semicolon |
| `"\r\n"` | CR และ LF จริง ใช้แบ่งบรรทัดในไฟล์ ICS |
| `/[-:]/g` | character class จับ - หรือ : ทุกตำแหน่ง |
| `/\.\d{3}/` | จุดจริงตามด้วยตัวเลขสามหลัก |
| `g` หลัง slash | global: ทำกับทุก match ไม่ใช่เฉพาะครั้งแรก |

## วงจรชีวิตข้อมูลสองชุด

1. Python อ่าน data.json เพื่อสร้าง items และ remaining_hours ในแต่ละ HTTP request
2. Jinja tojson ใส่ข้อมูลลง script element ชนิด application/json ในหน้า1
3. JSON.parse สร้าง tasks ใน JavaScript เพียงครั้งเดียวเมื่อโหลดหน้า
4. timer คำนวณความห่างวันที่ใหม่ แต่ใช้ชื่องานและชั่วโมงจาก tasks ชุดเดิม
5. เมื่อแก้ไขงานในอีกแท็บ ควร reload หน้า1 เพื่อให้ข้อมูลเตือนตรงกับข้อมูลล่าสุด
6. localStorage เก็บเพียงธงว่าเตือนวันนี้แล้ว ไม่ได้สำรองรายการงานทั้งหมด และไม่ใช่ระบบทำงานออฟไลน์แบบ PWA


## static/js/reminders.js

ไฟล์ใหม่สำหรับฟังก์ชันเสริมของหน้า1 มีสองเส้นทาง: การแจ้งเตือนในเบราว์เซอร์ และดาวน์โหลด .ics การสมัคร listener ปฏิทินอยู่นอก if ของระบบเตือน

จำนวน 111 บรรทัดจริง · SHA-256: b650e9c0f4efe69b7db27f63b6f24fb5c5e7624c96aaa4bfac32f128dc7b84ea

### บรรทัด 1

```javascript
// Browser reminders while the dashboard is open, plus calendar files for later alerts.
```

`//` เริ่ม comment จนจบบรรทัด ข้อความระบุวัตถุประสงค์สองส่วน: เตือนระหว่างเปิดหน้าภาพรวม และสร้างไฟล์ปฏิทินสำหรับเตือนภายหลัง เบราว์เซอร์ไม่ประมวลผลข้อความใน comment

### บรรทัด 2

```javascript
const reminderData = document.getElementById("reminder-data");
```

ประกาศตัวแปร `const reminderData` อ้างถึง element ที่มี `id="reminder-data"` ใน page1.html; `document` คือเอกสาร DOM ปัจจุบัน; `getElementById(...)` ค้นหาหนึ่ง element หรือคืน `null`; `=` กำหนดค่า; `;` ปิดคำสั่ง ส่วนนี้ยังไม่อ่าน JSON

### บรรทัด 3

```javascript
const reminderButton = document.getElementById("enable-reminders");
```

ค้นหาปุ่มที่มี id `enable-reminders` แล้วเก็บ reference ใน `reminderButton` เพื่อผูกการคลิกและเปลี่ยนสถานะปุ่ม ชื่อในเครื่องหมายคำพูดต้องตรงกับ id ใน HTML ทุกตัว

### บรรทัด 4

```javascript
const reminderStatus = document.getElementById("reminder-status");
```

ค้นหา element ข้อความสถานะที่มี id `reminder-status` แล้วเก็บไว้ใน `reminderStatus` สำหรับแสดงผลขอสิทธิ์หรือข้อผิดพลาด

### บรรทัด 5

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 6

```javascript
if (reminderData && reminderButton && reminderStatus) {
```

`if (...)` ตรวจว่าทั้งสาม reference มีค่าใช้งานได้; `&&` ต้องเป็นจริงทุกเงื่อนไขและหยุดตรวจทันทีที่พบค่าเท็จ; `{` เปิดขอบเขตคำสั่ง หากขาด element ใดจะข้ามระบบเตือนภายใน แต่ตัวจัดการไฟล์ปฏิทินบรรทัด 84 ยังถูกติดตั้ง

### บรรทัด 7

```javascript
  const tasks = JSON.parse(reminderData.textContent);
```

อ่าน `textContent` ของ element JSON แล้วใช้ `JSON.parse` แปลงข้อความเป็น array ของ object เก็บใน `tasks`; HTML ส่งข้อมูลจาก Python ด้วย Jinja `tojson` นี่เป็นสำเนาข้อมูลตอนโหลดหน้า ไม่ได้อ่าน data.json ตรงจากเครื่องหรือเรียก API ในทุกนาที การ parse ไม่มี try/catch ครอบ หาก JSON ผิดจะหยุดสคริปต์

### บรรทัด 8

```javascript
  let lastShownKey = "";
```

`let` ใช้เพราะตัวแปรนี้จะเปลี่ยนค่าได้; `lastShownKey = ""` เริ่มจากข้อความว่าง เพื่อจำกุญแจวันล่าสุดที่สคริปต์หน้านี้สร้าง notification สำเร็จ ไม่ใช่วันล่าสุดของทุกเครื่องหรือทุกผู้ใช้

### บรรทัด 9

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 10

```javascript
  function daysUntil(dateText) {
```

ประกาศฟังก์ชัน `daysUntil` รับ argument `dateText` เป็นวันที่ข้อความ แล้วคืนจำนวนวันห่างจากวันนี้; การประกาศฟังก์ชันยังไม่คำนวณจนกว่าจะเรียก

### บรรทัด 11

```javascript
    const parts = dateText.split("-").map(Number);
```

`split("-")` แยกเช่น "2026-10-01" เป็น ["2026","10","01"]; `map(Number)` แปลงสมาชิกเป็นตัวเลข ได้ [2026,10,1]; `Number` ถูกส่งเป็นฟังก์ชันให้ map ไม่ได้เป็นข้อความชื่อฟังก์ชัน

### บรรทัด 12

```javascript
    const now = new Date();
```

`new Date()` สร้างวัตถุเวลาปัจจุบันของอุปกรณ์ผู้เปิดเว็บ เก็บใน `now` จึงอาจต่างจากวันที่ที่ Python ใช้เมื่อเซิร์ฟเวอร์กับผู้ใช้ตั้งเขตเวลาหรือเวลาของเครื่องต่างกัน

### บรรทัด 13

```javascript
    const due = Date.UTC(parts[0], parts[1] - 1, parts[2]);
```

`parts[0]` ปี, `parts[1] - 1` เดือนลบหนึ่งเพราะ Date.UTC รับเดือน 0–11, `parts[2]` วัน; `Date.UTC` คืนจำนวนมิลลิวินาทีของวันนั้นที่เวลา 00:00 UTC นี่เป็นค่าตัวเลข ไม่ใช่ Date object

### บรรทัด 14

```javascript
    const today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
```

อ่านปี เดือน และวันตามเวลาท้องถิ่นจาก `now` แล้วนำไปสร้างเลข UTC ของวันเดียวกัน การใช้ UTC เป็นฐานทั้งสองฝั่งช่วยให้ส่วนต่างเป็นจำนวนวันตามปฏิทินโดยไม่ใช้ชั่วโมงปัจจุบันมาปน

### บรรทัด 15

```javascript
    return Math.round((due - today) / 86400000);
```

`due - today` ห่างกันเป็นมิลลิวินาที; `86400000` = 24×60×60×1000; หารเพื่อแปลงเป็นวันแล้ว `Math.round` ปัดเป็นจำนวนเต็ม; `return` ส่งกลับ เช่น -1 เกินกำหนดหนึ่งวัน, 0 ส่งวันนี้, 2 อีกสองวัน

### บรรทัด 16

```javascript
  }
```

ปีกกา `}` ปิดฟังก์ชัน daysUntil เมื่อถูกเรียกครั้งต่อไปจะสร้างตัวแปรภายในใหม่

### บรรทัด 17

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 18

```javascript
  function todayKey() {
```

ประกาศ `todayKey()` ไม่มีพารามิเตอร์ ใช้สร้างวันที่ของเครื่องเป็นข้อความมาตรฐานสำหรับกุญแจป้องกันการเตือนซ้ำ

### บรรทัด 19

```javascript
    const now = new Date();
```

อ่านเวลาปัจจุบันใหม่ ณ การเรียก todayKey เพื่อไม่ใช้ Date object เก่าตลอดการเปิดหน้า

### บรรทัด 20

```javascript
    return [now.getFullYear(), String(now.getMonth() + 1).padStart(2, "0"),
```

เปิด array ด้วย `[`; ใส่ปีเป็นสมาชิกแรก; เดือนใช้ `getMonth()+1` ให้ได้ 1–12; `String(...)` แปลงเป็นข้อความก่อน `padStart(2,"0")` เติมศูนย์ทางซ้ายให้ยาวอย่างน้อยสองตัว เช่น 9→"09"; comma ท้ายบรรทัดหมายถึงยังมีสมาชิกต่อ

### บรรทัด 21

```javascript
      String(now.getDate()).padStart(2, "0")].join("-");
```

แปลงวันที่เป็นสองหลักแล้วปิด array ด้วย `]`; `join("-")` เชื่อมด้วยขีดกลาง ได้เช่น "2026-09-29"; return ที่เริ่มในบรรทัดก่อนจบที่ semicolon นี้

### บรรทัด 22

```javascript
  }
```

ปิดฟังก์ชัน todayKey

### บรรทัด 23

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 24

```javascript
  function updateStatus() {
```

ประกาศ `updateStatus()` เพื่ออัปเดตข้อความและปุ่มตามความสามารถของเบราว์เซอร์และสถานะสิทธิ์ ไม่ได้สร้างการแจ้งเตือนเอง

### บรรทัด 25

```javascript
    if (!("Notification" in window) || !window.isSecureContext) {
```

`"Notification" in window` ตรวจว่ามี API นี้; `!` กลับค่าความจริง; `||` หมายถึงอย่างน้อยหนึ่งเงื่อนไขเป็นจริง; `!window.isSecureContext` ตรวจว่าไม่ใช่บริบทปลอดภัย หากไม่มี API หรือบริบทไม่เหมาะสมจะเข้ากิ่งแรก

### บรรทัด 26

```javascript
      reminderStatus.textContent = "เบราว์เซอร์นี้ไม่รองรับการแจ้งเตือนในหน้านี้";
```

กำหนดข้อความภาษาไทยลง `textContent` จึงตีความเป็นข้อความ ไม่เป็นแท็ก HTML ข้อความบอกว่าใช้การเตือนในหน้านี้ไม่ได้

### บรรทัด 27

```javascript
      reminderButton.disabled = true;
```

ตั้ง property `disabled = true` ปิดการกดปุ่มในกิ่งที่ไม่รองรับ ไม่ได้เปลี่ยนสิทธิ์ของเบราว์เซอร์

### บรรทัด 28

```javascript
    } else if (Notification.permission === "granted") {
```

`} else if (...) {` ปิดกิ่งก่อนและเปิดเงื่อนไขถัดไป; `Notification.permission` อ่านสถานะสิทธิ์; `===` เทียบค่ากับชนิดอย่างเคร่งครัด; "granted" คืออนุญาตแล้ว

### บรรทัด 29

```javascript
      reminderStatus.textContent = "เปิดแล้ว · เตือนเมื่อหน้านี้เปิดอยู่";
```

ข้อความอธิบายว่าเปิดสิทธิ์แล้วและเตือนขณะหน้าเว็บยังเปิดอยู่ ข้อความนี้ไม่ได้ยืนยันว่าระบบปฏิบัติการจะแสดงแบนเนอร์จริงทุกครั้ง

### บรรทัด 30

```javascript
      reminderButton.textContent = "🔔 เปิดการแจ้งเตือนแล้ว";
```

เปลี่ยนข้อความบนปุ่มเป็นรูปกระดิ่งและข้อความว่าเปิดแล้ว Emoji เป็นอักขระใน string ไม่มีการโหลดไฟล์ภาพ

### บรรทัด 31

```javascript
    } else if (Notification.permission === "denied") {
```

ถ้ากิ่งก่อนหน้าไม่ตรง ให้ตรวจว่า permission เป็น "denied" หรือถูกปฏิเสธ/ปิดกั้น

### บรรทัด 32

```javascript
      reminderStatus.textContent = "เบราว์เซอร์ปิดกั้นการแจ้งเตือน โปรดเปลี่ยนในการตั้งค่าเว็บไซต์";
```

แสดงวิธีให้ผู้ใช้ไปเปลี่ยนสิทธิ์ในการตั้งค่าเว็บไซต์ เพราะสคริปต์ไม่สามารถอนุญาตสิทธิ์แทนผู้ใช้ได้

### บรรทัด 33

```javascript
      reminderButton.disabled = true;
```

ปิดปุ่มเมื่อถูกปฏิเสธ หากผู้ใช้เปลี่ยนสิทธิ์ภายนอก ควรโหลดหน้าใหม่; ฟังก์ชันนี้ไม่มีบรรทัดตั้ง disabled กลับเป็น false

### บรรทัด 34

```javascript
    } else {
```

`else` รับกรณีที่เหลือหลังจากตรวจความสามารถและสิทธิ์แล้ว โดยทั่วไปคือสถานะ "default" ที่ยังไม่ตัดสินใจ

### บรรทัด 35

```javascript
      reminderStatus.textContent = "กดเพื่ออนุญาตให้เบราว์เซอร์เตือน";
```

บอกให้ผู้ใช้กดปุ่มเพื่อเริ่มขออนุญาต ไม่ส่งคำขออนุญาตทันทีตั้งแต่เปิดหน้า

### บรรทัด 36

```javascript
    }
```

ปิดกิ่ง else ของ updateStatus

### บรรทัด 37

```javascript
  }
```

ปิดฟังก์ชัน updateStatus

### บรรทัด 38

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 39

```javascript
  function checkReminders() {
```

ประกาศ `checkReminders()` ฟังก์ชันคัดงานเร่งด่วน ตรวจการเตือนซ้ำ แล้วลองสร้าง notification

### บรรทัด 40

```javascript
    if (!("Notification" in window) || Notification.permission !== "granted") return;
```

ถ้าไม่มี API หรือสิทธิ์ไม่ใช่ "granted" ให้ `return;` ออกจากฟังก์ชันทันทีโดยไม่คืนค่าเฉพาะ; `!==` คือไม่เท่ากันแบบไม่แปลงชนิด คำสั่งนี้ไม่มีวงเล็บปีกกาเพราะกิ่ง if มีคำสั่งเดียว

### บรรทัด 41

```javascript
    const urgent = tasks.filter((task) => task.remaining_hours > 0 && daysUntil(task.due_date) <= 3);
```

`filter` สร้าง array ใหม่จากงานที่ผ่าน callback `(task) => ...`; เงื่อนไขคืองานยังเหลือชั่วโมง `> 0` และวันถึงกำหนด `<= 3`; รวมงานเกินกำหนดทุกวันในอดีตเพราะไม่มีขอบเขตล่าง ผล filter คงลำดับต้นฉบับที่หน้า1จัดไว้แล้ว

### บรรทัด 42

```javascript
    if (urgent.length === 0) return;
```

ถ้า `urgent.length === 0` แปลว่าไม่มีงานตรงเงื่อนไข จึงจบฟังก์ชัน ไม่สร้าง notification และไม่เขียนกุญแจประจำวัน

### บรรทัด 43

```javascript
    const key = "deadline-reminder-" + todayKey();
```

นำ prefix "deadline-reminder-" ต่อกับ todayKey ด้วย `+` เช่น "deadline-reminder-2026-09-29" เพื่อใช้เป็นชื่อรายการใน localStorage

### บรรทัด 44

```javascript
    if (lastShownKey === key) return;
```

หากตัวแปรในหน่วยความจำบอกว่าเคยเตือนด้วยกุญแจวันนี้แล้ว ให้จบฟังก์ชัน เป็นชั้นป้องกันซ้ำภายในแท็บที่เปิดอยู่

### บรรทัด 45

```javascript
    try {
```

`try {` เริ่มส่วนที่อาจเกิดข้อผิดพลาดจากการเข้าถึงพื้นที่เก็บข้อมูลของเบราว์เซอร์

### บรรทัด 46

```javascript
      if (localStorage.getItem(key) === "shown") return;
```

`localStorage.getItem(key)` อ่านข้อความที่บันทึกกับกุญแจวันนั้น; ถ้าเท่ากับ "shown" ให้หยุด เป็นชั้นจำข้ามการโหลดหน้าใน origin เดิม เช่น host และ port เดิม

### บรรทัด 47

```javascript
    } catch (_) {
```

`catch (_)` รับ error ถ้าอ่าน localStorage ไม่ได้; ชื่อ `_` เป็นชื่อตัวแปรธรรมดาที่ผู้เขียนใช้สื่อว่าไม่ได้ใช้ค่า error ไม่ใช่ไวยากรณ์พิเศษสำหรับละเลยข้อผิดพลาด

### บรรทัด 48

```javascript
      // The notification can still appear if browser storage is unavailable.
```

comment บอกเจตนาว่าแม้พื้นที่เก็บข้อมูลใช้ไม่ได้ ก็ยังลองสร้าง notification ต่อได้ ไม่ใช่คำสั่งข้ามการขอสิทธิ์

### บรรทัด 49

```javascript
    }
```

ปิด catch แล้วไหลต่อไปยังการสร้างข้อความแจ้งเตือน

### บรรทัด 50

```javascript
    const body = urgent.length === 1
```

เริ่มกำหนด `body` ด้วย ternary expression เงื่อนไขคือจำนวน urgent เท่ากับ 1; เครื่องหมาย ? และ : ที่บรรทัดถัดไปเป็นส่วนเดียวกัน

### บรรทัด 51

```javascript
      ? urgent[0].title + " · ส่ง " + urgent[0].due_date
```

`?` เลือกคำตอบเมื่อจริง: ชื่องานแรก `urgent[0].title` ต่อข้อความและวันที่ส่ง; index 0 คือสมาชิกแรก ไม่ใช่ลำดับที่ผู้ใช้เห็นแบบเริ่มหนึ่ง

### บรรทัด 52

```javascript
      : "มี " + urgent.length + " งานที่ใกล้ส่งหรือเกินกำหนด · เริ่มจาก " + urgent[0].title;
```

`:` เลือกคำตอบเมื่อมีมากกว่าหนึ่งงาน: แจ้งจำนวนรวมและชื่องานแรก; JavaScript แปลงตัวเลข length เป็นข้อความเมื่อต่อกับ string ด้วย +

### บรรทัด 53

```javascript
    try {
```

เริ่ม try สำหรับการสร้าง notification เนื่องจาก API มีอยู่และอนุญาตแล้วก็ยังอาจสร้างไม่ได้ในบางสภาพแวดล้อม

### บรรทัด 54

```javascript
      const notification = new Notification("ตรวจเดดไลน์วันนี้", { body });
```

`new Notification(title, options)` สร้าง notification ชื่อ "ตรวจเดดไลน์วันนี้"; `{ body }` คือ object แบบย่อ เทียบเท่า {body: body}; การสร้างสำเร็จตาม JavaScript ไม่ใช่หลักฐานว่าผู้ใช้เห็นบนจอหรือได้ยินเสียง

### บรรทัด 55

```javascript
      notification.onclick = () => window.focus();
```

ตั้ง event handler `onclick` เป็น arrow function ไม่มีพารามิเตอร์; เมื่อกด notification จะเรียก `window.focus()` ขอให้หน้าต่างเดิมกลับมาเด่น ไม่ได้นำทางไปงานหนึ่งโดยอัตโนมัติ

### บรรทัด 56

```javascript
      lastShownKey = key;
```

หลัง constructor ไม่ throw จึงจำ key วันนี้ไว้ในตัวแปร lastShownKey เพื่อระงับการสร้างซ้ำในแท็บเดียวกัน

### บรรทัด 57

```javascript
      try { localStorage.setItem(key, "shown"); } catch (_) { /* storage is optional */ }
```

try/catch ซ้อนแบบบรรทัดเดียว: บันทึก key เป็น "shown" ใน localStorage; หากเขียนไม่ได้ให้ข้ามโดยไม่แสดง error; comment `/* ... */` จบที่ */ และไม่มีผลต่อการทำงาน

### บรรทัด 58

```javascript
    } catch (_) {
```

catch นี้รับข้อผิดพลาดจาก try บรรทัด53 เช่น notification constructor ไม่รองรับ; การเขียน storage ที่มี catch ของตนเองจะไม่หลุดมาถึงส่วนนี้

### บรรทัด 59

```javascript
      reminderStatus.textContent = "เบราว์เซอร์ไม่สามารถแสดงการแจ้งเตือนได้";
```

เปลี่ยนข้อความสถานะเพื่อแจ้งว่าสร้างการเตือนไม่สำเร็จ กิ่งนี้ไม่มีการเปลี่ยน key เพิ่มเอง

### บรรทัด 60

```javascript
    }
```

ปิด catch ของการสร้าง notification

### บรรทัด 61

```javascript
  }
```

ปิดฟังก์ชัน checkReminders

### บรรทัด 62

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 63

```javascript
  reminderButton.addEventListener("click", async () => {
```

`addEventListener("click", ...)` สมัคร callback เมื่อกดปุ่ม; `async () => {` ทำให้ callback ใช้ await ได้และคืน Promise; ไม่มีการเรียก callback ทันทีตอนลงทะเบียน

### บรรทัด 64

```javascript
    if (!("Notification" in window)) return;
```

ตรวจ API ซ้ำภายใน callback หากไม่มี ให้จบก่อนขออนุญาต แม้ปุ่มควรถูกปิดจาก updateStatus อยู่แล้ว

### บรรทัด 65

```javascript
    try {
```

เริ่ม try ครอบการขอสิทธิ์และการอัปเดตภายหลัง เพื่อแสดงข้อความแทนการปล่อย error

### บรรทัด 66

```javascript
      await Notification.requestPermission();
```

`await Notification.requestPermission()` รอผู้ใช้/เบราว์เซอร์ตอบเรื่องสิทธิ์โดยไม่ใช้ loop รอ; ผลลัพธ์ไม่ได้เก็บในตัวแปร แต่ฟังก์ชันถัดไปอ่าน Notification.permission

### บรรทัด 67

```javascript
      updateStatus();
```

อ่านสิทธิ์ล่าสุดและปรับข้อความด้วย updateStatus

### บรรทัด 68

```javascript
      checkReminders();
```

ลองคัดงานและเตือนทันทีหลังการตอบสิทธิ์ หากไม่อนุญาต checkReminders จะคืนกลับตั้งแต่ guard บรรทัด40

### บรรทัด 69

```javascript
    } catch (_) {
```

ถ้าคำสั่งใน try เกิดข้อผิดพลาด ให้เข้ากิ่ง catch นี้

### บรรทัด 70

```javascript
      reminderStatus.textContent = "ไม่สามารถขออนุญาตแจ้งเตือนได้ในเบราว์เซอร์นี้";
```

แสดงข้อความว่าขออนุญาตไม่ได้ โดยไม่อ้างว่าโปรแกรมจะเตือนได้เองแม้เบราว์เซอร์ปฏิเสธ

### บรรทัด 71

```javascript
    }
```

ปิด catch ของ callback การคลิกปุ่ม

### บรรทัด 72

```javascript
  });
```

`}` ปิด callback, `)` ปิดการเรียก addEventListener, `;` ปิดคำสั่ง เห็นหลายเครื่องหมายเพราะกำลังปิดโครงสร้างซ้อนกัน

### บรรทัด 73

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 74

```javascript
  updateStatus();
```

เรียก updateStatus ครั้งแรกทันทีที่โหลดและได้ element ครบ เพื่อแสดงสถานะที่ถูกต้องก่อนการกดปุ่ม

### บรรทัด 75

```javascript
  checkReminders();
```

เรียก checkReminders ครั้งแรก ถ้าเคยอนุญาตและยังไม่เตือนวันนี้ อาจสร้าง notification ได้เลยโดยไม่ต้องกดอีก

### บรรทัด 76

```javascript
  window.setInterval(checkReminders, 60000);
```

`setInterval(checkReminders, 60000)` ส่ง reference ฟังก์ชันให้ระบบเรียกซ้ำโดยขอช่วงห่าง 60,000 มิลลิวินาที = 60 วินาที; ไม่ใส่ () หลังชื่อฟังก์ชันเพราะไม่ได้ต้องการเรียกใน argument; เป็นการตรวจจาก tasks เดิมและอาจช้ากว่าหนึ่งนาทีเมื่อเบราว์เซอร์จำกัด timer

### บรรทัด 77

```javascript
}
```

ปิด if ใหญ่ที่เริ่มบรรทัด6 ฟังก์ชันเตือนและ tasks อยู่ในขอบเขตนี้

### บรรทัด 78

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 79

```javascript
function escapeCalendarText(value) {
```

ประกาศ `escapeCalendarText(value)` นอก if เตือน จึงใช้ในส่วนปฏิทินได้เสมอเมื่อสคริปต์โหลดสำเร็จ; รับข้อความและคืนข้อความที่ escape สำหรับค่า TEXT ของ iCalendar

### บรรทัด 80

```javascript
  return value.replace(/\\/g, "\\\\").replace(/\n/g, "\\n")
```

เรียก replace แบบต่อเนื่อง: regex `/\\/g` จับ backslash จริงทุกตัว แล้ว replacement `"\\\\"` เป็น backslash สองตัวจริง; regex `/\n/g` จับ LF จริง แล้ว `"\\n"` แทนด้วย backslash ตามด้วย n; escape backslash ก่อนจึงไม่ไปเพิ่มซ้ำให้ backslash ที่เพิ่งสร้างในขั้นถัดไป

### บรรทัด 81

```javascript
    .replace(/,/g, "\\,").replace(/;/g, "\\;");
```

regex `/,/g` และ `/;/g` จับ comma/semicolon ทุกตัว แล้วเติม backslash หน้าอักขระ; `.replace` ต่อจากผลบรรทัดก่อน; semicolon สุดท้ายจบ return หลายบรรทัดนี้ ดูตาราง escape ด้านล่างสำหรับจำนวนตัวอักษรจริง

### บรรทัด 82

```javascript
}
```

ปิด escapeCalendarText; ฟังก์ชันนี้ไม่ได้ escape HTML และไม่ได้ sanitize URL ใช้กับ TEXT ในไฟล์ปฏิทินเท่านั้น

### บรรทัด 83

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 84

```javascript
document.addEventListener("click", (event) => {
```

สมัคร click listener กับ document หนึ่งตัว ใช้หลัก event delegation ให้จับการคลิกปุ่มปฏิทินหลายปุ่มผ่านการส่งต่อเหตุการณ์; `event` คือข้อมูลการคลิก

### บรรทัด 85

```javascript
  const button = event.target.closest("[data-calendar-date]");
```

`event.target` คือ element ที่ถูกคลิก; `closest("[data-calendar-date]")` หา element นั้นหรือบรรพบุรุษใกล้ที่สุดที่มี attribute นี้; วงเล็บเหลี่ยมใน string เป็น CSS attribute selector ไม่ใช่ array

### บรรทัด 86

```javascript
  if (!button) return;
```

ถ้าไม่พบปุ่มตรงเงื่อนไข ให้ return ออกจาก callback คลิกครั้งนี้โดยไม่ทำอะไรเพิ่มเติม

### บรรทัด 87

```javascript

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 88

```javascript
  const dateText = button.dataset.calendarDate;
```

อ่าน `button.dataset.calendarDate` ซึ่งสัมพันธ์กับ HTML attribute `data-calendar-date`; ค่าที่ได้เป็น string เช่น "2026-10-01"

### บรรทัด 89

```javascript
  const start = dateText.replace(/-/g, "");
```

ลบขีดกลางทุกตัวด้วย regex `/-/g` เพื่อสร้างค่า DATE รูป YYYYMMDD เช่น "20261001"

### บรรทัด 90

```javascript
  const next = new Date(dateText + "T00:00:00Z");
```

นำวันต่อกับ "T00:00:00Z" แล้วสร้าง Date; T คั่นวันกับเวลา, Z ระบุ UTC; ใช้เวลาเที่ยงคืน UTC เพื่อคำนวณวันสิ้นสุดโดยไม่เลื่อนตามเขตเวลาท้องถิ่น

### บรรทัด 91

```javascript
  next.setUTCDate(next.getUTCDate() + 1);
```

อ่านเลขวัน UTC แล้วเพิ่มหนึ่ง ก่อนตั้งกลับด้วย setUTCDate; Date จัดการข้ามเดือน/ปีให้เอง เช่น 31 ธันวาคมไป 1 มกราคม

### บรรทัด 92

```javascript
  const end = next.toISOString().slice(0, 10).replace(/-/g, "");
```

แปลงวันถัดไปเป็น ISO string แล้ว `slice(0,10)` ตัดเอาตัวอักษรตำแหน่ง0–9 ซึ่งเป็นวัน YYYY-MM-DD จากนั้นลบขีดกลาง; ค่านี้คือวันสิ้นสุดที่ไม่นับรวมของกิจกรรมทั้งวัน

### บรรทัด 93

```javascript
  const stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d{3}/, "");
```

สร้าง DTSTAMP เป็นเวลาที่สร้างไฟล์ใน UTC; regex `/[-:]/g` ลบ - หรือ : ทุกตัว; `/\.\d{3}/` จับจุดจริงตามด้วยตัวเลขสามหลักเพื่อเอามิลลิวินาทีออก; คง T กับ Z ไว้ เช่น 20260929T130000Z

### บรรทัด 94

```javascript
  const title = escapeCalendarText("ส่งงาน: " + button.dataset.calendarTitle);
```

ประกอบหัวข้อ "ส่งงาน: " กับ dataset.calendarTitle แล้ว escape; ใน HTML ชื่อตรงกับ data-calendar-title; title ที่ escape แล้วจะถูกใช้ใน SUMMARY และข้อความของ alarm

### บรรทัด 95

```javascript
  const detail = escapeCalendarText("วิชา " + button.dataset.calendarCourse + " · เปิดเว็บเดดไลน์ไม่ชนกันเพื่อดูแผน");
```

สร้างรายละเอียดจากชื่อวิชาใน data-calendar-course และข้อความชวนกลับมาดูเว็บ ก่อน escape; ไม่มี URL แบบเชื่อมกลับเว็บเฉพาะรายการ

### บรรทัด 96

```javascript
  const lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Deadline Compass//TH",
```

เริ่ม array ของบรรทัด iCalendar: BEGIN:VCALENDAR เปิดเอกสาร, VERSION:2.0 ระบุรูปแบบ, PRODID เป็นตัวระบุซอฟต์แวร์ ไม่ใช่ชื่อบัญชีหรือเครื่องที่จะส่งข้อความ

### บรรทัด 97

```javascript
    "BEGIN:VEVENT", "UID:" + Date.now() + "@deadline-compass.local", "DTSTAMP:" + stamp,
```

BEGIN:VEVENT เปิดกิจกรรมหนึ่งรายการ; UID ต่อมิลลิวินาทีจาก Date.now กับโดเมนข้อความลงท้าย; DTSTAMP คือเวลาสร้างจากบรรทัด93; UID นี้สร้างใหม่ทุกครั้ง จึงไม่ใช่รหัสงานถาวรสำหรับซิงก์

### บรรทัด 98

```javascript
    "DTSTART;VALUE=DATE:" + start, "DTEND;VALUE=DATE:" + end,
```

DTSTART;VALUE=DATE ระบุวันที่เริ่มแบบทั้งวัน; DTEND;VALUE=DATE เป็นวันถัดไปแบบไม่นับรวม; semicolon และ colon ภายใน string เป็นไวยากรณ์ iCalendar ส่วน comma นอก string คั่นสมาชิก array ของ JavaScript

### บรรทัด 99

```javascript
    "SUMMARY:" + title, "DESCRIPTION:" + detail,
```

SUMMARY คือชื่อกิจกรรมและ DESCRIPTION คือรายละเอียดที่ escape แล้ว แต่ละ string เป็นคนละบรรทัดของไฟล์เมื่อ join

### บรรทัด 100

```javascript
    "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + title,
```

BEGIN:VALARM เปิดส่วนแจ้งเตือนย่อยในกิจกรรม; ACTION:DISPLAY ขอให้แสดงข้อความ; DESCRIPTION ใช้ชื่อกิจกรรม ไม่ใช่การส่งอีเมลหรือ push จาก Python

### บรรทัด 101

```javascript
    "TRIGGER:-P1D", "END:VALARM", "END:VEVENT", "END:VCALENDAR"];
```

TRIGGER:-P1D ขอเตือนหนึ่งวันก่อนเวลาเริ่ม โดย - แสดงก่อน, P เริ่ม duration, 1D คือหนึ่งวัน; END:VALARM, END:VEVENT, END:VCALENDAR ปิดส่วนจากในออกนอก; ] ปิด array; เวลาแสดงจริงขึ้นกับการนำเข้าและการตั้งค่าปฏิทิน

### บรรทัด 102

```javascript
  const file = new Blob([lines.join("\r\n") + "\r\n"], { type: "text/calendar;charset=utf-8" });
```

`lines.join("\r\n")` เชื่อมด้วย CRLF แล้วเติม CRLF ท้าย; `new Blob([text], {type: ...})` สร้างข้อมูลไฟล์ในหน่วยความจำ; MIME text/calendar และ charset=utf-8 ระบุรูปแบบและการเข้ารหัส รองรับข้อความไทย

### บรรทัด 103

```javascript
  const url = URL.createObjectURL(file);
```

`URL.createObjectURL(file)` ให้ URL ชั่วคราวอ้างถึง Blob ภายในเบราว์เซอร์ ไม่อัปโหลดไฟล์และไม่สร้างลิงก์สาธารณะบนอินเทอร์เน็ต

### บรรทัด 104

```javascript
  const link = document.createElement("a");
```

สร้าง element ลิงก์ <a> ในหน่วยความจำไว้กระตุ้นการดาวน์โหลด ขณะนี้ยังไม่ได้เพิ่มเข้าหน้า

### บรรทัด 105

```javascript
  link.href = url;
```

ตั้ง href ของลิงก์ให้ชี้ไป object URL

### บรรทัด 106

```javascript
  link.download = "deadline-" + dateText + ".ics";
```

ตั้ง attribute/property download ให้เสนอชื่อไฟล์เช่น "deadline-2026-10-01.ics"; นามสกุล .ics ช่วยให้ระบบรู้ว่าเป็นไฟล์ปฏิทิน แต่ผู้ใช้ยังต้องนำเข้าแอปปฏิทิน

### บรรทัด 107

```javascript
  document.body.appendChild(link);
```

เพิ่มลิงก์เป็นลูกของ document.body เพื่อให้การคลิกดาวน์โหลดทำงานได้ในเบราว์เซอร์ที่ต้องมี element อยู่ในเอกสาร

### บรรทัด 108

```javascript
  link.click();
```

เรียก click() ด้วยโปรแกรมเพื่อเริ่มดาวน์โหลดไฟล์จากการกดของผู้ใช้ ไม่ใช่การส่งฟอร์มไปเซิร์ฟเวอร์

### บรรทัด 109

```javascript
  link.remove();
```

นำลิงก์ที่สร้างชั่วคราวออกจาก DOM หลังคลิก ไม่ลบ Blob ในทันที

### บรรทัด 110

```javascript
  window.setTimeout(() => URL.revokeObjectURL(url), 1000);
```

ตั้ง timer หนึ่งครั้ง 1,000 มิลลิวินาทีให้เรียก revokeObjectURL เพื่อคืนทรัพยากรของ object URL หลังให้เวลาการดาวน์โหลดเริ่ม; ไม่ได้ลบไฟล์ที่ผู้ใช้บันทึกลงเครื่อง

### บรรทัด 111

```javascript
});
```

ปิด callback, การเรียก document.addEventListener และคำสั่งด้วย }); ครบโครงสร้างที่เปิดบรรทัด84



## เงื่อนไขและข้อจำกัดของการเตือนที่ควรตอบได้

- สคริปต์นี้ถูกโหลดในหน้า1เท่านั้น ไม่มี service worker, push server หรือ scheduler ใน Python เมื่อปิดหน้า/ปิดเบราว์เซอร์จึงไม่มีโค้ดชุดนี้ทำงานต่อ
- localStorage แยกตาม origin และอยู่ในเบราว์เซอร์นั้น กุญแจเป็นวัน ไม่ใช่งาน/บัญชี ถ้ามีงานเพิ่มหลังเตือนวันนี้ ระบบไม่ส่งอีกเพราะใช้กุญแจเดิม การล้าง storage ทำให้ความจำหาย
- เปิดหลายแท็บพร้อมกันอาจอ่านว่ายังไม่เตือนก่อนทั้งคู่เขียนค่า เกิดการเตือนซ้ำได้ จึงเป็นการลดความซ้ำ มิใช่การรับประกันหนึ่งครั้งทั้งระบบ
- ถ้า storage ใช้ไม่ได้ ตัวแปร lastShownKey ยังช่วยในแท็บเดิม แต่ reload แล้วค่าหาย
- การขอสิทธิ์ต้องอาศัยการกระทำของผู้ใช้ และความสามารถของเบราว์เซอร์ การแสดงผลยังขึ้นกับระบบปฏิบัติการ [MDN: Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification)
- ช่วงเวลา60วินาทีเป็นเวลาที่ร้องขอ ไม่ใช่การรับประกันว่าจะทำงานตรงทุกนาที [MDN: setInterval](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval)
- ICS เป็นสำเนากิจกรรมหนึ่งงาน ดาวน์โหลดแล้วต้องนำเข้าแอปปฏิทินเอง การแก้ไขหรือลบงานในเว็บไม่ซิงก์ไปแก้ในปฏิทิน และดาวน์โหลดซ้ำอาจนำเข้าเป็นกิจกรรมซ้ำเพราะ UID ใหม่
- DTEND ของกิจกรรมทั้งวันเป็นวันสิ้นสุดที่ไม่นับรวม ส่วน VALARM ขอเตือนก่อนเริ่มหนึ่งวัน การนำเข้าและการตั้งค่าแอปปลายทางมีผลต่อการเตือนจริง ไม่ได้กำหนดเวลา09:00ไว้ [RFC 5545 ส่วน3.6.1 และ3.8.6.3](https://www.rfc-editor.org/rfc/rfc5545.html)
- ตัวสร้าง ICS ยังไม่มีการพับบรรทัดยาวตามข้อแนะนำ75 octets และไม่ได้ตรวจความเข้ากันได้กับแอปปฏิทินทุกตัว จึงไม่ควรอ้างว่าผ่านการตรวจมาตรฐานครบถ้วน [RFC 5545 ส่วน3.1](https://www.rfc-editor.org/rfc/rfc5545.html#section-3.1)

## โครงสร้าง JSON และกติกาที่ทุกคนควรรู้

| ส่วน | ความหมาย |
|---|---|
| [ ... ] | array หลายรายการ; Python อ่านเป็น list |
| { ... } | object ของ key-value; Python อ่านเป็น dict |
| "key": value | colon จับคู่ชื่อ field กับค่า |
| , | คั่น field/รายการ; ห้ามมีตัวสุดท้ายเกินมา |
| "ข้อความ" | string ต้องใช้ double quote ใน JSON |
| 6, 2, 0 | number; JSON อาจเป็นจำนวนเต็มหรือทศนิยม |
| ช่องว่าง/การขึ้นบรรทัด | ช่วยอ่าน ไม่เปลี่ยนโครงสร้างข้อมูลนอก string |

ห้า field ของงานเป็นข้อมูลที่บันทึกจริง ส่วน remaining_hours, days_left, progress, status, tone, no, gap และ hours_per_day เป็นข้อมูลคำนวณเฉพาะหน้า ไม่จำเป็นต้องเพิ่มกลับลง data.json

## ต่างกันอย่างไรระหว่างไฟล์ข้อมูลสองไฟล์

data.json เป็นข้อมูลใช้งานปัจจุบัน หน้า2เขียนไฟล์นี้ ส่วน data.sample.json เป็นชุดตั้งต้นที่ตัวตรวจใช้คืนค่า ทั้งสองไฟล์ตรงกัน ณ วันที่จัดทำเอกสาร แต่ไม่มีระบบทำสำเนาให้ตรงกันทุกครั้งที่แก้ไขงาน หากจะเก็บงานจริงก่อนตรวจ ให้สำรองข้อมูลออกอีกไฟล์ หรือปรับ sample เมื่อกลุ่มตั้งใจเปลี่ยนชุดตั้งต้นด้วย


## data.json

เจ็ดงานตัวอย่าง มีห้า field ต่อรายการ

จำนวน 9 บรรทัดจริง · SHA-256: 74d01faf3a45a52d5f7a73d40c8593f4d49bf7d96e3d69e9d62e92dc873c17b1

### บรรทัด 1

```json
[
```

`[` เปิด array ของ JSON เมื่อ Python อ่านจะเป็น list เก็บงานตามลำดับ แต่ละงานเป็น object/dict และไม่มี field id ตามรูปแบบรายวิชา

### บรรทัด 2

```json
  {"title": "รายงานการทดลองวงจร", "course": "ฟิสิกส์", "due_date": "2026-09-26", "estimated_hours": 6, "done_hours": 2},
```

รายการตำแหน่ง 0 ใน list: `title` = รายงานการทดลองวงจร; `course` = ฟิสิกส์; `due_date` = 2026-09-26 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 6 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 2 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 3

```json
  {"title": "แบบฝึกหัดอนุพันธ์", "course": "คณิตศาสตร์", "due_date": "2026-09-27", "estimated_hours": 4, "done_hours": 0},
```

รายการตำแหน่ง 1 ใน list: `title` = แบบฝึกหัดอนุพันธ์; `course` = คณิตศาสตร์; `due_date` = 2026-09-27 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 4 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 4

```json
  {"title": "สรุปผลห้องปฏิบัติการ", "course": "เคมี", "due_date": "2026-09-28", "estimated_hours": 5, "done_hours": 1},
```

รายการตำแหน่ง 2 ใน list: `title` = สรุปผลห้องปฏิบัติการ; `course` = เคมี; `due_date` = 2026-09-28 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 5 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 1 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 5

```json
  {"title": "นำเสนอหัวข้อภาษาอังกฤษ", "course": "ภาษาอังกฤษ", "due_date": "2026-10-01", "estimated_hours": 6, "done_hours": 0},
```

รายการตำแหน่ง 3 ใน list: `title` = นำเสนอหัวข้อภาษาอังกฤษ; `course` = ภาษาอังกฤษ; `due_date` = 2026-10-01 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 6 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 6 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 6

```json
  {"title": "โครงงานเขียนโปรแกรม", "course": "การเขียนโปรแกรม", "due_date": "2026-10-04", "estimated_hours": 8, "done_hours": 2},
```

รายการตำแหน่ง 4 ใน list: `title` = โครงงานเขียนโปรแกรม; `course` = การเขียนโปรแกรม; `due_date` = 2026-10-04 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 8 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 2 ชั่วโมงที่ทำแล้ว; จึงเหลือ 6 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 7

```json
  {"title": "โปสเตอร์แนวคิดผลิตภัณฑ์", "course": "การออกแบบ", "due_date": "2026-10-06", "estimated_hours": 3, "done_hours": 0},
```

รายการตำแหน่ง 5 ใน list: `title` = โปสเตอร์แนวคิดผลิตภัณฑ์; `course` = การออกแบบ; `due_date` = 2026-10-06 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 3 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 3 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 8

```json
  {"title": "ทบทวนก่อนสอบย่อย", "course": "คณิตศาสตร์", "due_date": "2026-10-08", "estimated_hours": 2, "done_hours": 0}
```

รายการตำแหน่ง 6 ใน list: `title` = ทบทวนก่อนสอบย่อย; `course` = คณิตศาสตร์; `due_date` = 2026-10-08 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 2 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 2 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. ไม่มี comma หลังปีกกาปิด เพราะเป็นงานสุดท้าย

### บรรทัด 9

```json
]
```

`]` ปิด array ที่เริ่มบรรทัด1 ไม่มี comma ต่อท้ายรายการสุดท้าย JSON ใช้ข้อมูลล้วนและไม่รองรับ comment แบบ Python/JavaScript


## data.sample.json

สำเนาข้อมูลตั้งต้นเนื้อหาเหมือน data.json ณ วันที่เอกสารนี้จัดทำ อธิบายทุกบรรทัดซ้ำเพื่อให้เปิดอ่านแยกไฟล์ได้

จำนวน 9 บรรทัดจริง · SHA-256: 74d01faf3a45a52d5f7a73d40c8593f4d49bf7d96e3d69e9d62e92dc873c17b1

### บรรทัด 1

```json
[
```

`[` เปิด array ของ JSON เมื่อ Python อ่านจะเป็น list เก็บงานตามลำดับ แต่ละงานเป็น object/dict และไม่มี field id ตามรูปแบบรายวิชา

### บรรทัด 2

```json
  {"title": "รายงานการทดลองวงจร", "course": "ฟิสิกส์", "due_date": "2026-09-26", "estimated_hours": 6, "done_hours": 2},
```

รายการตำแหน่ง 0 ใน list: `title` = รายงานการทดลองวงจร; `course` = ฟิสิกส์; `due_date` = 2026-09-26 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 6 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 2 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 3

```json
  {"title": "แบบฝึกหัดอนุพันธ์", "course": "คณิตศาสตร์", "due_date": "2026-09-27", "estimated_hours": 4, "done_hours": 0},
```

รายการตำแหน่ง 1 ใน list: `title` = แบบฝึกหัดอนุพันธ์; `course` = คณิตศาสตร์; `due_date` = 2026-09-27 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 4 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 4

```json
  {"title": "สรุปผลห้องปฏิบัติการ", "course": "เคมี", "due_date": "2026-09-28", "estimated_hours": 5, "done_hours": 1},
```

รายการตำแหน่ง 2 ใน list: `title` = สรุปผลห้องปฏิบัติการ; `course` = เคมี; `due_date` = 2026-09-28 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 5 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 1 ชั่วโมงที่ทำแล้ว; จึงเหลือ 4 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 5

```json
  {"title": "นำเสนอหัวข้อภาษาอังกฤษ", "course": "ภาษาอังกฤษ", "due_date": "2026-10-01", "estimated_hours": 6, "done_hours": 0},
```

รายการตำแหน่ง 3 ใน list: `title` = นำเสนอหัวข้อภาษาอังกฤษ; `course` = ภาษาอังกฤษ; `due_date` = 2026-10-01 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 6 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 6 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 6

```json
  {"title": "โครงงานเขียนโปรแกรม", "course": "การเขียนโปรแกรม", "due_date": "2026-10-04", "estimated_hours": 8, "done_hours": 2},
```

รายการตำแหน่ง 4 ใน list: `title` = โครงงานเขียนโปรแกรม; `course` = การเขียนโปรแกรม; `due_date` = 2026-10-04 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 8 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 2 ชั่วโมงที่ทำแล้ว; จึงเหลือ 6 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 7

```json
  {"title": "โปสเตอร์แนวคิดผลิตภัณฑ์", "course": "การออกแบบ", "due_date": "2026-10-06", "estimated_hours": 3, "done_hours": 0},
```

รายการตำแหน่ง 5 ใน list: `title` = โปสเตอร์แนวคิดผลิตภัณฑ์; `course` = การออกแบบ; `due_date` = 2026-10-06 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 3 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 3 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. comma หลังปีกกาปิดคั่นรายการนี้จากงานถัดไป

### บรรทัด 8

```json
  {"title": "ทบทวนก่อนสอบย่อย", "course": "คณิตศาสตร์", "due_date": "2026-10-08", "estimated_hours": 2, "done_hours": 0}
```

รายการตำแหน่ง 6 ใน list: `title` = ทบทวนก่อนสอบย่อย; `course` = คณิตศาสตร์; `due_date` = 2026-10-08 เป็น string วันที่แบบปี-เดือน-วัน; `estimated_hours` = 2 ชั่วโมงที่คาดว่าจะใช้ทั้งหมด; `done_hours` = 0 ชั่วโมงที่ทำแล้ว; จึงเหลือ 2 ชั่วโมงจาก max(0, estimated_hours−done_hours). ปีกกาเปิด/ปิดครอบ object หนึ่งงาน; ชื่อ key และค่าข้อความใช้ double quote; colon ผูก key กับค่า; comma ภายใน object คั่นห้า field; ตัวเลขไม่ใส่ quote เพื่ออ่านเป็นจำนวนได้ทันที. ไม่มี comma หลังปีกกาปิด เพราะเป็นงานสุดท้าย

### บรรทัด 9

```json
]
```

`]` ปิด array ที่เริ่มบรรทัด1 ไม่มี comma ต่อท้ายรายการสุดท้าย JSON ใช้ข้อมูลล้วนและไม่รองรับ comment แบบ Python/JavaScript


## team.json

ข้อมูลทีมใช้ใน header/footer จาก base.html และในหน้า /team ผ่าน pages/team.py โดยไม่ต้องแก้ base.html

จำนวน 14 บรรทัดจริง · SHA-256: 08a3ff548fe93720618fd6764cd75415a10d4ff04bf6300f094bbddfd9180427

### บรรทัด 1

```json
{
```

ปีกกาเปิด JSON object ระดับนอกสุด มีสอง key คือ group และ members

### บรรทัด 2

```json
  "group": {
```

key `group` จับคู่กับ object ย่อยสำหรับข้อมูลกลุ่ม เปิดปีกกาไว้เพื่อใส่สี่ field

### บรรทัด 3

```json
    "name": "CodeMind",
```

`name` = "CodeMind" เป็นชื่อกลุ่มที่ base.html และหน้า /team นำไปแสดง ไม่ใช่ชื่อ class Python

### บรรทัด 4

```json
    "section": "กลุ่ม 6",
```

`section` = "กลุ่ม 6" คือข้อความแสดงกลุ่มตามที่ผู้ใช้ให้มา แม้ชื่อ field เดิมจะชื่อ section ก็ยังไม่ใช่หลักฐานยืนยันเลขเซกชันของรายวิชาแยกต่างหาก

### บรรทัด 5

```json
    "topic": "เดดไลน์ไม่ชนกัน",
```

`topic` = "เดดไลน์ไม่ชนกัน" เป็นชื่อโครงงาน แสดงในหน้าทีม/ส่วนท้ายเว็บ

### บรรทัด 6

```json
    "description": "เว็บช่วยบันทึกงาน วางแผนเวลา และเตือนก่อนงานหลายวิชาชนกัน"
```

`description` เก็บคำอธิบายสั้นของประโยชน์เว็บ ไม่มี comma ท้ายเพราะเป็น field สุดท้ายใน group

### บรรทัด 7

```json
  },
```

ปิด object group ด้วย } และใช้ comma คั่นก่อน key members ที่อยู่ระดับเดียวกัน

### บรรทัด 8

```json
  "members": [
```

`members` จับคู่กับ array ของสมาชิก เปิด [ เพื่อรับ object ของแต่ละคน

### บรรทัด 9

```json
    {"name": "นางสาวลักขณา ศรีโพธิ์", "id": "69130840153", "role": "Backend Dev (Python)", "task": "page1 · ภาพรวมงาน"},
```

สมาชิกคนที่1: ชื่อ นางสาวลักขณา ศรีโพธิ์; id "69130840153" เป็น string เพื่อเป็นรหัสประจำตัวไม่ใช่ค่าคำนวณ; role "Backend Dev (Python)"; task "page1 · ภาพรวมงาน". ทั้งสี่ key ใช้ในหน้า /team; comma หลัง } ระบุว่ายังมีสมาชิกถัดไป

### บรรทัด 10

```json
    {"name": "นายวายุ ทาโสม", "id": "69130840182", "role": "Project Lead (PM)", "task": "models.py · Assignment"},
```

สมาชิกคนที่2: ชื่อ นายวายุ ทาโสม; id "69130840182"; role "Project Lead (PM)"; task "models.py · Assignment". ค่านี้ระบุหน้าที่ตามที่กลุ่มมอบหมาย ไม่ได้เป็นหลักฐาน Git ว่าคนนี้เขียนทุกบรรทัดเอง

### บรรทัด 11

```json
    {"name": "นายไกรวิชญ์ บุ้งทอง", "id": "69130840247", "role": "Frontend Dev (HTML/CSS)", "task": "page2 · จัดการงาน"},
```

สมาชิกคนที่3: ชื่อ นายไกรวิชญ์ บุ้งทอง; id "69130840247"; role "Frontend Dev (HTML/CSS)"; task "page2 · จัดการงาน". เครื่องหมาย / และวงเล็บอยู่ภายใน string จึงเป็นเพียงข้อความ

### บรรทัด 12

```json
    {"name": "นายธีรเดช ฤทธิ์คำรพ", "id": "69130840320", "role": "QA / Test", "task": "page3 · แผนก่อนวันส่ง และ check.bat"}
```

สมาชิกคนที่4: ชื่อ นายธีรเดช ฤทธิ์คำรพ; id "69130840320"; role "QA / Test"; task "page3 · แผนก่อนวันส่ง และ check.bat". เป็นรายการสุดท้ายจึงไม่เติม comma หลังปีกกาปิด

### บรรทัด 13

```json
  ]
```

] ปิด array members ลำดับรายชื่อบนหน้าทีมตามลำดับข้อมูลนี้ อาจต่างจากลำดับพูดเพื่อให้เรื่องราวต่อเนื่อง

### บรรทัด 14

```json
}
```

} ปิด object ทั้งไฟล์ ต้องครบคู่กับบรรทัด1 ไม่มีคำสั่งให้โปรแกรมทำงานในไฟล์ JSON


## PAGES.md

เอกสารติดตามงานในแบบที่อาจารย์ให้มา ช่องติ๊กเป็นข้อความสถานะ ไม่ใช่ระบบทดสอบอัตโนมัติ

จำนวน 50 บรรทัดจริง · SHA-256: 7f332ea4c7777cdaa45ac358c8d38c8e7ddfe0d2b83e4e2c9ac6bb83240c5f80

### บรรทัด 1

```markdown
# PAGES · แดชบอร์ดความคืบหน้า
```

`#` ตามด้วยช่องว่างเป็นหัวเรื่อง Markdown ระดับ1; PAGES เป็นแบบบันทึกความคืบหน้าของรายวิชา ไม่ใช่โค้ด Python

### บรรทัด 2

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 3

```markdown
กรอกสัปดาห์ที่ 1 แล้วอัปเดตทุกครั้งที่ commit — อาจารย์ดูไฟล์นี้ + `git log` แทนการถาม
```

คำแนะนำเดิมให้อัปเดตแผนหลัง commit และใช้ Git log ตรวจงาน ข้อความนี้ไม่ได้สั่งให้โปรแกรมรัน git อัตโนมัติ

### บรรทัด 4

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 5

```markdown
**หัวข้อ:** เดดไลน์ไม่ชนกัน
```

`**...**` ทำตัวหนา; ระบุหัวข้อที่กลุ่มเลือกคือเดดไลน์ไม่ชนกัน

### บรรทัด 6

```markdown
**ชื่อกลุ่ม:** CodeMind · กลุ่ม 6
```

ระบุชื่อ CodeMind และกลุ่ม6 ตามข้อมูลผู้ใช้ เครื่องหมายจุดกลางใช้คั่นข้อความ

### บรรทัด 7

```markdown
**data.json เก็บอะไร (field):** title, course, due_date, estimated_hours, done_hours
```

บอกห้า field ใน data.json ให้ทีมใช้ชื่อสอดคล้องกันทุกหน้า การแสดงรายชื่อตรงนี้ไม่บังคับ schema ให้อัตโนมัติ

### บรรทัด 8

```markdown
**คัดลอก data.json → data.sample.json แล้ว:** [x]
```

`[x]` ในข้อความบอกว่ามีการคัดลอกข้อมูลตัวอย่างแล้ว; นี่เป็นบันทึกสถานะด้วยมือ ไม่ได้คัดลอกไฟล์เมื่อเปิด Markdown

### บรรทัด 9

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 10

```markdown
## team — หน้าทีม (สัปดาห์ 0)
```

`##` หัวข้อระดับ2 แยกงานหน้า /team ในสัปดาห์0

### บรรทัด 11

```markdown
- [x] กรอก `team.json` ครบทุกคน (ชื่อ, รหัส, บทบาท, งานที่รับผิดชอบ)
```

`- [x]` คือรายการตรวจที่ติ๊กแล้ว; กรอก team.json ครบชื่อ รหัส บทบาท และงาน เป็นสถานะตามเอกสาร

### บรรทัด 12

```markdown
- [x] เปิด /team เห็นชื่อทุกคน
```

บันทึกว่าตรวจหน้า /team แล้วเห็นสมาชิก ต้องตรวจซ้ำหลังเปลี่ยนข้อมูลหากจะยืนยันสถานะปัจจุบัน

### บรรทัด 13

```markdown
- [ ] commit `team: members filled` + push
```

`- [ ]` คือรายการยังไม่ติ๊ก; ข้อความใน backtick เป็นตัวอย่าง commit message การทำเอกสารชุดนี้ไม่ได้สร้าง commit หรือ push แทนสมาชิก

### บรรทัด 14

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 15

```markdown
## page1 — ผู้รับผิดชอบ: นางสาวลักขณา ศรีโพธิ์ · แบบจาก catalog: list + stats
```

กำหนดเจ้าของ page1 เป็นลักขณา และอ้างรูปแบบ list + stats จาก catalog ซึ่งสอดคล้องกับรายการงานและตัวนับสรุป

### บรรทัด 16

```markdown
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
```

บันทึกว่านำแบบตัวอย่างมาปรับ TITLE แล้ว TITLE ถูกใช้เป็นชื่อหน้าในเมนู

### บรรทัด 17

```markdown
- [x] ใช้ field ของ data.json ของกลุ่ม
```

บันทึกว่าหน้า1ใช้ชื่อ field ของกลุ่มตรงกับ JSON

### บรรทัด 18

```markdown
- [x] เปิด /page1 ได้ ไม่มี TODO
```

บันทึกว่าหน้า /page1 เปิดได้และไม่มีตัวแทนงานที่ยังไม่ทำในไฟล์ที่ตรวจ ไม่ได้หมายถึงทุกกรณีผิดพลาดผ่านการทดสอบแล้ว

### บรรทัด 19

```markdown
- [x] `check.bat` → /page1 ✓ ไม่มี warning
```

บันทึกผลตรวจหน้า1จาก check.bat ว่าผ่านและไม่มี warning ณ รอบที่บันทึก

### บรรทัด 20

```markdown
- [ ] commit `page1: ...`
```

ช่อง commit ของ page1 ยังว่าง ต้องเป็นประวัติงานจริงของผู้รับผิดชอบ ไม่ควรแต่งประวัติย้อนหลัง

### บรรทัด 21

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 22

```markdown
## page2 — ผู้รับผิดชอบ: นายไกรวิชญ์ บุ้งทอง · แบบจาก catalog: form
```

กำหนดเจ้าของ page2 เป็นไกรวิชญ์ และอ้าง catalog/form ซึ่งนำไปใช้กับเพิ่ม/แก้ไข/ลบงาน

### บรรทัด 23

```markdown
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
```

บันทึกว่าปรับแบบและ TITLE ของหน้า2 แล้ว

### บรรทัด 24

```markdown
- [x] ใช้ field ของ data.json ของกลุ่ม
```

บันทึกว่าหน้า2ใช้ field ตรงกับข้อมูล เช่น estimated_hours และ done_hours

### บรรทัด 25

```markdown
- [x] เปิด /page2 ได้ ไม่มี TODO
```

บันทึกว่าหน้า /page2 เปิดได้และไม่มี placeholder ในไฟล์ที่ระบบตรวจ

### บรรทัด 26

```markdown
- [x] `check.bat` → /page2 ✓ ไม่มี warning
```

บันทึกผล check.bat ของหน้า2 จากรอบที่ตรวจ ไม่ครอบคลุมการโจมตีหรือการใช้งานพร้อมกันหลายคน

### บรรทัด 27

```markdown
- [ ] commit `page2: ...`
```

ช่อง commit หน้า2 ยังว่าง เป็นงานด้านประวัติการทำงานที่สมาชิกต้องทำจริง

### บรรทัด 28

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 29

```markdown
## page3 — ผู้รับผิดชอบ: นายธีรเดช ฤทธิ์คำรพ · แบบจาก catalog: ranking + calculator
```

กำหนดเจ้าของ page3 เป็นธีรเดช อ้าง catalog/ranking + calculator: จัดลำดับวันส่งและคำนวณเวลาที่มี

### บรรทัด 30

```markdown
- [x] คัดลอกจาก catalog แล้วเปลี่ยน TITLE
```

บันทึกว่าปรับแบบและ TITLE หน้า3 แล้ว

### บรรทัด 31

```markdown
- [x] ใช้ field ของ data.json ของกลุ่ม
```

บันทึกว่าหน้า3ใช้ field กลุ่มตรงกัน

### บรรทัด 32

```markdown
- [x] เปิด /page3 ได้ ไม่มี TODO
```

บันทึกว่าหน้า /page3 เปิดได้และไม่เหลือ placeholder ในไฟล์ที่ตรวจ

### บรรทัด 33

```markdown
- [x] `check.bat` → /page3 ✓ ไม่มี warning
```

บันทึกผล check.bat ของหน้า3 ว่าผ่านในรอบที่ตรวจ

### บรรทัด 34

```markdown
- [ ] commit `page3: ...`
```

ช่อง commit หน้า3 ยังไม่ติ๊ก ไม่ถือว่าการสร้างคู่มือแทนที่ข้อกำหนดนี้

### บรรทัด 35

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 36

```markdown
## models.py — ผู้รับผิดชอบ: นายวายุ ทาโสม
```

หัวข้องาน models.py กำหนดวายุเป็นผู้รับผิดชอบอธิบายแบบจำลอง Assignment

### บรรทัด 37

```markdown
- [x] เปลี่ยนชื่อ class ให้ตรงหัวข้อ, field ตรง data.json
```

บันทึกว่าชื่อ class และ field ตรงหัวข้อและข้อมูลจริง

### บรรทัด 38

```markdown
- [x] method 1 ตัวที่มีประโยชน์ (ไม่เหลือ TODO)
```

บันทึกว่ามี method ที่มีประโยชน์ ปัจจุบันมี remaining_hours และ days_left เพิ่มจาก __init__

### บรรทัด 39

```markdown
- [x] มีหน้าใดหน้าหนึ่งใช้ class นี้ (เช่น แบบ detail)
```

บันทึกว่ามีหน้าใช้ class นี้จริง ปัจจุบัน page1/page2/page3 ต่างสร้าง Assignment

### บรรทัด 40

```markdown
- [x] `python check_project.py` → class ✓ 9/9
```

บันทึกผลคะแนนส่วน class 9/9 จากตัวตรวจ ไม่ใช่คะแนนรวมทั้งรายวิชา

### บรรทัด 41

```markdown
- [ ] commit `models: ...`
```

ช่อง commit models ยังว่าง ข้อความ models: ... เป็นรูปแบบให้สมาชิกใส่รายละเอียดจริง

### บรรทัด 42

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 43

```markdown
## ส่งงาน
```

หัวข้อรายการก่อนส่งงาน

### บรรทัด 44

```markdown
- [x] `check.bat` → 60/60, pytest 4 passed, ไม่มี warning
```

บันทึกผลเดิมว่า automated score60/60 และ pytest4ผ่าน ไม่มี warning; อีก40คะแนนเป็นอาจารย์ให้เรื่องทีมและการนำเสนอ จึงห้ามกล่าวว่าได้100/100แล้ว

### บรรทัด 45

```markdown
- [ ] ทุกคนอยู่ใน `git log`
```

ช่องยืนยันว่าทุกคนอยู่ใน git log ยังว่าง เอกสารนำเสนอระบุความรับผิดชอบ ไม่อ้างว่าข้อกำหนดนี้สำเร็จ

### บรรทัด 46

```markdown
- [ ] นำเสนอ: ทุกคนอธิบายหน้าของตัวเอง 1 นาที
```

ช่องซ้อมนำเสนอคนละหนึ่งนาทียังว่าง สคริปต์ฉบับย่อในเอกสารนำเสนอจัดไว้รองรับข้อนี้

### บรรทัด 47

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 48

```markdown
## หมายเหตุเรื่องข้อมูล
```

หัวข้อคำอธิบายผลข้างเคียงของตัวตรวจต่อข้อมูล

### บรรทัด 49

```markdown

```

บรรทัดว่าง แยกกลุ่มคำสั่งให้อ่านง่าย ไม่มีคำสั่งทำงานและไม่สร้างข้อมูลใหม่

### บรรทัด 50

```markdown
หน้านี้มีฟอร์มบันทึกงาน ก่อนรัน `check.bat` หรือ `check.sh` หลังจากกรอกงานจริงแล้ว ให้คัดลอก `data.json` ไป `data.sample.json` ก่อน เพราะตัวตรวจจะคืน `data.json` จากไฟล์สำรองนี้เมื่อทดสอบฟอร์ม
```

คำเตือนเฉพาะโครงการ: check_project ทดลอง handle({}) แล้วคืน data.json จาก sample; ถ้ามีข้อมูลจริงที่ต้องเก็บ ควรสำรองก่อนตรวจ การคัดลอกข้อมูลจริงไป sample เป็นทางเลือกเมื่อกลุ่มต้องการเปลี่ยนข้อมูลตั้งต้นด้วย อย่าคัดลอกทับโดยไม่ตรวจว่าต้องการเก็บ sample ชุดเดิมหรือไม่


## README.md

ไฟล์นี้เป็นบริบทเพิ่มเติมนอก14ไฟล์ที่ปรับทำโครงงาน ไม่ใช่ข้อกำหนดของระบบคำนวณ

จำนวน 1 บรรทัดจริง · SHA-256: 5d1b2b5f242be741d478c94acb43671007aa891a5bf4f10e37a550219c32e57a

### บรรทัด 1

```markdown
"# ManagerTime" 
```

ไฟล์ประกอบที่มีอยู่ก่อนงานเอกสารรอบนี้ ข้อความจริงคือ `"# ManagerTime" ` มี double quote ครอบข้อความ ทำให้ # ไม่ได้อยู่ต้นบรรทัดตามรูป heading Markdown ปกติ จึงอาจแสดงเป็นข้อความธรรมดา เอกสารนี้บันทึกไว้เพื่อให้เห็นบริบท ไม่ได้อ้างว่าเป็นไฟล์ที่ปรับระหว่างสร้างฟังก์ชันเดดไลน์



## ตัวอย่างข้อมูล ณ วันที่อ้างอิง 29 กันยายน 2569

วันอ้างอิงมีไว้สำหรับอธิบายเท่านั้น โปรแกรมอ่านวันจริงจากเครื่องเมื่อเปิดหน้า

| งาน | เหลือชั่วโมง | days_left | หน้า1 | สะสมก่อน/ถึงงานนี้ |
|---|---:|---:|---|---:|
| รายงานการทดลองวงจร | 4 | -3 | เกินกำหนด | 4 |
| แบบฝึกหัดอนุพันธ์ | 4 | -2 | เกินกำหนด | 8 |
| สรุปผลห้องปฏิบัติการ | 4 | -1 | เกินกำหนด | 12 |
| นำเสนอหัวข้อภาษาอังกฤษ | 6 | 2 | ใกล้ส่ง | 18 |
| โครงงานเขียนโปรแกรม | 6 | 5 | ยังมีเวลา | 24 |
| โปสเตอร์แนวคิดผลิตภัณฑ์ | 3 | 7 | ยังมีเวลา | 27 |
| ทบทวนก่อนสอบย่อย | 2 | 9 | ยังมีเวลา | 29 |

หน้า1จึงมีงานเปิด7งาน เหลือรวม29ชั่วโมง เกินกำหนด3งาน และใกล้ส่งรวมวันนี้ถึงอีก3วันจำนวน1งาน คำแสดงสถานะในตารางนี้สรุปความหมาย ให้ดู string ต้นฉบับ Python เมื่อต้องตอบข้อความบนจอแบบตรงตัว

ที่ว่างวันละ2ชั่วโมง หน้า3จะมองทั้ง7งานมีความเสี่ยง: สามงานแรกเกินกำหนด; งานภาษาอังกฤษมี18ชั่วโมงสะสมแต่มี6ชั่วโมงให้ทำจึงขาด12; โครงงานมี24แต่มี12จึงขาด12; โปสเตอร์มี27แต่มี16จึงขาด11; ทบทวนมี29แต่มี20จึงขาด9 ตัวเลขนี้ไม่ได้หมายความว่าวันอื่นจะได้ผลเหมือนกัน

## คำถามทบทวนส่วนนี้

1. JSON.parse กับ json.load ต่างกันอย่างไร? ตัวแรกในเบราว์เซอร์แปลงข้อความที่ฝังใน HTML ส่วนตัวหลังใน Python อ่านข้อมูลจาก file object
2. เหตุใด localStorage ไม่ใช่ฐานข้อมูลของเว็บนี้? มันเก็บเพียงกุญแจเตือนรายวัน ข้อมูลหลักยังอยู่ที่ data.json ฝั่ง Python
3. กดอนุญาตแล้วไม่เห็นแบนเนอร์แปลว่าโค้ดผิดเสมอหรือไม่? ไม่เสมอ อาจเตือนวันนี้แล้ว ไม่มีงานเข้าเกณฑ์ หรือระบบ/เบราว์เซอร์จำกัดการแสดง ต้องตรวจแต่ละเงื่อนไข
4. ไฟล์ .ics ทำงานเองเมื่อดาวน์โหลดหรือไม่? ไม่ ผู้ใช้ต้องนำเข้าในปฏิทินที่รองรับและเปิดการแจ้งเตือน
5. การรันตัวตรวจมีผลกับข้อมูลหรือไม่? มี ตัวตรวจคืน data.json จาก data.sample.json หลังทดลอง handler
6. เหตุใดรหัสนักศึกษาใส่ quote? เป็นรหัสระบุตัว ไม่ใช่ค่าที่นำมาบวกหรือลบ และควรคงตัวอักษรเดิม
