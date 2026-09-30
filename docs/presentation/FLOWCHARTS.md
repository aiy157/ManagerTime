# ผังงานระบบ “เดดไลน์ไม่ชนกัน”

ผังงานนี้อ้างอิงโค้ดจริง ณ วันที่ 29 กันยายน 2569 ลูกศรคือทิศทางการทำงาน สี่เหลี่ยมคือขั้นตอน ข้าวหลามตัดคือเงื่อนไข กระบอกคือไฟล์ข้อมูล และกรอบปลายมนคือจุดเริ่ม/จบ ผลที่เกี่ยวกับวันจะเปลี่ยนตามวันที่เครื่องรัน

## 1. ภาพรวมทั้งระบบ

```mermaid
flowchart LR
    U(["ผู้ใช้"]) --> B["เบราว์เซอร์"]
    B -->|GET หรือ POST| A["app.py<br/>โครงที่อาจารย์ให้"]
    A --> R{"เส้นทางใด"}
    R -->|หน้าแรก| H["home.html"]
    R -->|/team| T["team.py + team.html"]
    R -->|/page1| P1["page1.py + page1.html"]
    R -->|/page2| P2["page2.py + page2.html"]
    R -->|/page3| P3["page3.py + page3.html"]
    J[(data.json)] --> S["storage.load()"]
    S --> P1
    S --> P2
    S --> P3
    M["models.Assignment"] --> P1
    M --> P2
    M --> P3
    P2 -->|storage.save| J
    TJ[(team.json)] --> T
    P1 --> JS["reminders.js"]
    JS --> N["Browser Notification"]
    JS --> I["ดาวน์โหลดไฟล์ .ics"]
```

ข้อสังเกต: app.py, storage.py, base.html และไฟล์ตรวจเป็นไฟล์ห้ามแก้ ระบบไม่มีฐานข้อมูล บัญชีผู้ใช้ หรือบริการ push ภายนอก การบันทึกจากหน้า2เขียน data.json ทั้งไฟล์

## 2. หน้าแรก /

```mermaid
flowchart TD
    A(["เปิด /"]) --> B["app.py เรียก route home"]
    B --> C["render templates/home.html"]
    C --> D["base.html สร้างหัวเว็บ เมนู main และ footer"]
    D --> E["home.html แสดงชื่อหัวข้อ คำอธิบาย และทางลัด 3 หน้า"]
    E --> F(["ผู้ใช้เลือก ภาพรวม / จัดการงาน / แผนก่อนวันส่ง"])
```

หน้าแรกไม่มี `build()` และไม่อ่าน `data.json` เพื่อคำนวณตัวเลข เป็นทางเข้าและอธิบายประโยชน์ของระบบ ชื่อกลุ่มในหัว/ท้ายมาจาก context ของ `team.json` ที่ app.py จัดให้

## 3. หน้าทีม /team

```mermaid
flowchart TD
    A(["เปิด /team"]) --> B["team.build()"]
    B --> C["เปิด team.json แบบ UTF-8"]
    C --> D["วนสมาชิกทีละคน"]
    D --> E["ตัดคำนำหน้าชื่อที่รู้จัก"]
    E --> F{"ชื่อที่เหลือว่างหรือไม่"}
    F -->|ใช่| G["initial = ?"]
    F -->|ไม่ใช่| H["initial = อักขระแรก"]
    G --> I["เพิ่มสมาชิกในรายการแสดง"]
    H --> I
    I --> J{"ยังมีสมาชิกอีกหรือไม่"}
    J -->|มี| D
    J -->|หมด| K["คืน group, members, count"]
    K --> L["team.html แสดงข้อมูลกลุ่มและสมาชิก"]
    L --> M(["จบ"])
```

หน้าทีมใช้ไฟล์เดิมจาก skeleton ซึ่งกลุ่มแก้เฉพาะข้อมูลใน `team.json` ไม่ควรกล่าวว่าแก้ `pages/team.py` หรือ `templates/team.html` หากไม่มีการเปลี่ยนจริง

## 4. Page 1 — ภาพรวมงาน

```mermaid
flowchart TD
    A(["GET /page1"]) --> B["page1.build()"]
    B --> C["สร้าง list และตัวนับเป็นศูนย์"]
    C --> D["storage.load() อ่าน data.json"]
    D --> E{"มี row ถัดไปหรือไม่"}
    E -->|มี| F["สร้าง Assignment จาก 5 field"]
    F --> G["คำนวณ remaining_hours และ days_left"]
    G --> H["สำเนา row แล้วเติม remaining, days, progress"]
    H --> I{"remaining = 0 หรือไม่"}
    I -->|ใช่| J["status เสร็จแล้ว<br/>tone good"]
    I -->|ไม่ใช่| K["เพิ่ม open_count และ remaining_total"]
    K --> L{"days_left อยู่ช่วงใด"}
    L -->|น้อยกว่า 0| M["เพิ่ม overdue_count<br/>status เกินกำหนด<br/>tone bad"]
    L -->|เท่ากับ 0| N["เพิ่ม soon_count<br/>status ส่งวันนี้<br/>tone bad"]
    L -->|1 ถึง 3| O["เพิ่ม soon_count<br/>status อีก N วัน<br/>tone gold"]
    L -->|มากกว่า 3| P["status อีก N วัน<br/>tone ว่าง"]
    J --> Q["append item"]
    M --> Q
    N --> Q
    O --> Q
    P --> Q
    Q --> E
    E -->|หมด| R["selection loop"]
    R --> S["งานค้างขึ้นก่อน<br/>ในงานค้าง วันส่งใกล้ขึ้นก่อน"]
    S --> T["คืน items และสถิติ 4 ค่า"]
    T --> U["page1.html แสดงการ์ด รายการ progress และปุ่ม"]
    U --> V(["จบการ render"])
```

### นิยามที่มักสับสน

- `soon_count` นับงานค้างที่ส่งวันนี้ถึงอีก 3 วัน ไม่รวมงานเกินกำหนด
- `progress` ใช้ `int` ตัดเศษและ `min(100, ...)` จำกัดไม่เกิน 100
- งานเสร็จยังอยู่ในรายการ แต่ selection loop วางไว้หลังงานค้าง
- การเรียงเป็น selection loop ประมาณ `O(n²)` เพื่อให้เห็น loop/if ตามบทเรียน

## 5. Page 1 — การแจ้งเตือนในเบราว์เซอร์

```mermaid
flowchart TD
    A(["page1 โหลด reminders.js"]) --> B{"พบ data ปุ่ม และ status ครบหรือไม่"}
    B -->|ไม่ครบ| Z["ข้ามระบบแจ้งเตือน<br/>ส่วนปฏิทินยังติด listener"]
    B -->|ครบ| C["JSON.parse ข้อมูล snapshot"]
    C --> D["updateStatus()"]
    D --> E{"รองรับ Notification<br/>และ secure context หรือไม่"}
    E -->|ไม่| F["แสดงไม่รองรับ และปิดปุ่ม"]
    E -->|ใช่| G{"permission"}
    G -->|granted| H["แสดงเปิดแล้ว"]
    G -->|denied| I["แสดงถูกปิดกั้น และปิดปุ่ม"]
    G -->|default| J["เชิญให้กดอนุญาต"]
    J --> K{"ผู้ใช้กดปุ่มหรือไม่"}
    K -->|กด| L["requestPermission()"]
    L --> D
    H --> M["checkReminders ทันที<br/>และขอทำซ้ำทุก 60 วินาที"]
    M --> N{"สิทธิ์ยัง granted หรือไม่"}
    N -->|ไม่| Y(["จบรอบ"])
    N -->|ใช่| O["filter งาน remaining > 0<br/>และ daysUntil <= 3"]
    O --> P{"มีงานเร่งด่วนหรือไม่"}
    P -->|ไม่มี| Y
    P -->|มี| Q["สร้าง key ตามวันที่เครื่อง"]
    Q --> R{"ตัวแปรหรือ localStorage<br/>บอกว่าเตือนวันนี้แล้วหรือไม่"}
    R -->|ใช่| Y
    R -->|ไม่| S["สร้าง Notification"]
    S --> T{"สร้างสำเร็จหรือไม่"}
    T -->|สำเร็จ| U["จำ key ในตัวแปรและ localStorage"]
    T -->|ล้มเหลว| V["แสดงข้อความผิดพลาด"]
    U --> Y
    V --> Y
```

ข้อจำกัดสำคัญ: `tasks` เป็นข้อมูลตอนโหลดหน้า หากแก้ข้อมูลในอีกแท็บต้อง reload; งานเกินกำหนดเข้าเกณฑ์เพราะค่าติดลบยัง `<= 3`; timer อาจถูกเบราว์เซอร์หน่วง; เมื่อปิดหน้าไม่มี service worker หรือ push ทำงานต่อ; localStorage ลดการเตือนซ้ำใน origin เดิมแต่ไม่รับประกันหนึ่งครั้งในหลายแท็บ/หลายเครื่อง

## 6. Page 1 — ดาวน์โหลดไฟล์ปฏิทิน

```mermaid
flowchart TD
    A(["ผู้ใช้กดปุ่มเพิ่มปฏิทิน"]) --> B["document click listener"]
    B --> C["closest หา element ที่มี data-calendar-date"]
    C --> D{"พบปุ่มหรือไม่"}
    D -->|ไม่พบ| Z(["จบ click"])
    D -->|พบ| E["อ่านวัน ชื่องาน วิชา จาก dataset"]
    E --> F["แปลงวันเริ่มเป็น YYYYMMDD"]
    F --> G["คำนวณวันถัดไปเป็น DTEND แบบไม่นับรวม"]
    G --> H["สร้าง DTSTAMP และ escape ข้อความ"]
    H --> I["ประกอบ VCALENDAR, VEVENT, VALARM"]
    I --> J["TRIGGER -P1D = ขอเตือนก่อน 1 วัน"]
    J --> K["สร้าง Blob ชนิด text/calendar UTF-8"]
    K --> L["สร้าง object URL และลิงก์ชั่วคราว"]
    L --> M["สั่งดาวน์โหลด deadline-วันที่.ics"]
    M --> N["ลบลิงก์ และ revoke URL หลัง 1 วินาที"]
    N --> O(["ผู้ใช้ต้องนำเข้าไฟล์ในแอปปฏิทิน"])
```

นี่เป็นกิจกรรมทั้งวัน ไม่มีเวลา 09:00 หรือ 23:59 ไม่มีการเชื่อม Google Calendar API และไม่มี live sync เมื่อแก้งาน UID สร้างจากเวลาที่กดทุกครั้ง การดาวน์โหลดซ้ำจึงอาจนำเข้าเป็นรายการซ้ำ

## 7. Page 2 — เปิดหน้าจัดการงาน

```mermaid
flowchart TD
    A(["GET /page2"]) --> B["page2.build()"]
    B --> C["items = [] และ position = 0"]
    C --> D["storage.load()"]
    D --> E{"มี row ถัดไปหรือไม่"}
    E -->|มี| F["สำเนา row เป็น item"]
    F --> G["item.no = position"]
    G --> H["สร้าง Assignment และคำนวณ remaining_hours"]
    H --> I["append item"]
    I --> J["position = position + 1"]
    J --> E
    E -->|หมด| K["คืน items และ count"]
    K --> L["page2.html แสดงฟอร์มเพิ่ม<br/>และการ์ดแก้ไข/ลบทุกงาน"]
    L --> M(["รอผู้ใช้ส่ง POST"])
```

`no` เป็นตำแหน่งชั่วคราวเริ่ม 0 ไม่ใช่รหัสงานถาวร ฟอร์มเพิ่ม แก้ไข และลบเป็นคนละ `form` ไม่ซ้อนกัน

## 8. Page 2 — ตรวจข้อมูลร่วม

```mermaid
flowchart TD
    A(["check(form)"]) --> B["อ่าน title/course แล้ว strip"]
    B --> C["อ่าน due_date"]
    C --> D["read_hours estimated และ done"]
    D --> E{"title หรือ course ว่างหรือไม่"}
    E -->|ใช่| X1["คืน error ต้องกรอกชื่อและวิชา"]
    E -->|ไม่| F{"title > 80 หรือ course > 40 หรือไม่"}
    F -->|ใช่| X2["คืน error ข้อความยาวเกิน"]
    F -->|ไม่| G{"date.fromisoformat ผ่านหรือไม่"}
    G -->|ไม่ผ่าน| X3["คืน error วันส่งไม่ถูกต้อง"]
    G -->|ผ่าน| H{"estimate เป็นเลข<br/>0 < estimate <= 200 หรือไม่"}
    H -->|ไม่| X4["คืน error ชั่วโมงประมาณการ"]
    H -->|ใช่| I{"done เป็นเลข<br/>0 <= done <= estimate หรือไม่"}
    I -->|ไม่| X5["คืน error ชั่วโมงที่ทำแล้ว"]
    I -->|ใช่| J["คืน dict 5 field และ error ว่าง"]
```

`read_hours` รับ `TypeError/ValueError` และปฏิเสธ `NaN` กับ infinity ด้วย Python validation จึงไม่พึ่งเพียง `required/min/max` ใน HTML

## 9. Page 2 — POST เพิ่ม แก้ไข ลบ

```mermaid
flowchart TD
    A(["POST /page2"]) --> B["app.py ส่ง dict ฟอร์มเข้า handle"]
    B --> C["อ่าน action และ load items"]
    C --> D{"action = add หรือไม่"}
    D -->|ใช่| E["check(form)"]
    E --> F{"มี error หรือไม่"}
    F -->|มี| X["คืนข้อความ ✗ โดยไม่ save"]
    F -->|ไม่มี| G["append task และ storage.save"]
    G --> OK1["คืน ✓ เพิ่มงานแล้ว"]
    D -->|ไม่| H["อ่าน no เป็น position"]
    H --> I{"เป็น digit และ index อยู่ใน list หรือไม่"}
    I -->|ไม่| NF["คืน ✗ ไม่พบงานนี้"]
    I -->|ใช่| J["index = int(position)"]
    J --> K{"action ใด"}
    K -->|delete| L["pop(index) และ save"]
    L --> OK2["คืน ✓ ลบงานแล้ว"]
    K -->|update| M["check(form)"]
    M --> N{"มี error หรือไม่"}
    N -->|มี| X
    N -->|ไม่มี| O["items[index] = task และ save"]
    O --> OK3["คืน ✓ บันทึกการแก้ไขแล้ว"]
    K -->|ค่าอื่น| UK["คืน ✗ ไม่รู้จักคำสั่ง"]
    X --> R["app.py redirect กลับ /page2 พร้อม msg"]
    OK1 --> R
    NF --> R
    OK2 --> R
    OK3 --> R
    UK --> R
    R --> S(["GET ใหม่และแสดง banner"])
```

การ reload จาก POST ผ่าน redirect ช่วยลดการส่งฟอร์มซ้ำเมื่อผู้ใช้กด refresh แต่ไม่มี transaction หรือการป้องกันสองผู้ใช้เขียนพร้อมกัน

## 10. Page 3 — แผนก่อนวันส่ง

```mermaid
flowchart TD
    A(["GET /page3?hours=..."]) --> B["อ่าน hours ค่าเริ่มต้น 2"]
    B --> C{"float แปลงได้หรือไม่"}
    C -->|ไม่ได้| D["daily_hours = 2<br/>notice ใช้ค่าเริ่มต้น"]
    C -->|ได้| E{"NaN, infinity,<br/><= 0 หรือ > 12 หรือไม่"}
    E -->|ใช่| F["daily_hours = 2<br/>notice แจ้งช่วงถูกต้อง"]
    E -->|ไม่| G["ใช้ค่าที่กรอก"]
    D --> H["load data.json"]
    F --> H
    G --> H
    H --> I["วนสร้าง Assignment"]
    I --> J{"remaining_hours > 0 หรือไม่"}
    J -->|ไม่| K["ข้ามงานเสร็จ"]
    J -->|ใช่| L["เก็บ title/course/due/days/remaining"]
    K --> M{"มี row ต่อหรือไม่"}
    L --> M
    M -->|มี| I
    M -->|หมด| N["selection loop เรียง due_date"]
    N --> O["cumulative = 0, risk = 0"]
    O --> P{"มี task ถัดไปหรือไม่"}
    P -->|มี| Q["บวก remaining เข้า cumulative ก่อน"]
    Q --> R{"days_left < 0 หรือไม่"}
    R -->|ใช่| S["เกินกำหนด, bad<br/>gap = ชั่วโมงงาน<br/>risk + 1"]
    R -->|ไม่| T["capacity = (days + 1) × daily"]
    T --> U["gap = round(max(0, cumulative-capacity),1)<br/>hours/day = round(cumulative/(days+1),1)"]
    U --> V{"gap > 0 หรือไม่"}
    V -->|ใช่| W["เวลาไม่พอ, bad, risk + 1"]
    V -->|ไม่| X{"days_left <= 3 หรือไม่"}
    X -->|ใช่| Y["ควรเริ่มตอนนี้, gold"]
    X -->|ไม่| Z["ตามแผน, good"]
    S --> P
    W --> P
    Y --> P
    Z --> P
    P -->|หมด| AA["focus = งานแรกถ้ามี"]
    AA --> AB["คืน tasks, daily_hours, risk_count, focus, notice"]
    AB --> AC["page3.html แสดงแผนและแบบปรับชั่วโมง"]
    AC --> AD(["จบ"])
```

จุดที่ต้องตอบตามโค้ด: งานเกินกำหนดถูกบวกใน `cumulative_hours` ก่อนเข้ากิ่ง และจึงเพิ่มภาระให้ deadline ถัดไป; capacity รวมวันนี้ด้วย `+1`; `gap` ถูกปัดหนึ่งตำแหน่งก่อนตรวจ; `risk_count` นับรายการเสี่ยง ไม่ได้นับจำนวนวันที่ชนกัน

## 11. การทดสอบและการส่งงาน

```mermaid
flowchart TD
    A(["ก่อนทดสอบ"]) --> B["สำรอง data.json ที่ต้องการเก็บ"]
    B --> C["รัน check.bat"]
    C --> D["check_project ตรวจหน้า 1-3<br/>พื้นฐาน Python และ hash ไฟล์ห้ามแก้"]
    D --> E["ตัวตรวจอาจเรียก handle ด้วยฟอร์มว่าง"]
    E --> F["finally: storage.reset<br/>คัดลอก data.sample.json ทับ data.json"]
    F --> G["pytest ตรวจ 4 กรณีที่อาจารย์ให้"]
    G --> H{"ผลเป็น 60/60 และ 4 passed หรือไม่"}
    H -->|ไม่| I["อ่าน error แล้วแก้เฉพาะไฟล์ที่อนุญาต"]
    I --> C
    H -->|ใช่| J["ตรวจหน้าจอและข้อมูลจริงอีกครั้ง"]
    J --> K["ตรวจ Git log ว่าทุกคนมีงานจริง"]
    K --> L["ซ้อมบทพูดและสาธิต"]
    L --> M(["พร้อมส่งเมื่อข้อกำหนดอาจารย์ครบ"])
```

60/60 เป็นคะแนนอัตโนมัติจาก 60 คะแนน อีก 40 คะแนนเป็นการทำงานเป็นทีมและการนำเสนอ ตัวทดสอบสี่กรณีไม่ได้พิสูจน์สูตร การแจ้งเตือน ความเข้ากันได้ของปฏิทิน หรือการใช้งานพร้อมกันทุกกรณี

## 12. ตารางเชื่อมผังงานกับไฟล์

| ผัง | แหล่งหลัก |
|---|---|
| ภาพรวม/route | app.py, storage.py, base.html ซึ่งห้ามแก้ |
| หน้าแรก | templates/home.html |
| ทีม | team.json ร่วมกับ pages/team.py และ templates/team.html เดิม |
| Page 1 | models.py, pages/page1.py, templates/page1.html |
| Notification/ICS | templates/page1.html, static/js/reminders.js |
| Page 2 | pages/page2.py, templates/page2.html |
| Page 3 | pages/page3.py, templates/page3.html |
| ทดสอบ | check.bat, check_project.py, test_pages.py, data.sample.json |

## วิธีใช้ตอนพรีเซนต์

เลือกแสดงผัง 1, 4, 9 และ 10 เป็นหลัก: ผัง 1 ให้ภาพรวม ผัง 4 อธิบายสถานะ ผัง 9 สาธิต CRUD และ validation ผัง 10 อธิบายความเสี่ยง หากอาจารย์ถามการแจ้งเตือนค่อยเปิดผัง 5–6 ไม่จำเป็นต้องอ่านทุกกล่องตามลำดับ ให้ชี้จุดตัดสินใจและยกตัวอย่างหนึ่งงาน
