# คู่มือ HTML, Jinja และ CSS ทุกบรรทัด — CodeMind กลุ่ม 6

เอกสารเพื่อให้นักศึกษาปี 1 ทบทวนและตอบคำถามอาจารย์ อ่านจากไฟล์จริงวันที่ 29 กันยายน 2026 รวมบรรทัดว่าง แยก HTML ทุกแท็ก ทุก attribute และ Jinja ทุกคำสั่ง ส่วน CSS แยกทุก selector และ declaration พร้อมค่าจริง ไม่ได้แก้แอปหรือรันชุดทดสอบในการจัดทำเอกสารนี้ และไม่ใช่การรับรองความปลอดภัยระดับระบบใช้งานจริง

## วิธีอ่าน

หัวข้อ L001 หมายถึง physical line ที่ 1 ของไฟล์ในหัวข้อใหญ่ปัจจุบัน กรอบโค้ดคัดลอกจากบรรทัดนั้นตรง ๆ รวมการย่อหน้า บรรทัดว่างมีกรอบว่างและคำอธิบาย ชื่อและตัวเลขที่เขียนตายตัวเป็น literal ส่วนที่อยู่ใน Jinja คำนวณก่อนส่งหน้าให้ browser

CRLF หรือ LF เป็นตัวจบบรรทัดและไม่มีความหมายเป็นคำสั่งของแอป HTML ปกติรวม whitespace ต่อเนื่องเป็นช่องว่างเดียว การย่อหน้า HTML/CSS ช่วยอ่านโครงสร้าง ต่างจาก Python ที่จำนวนการเยื้องแบ่งบล็อกคำสั่ง

## พจนานุกรมอักขระ HTML และ Jinja

| รูปแบบ | ความหมาย |
|---|---|
| <tag ...> | เครื่องหมาย < กับ > ล้อมแท็กเปิดและ attributes |
| </tag> | / หลัง < บอกว่าเป็นแท็กปิด ไม่ใช่การหาร |
| input | void element ไม่มีแท็กปิดใน HTML นี้ |
| name="value" | = เชื่อมชื่อ attribute กับค่า คำพูดคู่ล้อมค่า ไม่ปรากฏบนหน้าจอ |
| class="a b" | มีคลาส a และ b บน element เดียว ช่องว่างคั่นชื่อ CSS ใช้คลาสเลือก element |
| id="..." | ชื่อเฉพาะ element ในหน้า ใช้อ้างจาก label หรือ JavaScript |
| {{ expression }} | ประเมินค่า Jinja ฝั่งเซิร์ฟเวอร์แล้วแทรกผลลง HTML ปีกกาคู่ไม่ถูกส่งเป็นตัวอักษรให้ผู้ใช้เห็น |
| {% statement %} | คำสั่งควบคุม Jinja เช่น if, for, block ไม่ใช่ข้อความที่แสดง |
| 'text' หรือ "text" ใน Jinja | string literal คำพูดเดี่ยวภายใน expression เป็นคนละชั้นกับคำพูดคู่ที่ล้อม HTML attribute |
| item.title | จุดเข้าถึงค่าของสมาชิก ในงานนี้ item เป็น dict ที่ Jinja อ่าน key title ผ่านจุดได้ |
| () | เรียกฟังก์ชันหรือเมธอดและล้อม arguments |
| , ใน arguments | คั่น argument แต่ละตัว |
| name='page1' | keyword argument ของ url_for ไม่ใช่การแก้ตัวแปรบนหน้า |
| ==, >, >= | เท่ากัน มากกว่า มากกว่าหรือเท่ากัน เป็นการเปรียบเทียบ |
| and | เงื่อนไขสองฝั่งต้องจริงพร้อมกัน |
| A if condition else B | เลือก A เมื่อจริง ไม่เช่นนั้นเลือก B |
| x \| filter | ส่ง x ผ่าน filter ของ Jinja เช่น length หรือ tojson ไม่ใช่ OR |
| "{:,.1f}".format(x) | {} ช่องแทนค่า, : เริ่มข้อกำหนด, , คั่นหลักพัน, .1 ทศนิยมหนึ่งตำแหน่ง, f เลขทศนิยมคงที่ ไม่แก้ค่าที่บันทึกจริง |
| else ของ for | แสดงเมื่อไม่มีรายการให้วน ไม่ได้แสดงหลังจบลูปที่มีสมาชิกตามปกติ |
| else ของ if | แสดงเมื่อเงื่อนไข if เป็นเท็จ |
| data-* | attribute เก็บข้อมูลกำหนดเองที่ JavaScript อ่านผ่าน dataset เช่น data-calendar-title → dataset.calendarTitle |
| ✓, 28, →, +, ·, 🔔 ในข้อความ | ตัวอักษร/สัญลักษณ์แสดงผล โดย · คั่นข้อความและ 28 เป็นเลขตกแต่งคงที่ ไม่ใช่วันที่ปัจจุบัน |

Flask ใช้ autoescape กับ template .html ตามค่าปกติของโครงงาน ชื่องานที่มีเครื่องหมาย HTML จึงถูกแสดงเป็นข้อความที่ escape แล้ว การ escape ไม่ทดแทนการตรวจเลข วันที่ หรือสิทธิ์ฝั่งเซิร์ฟเวอร์

## ข้อมูลเชื่อม Python กับหน้าเว็บ

| ไฟล์ | ผู้เตรียมข้อมูลและความหมาย |
|---|---|
| home.html | route home ใน app.py และข้อมูลส่วนกลาง หน้า home มีทางลัด ไม่มีการคำนวณจำนวนงานเอง |
| page1.html | page1.build(): items มีข้อมูลทุกงานพร้อม remaining_hours, days_left, progress, tone, status; open_count งานยังไม่เสร็จ; soon_count งานส่งวันนี้ถึงอีก 3 วันซึ่งยังไม่เสร็จ; overdue_count งานค้างเลยกำหนด; remaining_total รวมชั่วโมงค้าง |
| page2.html | page2.build(): items พร้อม no ซึ่งเป็นตำแหน่งแถวเริ่มที่ 0 และ remaining_hours; count คือ len(items); handle(form) รับ action add/update/delete จาก POST |
| page3.html | page3.build(query): tasks งานยังไม่เสร็จเรียงวันส่ง; daily_hours เวลาต่อวันที่ตรวจแล้ว; risk_count จำนวนงานเกินกำหนดหรือ gap > 0; focus งานแรกหรือ None; notice แสดงโดย base.html |

base.html เป็นแม่แบบหลักที่ห้ามแก้ มี html/head/header/menu/main/footer และ link stylesheet แล้ว ทุก template นี้สืบทอดและแทนพื้นที่ block content หน้า 1 เพิ่ม block scripts ที่ท้าย body

ฟอร์มหน้า 2 ไม่มี action attribute จึงส่งไป URL ปัจจุบันด้วย POST ช่อง hidden ชื่อ action คือข้อมูลเลือกคำสั่ง ไม่ใช่ attribute action ของ form ฟอร์มเพิ่มไม่มี done_hours จึงใช้ค่าตั้งต้น 0 ใน Python ฟอร์มแก้ไขกับฟอร์มลบแยกกัน ไม่ได้ซ้อนกัน

ฟอร์มหน้า 3 ใช้ GET เพราะเป็นการคำนวณแผน URL จึงมี ?hours=... และไม่มีการบันทึก hours ลง data.json ข้อความ notice อยู่ใน base.html จึงไม่พบตัวแปร notice โดยตรงใน page3.html

## ข้อจำกัดและจุดที่ควรตอบให้ตรง source

1. การแจ้งเตือนและไฟล์ reminders.js โหลดเฉพาะหน้า 1 ปุ่มเปิดสิทธิ์และกล่อง JSON ก็อยู่หน้านี้ การปิดหน้า 1 จึงไม่เหลือสคริปต์หน้านั้นทำงานแบบ push เบื้องหลัง การนำไฟล์นัดหมายเข้าแอปปฏิทินต้องทำโดยผู้ใช้ และการเตือนหลังปิดเว็บขึ้นกับแอปปฏิทิน
2. รายชื่อ font-family เป็น fallback ตามฟอนต์ที่ติดตั้ง/รองรับอักษร ไม่มี @font-face หรือ @import ดาวน์โหลดฟอนต์ ไม่มีหลักประกันว่าทุกเครื่องแสดง Sarabun
3. CSS จอไม่เกิน 720px ทำหน้าจัดการเป็นคอลัมน์เดียวและยกเลิก sticky ส่วนไม่เกิน 640px ปรับการ์ด/ปุ่มและซ่อนรูปตกแต่ง นี่อธิบายโค้ดที่รองรับ responsive ไม่ใช่หลักฐานว่าทดสอบครบทุกอุปกรณ์
4. required/min/max/maxlength เป็นการช่วยกรอกใน browser ผู้ใช้แก้ request ได้ Python จึงต้องตรวจซ้ำ
5. no เป็นตำแหน่งแถวปัจจุบันเริ่มที่ 0 ไม่ใช่รหัสถาวร หากหลายแท็บลบ/แก้พร้อมกัน ตำแหน่งเดิมอาจชี้รายการใหม่ เป็นข้อจำกัดของงานที่ใช้ JSON
6. สีมีข้อความสถานะกำกับ มี label/ARIA และ focus บางส่วน แต่ไม่อ้างว่าตรวจมาตรฐานการเข้าถึงครบทั้งระบบ
7. หน้า 3 ประเมินภาระสะสมจากชั่วโมงที่กรอก ไม่ใช่ระบบจัดปฏิทินรายชั่วโมงอัตโนมัติ และชั่วโมงที่ทำแล้วต้องกรอกเอง
8. เลข 28 ในรูปปฏิทินเป็น literal รูปทั้งก้อนมี aria-hidden=true เพื่อให้โปรแกรมอ่านหน้าจอข้าม

## พจนานุกรม CSS

| รูปแบบ | ความหมาย |
|---|---|
| /* ... */ | comment ไม่เป็นกฎแสดงผล |
| selector { property: value; } | selector เลือก element; {} ครอบบล็อก; : คั่นชื่อกับค่า; ; จบ declaration |
| .class | คลาส; .btn.small ต้องมีทั้งสองคลาสบน element เดียว |
| A B | เลือก B ที่อยู่ภายใน A ระดับใดก็ได้ |
| A > B | B เป็นลูกโดยตรงของ A |
| A, B | หลาย selector ใช้ declarations ชุดเดียว |
| :root | element รากของ HTML ใช้ประกาศตัวแปรสี |
| :hover | สถานะเมาส์ชี้ พฤติกรรมสัมผัสอาจต่างจากเมาส์ |
| :first-child / :last-child | ลูกตัวแรก/สุดท้ายในกลุ่มพี่น้อง |
| :focus-visible | browser เห็นว่าควรแสดง focus เช่นใช้แป้นพิมพ์ |
| --name / var(--name) | custom property และการอ่านค่ามาใช้ |
| @media (max-width: Npx) | กฎทำงานเมื่อ viewport กว้างไม่เกิน N รวมเท่ากับ N |
| px | CSS pixel ไม่จำเป็นต้องเท่าจุดจริงของฮาร์ดแวร์ |
| % | สัดส่วนตาม property เช่น width เทียบกล่องครอบ; border-radius 50% ทำวงกลมเมื่อกล่องจัตุรัส |
| vh / vw | 1% ของความสูง/ความกว้าง viewport |
| em | เท่าของ font-size เช่น letter-spacing .13em |
| fr | ส่วนแบ่งพื้นที่เหลือของ Grid หลังหัก gap และพิจารณาข้อจำกัด |
| deg | องศามุมหมุนหรือไล่สี |
| s | วินาที เช่น .1s = 0.1 วินาที |
| 0, .85, 1.55 | เลขไม่มีหน่วย; 0 ระยะศูนย์, opacity 0–1, line-height ไม่มีหน่วยคูณ font-size |
| #fff / #ffffff | สีฐานสิบหก 3/6 หลัก ทั้งสองตัวอย่างคือสีขาว |
| rgba(r,g,b,a) | RGB 0–255 และ alpha 0–1 ค่าท้ายต่ำยิ่งโปร่งใส |
| linear-gradient(...) | ไล่สีเส้นตรง องศากำหนดทิศและ % กำหนดจุดเปลี่ยนสี |
| conic-gradient(...) | ไล่สีวนรอบศูนย์กลาง ใช้ทำ donut ร่วมวงพื้นด้านใน |
| repeat(auto-fit, minmax(...)) | สร้างคอลัมน์ตามที่ว่างพร้อมยุบช่องว่างไม่มีสมาชิก minmax บอกขอบล่าง/บน |
| repeat(auto-fill, minmax(...)) | เติมช่องให้เต็มพื้นที่และอาจเหลือช่องเปล่า ต่างจาก auto-fit |
| min(...) / clamp(min, preferred, max) | เลือกค่าต่ำสุดในรายการ/บังคับค่ากลางให้อยู่ในช่วง |
| calc(...) | คำนวณ CSS เช่น var(--p) * 1% |
| padding/margin 1/2/3/4 ค่า | ทุกด้าน / บนล่าง-ซ้ายขวา / บน-ซ้ายขวา-ล่าง / บน-ขวา-ล่าง-ซ้าย |
| border: width style color | ความหนา ชนิดเส้น สี; solid ทึบ dashed ประ transparent โปร่งใส |
| box-shadow: x y blur color | ระยะเงานอน ตั้ง ฟุ้ง สี โดย blur=0 ขอบคม |
| flex: grow shrink basis | อัตราขยาย หด ฐาน เช่น 0 0 170px ไม่ขยายไม่หดและเริ่ม 170px |
| auto / none / inherit | ให้คำนวณอัตโนมัติ / ไม่มีตาม property / สืบค่าจากแม่ |
| ค่าลบ | เช่น translateY(-2px) ยกขึ้น และไม่เปลี่ยนตำแหน่งฐานใน layout |

ไม่มีกฎ !important ในไฟล์นี้ การทับกฎอาศัย specificity และลำดับใน stylesheet กฎท้ายไฟล์ไม่ได้ชนะทุกกรณีโดยอัตโนมัติ ส่วน .deadline-form-layout ต้องมี media query เฉพาะท้ายไฟล์ เพราะประกาศคอลัมน์ทับ .two-col ของเดิมมาแล้ว

## รายการต้นฉบับ

| ไฟล์ | บรรทัด | SHA-256 ขณะอ่าน |
|---|---:|---|
| `templates/home.html` | 17 | `7f0f5c8caedfe79704fcdcafb3fe1066a3c978d9a2f93e929452751bba0edb97` |
| `templates/page1.html` | 53 | `86a767ec39886bd9662f1efb4536ab8ccbe253463549bcf2c7f6fffb0f8dd351` |
| `templates/page2.html` | 36 | `1f4701f31b30eff539eb7d34a97161e47a2344fc73e2684d008f69ce66e5df1e` |
| `templates/page3.html` | 30 | `20f788b1d050a902d1ef119faee3479748e4bfe59cc6afc849352368c7873811` |
| `static/style.css` | 239 | `f6f4bbc0f896e9c83a767704666460879cafcdda7dbcab8a238f2590160f3820` |

## templates/home.html — 17 บรรทัด

### L001

```html
{% extends "base.html" %}
```

- Jinja `{% extends "base.html" %}`: สืบทอดแม่แบบหลัก base.html ร่วม header/menu/footer/stylesheet

### L002

```html
{% block content %}
```

- Jinja `{% block content %}`: เปิดบล็อกเนื้อหาแทนพื้นที่ content ของแม่แบบ

### L003

```html
<section class="deadline-hero deadline-home-hero">
```

- `<section>`: กลุ่มเนื้อหาที่มีหัวข้อร่วมกัน
  - `class="deadline-hero deadline-home-hero"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L004

```html
  <div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS

### L005

```html
    <span class="deadline-eyebrow">DEADLINE COMPASS</span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-eyebrow"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `DEADLINE COMPASS`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L006

```html
    <h1>เดดไลน์ไม่ชนกัน</h1>
```

- `<h1>`: หัวข้อหลัก
- ข้อความแสดงผล `เดดไลน์ไม่ชนกัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h1>`: ปิด h1 ที่เปิดไว้ตามลำดับการซ้อน HTML

### L007

```html
    <p>เห็นงานทั้งหมด วางเวลาที่มี และเริ่มงานสำคัญก่อนถึงวันส่ง</p>
```

- `<p>`: ย่อหน้าข้อความ
- ข้อความแสดงผล `เห็นงานทั้งหมด วางเวลาที่มี และเริ่มงานสำคัญก่อนถึงวันส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L008

```html
    <a class="btn" href="{{ url_for('page', name='page1') }}">เปิดภาพรวมงาน →</a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="btn"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page1') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page1') }}`: Flask url_for(endpoint page, name=page1) สร้าง URL ไป /page1 ตาม route ของ app.py
- ข้อความแสดงผล `เปิดภาพรวมงาน →`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L009

```html
  </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L010

```html
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>28</span></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-hero-mark"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `aria-hidden="true"`: true ให้โปรแกรมอ่านหน้าจอข้ามเพราะเป็นสิ่งตกแต่ง
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
- ข้อความแสดงผล `✓`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
- ข้อความแสดงผล `28`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L011

```html
</section>
```

- `</section>`: ปิด section ที่เปิดไว้ตามลำดับการซ้อน HTML

### L012

```html
<section class="cards deadline-home-cards">
```

- `<section>`: กลุ่มเนื้อหาที่มีหัวข้อร่วมกัน
  - `class="cards deadline-home-cards"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L013

```html
  <a class="card" href="{{ url_for('page', name='page1') }}"><span class="card-kicker">01 · ภาพรวม</span><span class="card-title">วันนี้มีอะไรต้องทำ</span><span class="note">ดูงานและสถานะในที่เดียว</span></a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="card"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page1') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page1') }}`: Flask url_for(endpoint page, name=page1) สร้าง URL ไป /page1 ตาม route ของ app.py
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-kicker"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `01 · ภาพรวม`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-title"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `วันนี้มีอะไรต้องทำ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ดูงานและสถานะในที่เดียว`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L014

```html
  <a class="card" href="{{ url_for('page', name='page2') }}"><span class="card-kicker">02 · จัดการ</span><span class="card-title">บันทึกงานให้ครบ</span><span class="note">เพิ่ม แก้ไข และติดตามชั่วโมง</span></a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="card"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page2') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page2') }}`: Flask url_for(endpoint page, name=page2) สร้าง URL ไป /page2 ตาม route ของ app.py
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-kicker"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `02 · จัดการ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-title"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `บันทึกงานให้ครบ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เพิ่ม แก้ไข และติดตามชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L015

```html
  <a class="card" href="{{ url_for('page', name='page3') }}"><span class="card-kicker">03 · วางแผน</span><span class="card-title">รู้ทันงานที่ชนกัน</span><span class="note">เทียบงานค้างกับเวลาที่มีจริง</span></a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="card"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page3') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page3') }}`: Flask url_for(endpoint page, name=page3) สร้าง URL ไป /page3 ตาม route ของ app.py
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-kicker"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `03 · วางแผน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="card-title"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `รู้ทันงานที่ชนกัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เทียบงานค้างกับเวลาที่มีจริง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L016

```html
</section>
```

- `</section>`: ปิด section ที่เปิดไว้ตามลำดับการซ้อน HTML

### L017

```html
{% endblock %}
```

- Jinja `{% endblock %}`: ปิดบล็อกล่าสุด ไม่มีตัวอักษรแสดงจากคำสั่งนี้

## templates/page1.html — 53 บรรทัด

### L001

```html
{% extends "base.html" %}
```

- Jinja `{% extends "base.html" %}`: สืบทอดแม่แบบหลัก base.html ร่วม header/menu/footer/stylesheet

### L002

```html
{% block content %}
```

- Jinja `{% block content %}`: เปิดบล็อกเนื้อหาแทนพื้นที่ content ของแม่แบบ

### L003

```html
<section class="deadline-hero">
```

- `<section>`: กลุ่มเนื้อหาที่มีหัวข้อร่วมกัน
  - `class="deadline-hero"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L004

```html
  <div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS

### L005

```html
    <span class="deadline-eyebrow">DEADLINE COMPASS · ภาพรวม</span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-eyebrow"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `DEADLINE COMPASS · ภาพรวม`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L006

```html
    <h1>เห็นทุกงาน ก่อนงานจะชนกัน</h1>
```

- `<h1>`: หัวข้อหลัก
- ข้อความแสดงผล `เห็นทุกงาน ก่อนงานจะชนกัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h1>`: ปิด h1 ที่เปิดไว้ตามลำดับการซ้อน HTML

### L007

```html
    <p>เช็กสิ่งที่ต้องส่งและเวลาที่เหลือ แล้วเลือกงานที่ควรเริ่มวันนี้</p>
```

- `<p>`: ย่อหน้าข้อความ
- ข้อความแสดงผล `เช็กสิ่งที่ต้องส่งและเวลาที่เหลือ แล้วเลือกงานที่ควรเริ่มวันนี้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L008

```html
    <a class="btn" href="{{ url_for('page', name='page2') }}">+ เพิ่มงานใหม่</a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="btn"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page2') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page2') }}`: Flask url_for(endpoint page, name=page2) สร้าง URL ไป /page2 ตาม route ของ app.py
- ข้อความแสดงผล `+ เพิ่มงานใหม่`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L009

```html
    <a class="btn ghost" href="{{ url_for('page', name='page3') }}">ดูแผนก่อนวันส่ง →</a>
```

- `<a>`: ลิงก์ไป URL ปลายทางเมื่อกด
  - `class="btn ghost"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `href="{{ url_for('page', name='page3') }}"`: URL ปลายทางของลิงก์ สร้างโดย url_for
    - Expression `{{ url_for('page', name='page3') }}`: Flask url_for(endpoint page, name=page3) สร้าง URL ไป /page3 ตาม route ของ app.py
- ข้อความแสดงผล `ดูแผนก่อนวันส่ง →`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</a>`: ปิด a ที่เปิดไว้ตามลำดับการซ้อน HTML

### L010

```html
  </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L011

```html
  <div class="deadline-hero-mark" aria-hidden="true"><span>✓</span><span>28</span></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-hero-mark"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `aria-hidden="true"`: true ให้โปรแกรมอ่านหน้าจอข้ามเพราะเป็นสิ่งตกแต่ง
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
- ข้อความแสดงผล `✓`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
- ข้อความแสดงผล `28`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L012

```html
</section>
```

- `</section>`: ปิด section ที่เปิดไว้ตามลำดับการซ้อน HTML

### L013

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L014

```html
<div class="stat-grid deadline-summary">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat-grid deadline-summary"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L015

```html
  <div class="stat"><div class="label">งานที่ยังไม่เสร็จ</div><div class="value">{{ open_count }}</div><div class="unit">รายการ</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `งานที่ยังไม่เสร็จ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ open_count }}`: จำนวนงานที่ remaining_hours > 0 จาก page1
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `รายการ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L016

```html
  <div class="stat gold"><div class="label">ส่งภายใน 3 วัน</div><div class="value">{{ soon_count }}</div><div class="unit">รายการ</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat gold"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ส่งภายใน 3 วัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ soon_count }}`: งานยังไม่เสร็จที่ days_left 0 ถึง 3 ไม่รวมเลยกำหนด
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `รายการ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L017

```html
  <div class="stat"><div class="label">เวลาที่ยังต้องใช้</div><div class="value">{{ "{:,.1f}".format(remaining_total) }}</div><div class="unit">ชั่วโมง</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เวลาที่ยังต้องใช้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ "{:,.1f}".format(remaining_total) }}`: จัด remaining_total (ผลรวมชั่วโมงคงเหลืองานยังไม่เสร็จ) เป็นข้อความคั่นหลักพันและทศนิยม 1 ตำแหน่งตามพจนานุกรม ไม่แก้ข้อมูลจริง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L018

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L019

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L020

```html
{% if overdue_count %}<div class="deadline-alert" role="status">มีงานเกินกำหนด {{ overdue_count }} รายการ ควรตรวจและปรับแผนวันนี้</div>{% endif %}
```

- Jinja `{% if overdue_count %}`: แสดงคำเตือนเมื่อจำนวนงานค้างเกินกำหนดไม่เป็นศูนย์
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-alert"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `role="status"`: บทบาทสำหรับเทคโนโลยีช่วยอ่าน status=ข้อความสถานะ progressbar=แถบความคืบหน้า
- Expression `{{ overdue_count }}`: งานยังไม่เสร็จที่ days_left < 0
- ข้อความแสดงผล `มีงานเกินกำหนด  รายการ ควรตรวจและปรับแผนวันนี้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endif %}`: ปิด if ล่าสุดที่ยังเปิดอยู่ ถ้าซ้อนกันปิดจากด้านในออกด้านนอก

### L021

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L022

```html
<div class="deadline-section-head">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-section-head"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L023

```html
  <div><h2>งานทั้งหมด</h2><p class="note">สีช่วยแยกสถานะ และมีข้อความกำกับทุกงาน</p></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
- `<h2>`: หัวข้อรอง
- ข้อความแสดงผล `งานทั้งหมด`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h2>`: ปิด h2 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `สีช่วยแยกสถานะ และมีข้อความกำกับทุกงาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L024

```html
  <div class="deadline-reminder-control">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-reminder-control"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L025

```html
    <button id="enable-reminders" class="btn ghost small" type="button">🔔 เปิดการแจ้งเตือน</button>
```

- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `id="enable-reminders"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `class="btn ghost small"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="button"`: ปุ่มทั่วไปไม่ส่งฟอร์ม ใช้ให้ JS รับ click
- ข้อความแสดงผล `🔔 เปิดการแจ้งเตือน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML

### L026

```html
    <span id="reminder-status" class="note" aria-live="polite"></span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `id="reminder-status"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `aria-live="polite"`: polite แจ้งข้อความเมื่อเปลี่ยนโดยรอจังหวะไม่ขัดการอ่านเดิม
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L027

```html
  </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L028

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L029

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L030

```html
<div class="deadline-task-list">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-task-list"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L031

```html
  {% for item in items %}
```

- Jinja `{% for item in items %}`: วนสมาชิกจาก items ทีละตัวในชื่อตัวแปร item HTML ภายในจึงซ้ำตามจำนวนสมาชิก

### L032

```html
  <article class="deadline-task">
```

- `<article>`: เนื้อหาหนึ่งรายการแยกอ่านได้ เช่นการ์ดงาน
  - `class="deadline-task"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L033

```html
    <div class="deadline-task-main">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-task-main"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L034

```html
      <span class="deadline-course">{{ item.course }}</span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-course"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ item.course }}`: item คือ สมาชิกปัจจุบันของ items; ชื่อวิชา
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L035

```html
      <h3>{{ item.title }}</h3>
```

- `<h3>`: หัวข้องาน/หัวข้อย่อยลำดับสาม
- Expression `{{ item.title }}`: item คือ สมาชิกปัจจุบันของ items; ชื่องาน
- `</h3>`: ปิด h3 ที่เปิดไว้ตามลำดับการซ้อน HTML

### L036

```html
      <p class="deadline-meta">กำหนดส่ง <time datetime="{{ item.due_date }}">{{ item.due_date }}</time> · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง</p>
```

- `<p>`: ย่อหน้าข้อความ
  - `class="deadline-meta"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `กำหนดส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `<time>`: วันที่ที่มีข้อความสำหรับคนและ datetime สำหรับเครื่อง
  - `datetime="{{ item.due_date }}"`: วันที่รูปแบบ ISO ให้เครื่องอ่าน ข้อความใน time ให้คนอ่าน
    - Expression `{{ item.due_date }}`: item คือ สมาชิกปัจจุบันของ items; วันส่ง ISO YYYY-MM-DD
- Expression `{{ item.due_date }}`: item คือ สมาชิกปัจจุบันของ items; วันส่ง ISO YYYY-MM-DD
- `</time>`: ปิด time ที่เปิดไว้ตามลำดับการซ้อน HTML
- Expression `{{ "{:,.1f}".format(item.remaining_hours) }}`: จัด item.remaining_hours (item คือ สมาชิกปัจจุบันของ items; ชั่วโมงที่ Assignment.remaining_hours() คำนวณ) เป็นข้อความคั่นหลักพันและทศนิยม 1 ตำแหน่งตามพจนานุกรม ไม่แก้ข้อมูลจริง
- ข้อความแสดงผล `· เหลือ  ชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L037

```html
      <div class="progress deadline-progress" role="progressbar" aria-label="ความคืบหน้า {{ item.title }}" aria-valuenow="{{ item.progress }}" aria-valuemin="0" aria-valuemax="100"><div style="width: {{ item.progress }}%"></div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="progress deadline-progress"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `role="progressbar"`: บทบาทสำหรับเทคโนโลยีช่วยอ่าน status=ข้อความสถานะ progressbar=แถบความคืบหน้า
  - `aria-label="ความคืบหน้า {{ item.title }}"`: ชื่อสำหรับโปรแกรมอ่านหน้าจอ แทรกชื่องานให้รู้ว่าเป็นแถบของงานใด
    - Expression `{{ item.title }}`: item คือ สมาชิกปัจจุบันของ items; ชื่องาน
  - `aria-valuenow="{{ item.progress }}"`: ค่าความคืบหน้าปัจจุบัน อ่าน item.progress เดียวกับความกว้างแถบ
    - Expression `{{ item.progress }}`: item คือ สมาชิกปัจจุบันของ items; เปอร์เซ็นต์จำนวนเต็มที่ page1 คำนวณ จำกัดบน 100
  - `aria-valuemin="0"`: ขอบล่างช่วงความคืบหน้าเป็น 0
  - `aria-valuemax="100"`: ขอบบนช่วงความคืบหน้าเป็น 100
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `style="width: {{ item.progress }}%"`: CSS เฉพาะ element: width ใช้ item.progress ต่อด้วย % จึงเป็นสัดส่วนของแถบแม่
    - Expression `{{ item.progress }}`: item คือ สมาชิกปัจจุบันของ items; เปอร์เซ็นต์จำนวนเต็มที่ page1 คำนวณ จำกัดบน 100
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L038

```html
    </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L039

```html
    <div class="deadline-task-actions">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-task-actions"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L040

```html
      <span class="badge {{ item.tone }}">{{ item.status }}</span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="badge {{ item.tone }}"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
    - Expression `{{ item.tone }}`: item คือ สมาชิกปัจจุบันของ items; คลาสสีจาก Python good/bad/gold หรือว่าง
- Expression `{{ item.status }}`: item คือ สมาชิกปัจจุบันของ items; ข้อความสถานะจากเงื่อนไข Python
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L041

```html
      {% if item.remaining_hours > 0 and item.days_left >= 0 %}
```

- Jinja `{% if item.remaining_hours > 0 and item.days_left >= 0 %}`: แสดงปฏิทินเมื่อยังไม่เสร็จและวันส่งยังไม่ผ่าน วันนี้มี days_left=0 จึงผ่าน

### L042

```html
      <button class="deadline-text-button" type="button" data-calendar-title="{{ item.title }}" data-calendar-course="{{ item.course }}" data-calendar-date="{{ item.due_date }}">เพิ่มลงปฏิทิน</button>
```

- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `class="deadline-text-button"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="button"`: ปุ่มทั่วไปไม่ส่งฟอร์ม ใช้ให้ JS รับ click
  - `data-calendar-title="{{ item.title }}"`: ส่ง ชื่องาน ให้ reminders.js สร้างไฟล์ปฏิทินเมื่อกด ไม่ได้นำเข้าแอปปฏิทินโดยอัตโนมัติ
    - Expression `{{ item.title }}`: item คือ สมาชิกปัจจุบันของ items; ชื่องาน
  - `data-calendar-course="{{ item.course }}"`: ส่ง วิชา ให้ reminders.js สร้างไฟล์ปฏิทินเมื่อกด ไม่ได้นำเข้าแอปปฏิทินโดยอัตโนมัติ
    - Expression `{{ item.course }}`: item คือ สมาชิกปัจจุบันของ items; ชื่อวิชา
  - `data-calendar-date="{{ item.due_date }}"`: ส่ง วันส่ง ให้ reminders.js สร้างไฟล์ปฏิทินเมื่อกด ไม่ได้นำเข้าแอปปฏิทินโดยอัตโนมัติ
    - Expression `{{ item.due_date }}`: item คือ สมาชิกปัจจุบันของ items; วันส่ง ISO YYYY-MM-DD
- ข้อความแสดงผล `เพิ่มลงปฏิทิน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML

### L043

```html
      {% endif %}
```

- Jinja `{% endif %}`: ปิด if ล่าสุดที่ยังเปิดอยู่ ถ้าซ้อนกันปิดจากด้านในออกด้านนอก

### L044

```html
    </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L045

```html
  </article>
```

- `</article>`: ปิด article ที่เปิดไว้ตามลำดับการซ้อน HTML

### L046

```html
  {% else %}
```

- Jinja `{% else %}`: else ของลูป แสดงสถานะรายการว่างเมื่อไม่มีสมาชิก

### L047

```html
  <div class="empty">ยังไม่มีงาน เพิ่มงานแรกในหน้าจัดการงาน</div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="empty"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ยังไม่มีงาน เพิ่มงานแรกในหน้าจัดการงาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L048

```html
  {% endfor %}
```

- Jinja `{% endfor %}`: ปิดลูปล่าสุด ถัดจากนี้อยู่นอก HTML ที่ทำซ้ำ

### L049

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L050

```html
<p class="note deadline-footnote">การเตือนผ่านเบราว์เซอร์ทำงานเมื่อเปิดหน้านี้อยู่ หากต้องการเตือนหลังปิดเว็บ ให้กด “เพิ่มลงปฏิทิน” แล้วนำไฟล์ที่ได้เข้าแอปปฏิทินของคุณ</p>
```

- `<p>`: ย่อหน้าข้อความ
  - `class="note deadline-footnote"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `การเตือนผ่านเบราว์เซอร์ทำงานเมื่อเปิดหน้านี้อยู่ หากต้องการเตือนหลังปิดเว็บ ให้กด “เพิ่มลงปฏิทิน” แล้วนำไฟล์ที่ได้เข้าแอปปฏิทินของคุณ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L051

```html
<script id="reminder-data" type="application/json">{{ items|tojson }}</script>
```

- `<script>`: ส่วนข้อมูลหรือโหลดสคริปต์ พิจารณา type และ src
  - `id="reminder-data"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `type="application/json"`: ข้อมูล JSON ไม่ใช่ JS executable ให้ reminders.js อ่าน
- Expression `{{ items|tojson }}`: Jinja filter tojson แปลงรายการ dict เป็น JSON พร้อม escape อักขระที่เสี่ยงปิด script ในบริบทนี้ วางใน script application/json เป็นข้อมูลให้ JS อ่าน ไม่ได้รันข้อมูลนี้เป็นโค้ด
- `</script>`: ปิด script ที่เปิดไว้ตามลำดับการซ้อน HTML

### L052

```html
{% endblock %}
```

- Jinja `{% endblock %}`: ปิดบล็อกล่าสุด ไม่มีตัวอักษรแสดงจากคำสั่งนี้

### L053

```html
{% block scripts %}<script src="{{ url_for('static', filename='js/reminders.js') }}" defer></script>{% endblock %}
```

- Jinja `{% block scripts %}`: เปิดบล็อกสคริปต์เฉพาะหน้าที่แม่แบบวางท้าย body
- `<script>`: ส่วนข้อมูลหรือโหลดสคริปต์ พิจารณา type และ src
  - `src="{{ url_for('static', filename='js/reminders.js') }}"`: URL ไฟล์ script ภายนอกสร้างด้วย url_for
    - Expression `{{ url_for('static', filename='js/reminders.js') }}`: Flask url_for(endpoint static, filename=js/reminders.js) สร้าง URL สคริปต์ ปกติ /static/js/reminders.js
  - `defer`: boolean โหลด external script ระหว่าง parse HTML ได้ แต่รอ parse เสร็จจึงรัน
- `</script>`: ปิด script ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endblock %}`: ปิดบล็อกล่าสุด ไม่มีตัวอักษรแสดงจากคำสั่งนี้

## templates/page2.html — 36 บรรทัด

### L001

```html
{% extends "base.html" %}
```

- Jinja `{% extends "base.html" %}`: สืบทอดแม่แบบหลัก base.html ร่วม header/menu/footer/stylesheet

### L002

```html
{% block content %}
```

- Jinja `{% block content %}`: เปิดบล็อกเนื้อหาแทนพื้นที่ content ของแม่แบบ

### L003

```html
<div class="deadline-page-title"><span class="deadline-eyebrow">จัดการงาน</span><h1>เพิ่มงานและอัปเดตความคืบหน้า</h1><p class="lead">กรอกเวลาที่คาดว่าจะใช้ให้ใกล้เคียงจริง เพื่อให้หน้าแผนช่วยเตือนได้แม่นยำ</p></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-page-title"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-eyebrow"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `จัดการงาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<h1>`: หัวข้อหลัก
- ข้อความแสดงผล `เพิ่มงานและอัปเดตความคืบหน้า`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h1>`: ปิด h1 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="lead"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `กรอกเวลาที่คาดว่าจะใช้ให้ใกล้เคียงจริง เพื่อให้หน้าแผนช่วยเตือนได้แม่นยำ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L004

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L005

```html
<div class="two-col deadline-form-layout">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="two-col deadline-form-layout"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L006

```html
  <form method="post" class="panel deadline-add-form">
```

- `<form>`: ชุดข้อมูลที่ส่งเมื่อ submit
  - `method="post"`: post ส่งข้อมูลใน body ให้ handle(form); get ส่ง query string ให้ build(query)
  - `class="panel deadline-add-form"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L007

```html
    <h2>งานใหม่</h2>
```

- `<h2>`: หัวข้อรอง
- ข้อความแสดงผล `งานใหม่`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h2>`: ปิด h2 ที่เปิดไว้ตามลำดับการซ้อน HTML

### L008

```html
    <input type="hidden" name="action" value="add">
```

- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `type="hidden"`: ช่องซ่อนส่ง action/no แก้ได้ผ่านเครื่องมือ browser จึงไม่ใช่ความลับหรือหลักฐานสิทธิ์
  - `name="action"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="add"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ

### L009

```html
    <div class="field"><label for="new-title">ชื่องาน</label><input id="new-title" name="title" maxlength="80" placeholder="เช่น รายงานการทดลอง" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="new-title"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
- ข้อความแสดงผล `ชื่องาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="new-title"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `name="title"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `maxlength="80"`: จำกัดความยาวข้อความที่ browser ยอมรับ Python ตรวจซ้ำ
  - `placeholder="เช่น รายงานการทดลอง"`: ตัวอย่างเมื่อช่องว่าง ไม่ใช่ข้อมูลที่ส่งและไม่แทน label
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L010

```html
    <div class="field"><label for="new-course">วิชา</label><input id="new-course" name="course" maxlength="40" placeholder="เช่น ฟิสิกส์" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="new-course"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
- ข้อความแสดงผล `วิชา`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="new-course"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `name="course"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `maxlength="40"`: จำกัดความยาวข้อความที่ browser ยอมรับ Python ตรวจซ้ำ
  - `placeholder="เช่น ฟิสิกส์"`: ตัวอย่างเมื่อช่องว่าง ไม่ใช่ข้อมูลที่ส่งและไม่แทน label
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L011

```html
    <div class="field"><label for="new-date">วันส่ง</label><input id="new-date" name="due_date" type="date" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="new-date"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
- ข้อความแสดงผล `วันส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="new-date"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `name="due_date"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="date"`: ช่องวัน browser ส่ง ISO YYYY-MM-DD แม้หน้าตาอาจตามภาษาท้องถิ่น
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L012

```html
    <div class="field"><label for="new-hours">เวลาที่คาดว่าจะใช้ (ชั่วโมง)</label><input id="new-hours" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" placeholder="เช่น 4" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="new-hours"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
- ข้อความแสดงผล `เวลาที่คาดว่าจะใช้ (ชั่วโมง)`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="new-hours"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `name="estimated_hours"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="number"`: ช่องเลขใช้ min/max/step แต่ Python ได้ข้อความก่อนแปลง float
  - `min="0.1"`: ขอบล่างช่องตัวเลขฝั่ง browser Python ตรวจเงื่อนไขซ้ำ
  - `max="200"`: ขอบบนช่องตัวเลขฝั่ง browser Python ตรวจซ้ำ
  - `step="0.1"`: ขั้นของเลขที่ browser ยอมรับและปุ่มเพิ่มลด 0.1 คือทีละหนึ่งส่วนสิบ
  - `placeholder="เช่น 4"`: ตัวอย่างเมื่อช่องว่าง ไม่ใช่ข้อมูลที่ส่งและไม่แทน label
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L013

```html
    <button class="btn full" type="submit">บันทึกงาน</button>
```

- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `class="btn full"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="submit"`: ปุ่มส่ง form ที่ตนอยู่ภายใน
- ข้อความแสดงผล `บันทึกงาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML

### L014

```html
  </form>
```

- `</form>`: ปิด form ที่เปิดไว้ตามลำดับการซ้อน HTML

### L015

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L016

```html
  <div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS

### L017

```html
    <div class="deadline-section-head"><div><h2>รายการที่บันทึก</h2><p class="note">{{ count }} งาน · เปิดแต่ละการ์ดเพื่อแก้ไข</p></div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-section-head"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
- `<h2>`: หัวข้อรอง
- ข้อความแสดงผล `รายการที่บันทึก`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h2>`: ปิด h2 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ count }}`: len(items) ใน page2.build()
- ข้อความแสดงผล `งาน · เปิดแต่ละการ์ดเพื่อแก้ไข`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L018

```html
    {% for item in items %}
```

- Jinja `{% for item in items %}`: วนสมาชิกจาก items ทีละตัวในชื่อตัวแปร item HTML ภายในจึงซ้ำตามจำนวนสมาชิก

### L019

```html
    <article class="panel deadline-edit-card">
```

- `<article>`: เนื้อหาหนึ่งรายการแยกอ่านได้ เช่นการ์ดงาน
  - `class="panel deadline-edit-card"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L020

```html
      <div class="deadline-edit-heading"><div><span class="deadline-course">{{ item.course }}</span><h3>{{ item.title }}</h3><p class="deadline-meta">ส่ง {{ item.due_date }} · เหลือ {{ "{:,.1f}".format(item.remaining_hours) }} ชั่วโมง</p></div><span class="badge {{ 'good' if item.remaining_hours == 0 else 'gold' }}">{{ 'เสร็จแล้ว' if item.remaining_hours == 0 else 'กำลังทำ' }}</span></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-edit-heading"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-course"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ item.course }}`: item คือ สมาชิกปัจจุบันของ items; ชื่อวิชา
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<h3>`: หัวข้องาน/หัวข้อย่อยลำดับสาม
- Expression `{{ item.title }}`: item คือ สมาชิกปัจจุบันของ items; ชื่องาน
- `</h3>`: ปิด h3 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="deadline-meta"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ item.due_date }}`: item คือ สมาชิกปัจจุบันของ items; วันส่ง ISO YYYY-MM-DD
- Expression `{{ "{:,.1f}".format(item.remaining_hours) }}`: จัด item.remaining_hours (item คือ สมาชิกปัจจุบันของ items; ชั่วโมงที่ Assignment.remaining_hours() คำนวณ) เป็นข้อความคั่นหลักพันและทศนิยม 1 ตำแหน่งตามพจนานุกรม ไม่แก้ข้อมูลจริง
- ข้อความแสดงผล `ส่ง  · เหลือ  ชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="badge {{ 'good' if item.remaining_hours == 0 else 'gold' }}"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
    - Expression `{{ 'good' if item.remaining_hours == 0 else 'gold' }}`: เลือกคลาส good ถ้าชั่วโมงเหลือ 0 มิฉะนั้น gold
- Expression `{{ 'เสร็จแล้ว' if item.remaining_hours == 0 else 'กำลังทำ' }}`: เลือกข้อความเสร็จแล้วเมื่อชั่วโมงเหลือ 0 มิฉะนั้นกำลังทำ; หน้า 2 ไม่แยก badge งานเกินกำหนดแบบหน้า 1
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L021

```html
      <details>
```

- `<details>`: ส่วนพับ/ขยาย native browser ไม่ต้องเขียน JS ควบคุมการเปิดเอง

### L022

```html
        <summary>แก้ไขงานหรือบันทึกชั่วโมงที่ทำแล้ว</summary>
```

- `<summary>`: หัวข้อกดเปิด/ปิดของ details
- ข้อความแสดงผล `แก้ไขงานหรือบันทึกชั่วโมงที่ทำแล้ว`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</summary>`: ปิด summary ที่เปิดไว้ตามลำดับการซ้อน HTML

### L023

```html
        <form method="post" class="deadline-edit-form">
```

- `<form>`: ชุดข้อมูลที่ส่งเมื่อ submit
  - `method="post"`: post ส่งข้อมูลใน body ให้ handle(form); get ส่ง query string ให้ build(query)
  - `class="deadline-edit-form"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L024

```html
          <input type="hidden" name="action" value="update"><input type="hidden" name="no" value="{{ item.no }}">
```

- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `type="hidden"`: ช่องซ่อนส่ง action/no แก้ได้ผ่านเครื่องมือ browser จึงไม่ใช่ความลับหรือหลักฐานสิทธิ์
  - `name="action"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="update"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `type="hidden"`: ช่องซ่อนส่ง action/no แก้ได้ผ่านเครื่องมือ browser จึงไม่ใช่ความลับหรือหลักฐานสิทธิ์
  - `name="no"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="{{ item.no }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร

### L025

```html
          <div class="field"><label for="title-{{ item.no }}">ชื่องาน</label><input id="title-{{ item.no }}" name="title" value="{{ item.title }}" maxlength="80" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="title-{{ item.no }}"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- ข้อความแสดงผล `ชื่องาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="title-{{ item.no }}"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
  - `name="title"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="{{ item.title }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.title }}`: item คือ สมาชิกปัจจุบันของ items; ชื่องาน
  - `maxlength="80"`: จำกัดความยาวข้อความที่ browser ยอมรับ Python ตรวจซ้ำ
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L026

```html
          <div class="field"><label for="course-{{ item.no }}">วิชา</label><input id="course-{{ item.no }}" name="course" value="{{ item.course }}" maxlength="40" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="course-{{ item.no }}"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- ข้อความแสดงผล `วิชา`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="course-{{ item.no }}"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
  - `name="course"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="{{ item.course }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.course }}`: item คือ สมาชิกปัจจุบันของ items; ชื่อวิชา
  - `maxlength="40"`: จำกัดความยาวข้อความที่ browser ยอมรับ Python ตรวจซ้ำ
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L027

```html
          <div class="field-row"><div class="field"><label for="date-{{ item.no }}">วันส่ง</label><input id="date-{{ item.no }}" name="due_date" type="date" value="{{ item.due_date }}" required></div><div class="field"><label for="hours-{{ item.no }}">ชั่วโมงทั้งหมด</label><input id="hours-{{ item.no }}" name="estimated_hours" type="number" min="0.1" max="200" step="0.1" value="{{ item.estimated_hours }}" required></div><div class="field"><label for="done-{{ item.no }}">ทำแล้ว (ชั่วโมง)</label><input id="done-{{ item.no }}" name="done_hours" type="number" min="0" step="0.1" value="{{ item.done_hours }}" required></div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field-row"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="date-{{ item.no }}"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- ข้อความแสดงผล `วันส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="date-{{ item.no }}"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
  - `name="due_date"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="date"`: ช่องวัน browser ส่ง ISO YYYY-MM-DD แม้หน้าตาอาจตามภาษาท้องถิ่น
  - `value="{{ item.due_date }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.due_date }}`: item คือ สมาชิกปัจจุบันของ items; วันส่ง ISO YYYY-MM-DD
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="hours-{{ item.no }}"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- ข้อความแสดงผล `ชั่วโมงทั้งหมด`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="hours-{{ item.no }}"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
  - `name="estimated_hours"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="number"`: ช่องเลขใช้ min/max/step แต่ Python ได้ข้อความก่อนแปลง float
  - `min="0.1"`: ขอบล่างช่องตัวเลขฝั่ง browser Python ตรวจเงื่อนไขซ้ำ
  - `max="200"`: ขอบบนช่องตัวเลขฝั่ง browser Python ตรวจซ้ำ
  - `step="0.1"`: ขั้นของเลขที่ browser ยอมรับและปุ่มเพิ่มลด 0.1 คือทีละหนึ่งส่วนสิบ
  - `value="{{ item.estimated_hours }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.estimated_hours }}`: item คือ สมาชิกปัจจุบันของ items; ชั่วโมงทั้งหมดที่ประมาณไว้
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="done-{{ item.no }}"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- ข้อความแสดงผล `ทำแล้ว (ชั่วโมง)`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="done-{{ item.no }}"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
  - `name="done_hours"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="number"`: ช่องเลขใช้ min/max/step แต่ Python ได้ข้อความก่อนแปลง float
  - `min="0"`: ขอบล่างช่องตัวเลขฝั่ง browser Python ตรวจเงื่อนไขซ้ำ
  - `step="0.1"`: ขั้นของเลขที่ browser ยอมรับและปุ่มเพิ่มลด 0.1 คือทีละหนึ่งส่วนสิบ
  - `value="{{ item.done_hours }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.done_hours }}`: item คือ สมาชิกปัจจุบันของ items; ชั่วโมงที่ผู้ใช้บันทึกว่าทำแล้ว
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L028

```html
          <button class="btn small" type="submit">บันทึกการแก้ไข</button>
```

- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `class="btn small"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="submit"`: ปุ่มส่ง form ที่ตนอยู่ภายใน
- ข้อความแสดงผล `บันทึกการแก้ไข`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML

### L029

```html
        </form>
```

- `</form>`: ปิด form ที่เปิดไว้ตามลำดับการซ้อน HTML

### L030

```html
        <form method="post" class="deadline-delete-form" onsubmit="return confirm('ต้องการลบงานนี้หรือไม่?')"><input type="hidden" name="action" value="delete"><input type="hidden" name="no" value="{{ item.no }}"><button class="btn danger small" type="submit">ลบงานนี้</button></form>
```

- `<form>`: ชุดข้อมูลที่ส่งเมื่อ submit
  - `method="post"`: post ส่งข้อมูลใน body ให้ handle(form); get ส่ง query string ให้ build(query)
  - `class="deadline-delete-form"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `onsubmit="return confirm('ต้องการลบงานนี้หรือไม่?')"`: JS return confirm(...) ถามก่อนส่ง true ส่งต่อ false ยกเลิก; คำพูดเดี่ยวล้อมข้อความภายใน attribute คำพูดคู่
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `type="hidden"`: ช่องซ่อนส่ง action/no แก้ได้ผ่านเครื่องมือ browser จึงไม่ใช่ความลับหรือหลักฐานสิทธิ์
  - `name="action"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="delete"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `type="hidden"`: ช่องซ่อนส่ง action/no แก้ได้ผ่านเครื่องมือ browser จึงไม่ใช่ความลับหรือหลักฐานสิทธิ์
  - `name="no"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `value="{{ item.no }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ item.no }}`: item คือ สมาชิกปัจจุบันของ items; ตำแหน่งแถวใน storage.load() เริ่ม 0 ที่ page2 เพิ่ม ไม่ใช่ ID ถาวร
- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `class="btn danger small"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="submit"`: ปุ่มส่ง form ที่ตนอยู่ภายใน
- ข้อความแสดงผล `ลบงานนี้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</form>`: ปิด form ที่เปิดไว้ตามลำดับการซ้อน HTML

### L031

```html
      </details>
```

- `</details>`: ปิด details ที่เปิดไว้ตามลำดับการซ้อน HTML

### L032

```html
    </article>
```

- `</article>`: ปิด article ที่เปิดไว้ตามลำดับการซ้อน HTML

### L033

```html
    {% else %}<div class="empty">ยังไม่มีงานที่บันทึกไว้</div>{% endfor %}
```

- Jinja `{% else %}`: else ของลูป แสดงสถานะรายการว่างเมื่อไม่มีสมาชิก
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="empty"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ยังไม่มีงานที่บันทึกไว้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endfor %}`: ปิดลูปล่าสุด ถัดจากนี้อยู่นอก HTML ที่ทำซ้ำ

### L034

```html
  </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L035

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L036

```html
{% endblock %}
```

- Jinja `{% endblock %}`: ปิดบล็อกล่าสุด ไม่มีตัวอักษรแสดงจากคำสั่งนี้

## templates/page3.html — 30 บรรทัด

### L001

```html
{% extends "base.html" %}
```

- Jinja `{% extends "base.html" %}`: สืบทอดแม่แบบหลัก base.html ร่วม header/menu/footer/stylesheet

### L002

```html
{% block content %}
```

- Jinja `{% block content %}`: เปิดบล็อกเนื้อหาแทนพื้นที่ content ของแม่แบบ

### L003

```html
<div class="deadline-page-title"><span class="deadline-eyebrow">วางแผน</span><h1>รู้ก่อนว่างานจะชนกัน</h1><p class="lead">กำหนดเวลาที่คุณทำงานได้ต่อวัน แล้วดูว่าแต่ละช่วงมีเวลาพอหรือไม่</p></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-page-title"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-eyebrow"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `วางแผน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<h1>`: หัวข้อหลัก
- ข้อความแสดงผล `รู้ก่อนว่างานจะชนกัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h1>`: ปิด h1 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="lead"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `กำหนดเวลาที่คุณทำงานได้ต่อวัน แล้วดูว่าแต่ละช่วงมีเวลาพอหรือไม่`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L004

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L005

```html
<form method="get" class="panel deadline-hours-form">
```

- `<form>`: ชุดข้อมูลที่ส่งเมื่อ submit
  - `method="get"`: post ส่งข้อมูลใน body ให้ handle(form); get ส่ง query string ให้ build(query)
  - `class="panel deadline-hours-form"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L006

```html
  <div class="field"><label for="daily-hours">เวลาที่ทำงานได้ต่อวัน (ชั่วโมง)</label><input id="daily-hours" name="hours" type="number" min="0.1" max="12" step="0.1" value="{{ daily_hours }}" required></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="field"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<label>`: ชื่อช่องผูกกับ input ด้วย for/id
  - `for="daily-hours"`: ผูก label กับ input id เดียวกัน คลิกชื่อเพื่อเลือกช่องได้
- ข้อความแสดงผล `เวลาที่ทำงานได้ต่อวัน (ชั่วโมง)`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</label>`: ปิด label ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<input>`: ช่องรับข้อมูลแบบ void ไม่มีแท็กปิด
  - `id="daily-hours"`: ชื่อ element สำหรับ label หรือ JS อ้างอิง ต้องไม่ซ้ำในหน้า
  - `name="hours"`: key ที่ browser ส่งให้ Python ตามชื่อนี้
  - `type="number"`: ช่องเลขใช้ min/max/step แต่ Python ได้ข้อความก่อนแปลง float
  - `min="0.1"`: ขอบล่างช่องตัวเลขฝั่ง browser Python ตรวจเงื่อนไขซ้ำ
  - `max="12"`: ขอบบนช่องตัวเลขฝั่ง browser Python ตรวจซ้ำ
  - `step="0.1"`: ขั้นของเลขที่ browser ยอมรับและปุ่มเพิ่มลด 0.1 คือทีละหนึ่งส่วนสิบ
  - `value="{{ daily_hours }}"`: ค่าเริ่มต้น/ค่าที่ส่งในฟอร์ม hidden ส่งค่าถึงจะไม่มีช่องบนจอ
    - Expression `{{ daily_hours }}`: ชั่วโมงต่อวันที่ page3 ตรวจแล้ว ค่าเริ่มต้นหรือค่าผิดใช้ 2
  - `required`: boolean attribute มีอยู่หมายถึงต้องกรอก browser ตรวจตอน submit ไม่จำเป็นเขียน =true
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L007

```html
  <button class="btn" type="submit">คำนวณแผน</button>
```

- `<button>`: ปุ่มสำหรับผู้ใช้กด
  - `class="btn"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
  - `type="submit"`: ปุ่มส่ง form ที่ตนอยู่ภายใน
- ข้อความแสดงผล `คำนวณแผน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</button>`: ปิด button ที่เปิดไว้ตามลำดับการซ้อน HTML

### L008

```html
</form>
```

- `</form>`: ปิด form ที่เปิดไว้ตามลำดับการซ้อน HTML

### L009

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L010

```html
<div class="stat-grid deadline-summary">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat-grid deadline-summary"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L011

```html
  <div class="stat"><div class="label">งานที่ต้องวางแผน</div><div class="value">{{ tasks|length }}</div><div class="unit">รายการ</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `งานที่ต้องวางแผน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ tasks|length }}`: Jinja filter length คืนจำนวนงานยังไม่เสร็จใน tasks
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `รายการ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L012

```html
  <div class="stat {{ 'bad' if risk_count else 'good' }}"><div class="label">งานที่เสี่ยงไม่ทัน</div><div class="value">{{ risk_count }}</div><div class="unit">รายการ</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat {{ 'bad' if risk_count else 'good' }}"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
    - Expression `{{ 'bad' if risk_count else 'good' }}`: เลือก bad เมื่อ risk_count ไม่เป็นศูนย์ มิฉะนั้น good เพื่อเปลี่ยนสีตัวเลขสรุป
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `งานที่เสี่ยงไม่ทัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ risk_count }}`: จำนวนงานเกินกำหนดหรือมี gap > 0
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `รายการ`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L013

```html
  <div class="stat gold"><div class="label">เวลาที่แบ่งได้</div><div class="value">{{ daily_hours }}</div><div class="unit">ชั่วโมงต่อวัน</div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="stat gold"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="label"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เวลาที่แบ่งได้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="value"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ daily_hours }}`: ชั่วโมงต่อวันที่ page3 ตรวจแล้ว ค่าเริ่มต้นหรือค่าผิดใช้ 2
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="unit"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ชั่วโมงต่อวัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L014

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L015

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L016

```html
{% if focus %}<div class="deadline-focus"><span class="deadline-eyebrow">เริ่มจากงานนี้</span><strong>{{ focus.title }}</strong><span>วิชา {{ focus.course }} · ส่ง {{ focus.due_date }}</span></div>{% endif %}
```

- Jinja `{% if focus %}`: แสดงงานแนะนำเมื่อ focus เป็นงานจริง ถ้า None จะข้าม
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-focus"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-eyebrow"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เริ่มจากงานนี้`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<strong>`: เน้นความสำคัญเชิงความหมาย ปกติแสดงตัวหนา
- Expression `{{ focus.title }}`: focus คือ งานแรกของ page3; ชื่องาน
- `</strong>`: ปิด strong ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
- Expression `{{ focus.course }}`: focus คือ งานแรกของ page3; ชื่อวิชา
- Expression `{{ focus.due_date }}`: focus คือ งานแรกของ page3; วันส่ง ISO YYYY-MM-DD
- ข้อความแสดงผล `วิชา  · ส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endif %}`: ปิด if ล่าสุดที่ยังเปิดอยู่ ถ้าซ้อนกันปิดจากด้านในออกด้านนอก

### L017

```html

```

บรรทัดว่างแบ่งส่วนให้อ่านง่าย ไม่สร้าง element หรือคำสั่งเพิ่ม

### L018

```html
<div class="deadline-section-head"><div><h2>ลำดับงานตามวันส่ง</h2><p class="note">ระบบรวมชั่วโมงงานที่ต้องเสร็จก่อนแต่ละวัน แล้วเทียบกับเวลาที่มี</p></div></div>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-section-head"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
- `<h2>`: หัวข้อรอง
- ข้อความแสดงผล `ลำดับงานตามวันส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</h2>`: ปิด h2 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="note"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ระบบรวมชั่วโมงงานที่ต้องเสร็จก่อนแต่ละวัน แล้วเทียบกับเวลาที่มี`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L019

```html
<div class="deadline-task-list">
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-task-list"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L020

```html
  {% for task in tasks %}
```

- Jinja `{% for task in tasks %}`: วนสมาชิกจาก tasks ทีละตัวในชื่อตัวแปร task HTML ภายในจึงซ้ำตามจำนวนสมาชิก

### L021

```html
  <article class="deadline-task deadline-plan-task">
```

- `<article>`: เนื้อหาหนึ่งรายการแยกอ่านได้ เช่นการ์ดงาน
  - `class="deadline-task deadline-plan-task"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS

### L022

```html
    <div class="deadline-task-main"><span class="deadline-course">{{ task.course }}</span><h3>{{ task.title }}</h3><p class="deadline-meta">ส่ง <time datetime="{{ task.due_date }}">{{ task.due_date }}</time> · เหลือ {{ "{:,.1f}".format(task.remaining_hours) }} ชั่วโมง</p>
```

- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="deadline-task-main"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="deadline-course"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- Expression `{{ task.course }}`: task คือ สมาชิกปัจจุบันของ tasks; ชื่อวิชา
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<h3>`: หัวข้องาน/หัวข้อย่อยลำดับสาม
- Expression `{{ task.title }}`: task คือ สมาชิกปัจจุบันของ tasks; ชื่องาน
- `</h3>`: ปิด h3 ที่เปิดไว้ตามลำดับการซ้อน HTML
- `<p>`: ย่อหน้าข้อความ
  - `class="deadline-meta"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ส่ง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `<time>`: วันที่ที่มีข้อความสำหรับคนและ datetime สำหรับเครื่อง
  - `datetime="{{ task.due_date }}"`: วันที่รูปแบบ ISO ให้เครื่องอ่าน ข้อความใน time ให้คนอ่าน
    - Expression `{{ task.due_date }}`: task คือ สมาชิกปัจจุบันของ tasks; วันส่ง ISO YYYY-MM-DD
- Expression `{{ task.due_date }}`: task คือ สมาชิกปัจจุบันของ tasks; วันส่ง ISO YYYY-MM-DD
- `</time>`: ปิด time ที่เปิดไว้ตามลำดับการซ้อน HTML
- Expression `{{ "{:,.1f}".format(task.remaining_hours) }}`: จัด task.remaining_hours (task คือ สมาชิกปัจจุบันของ tasks; ชั่วโมงที่ Assignment.remaining_hours() คำนวณ) เป็นข้อความคั่นหลักพันและทศนิยม 1 ตำแหน่งตามพจนานุกรม ไม่แก้ข้อมูลจริง
- ข้อความแสดงผล `· เหลือ  ชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L023

```html
      {% if task.days_left >= 0 %}<p class="deadline-plan-detail">งานสะสมถึงวันส่งนี้ต้องทำเฉลี่ย <strong>{{ task.hours_per_day }} ชั่วโมง/วัน</strong>{% if task.gap > 0 %} · ขาดเวลาอีก <strong>{{ task.gap }} ชั่วโมง</strong>{% endif %}</p>{% else %}<p class="deadline-plan-detail">เลยวันส่งแล้ว ควรติดต่อผู้สอนและจัดการงานนี้ก่อน</p>{% endif %}
```

- Jinja `{% if task.days_left >= 0 %}`: แสดง hours_per_day เฉพาะงานยังไม่เลยกำหนด งานเลยกำหนดไม่มี key นี้
- `<p>`: ย่อหน้าข้อความ
  - `class="deadline-plan-detail"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `งานสะสมถึงวันส่งนี้ต้องทำเฉลี่ย`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `<strong>`: เน้นความสำคัญเชิงความหมาย ปกติแสดงตัวหนา
- Expression `{{ task.hours_per_day }}`: task คือ สมาชิกปัจจุบันของ tasks; ชั่วโมงงานสะสมหาร days_left+1 ปัดทศนิยม 1 ตำแหน่ง
- ข้อความแสดงผล `ชั่วโมง/วัน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</strong>`: ปิด strong ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% if task.gap > 0 %}`: เพิ่มข้อความขาดเวลาเมื่อ gap > 0 เท่านั้น
- ข้อความแสดงผล `· ขาดเวลาอีก`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `<strong>`: เน้นความสำคัญเชิงความหมาย ปกติแสดงตัวหนา
- Expression `{{ task.gap }}`: task คือ สมาชิกปัจจุบันของ tasks; ชั่วโมงที่ภาระสะสมเกินเวลาที่มี ปัดทศนิยม 1 ตำแหน่ง
- ข้อความแสดงผล `ชั่วโมง`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</strong>`: ปิด strong ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endif %}`: ปิด if ล่าสุดที่ยังเปิดอยู่ ถ้าซ้อนกันปิดจากด้านในออกด้านนอก
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% else %}`: else ของ if task.days_left >= 0 แสดงข้อความเมื่อเลยวันส่ง
- `<p>`: ย่อหน้าข้อความ
  - `class="deadline-plan-detail"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `เลยวันส่งแล้ว ควรติดต่อผู้สอนและจัดการงานนี้ก่อน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endif %}`: ปิด if ล่าสุดที่ยังเปิดอยู่ ถ้าซ้อนกันปิดจากด้านในออกด้านนอก

### L024

```html
    </div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L025

```html
    <span class="badge {{ task.tone }}">{{ task.status }}</span>
```

- `<span>`: ข้อความย่อยแบบ inline ตามปกติ ก่อน CSS เปลี่ยน display
  - `class="badge {{ task.tone }}"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
    - Expression `{{ task.tone }}`: task คือ สมาชิกปัจจุบันของ tasks; คลาสสีจาก Python good/bad/gold หรือว่าง
- Expression `{{ task.status }}`: task คือ สมาชิกปัจจุบันของ tasks; ข้อความสถานะจากเงื่อนไข Python
- `</span>`: ปิด span ที่เปิดไว้ตามลำดับการซ้อน HTML

### L026

```html
  </article>
```

- `</article>`: ปิด article ที่เปิดไว้ตามลำดับการซ้อน HTML

### L027

```html
  {% else %}<div class="empty">งานทั้งหมดเสร็จแล้ว หรือยังไม่ได้เพิ่มงาน</div>{% endfor %}
```

- Jinja `{% else %}`: else ของลูป แสดงสถานะรายการว่างเมื่อไม่มีสมาชิก
- `<div>`: กล่องโครงสร้างทั่วไปสำหรับจัดวางด้วย CSS
  - `class="empty"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `งานทั้งหมดเสร็จแล้ว หรือยังไม่ได้เพิ่มงาน`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML
- Jinja `{% endfor %}`: ปิดลูปล่าสุด ถัดจากนี้อยู่นอก HTML ที่ทำซ้ำ

### L028

```html
</div>
```

- `</div>`: ปิด div ที่เปิดไว้ตามลำดับการซ้อน HTML

### L029

```html
<p class="note deadline-footnote">ผลลัพธ์เป็นการประมาณจากชั่วโมงที่กรอกไว้ หากมีเวลาทำงานไม่เท่ากันในแต่ละวัน ให้ปรับค่าแล้วคำนวณใหม่</p>
```

- `<p>`: ย่อหน้าข้อความ
  - `class="note deadline-footnote"`: คลาสที่ใช้เลือกกฎ CSS แยกแต่ละชื่อด้วยช่องว่าง ดูคำอธิบาย selector ในส่วน CSS
- ข้อความแสดงผล `ผลลัพธ์เป็นการประมาณจากชั่วโมงที่กรอกไว้ หากมีเวลาทำงานไม่เท่ากันในแต่ละวัน ให้ปรับค่าแล้วคำนวณใหม่`: literal อ่านตามอักขระ ไม่มีการคำนวณแฝง
- `</p>`: ปิด p ที่เปิดไว้ตามลำดับการซ้อน HTML

### L030

```html
{% endblock %}
```

- Jinja `{% endblock %}`: ปิดบล็อกล่าสุด ไม่มีตัวอักษรแสดงจากคำสั่งนี้

## static/style.css — 239 บรรทัด

ส่วนเดิมจาก skeleton คือบรรทัด 1–170 บรรทัด 171 เป็น marker your own styles below ส่วนโครงการ Deadline Compass เพิ่มหลัง marker นี้ การอธิบายส่วนเดิมไม่ได้หมายความว่าสมาชิกเขียน CSS เดิมทั้งหมด บาง component เช่น gallery/chart/donut/game-board มีอยู่ใน skeleton แต่ไม่ได้เรียกใช้จาก template โครงงานปัจจุบัน

### L001

```css
/* style.css — given, but you may ADD your own rules at the bottom. */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L002

```css
:root {
```

ส่วนเดิมของ skeleton

- Selector `:root`: element ราก HTML ใช้ประกาศ custom properties ที่สืบทอดไปยังลูก

### L003

```css
  --maroon: #7a1f2b;
```

ส่วนเดิมของ skeleton

- Declaration `--maroon: #7a1f2b;`: ประกาศตัวแปร CSS --maroon เป็นสีแดงเลือดหมูหลัก ใช้ซ้ำได้ด้วย var(--maroon); ค่าที่ใช้จริงคือ `#7a1f2b` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L004

```css
  --maroon-dark: #5c1620;
```

ส่วนเดิมของ skeleton

- Declaration `--maroon-dark: #5c1620;`: ประกาศตัวแปร CSS --maroon-dark เป็นสีแดงเลือดหมูเข้ม ใช้ซ้ำได้ด้วย var(--maroon-dark); ค่าที่ใช้จริงคือ `#5c1620` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L005

```css
  --gold: #e6b422;
```

ส่วนเดิมของ skeleton

- Declaration `--gold: #e6b422;`: ประกาศตัวแปร CSS --gold เป็นสีทองเน้นข้อมูล ใช้ซ้ำได้ด้วย var(--gold); ค่าที่ใช้จริงคือ `#e6b422` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L006

```css
  --ink: #1f2933;
```

ส่วนเดิมของ skeleton

- Declaration `--ink: #1f2933;`: ประกาศตัวแปร CSS --ink เป็นสีข้อความหลักเข้ม ใช้ซ้ำได้ด้วย var(--ink); ค่าที่ใช้จริงคือ `#1f2933` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L007

```css
  --muted: #6b7280;
```

ส่วนเดิมของ skeleton

- Declaration `--muted: #6b7280;`: ประกาศตัวแปร CSS --muted เป็นสีข้อความรองเทา ใช้ซ้ำได้ด้วย var(--muted); ค่าที่ใช้จริงคือ `#6b7280` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L008

```css
  --line: #e5e7eb;
```

ส่วนเดิมของ skeleton

- Declaration `--line: #e5e7eb;`: ประกาศตัวแปร CSS --line เป็นสีเส้นแบ่งอ่อน ใช้ซ้ำได้ด้วย var(--line); ค่าที่ใช้จริงคือ `#e5e7eb` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L009

```css
  --bg: #f7f5f2;
```

ส่วนเดิมของ skeleton

- Declaration `--bg: #f7f5f2;`: ประกาศตัวแปร CSS --bg เป็นสีพื้นหลังครีม ใช้ซ้ำได้ด้วย var(--bg); ค่าที่ใช้จริงคือ `#f7f5f2` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L010

```css
  --card: #ffffff;
```

ส่วนเดิมของ skeleton

- Declaration `--card: #ffffff;`: ประกาศตัวแปร CSS --card เป็นสีพื้นการ์ดขาว ใช้ซ้ำได้ด้วย var(--card); ค่าที่ใช้จริงคือ `#ffffff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L011

```css
}
```

ส่วนเดิมของ skeleton

ปีกกาปิดจบบล็อก `:root` กฎถัดไปจึงอยู่นอกขอบเขตนี้

### L012

```css
* { box-sizing: border-box; }
```

ส่วนเดิมของ skeleton

- Selector `*`: universal selector เลือกทุก element
- Declaration `box-sizing: border-box;`: border-box ทำให้ width/height รวม padding และ border แล้ว ช่วยคุมกล่องไม่ขยายเกินขนาดที่กำหนด; ค่าที่ใช้จริงคือ `border-box` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L013

```css
html, body { margin: 0; }
```

ส่วนเดิมของ skeleton

- Selector `html`: แท็ก html
- Selector `body`: แท็ก body
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L014

```css
body {
```

ส่วนเดิมของ skeleton

- Selector `body`: แท็ก body

### L015

```css
  font-family: "Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif;
```

ส่วนเดิมของ skeleton

- Declaration `font-family: "Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif;`: รายชื่อฟอนต์สำรองเรียงลำดับ ไม่มีการดาวน์โหลดฟอนต์จาก property นี้; inherit รับจากแม่; monospace คือตัวกว้างเท่ากัน; ค่าที่ใช้จริงคือ `"Segoe UI", Sarabun, "Noto Sans Thai", system-ui, sans-serif` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L016

```css
  color: var(--ink);
```

ส่วนเดิมของ skeleton

- Declaration `color: var(--ink);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --ink; ค่าที่ใช้จริงคือ `var(--ink)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L017

```css
  background: var(--bg);
```

ส่วนเดิมของ skeleton

- Declaration `background: var(--bg);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --bg; ค่าที่ใช้จริงคือ `var(--bg)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L018

```css
  line-height: 1.55;
```

ส่วนเดิมของ skeleton

- Declaration `line-height: 1.55;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `1.55` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L019

```css
  display: flex; flex-direction: column; min-height: 100vh;
```

ส่วนเดิมของ skeleton

- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `min-height: 100vh;`: ความสูงขั้นต่ำ; 100vh อย่างน้อยเท่าความสูง viewport; ค่าที่ใช้จริงคือ `100vh` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L020

```css
}
```

ส่วนเดิมของ skeleton

ปีกกาปิดจบบล็อก `body` กฎถัดไปจึงอยู่นอกขอบเขตนี้

### L021

```css
.wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; width: 100%; }
```

ส่วนเดิมของ skeleton

- Selector `.wrap`: คลาส wrap
- Declaration `max-width: 960px;`: ขอบบนของความกว้าง; none ยกเลิกเพดานความกว้างเดิม; ค่าที่ใช้จริงคือ `960px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0 auto;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บนล่าง 0; ซ้ายขวา auto; ค่าที่ใช้จริงคือ `0 auto` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 0 20px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 0; ซ้ายขวา 20px; ค่าที่ใช้จริงคือ `0 20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L022

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L023

```css
/* ---------- header ---------- */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L024

```css
.site-header { background: linear-gradient(180deg, var(--maroon), var(--maroon-dark)); color: #fff; }
```

ส่วนเดิมของ skeleton

- Selector `.site-header`: คลาส site-header
- Declaration `background: linear-gradient(180deg, var(--maroon), var(--maroon-dark));`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon, --maroon-dark; ไล่สีตามองศาและจุดสี/% เรียงในวงเล็บ; ค่าที่ใช้จริงคือ `linear-gradient(180deg, var(--maroon), var(--maroon-dark))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L025

```css
.header-row { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 12px 20px; }
```

ส่วนเดิมของ skeleton

- Selector `.header-row`: คลาส header-row
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 16px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 12px 20px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 12px; ซ้ายขวา 20px; ค่าที่ใช้จริงคือ `12px 20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L026

```css
.brand { display: flex; align-items: center; gap: 14px; color: #fff; text-decoration: none; }
```

ส่วนเดิมของ skeleton

- Selector `.brand`: คลาส brand
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: none;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L027

```css
.brand img { height: 56px; width: 56px; border-radius: 50%; background: #fff; padding: 2px; }
```

ส่วนเดิมของ skeleton

- Selector `.brand img`: คลาส brand; แท็ก img; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `height: 56px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `width: 56px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 50%;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `50%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 2px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `2px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L028

```css
.brand-text { display: flex; flex-direction: column; }
```

ส่วนเดิมของ skeleton

- Selector `.brand-text`: คลาส brand-text
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L029

```css
.brand-line1 { font-weight: 700; font-size: 17px; letter-spacing: .2px; }
```

ส่วนเดิมของ skeleton

- Selector `.brand-line1`: คลาส brand-line1
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 17px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `17px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `letter-spacing: .2px;`: ช่องเพิ่มระหว่างอักขระ; em เทียบขนาดฟอนต์ปัจจุบัน; ค่าที่ใช้จริงคือ `.2px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L030

```css
.brand-line2 { font-size: 12.5px; opacity: .85; }
```

ส่วนเดิมของ skeleton

- Selector `.brand-line2`: คลาส brand-line2
- Declaration `font-size: 12.5px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12.5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `opacity: .85;`: ความทึบทั้ง element และเนื้อหาลูก 1 ทึบเต็ม ค่าน้อยลงยิ่งโปร่ง; ค่าที่ใช้จริงคือ `.85` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L031

```css
.group-badge { font-size: 13px; background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.3); padding: 4px 12px; border-radius: 999px; white-space: nowrap; }
```

ส่วนเดิมของ skeleton

- Selector `.group-badge`: คลาส group-badge
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: rgba(255,255,255,.14);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `rgba(255,255,255,.14)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid rgba(255,255,255,.3);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid rgba(255,255,255,.3)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 4px 12px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 4px; ซ้ายขวา 12px; ค่าที่ใช้จริงคือ `4px 12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 999px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `999px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `white-space: nowrap;`: nowrap ป้องกันการตัดขึ้นบรรทัดใหม่ตามปกติ; ค่าที่ใช้จริงคือ `nowrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L032

```css
.site-nav { display: flex; gap: 4px; flex-wrap: wrap; padding: 0 20px 0; border-top: 1px solid rgba(255,255,255,.15); }
```

ส่วนเดิมของ skeleton

- Selector `.site-nav`: คลาส site-nav
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 4px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 0 20px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บน 0; ซ้ายขวา 20px; ล่าง 0; ค่าที่ใช้จริงคือ `0 20px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-top: 1px solid rgba(255,255,255,.15);`: เส้นขอบเฉพาะด้านบน; ค่าที่ใช้จริงคือ `1px solid rgba(255,255,255,.15)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L033

```css
.site-nav a { color: #fff; text-decoration: none; padding: 10px 14px; font-size: 14px; border-bottom: 3px solid transparent; opacity: .85; }
```

ส่วนเดิมของ skeleton

- Selector `.site-nav a`: คลาส site-nav; แท็ก a; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: none;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 10px 14px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 10px; ซ้ายขวา 14px; ค่าที่ใช้จริงคือ `10px 14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-bottom: 3px solid transparent;`: เส้นขอบเฉพาะด้านล่าง; none ยกเลิก; ค่าที่ใช้จริงคือ `3px solid transparent` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `opacity: .85;`: ความทึบทั้ง element และเนื้อหาลูก 1 ทึบเต็ม ค่าน้อยลงยิ่งโปร่ง; ค่าที่ใช้จริงคือ `.85` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L034

```css
.site-nav a:hover { opacity: 1; }
```

ส่วนเดิมของ skeleton

- Selector `.site-nav a:hover`: คลาส site-nav; แท็ก a; สถานะ/ตำแหน่ง :hover ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `opacity: 1;`: ความทึบทั้ง element และเนื้อหาลูก 1 ทึบเต็ม ค่าน้อยลงยิ่งโปร่ง; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L035

```css
.site-nav a.active { border-bottom-color: var(--gold); opacity: 1; font-weight: 600; }
```

ส่วนเดิมของ skeleton

- Selector `.site-nav a.active`: คลาส site-nav; คลาส active; แท็ก a; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `border-bottom-color: var(--gold);`: เปลี่ยนสีเส้นล่างโดยรักษาความหนาและรูปแบบจากเดิม; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `opacity: 1;`: ความทึบทั้ง element และเนื้อหาลูก 1 ทึบเต็ม ค่าน้อยลงยิ่งโปร่ง; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L036

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L037

```css
/* ---------- main ---------- */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L038

```css
main { flex: 1; padding: 28px 20px 48px; }
```

ส่วนเดิมของ skeleton

- Selector `main`: แท็ก main
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 28px 20px 48px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บน 28px; ซ้ายขวา 20px; ล่าง 48px; ค่าที่ใช้จริงคือ `28px 20px 48px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L039

```css
h1 { font-size: 26px; margin: 0 0 8px; }
```

ส่วนเดิมของ skeleton

- Selector `h1`: แท็ก h1
- Declaration `font-size: 26px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `26px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0 0 8px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 0; ซ้ายขวา 0; ล่าง 8px; ค่าที่ใช้จริงคือ `0 0 8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L040

```css
h2 { font-size: 19px; margin: 28px 0 10px; }
```

ส่วนเดิมของ skeleton

- Selector `h2`: แท็ก h2
- Declaration `font-size: 19px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `19px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 28px 0 10px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 28px; ซ้ายขวา 0; ล่าง 10px; ค่าที่ใช้จริงคือ `28px 0 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L041

```css
.lead { color: var(--muted); margin-top: 0; }
```

ส่วนเดิมของ skeleton

- Selector `.lead`: คลาส lead
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-top: 0;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L042

```css
.muted { color: var(--muted); font-weight: normal; font-size: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.muted`: คลาส muted
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: normal;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `normal` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L043

```css
small.muted { font-size: 15px; }
```

ส่วนเดิมของ skeleton

- Selector `small.muted`: คลาส muted; แท็ก small
- Declaration `font-size: 15px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `15px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L044

```css
.banner { background: #fff8e1; border: 1px solid #f6d46a; color: #6b4d00; padding: 10px 14px; border-radius: 8px; margin-bottom: 18px; }
```

ส่วนเดิมของ skeleton

- Selector `.banner`: คลาส banner
- Declaration `background: #fff8e1;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff8e1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid #f6d46a;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid #f6d46a` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #6b4d00;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#6b4d00` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 10px 14px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 10px; ซ้ายขวา 14px; ค่าที่ใช้จริงคือ `10px 14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 8px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 18px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L045

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L046

```css
table { width: 100%; border-collapse: collapse; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
```

ส่วนเดิมของ skeleton

- Selector `table`: แท็ก table
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-collapse: collapse;`: collapse ให้เส้น cell ตารางติดกันรวมเป็นเส้นเดียว; ค่าที่ใช้จริงคือ `collapse` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L047

```css
th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); font-size: 14.5px; }
```

ส่วนเดิมของ skeleton

- Selector `th`: แท็ก th
- Selector `td`: แท็ก td
- Declaration `text-align: left;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `left` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 10px 12px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 10px; ซ้ายขวา 12px; ค่าที่ใช้จริงคือ `10px 12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-bottom: 1px solid var(--line);`: เส้นขอบเฉพาะด้านล่าง; none ยกเลิก; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14.5px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14.5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L048

```css
th { background: #f1ede8; color: var(--muted); font-weight: 600; font-size: 13px; }
```

ส่วนเดิมของ skeleton

- Selector `th`: แท็ก th
- Declaration `background: #f1ede8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#f1ede8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L049

```css
tr:last-child td { border-bottom: none; }
```

ส่วนเดิมของ skeleton

- Selector `tr:last-child td`: แท็ก tr, td; สถานะ/ตำแหน่ง :last-child ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `border-bottom: none;`: เส้นขอบเฉพาะด้านล่าง; none ยกเลิก; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L050

```css
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
```

ส่วนเดิมของ skeleton

- Selector `td.num`: คลาส num; แท็ก td
- Selector `th.num`: คลาส num; แท็ก th
- Declaration `text-align: right;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `right` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-variant-numeric: tabular-nums;`: tabular-nums ขอรูปแบบเลขความกว้างเท่ากันจากฟอนต์ ช่วยอ่านจำนวนเรียงกัน; ค่าที่ใช้จริงคือ `tabular-nums` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L051

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L052

```css
.btn { display: inline-block; padding: 8px 16px; border-radius: 8px; border: 1px solid var(--maroon); background: var(--maroon); color: #fff; font-size: 14px; text-decoration: none; cursor: pointer; }
```

ส่วนเดิมของ skeleton

- Selector `.btn`: คลาส btn
- Declaration `display: inline-block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `inline-block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 8px 16px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 8px; ซ้ายขวา 16px; ค่าที่ใช้จริงคือ `8px 16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 8px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--maroon);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `1px solid var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: none;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `cursor: pointer;`: pointer เปลี่ยนตัวชี้เมาส์เป็นมือเหนือสิ่งกดได้; ค่าที่ใช้จริงคือ `pointer` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L053

```css
.btn.ghost { background: #fff; color: var(--maroon); }
```

ส่วนเดิมของ skeleton

- Selector `.btn.ghost`: คลาส btn; คลาส ghost; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L054

```css
.field { margin-bottom: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.field`: คลาส field
- Declaration `margin-bottom: 14px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L055

```css
.field label { display: block; font-size: 13px; color: var(--muted); margin-bottom: 4px; }
```

ส่วนเดิมของ skeleton

- Selector `.field label`: คลาส field; แท็ก label; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 4px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L056

```css
.field input, .field select, .field textarea { width: 100%; max-width: 380px; padding: 8px 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; font-family: inherit; }
```

ส่วนเดิมของ skeleton

- Selector `.field input`: คลาส field; แท็ก input; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.field select`: คลาส field; แท็ก select; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.field textarea`: คลาส field; แท็ก textarea; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `max-width: 380px;`: ขอบบนของความกว้าง; none ยกเลิกเพดานความกว้างเดิม; ค่าที่ใช้จริงคือ `380px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 8px 10px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 8px; ซ้ายขวา 10px; ค่าที่ใช้จริงคือ `8px 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid #cbd5e1;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid #cbd5e1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 8px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-family: inherit;`: รายชื่อฟอนต์สำรองเรียงลำดับ ไม่มีการดาวน์โหลดฟอนต์จาก property นี้; inherit รับจากแม่; monospace คือตัวกว้างเท่ากัน; ค่าที่ใช้จริงคือ `inherit` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L057

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L058

```css
.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }
```

ส่วนเดิมของ skeleton

- Selector `.stat-grid`: คลาส stat-grid
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; auto-fit ยุบช่องที่ไม่มี item; minmax กำหนดกว้างขั้นต่ำและขยายสูงสุดตาม 1fr; ค่าที่ใช้จริงคือ `repeat(auto-fit, minmax(180px, 1fr))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 12px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L059

```css
.stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; }
```

ส่วนเดิมของ skeleton

- Selector `.stat`: คลาส stat
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 14px 16px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 14px; ซ้ายขวา 16px; ค่าที่ใช้จริงคือ `14px 16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L060

```css
.stat .label { color: var(--muted); font-size: 13px; }
```

ส่วนเดิมของ skeleton

- Selector `.stat .label`: คลาส stat; คลาส label; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L061

```css
.stat .value { font-size: 26px; font-weight: 700; color: var(--maroon); }
```

ส่วนเดิมของ skeleton

- Selector `.stat .value`: คลาส stat; คลาส value; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-size: 26px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `26px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L062

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L063

```css
.empty { color: var(--muted); padding: 32px; text-align: center; background: var(--card); border: 1px dashed var(--line); border-radius: 10px; }
```

ส่วนเดิมของ skeleton

- Selector `.empty`: คลาส empty
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 32px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `32px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px dashed var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px dashed var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L064

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L065

```css
/* home */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L066

```css
.hero { padding: 8px 0 20px; }
```

ส่วนเดิมของ skeleton

- Selector `.hero`: คลาส hero
- Declaration `padding: 8px 0 20px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บน 8px; ซ้ายขวา 0; ล่าง 20px; ค่าที่ใช้จริงคือ `8px 0 20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L067

```css
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.cards`: คลาส cards
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; auto-fit ยุบช่องที่ไม่มี item; minmax กำหนดกว้างขั้นต่ำและขยายสูงสุดตาม 1fr; ค่าที่ใช้จริงคือ `repeat(auto-fit, minmax(200px, 1fr))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L068

```css
.card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-decoration: none; color: var(--ink); display: flex; flex-direction: column; gap: 4px; transition: transform .1s, box-shadow .1s; }
```

ส่วนเดิมของ skeleton

- Selector `.card`: คลาส card
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 18px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: none;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--ink);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --ink; ค่าที่ใช้จริงคือ `var(--ink)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 4px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `transition: transform .1s, box-shadow .1s;`: เปลี่ยน transform และ box-shadow แบบค่อยเป็นค่อยไปอย่างละ .1s=0.1 วินาทีเมื่อสถานะเปลี่ยน; ค่าที่ใช้จริงคือ `transform .1s, box-shadow .1s` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L069

```css
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.07); }
```

ส่วนเดิมของ skeleton

- Selector `.card:hover`: คลาส card; สถานะ/ตำแหน่ง :hover ตามพจนานุกรม
- Declaration `transform: translateY(-2px);`: แปลงตำแหน่ง/หมุนภาพโดยไม่จัด layout ฐานใหม่: translateY(-2px) ยก 2px; rotate(9deg) หมุน 9 องศา; ค่าที่ใช้จริงคือ `translateY(-2px)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `box-shadow: 0 6px 18px rgba(0,0,0,.07);`: เงากล่อง อ่านเป็น x y ความฟุ้ง และสี rgba ตามลำดับ; ค่าที่ใช้จริงคือ `0 6px 18px rgba(0,0,0,.07)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L070

```css
.card-kicker { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; }
```

ส่วนเดิมของ skeleton

- Selector `.card-kicker`: คลาส card-kicker
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-transform: uppercase;`: uppercase แสดงตัวอักษรที่มีรูปพิมพ์ใหญ่ เช่นอังกฤษ เป็นพิมพ์ใหญ่ ไม่เปลี่ยนต้นฉบับใน DOM; ค่าที่ใช้จริงคือ `uppercase` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `letter-spacing: .5px;`: ช่องเพิ่มระหว่างอักขระ; em เทียบขนาดฟอนต์ปัจจุบัน; ค่าที่ใช้จริงคือ `.5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L071

```css
.card-title { font-size: 17px; font-weight: 600; color: var(--maroon); }
```

ส่วนเดิมของ skeleton

- Selector `.card-title`: คลาส card-title
- Declaration `font-size: 17px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `17px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L072

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L073

```css
/* team */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L074

```css
.member-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 8px; }
```

ส่วนเดิมของ skeleton

- Selector `.member-grid`: คลาส member-grid
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; auto-fit ยุบช่องที่ไม่มี item; minmax กำหนดกว้างขั้นต่ำและขยายสูงสุดตาม 1fr; ค่าที่ใช้จริงคือ `repeat(auto-fit, minmax(200px, 1fr))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 8px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L075

```css
.member { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; text-align: center; }
```

ส่วนเดิมของ skeleton

- Selector `.member`: คลาส member
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 18px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L076

```css
.avatar { width: 56px; height: 56px; border-radius: 50%; background: var(--maroon); color: #fff; font-size: 24px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; }
```

ส่วนเดิมของ skeleton

- Selector `.avatar`: คลาส avatar
- Declaration `width: 56px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 56px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 50%;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `50%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 24px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `24px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: center;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0 auto 10px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 0; ซ้ายขวา auto; ล่าง 10px; ค่าที่ใช้จริงคือ `0 auto 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L077

```css
.member-name { font-weight: 600; }
```

ส่วนเดิมของ skeleton

- Selector `.member-name`: คลาส member-name
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L078

```css
.role { color: var(--maroon); font-size: 13px; margin-top: 4px; }
```

ส่วนเดิมของ skeleton

- Selector `.role`: คลาส role
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-top: 4px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L079

```css
.task { color: var(--muted); font-size: 13px; }
```

ส่วนเดิมของ skeleton

- Selector `.task`: คลาส task
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L080

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L081

```css
/* gallery */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L082

```css
.gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.gallery`: คลาส gallery
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; auto-fill สร้างช่องจนเต็มพื้นที่ อาจเหลือช่องว่าง; minmax กำหนดขั้นต่ำและ 1fr; ค่าที่ใช้จริงคือ `repeat(auto-fill, minmax(180px, 1fr))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L083

```css
.gallery figure { margin: 0; background: var(--card); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }
```

ส่วนเดิมของ skeleton

- Selector `.gallery figure`: คลาส gallery; แท็ก figure; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L084

```css
.gallery img { width: 100%; height: 140px; object-fit: cover; display: block; }
```

ส่วนเดิมของ skeleton

- Selector `.gallery img`: คลาส gallery; แท็ก img; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 140px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `140px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `object-fit: cover;`: cover รักษาสัดส่วนภาพและครอบส่วนเกินให้เต็มกรอบ ไม่ยืดภาพผิดสัดส่วน; ค่าที่ใช้จริงคือ `cover` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L085

```css
.gallery figcaption { padding: 8px 10px; font-size: 13.5px; }
```

ส่วนเดิมของ skeleton

- Selector `.gallery figcaption`: คลาส gallery; แท็ก figcaption; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `padding: 8px 10px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 8px; ซ้ายขวา 10px; ค่าที่ใช้จริงคือ `8px 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13.5px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13.5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L086

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L087

```css
/* not built */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L088

```css
.notbuilt { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 28px; }
```

ส่วนเดิมของ skeleton

- Selector `.notbuilt`: คลาส notbuilt
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 28px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `28px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L089

```css
.notbuilt .reason { font-size: 16px; }
```

ส่วนเดิมของ skeleton

- Selector `.notbuilt .reason`: คลาส notbuilt; คลาส reason; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-size: 16px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L090

```css
.notbuilt pre { background: #1f2933; color: #f8fafc; padding: 12px; border-radius: 8px; overflow-x: auto; font-size: 12.5px; }
```

ส่วนเดิมของ skeleton

- Selector `.notbuilt pre`: คลาส notbuilt; แท็ก pre; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `background: #1f2933;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#1f2933` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #f8fafc;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#f8fafc` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 12px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 8px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow-x: auto;`: auto แสดงเลื่อนแนวนอนเมื่อเนื้อหาล้น; ค่าที่ใช้จริงคือ `auto` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12.5px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12.5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L091

```css
.notbuilt code { background: #f1ede8; padding: 1px 6px; border-radius: 4px; }
```

ส่วนเดิมของ skeleton

- Selector `.notbuilt code`: คลาส notbuilt; แท็ก code; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `background: #f1ede8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#f1ede8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 1px 6px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 1px; ซ้ายขวา 6px; ค่าที่ใช้จริงคือ `1px 6px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 4px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L092

```css
.hint { color: var(--muted); font-size: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.hint`: คลาส hint
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L093

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L094

```css
/* footer */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L095

```css
.site-footer { border-top: 1px solid var(--line); color: var(--muted); font-size: 13px; padding: 12px 0; background: #fff; }
```

ส่วนเดิมของ skeleton

- Selector `.site-footer`: คลาส site-footer
- Declaration `border-top: 1px solid var(--line);`: เส้นขอบเฉพาะด้านบน; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 12px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 12px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `12px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L096

```css
.site-footer .wrap { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
```

ส่วนเดิมของ skeleton

- Selector `.site-footer .wrap`: คลาส site-footer; คลาส wrap; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 8px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L097

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L098

```css
@media (max-width: 640px) {
```

ส่วนเดิมของ skeleton

- Media query `@media (max-width: 640px)`: ใช้กฎด้านในเมื่อ viewport กว้างไม่เกิน 640 CSS px รวมเท่ากับค่านี้; วงเล็บครอบเงื่อนไข ปีกกาครอบกฎ

### L099

```css
  .brand-line1 { font-size: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.brand-line1`: คลาส brand-line1
- Declaration `font-size: 14px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L100

```css
  .brand-line2 { display: none; }
```

ส่วนเดิมของ skeleton

- Selector `.brand-line2`: คลาส brand-line2
- Declaration `display: none;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L101

```css
  .group-badge { display: none; }
```

ส่วนเดิมของ skeleton

- Selector `.group-badge`: คลาส group-badge
- Declaration `display: none;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L102

```css
}
```

ส่วนเดิมของ skeleton

ปีกกาปิดจบบล็อก `@media max-width 640px` กฎถัดไปจึงอยู่นอกขอบเขตนี้

### L103

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L104

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L105

```css
/* ---------- components you can use on any page ---------- */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L106

```css
/* panel / card */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L107

```css
.panel { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 18px; }
```

ส่วนเดิมของ skeleton

- Selector `.panel`: คลาส panel
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 18px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L108

```css
.two-col { display: grid; grid-template-columns: 2fr 1fr; gap: 18px; align-items: start; }
```

ส่วนเดิมของ skeleton

- Selector `.two-col`: คลาส two-col
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: 2fr 1fr;`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; คอลัมน์ซ้ายประมาณ 2 ส่วน ขวา 1 ส่วน; ค่าที่ใช้จริงคือ `2fr 1fr` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 18px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L109

```css
@media (max-width: 720px) { .two-col { grid-template-columns: 1fr; } }
```

ส่วนเดิมของ skeleton

- Media query `@media (max-width: 720px)`: ใช้กฎด้านในเมื่อ viewport กว้างไม่เกิน 720 CSS px รวมเท่ากับค่านี้; วงเล็บครอบเงื่อนไข ปีกกาครอบกฎ
- Selector `.two-col`: คลาส two-col
- Declaration `grid-template-columns: 1fr;`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; ค่าที่ใช้จริงคือ `1fr` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L110

```css
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
```

ส่วนเดิมของ skeleton

- Selector `.card-grid`: คลาส card-grid
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; auto-fill สร้างช่องจนเต็มพื้นที่ อาจเหลือช่องว่าง; minmax กำหนดขั้นต่ำและ 1fr; ค่าที่ใช้จริงคือ `repeat(auto-fill, minmax(200px, 1fr))` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L111

```css
.item-card { background: var(--card); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; display: flex; flex-direction: column; }
```

ส่วนเดิมของ skeleton

- Selector `.item-card`: คลาส item-card
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L112

```css
.item-card img { width: 100%; height: 140px; object-fit: cover; background: #f1ede8; }
```

ส่วนเดิมของ skeleton

- Selector `.item-card img`: คลาส item-card; แท็ก img; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 140px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `140px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `object-fit: cover;`: cover รักษาสัดส่วนภาพและครอบส่วนเกินให้เต็มกรอบ ไม่ยืดภาพผิดสัดส่วน; ค่าที่ใช้จริงคือ `cover` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #f1ede8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#f1ede8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L113

```css
.item-card .body { padding: 12px 14px; display: flex; flex-direction: column; gap: 4px; flex: 1; }
```

ส่วนเดิมของ skeleton

- Selector `.item-card .body`: คลาส item-card; คลาส body; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `padding: 12px 14px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 12px; ซ้ายขวา 14px; ค่าที่ใช้จริงคือ `12px 14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 4px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L114

```css
.item-card .price { font-weight: 700; color: var(--maroon); font-size: 18px; margin-top: auto; }
```

ส่วนเดิมของ skeleton

- Selector `.item-card .price`: คลาส item-card; คลาส price; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 18px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-top: auto;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `auto` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L115

```css
/* badges & pills */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L116

```css
.badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 12px; font-weight: 600; background: #f1ede8; color: var(--muted); }
```

ส่วนเดิมของ skeleton

- Selector `.badge`: คลาส badge
- Declaration `display: inline-block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `inline-block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 2px 9px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 2px; ซ้ายขวา 9px; ค่าที่ใช้จริงคือ `2px 9px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 999px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `999px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #f1ede8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#f1ede8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L117

```css
.badge.good { background: #e6f5ec; color: #1b6b3a; }
```

ส่วนเดิมของ skeleton

- Selector `.badge.good`: คลาส badge; คลาส good; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #e6f5ec;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#e6f5ec` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #1b6b3a;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#1b6b3a` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L118

```css
.badge.bad { background: #fdecec; color: #9b1c1c; }
```

ส่วนเดิมของ skeleton

- Selector `.badge.bad`: คลาส badge; คลาส bad; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #fdecec;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fdecec` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #9b1c1c;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#9b1c1c` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L119

```css
.badge.gold { background: #fff5d6; color: #8a6100; }
```

ส่วนเดิมของ skeleton

- Selector `.badge.gold`: คลาส badge; คลาส gold; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #fff5d6;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff5d6` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #8a6100;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#8a6100` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L120

```css
.pills { display: flex; gap: 6px; flex-wrap: wrap; margin: 10px 0; }
```

ส่วนเดิมของ skeleton

- Selector `.pills`: คลาส pills
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 6px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `6px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 10px 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บนล่าง 10px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `10px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L121

```css
.pills a { padding: 5px 12px; border-radius: 999px; border: 1px solid var(--line); background: #fff; color: var(--ink); text-decoration: none; font-size: 13px; }
```

ส่วนเดิมของ skeleton

- Selector `.pills a`: คลาส pills; แท็ก a; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `padding: 5px 12px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 5px; ซ้ายขวา 12px; ค่าที่ใช้จริงคือ `5px 12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 999px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `999px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--ink);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --ink; ค่าที่ใช้จริงคือ `var(--ink)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: none;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L122

```css
.pills a.active { background: var(--maroon); border-color: var(--maroon); color: #fff; }
```

ส่วนเดิมของ skeleton

- Selector `.pills a.active`: คลาส pills; คลาส active; แท็ก a; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-color: var(--maroon);`: เปลี่ยนสีเส้นขอบทุกด้านโดยรักษาความหนา/ชนิดเดิม; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L123

```css
/* stat card variants */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L124

```css
.stat.good .value { color: #1b6b3a; }
```

ส่วนเดิมของ skeleton

- Selector `.stat.good .value`: คลาส stat; คลาส good; คลาส value; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `color: #1b6b3a;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#1b6b3a` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L125

```css
.stat.bad .value { color: #9b1c1c; }
```

ส่วนเดิมของ skeleton

- Selector `.stat.bad .value`: คลาส stat; คลาส bad; คลาส value; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `color: #9b1c1c;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#9b1c1c` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L126

```css
.stat.gold { background: #fffbe8; border-color: #f2df9a; }
```

ส่วนเดิมของ skeleton

- Selector `.stat.gold`: คลาส stat; คลาส gold; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #fffbe8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fffbe8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-color: #f2df9a;`: เปลี่ยนสีเส้นขอบทุกด้านโดยรักษาความหนา/ชนิดเดิม; ค่าที่ใช้จริงคือ `#f2df9a` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L127

```css
.stat .unit { color: var(--muted); font-size: 12px; }
```

ส่วนเดิมของ skeleton

- Selector `.stat .unit`: คลาส stat; คลาส unit; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L128

```css
/* horizontal bars: width = percent of the biggest value (compute the % in Python) */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L129

```css
.bar-row { display: grid; grid-template-columns: 120px 1fr 90px; align-items: center; gap: 10px; padding: 6px 0; }
```

ส่วนเดิมของ skeleton

- Selector `.bar-row`: คลาส bar-row
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `grid-template-columns: 120px 1fr 90px;`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; คอลัมน์ชื่อ 120px แถบขยายในพื้นที่เหลือ ตัวเลข 90px; ค่าที่ใช้จริงคือ `120px 1fr 90px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 10px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 6px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 6px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `6px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L130

```css
.bar-track { background: #efeae4; border-radius: 6px; height: 14px; overflow: hidden; }
```

ส่วนเดิมของ skeleton

- Selector `.bar-track`: คลาส bar-track
- Declaration `background: #efeae4;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#efeae4` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 6px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `6px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 14px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L131

```css
.bar-fill { background: var(--maroon); height: 100%; border-radius: 6px; }
```

ส่วนเดิมของ skeleton

- Selector `.bar-fill`: คลาส bar-fill
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 100%;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 6px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `6px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L132

```css
.bar-fill.gold { background: var(--gold); }
```

ส่วนเดิมของ skeleton

- Selector `.bar-fill.gold`: คลาส bar-fill; คลาส gold; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: var(--gold);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L133

```css
.bar-fill.green { background: #2e8b57; }
```

ส่วนเดิมของ skeleton

- Selector `.bar-fill.green`: คลาส bar-fill; คลาส green; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #2e8b57;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#2e8b57` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L134

```css
.bar-row .num { text-align: right; font-variant-numeric: tabular-nums; }
```

ส่วนเดิมของ skeleton

- Selector `.bar-row .num`: คลาส bar-row; คลาส num; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `text-align: right;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `right` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-variant-numeric: tabular-nums;`: tabular-nums ขอรูปแบบเลขความกว้างเท่ากันจากฟอนต์ ช่วยอ่านจำนวนเรียงกัน; ค่าที่ใช้จริงคือ `tabular-nums` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L135

```css
/* progress bar */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L136

```css
.progress { background: #efeae4; border-radius: 999px; height: 12px; overflow: hidden; }
```

ส่วนเดิมของ skeleton

- Selector `.progress`: คลาส progress
- Declaration `background: #efeae4;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#efeae4` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 999px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `999px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 12px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L137

```css
.progress > div { background: var(--gold); height: 100%; border-radius: 999px; }
```

ส่วนเดิมของ skeleton

- Selector `.progress > div`: คลาส progress; แท็ก div; > เลือกลูกโดยตรงเท่านั้น
- Declaration `background: var(--gold);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 100%;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 999px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `999px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L138

```css
/* vertical columns chart: height = percent (compute the % in Python) */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L139

```css
.chart { display: flex; align-items: flex-end; gap: 8px; height: 180px; padding: 8px 0; border-bottom: 1px solid var(--line); }
```

ส่วนเดิมของ skeleton

- Selector `.chart`: คลาส chart
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: flex-end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `flex-end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 8px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 180px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `180px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 8px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 8px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `8px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-bottom: 1px solid var(--line);`: เส้นขอบเฉพาะด้านล่าง; none ยกเลิก; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L140

```css
.chart .col { flex: 1; display: flex; flex-direction: column; justify-content: flex-end; height: 100%; }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col`: คลาส chart; คลาส col; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: flex-end;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `flex-end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 100%;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L141

```css
.chart .col > div { background: var(--maroon); border-radius: 4px 4px 0 0; }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col > div`: คลาส chart; คลาส col; แท็ก div; > เลือกลูกโดยตรงเท่านั้น
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 4px 4px 0 0;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ซ้ายบน/ขวาบน/ขวาล่าง/ซ้ายล่าง 4px / 4px / 0 / 0; ค่าที่ใช้จริงคือ `4px 4px 0 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L142

```css
.chart .col > div.gold { background: var(--gold); }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col > div.gold`: คลาส chart; คลาส col; คลาส gold; แท็ก div; > เลือกลูกโดยตรงเท่านั้น
- Declaration `background: var(--gold);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L143

```css
.chart-labels { display: flex; gap: 8px; }
```

ส่วนเดิมของ skeleton

- Selector `.chart-labels`: คลาส chart-labels
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 8px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L144

```css
.chart-labels span { flex: 1; text-align: center; font-size: 12px; color: var(--muted); }
```

ส่วนเดิมของ skeleton

- Selector `.chart-labels span`: คลาส chart-labels; แท็ก span; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L145

```css
/* buttons */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L146

```css
.btn.small { padding: 4px 10px; font-size: 13px; }
```

ส่วนเดิมของ skeleton

- Selector `.btn.small`: คลาส btn; คลาส small; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `padding: 4px 10px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 4px; ซ้ายขวา 10px; ค่าที่ใช้จริงคือ `4px 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L147

```css
.btn.full { display: block; width: 100%; text-align: center; }
```

ส่วนเดิมของ skeleton

- Selector `.btn.full`: คลาส btn; คลาส full; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L148

```css
.btn.danger { background: #fff; color: #9b1c1c; border-color: #f3b4b4; }
```

ส่วนเดิมของ skeleton

- Selector `.btn.danger`: คลาส btn; คลาส danger; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #9b1c1c;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#9b1c1c` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-color: #f3b4b4;`: เปลี่ยนสีเส้นขอบทุกด้านโดยรักษาความหนา/ชนิดเดิม; ค่าที่ใช้จริงคือ `#f3b4b4` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L149

```css
form.inline { display: inline; }
```

ส่วนเดิมของ skeleton

- Selector `form.inline`: คลาส inline; แท็ก form
- Declaration `display: inline;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `inline` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L150

```css
/* misc */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L151

```css
.kbd { display: inline-block; padding: 2px 8px; border: 1px solid #cbd5e1; border-bottom-width: 3px; border-radius: 6px; background: #fff; font-family: monospace; font-size: 12px; }
```

ส่วนเดิมของ skeleton

- Selector `.kbd`: คลาส kbd
- Declaration `display: inline-block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `inline-block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 2px 8px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 2px; ซ้ายขวา 8px; ค่าที่ใช้จริงคือ `2px 8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid #cbd5e1;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid #cbd5e1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-bottom-width: 3px;`: ความหนาเฉพาะเส้นขอบล่าง; ค่าที่ใช้จริงคือ `3px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 6px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `6px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-family: monospace;`: รายชื่อฟอนต์สำรองเรียงลำดับ ไม่มีการดาวน์โหลดฟอนต์จาก property นี้; inherit รับจากแม่; monospace คือตัวกว้างเท่ากัน; ค่าที่ใช้จริงคือ `monospace` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L152

```css
.hero-box { background: linear-gradient(135deg, #fff, #f7efe9); border: 1px solid var(--line); border-radius: 14px; padding: 24px; margin-bottom: 18px; }
```

ส่วนเดิมของ skeleton

- Selector `.hero-box`: คลาส hero-box
- Declaration `background: linear-gradient(135deg, #fff, #f7efe9);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ไล่สีตามองศาและจุดสี/% เรียงในวงเล็บ; ค่าที่ใช้จริงคือ `linear-gradient(135deg, #fff, #f7efe9)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 14px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 24px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `24px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 18px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L153

```css
.note { font-size: 13px; color: var(--muted); }
```

ส่วนเดิมของ skeleton

- Selector `.note`: คลาส note
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L154

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L155

```css
/* stacked columns: put several <div class="seg"> inside a .col, heights in % of the column */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L156

```css
.chart .col .seg { width: 100%; }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col .seg`: คลาส chart; คลาส col; คลาส seg; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L157

```css
.chart .col .seg.gold { background: var(--gold); }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col .seg.gold`: คลาส chart; คลาส col; คลาส seg; คลาส gold; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: var(--gold);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L158

```css
.chart .col .seg.green { background: #2e8b57; }
```

ส่วนเดิมของ skeleton

- Selector `.chart .col .seg.green`: คลาส chart; คลาส col; คลาส seg; คลาส green; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `background: #2e8b57;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#2e8b57` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L159

```css
/* donut: style="--p: 42" (percent) */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L160

```css
.donut { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0); display: flex; align-items: center; justify-content: center; }
```

ส่วนเดิมของ skeleton

- Selector `.donut`: คลาส donut
- Declaration `width: 120px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `120px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 120px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `120px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 50%;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `50%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon, --p; สีแรกกินวงตาม --p×1% สี #efeae4 เป็นส่วนที่เหลือ โดย donut ไม่ได้ถูกใช้ในหน้า 1–3 ปัจจุบัน; ค่าที่ใช้จริงคือ `conic-gradient(var(--maroon) calc(var(--p) * 1%), #efeae4 0)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: center;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L161

```css
.donut > span { width: 78px; height: 78px; border-radius: 50%; background: var(--card); display: flex; align-items: center; justify-content: center; font-weight: 700; color: var(--maroon); }
```

ส่วนเดิมของ skeleton

- Selector `.donut > span`: คลาส donut; แท็ก span; > เลือกลูกโดยตรงเท่านั้น
- Declaration `width: 78px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `78px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 78px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `78px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 50%;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `50%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: center;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L162

```css
/* small things forms and summaries keep needing */
```

ส่วนเดิมของ skeleton

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L163

```css
.thumb { width: 56px; height: 56px; object-fit: cover; border-radius: 8px; background: #f1ede8; }
```

ส่วนเดิมของ skeleton

- Selector `.thumb`: คลาส thumb
- Declaration `width: 56px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 56px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `56px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `object-fit: cover;`: cover รักษาสัดส่วนภาพและครอบส่วนเกินให้เต็มกรอบ ไม่ยืดภาพผิดสัดส่วน; ค่าที่ใช้จริงคือ `cover` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 8px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #f1ede8;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#f1ede8` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L164

```css
.field-row { display: flex; gap: 14px; flex-wrap: wrap; align-items: flex-end; }
```

ส่วนเดิมของ skeleton

- Selector `.field-row`: คลาส field-row
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 14px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: flex-end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `flex-end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L165

```css
.field-row .field { margin: 0; }
```

ส่วนเดิมของ skeleton

- Selector `.field-row .field`: คลาส field-row; คลาส field; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L166

```css
.sum-row { display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--line); }
```

ส่วนเดิมของ skeleton

- Selector `.sum-row`: คลาส sum-row
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 6px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 6px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `6px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-bottom: 1px solid var(--line);`: เส้นขอบเฉพาะด้านล่าง; none ยกเลิก; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L167

```css
.sum-row.total { border: 0; font-size: 18px; font-weight: 700; color: var(--maroon); }
```

ส่วนเดิมของ skeleton

- Selector `.sum-row.total`: คลาส sum-row; คลาส total; คลาสติดกันต้องอยู่ใน element เดียว
- Declaration `border: 0;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 18px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L168

```css
.game-board { display: block; margin: 0 auto; background: #1f2933; border: 4px solid var(--maroon); border-radius: 10px; }
```

ส่วนเดิมของ skeleton

- Selector `.game-board`: คลาส game-board
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0 auto;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บนล่าง 0; ซ้ายขวา auto; ค่าที่ใช้จริงคือ `0 auto` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #1f2933;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#1f2933` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 4px solid var(--maroon);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `4px solid var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L169

```css
.hud { display: flex; gap: 10px; justify-content: center; margin: 10px 0; }
```

ส่วนเดิมของ skeleton

- Selector `.hud`: คลาส hud
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 10px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: center;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 10px 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บนล่าง 10px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `10px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L170

```css

```

ส่วนเดิมของ skeleton

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L171

```css
/* ---------- your own styles below ---------- */
```

marker แบ่งส่วน

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L172

```css

```

ส่วนเพิ่ม Deadline Compass

บรรทัดว่างแบ่งกลุ่มให้อ่านง่าย ไม่มีผลสร้างกฎใหม่

### L173

```css
/* Deadline Compass: page styles added without changing the given components. */
```

ส่วนเพิ่ม Deadline Compass

Comment อธิบายชื่อกลุ่ม/การใช้งาน component ตามข้อความต้นฉบับ Browser ข้ามข้อความระหว่าง /* กับ */ ไม่เป็นคำสั่งตกแต่ง

### L174

```css
.deadline-eyebrow { display: inline-block; color: var(--maroon); font-size: 12px; font-weight: 800; letter-spacing: .13em; text-transform: uppercase; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-eyebrow`: คลาส deadline-eyebrow
- Declaration `display: inline-block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `inline-block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 800;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `800` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `letter-spacing: .13em;`: ช่องเพิ่มระหว่างอักขระ; em เทียบขนาดฟอนต์ปัจจุบัน; ค่าที่ใช้จริงคือ `.13em` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-transform: uppercase;`: uppercase แสดงตัวอักษรที่มีรูปพิมพ์ใหญ่ เช่นอังกฤษ เป็นพิมพ์ใหญ่ ไม่เปลี่ยนต้นฉบับใน DOM; ค่าที่ใช้จริงคือ `uppercase` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L175

```css
.deadline-hero { display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 32px; margin-bottom: 20px; border: 1px solid #ead8cf; border-radius: 18px; background: linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%); overflow: hidden; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero`: คลาส deadline-hero
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 24px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `24px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 32px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; ค่าที่ใช้จริงคือ `32px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 20px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid #ead8cf;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid #ead8cf` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 18px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ไล่สีตามองศาและจุดสี/% เรียงในวงเล็บ; ค่าที่ใช้จริงคือ `linear-gradient(115deg, #fffaf4 0%, #f8ece5 68%, #f4e0d4 100%)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L176

```css
.deadline-hero h1 { font-size: clamp(27px, 4vw, 40px); line-height: 1.2; margin: 8px 0 10px; color: var(--maroon-dark); }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero h1`: คลาส deadline-hero; แท็ก h1; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-size: clamp(27px, 4vw, 40px);`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ต่ำสุด 27px ค่ากลาง 4% ความกว้าง viewport สูงสุด 40px; ค่าที่ใช้จริงคือ `clamp(27px, 4vw, 40px)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `line-height: 1.2;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `1.2` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 8px 0 10px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 8px; ซ้ายขวา 0; ล่าง 10px; ค่าที่ใช้จริงคือ `8px 0 10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon-dark);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon-dark; ค่าที่ใช้จริงคือ `var(--maroon-dark)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L177

```css
.deadline-hero p { max-width: 480px; margin: 0 0 20px; color: #5d5552; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero p`: คลาส deadline-hero; แท็ก p; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `max-width: 480px;`: ขอบบนของความกว้าง; none ยกเลิกเพดานความกว้างเดิม; ค่าที่ใช้จริงคือ `480px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0 0 20px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 0; ซ้ายขวา 0; ล่าง 20px; ค่าที่ใช้จริงคือ `0 0 20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #5d5552;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#5d5552` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L178

```css
.deadline-hero .btn { margin: 0 7px 7px 0; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero .btn`: คลาส deadline-hero; คลาส btn; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0 7px 7px 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน/ขวา/ล่าง/ซ้าย 0 / 7px / 7px / 0; ค่าที่ใช้จริงคือ `0 7px 7px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L179

```css
.deadline-hero-mark { flex: 0 0 170px; width: 170px; height: 170px; transform: rotate(9deg); border: 9px solid var(--maroon); border-radius: 22px; background: #fff; box-shadow: 16px 16px 0 rgba(122,31,43,.11); text-align: center; overflow: hidden; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero-mark`: คลาส deadline-hero-mark
- Declaration `flex: 0 0 170px;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; grow=0 shrink=0 basis=170px; ค่าที่ใช้จริงคือ `0 0 170px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `width: 170px;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `170px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 170px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `170px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `transform: rotate(9deg);`: แปลงตำแหน่ง/หมุนภาพโดยไม่จัด layout ฐานใหม่: translateY(-2px) ยก 2px; rotate(9deg) หมุน 9 องศา; ค่าที่ใช้จริงคือ `rotate(9deg)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 9px solid var(--maroon);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `9px solid var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 22px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `22px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: #fff;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `box-shadow: 16px 16px 0 rgba(122,31,43,.11);`: เงากล่อง อ่านเป็น x y ความฟุ้ง และสี rgba ตามลำดับ; ค่าที่ใช้จริงคือ `16px 16px 0 rgba(122,31,43,.11)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `overflow: hidden;`: hidden ตัดส่วนที่ล้นกล่องจากการแสดงผล ไม่ลบข้อมูลจาก DOM; ค่าที่ใช้จริงคือ `hidden` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L180

```css
.deadline-hero-mark span:first-child { display: block; height: 40px; background: var(--maroon); color: white; font-size: 26px; line-height: 32px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero-mark span:first-child`: คลาส deadline-hero-mark; แท็ก span; สถานะ/ตำแหน่ง :first-child ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 40px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `40px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: white;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `white` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 26px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `26px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `line-height: 32px;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `32px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L181

```css
.deadline-hero-mark span:last-child { display: block; color: var(--maroon); font-size: 76px; font-weight: 800; line-height: 115px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero-mark span:last-child`: คลาส deadline-hero-mark; แท็ก span; สถานะ/ตำแหน่ง :last-child ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 76px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `76px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 800;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `800` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `line-height: 115px;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `115px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L182

```css
.deadline-summary { margin: 16px 0 24px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-summary`: คลาส deadline-summary
- Declaration `margin: 16px 0 24px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 16px; ซ้ายขวา 0; ล่าง 24px; ค่าที่ใช้จริงคือ `16px 0 24px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L183

```css
.deadline-summary .stat { box-shadow: 0 5px 18px rgba(31,41,51,.035); }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-summary .stat`: คลาส deadline-summary; คลาส stat; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `box-shadow: 0 5px 18px rgba(31,41,51,.035);`: เงากล่อง อ่านเป็น x y ความฟุ้ง และสี rgba ตามลำดับ; ค่าที่ใช้จริงคือ `0 5px 18px rgba(31,41,51,.035)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L184

```css
.deadline-summary .value { font-variant-numeric: tabular-nums; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-summary .value`: คลาส deadline-summary; คลาส value; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-variant-numeric: tabular-nums;`: tabular-nums ขอรูปแบบเลขความกว้างเท่ากันจากฟอนต์ ช่วยอ่านจำนวนเรียงกัน; ค่าที่ใช้จริงคือ `tabular-nums` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L185

```css
.deadline-alert { background: #fdecec; border: 1px solid #eab4b4; color: #802020; border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; font-weight: 600; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-alert`: คลาส deadline-alert
- Declaration `background: #fdecec;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `#fdecec` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid #eab4b4;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `1px solid #eab4b4` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #802020;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#802020` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 10px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 12px 16px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 12px; ซ้ายขวา 16px; ค่าที่ใช้จริงคือ `12px 16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-bottom: 18px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 600;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `600` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L186

```css
.deadline-section-head { display: flex; align-items: end; justify-content: space-between; gap: 16px; margin: 22px 0 12px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-section-head`: คลาส deadline-section-head
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 16px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 22px 0 12px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 22px; ซ้ายขวา 0; ล่าง 12px; ค่าที่ใช้จริงคือ `22px 0 12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L187

```css
.deadline-section-head h2 { margin: 0 0 2px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-section-head h2`: คลาส deadline-section-head; แท็ก h2; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0 0 2px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 0; ซ้ายขวา 0; ล่าง 2px; ค่าที่ใช้จริงคือ `0 0 2px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L188

```css
.deadline-section-head .note { margin: 0; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-section-head .note`: คลาส deadline-section-head; คลาส note; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L189

```css
.deadline-reminder-control { display: flex; flex-direction: column; align-items: end; gap: 4px; text-align: right; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-reminder-control`: คลาส deadline-reminder-control
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 4px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: right;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `right` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L190

```css
.deadline-task-list { display: grid; gap: 10px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task-list`: คลาส deadline-task-list
- Declaration `display: grid;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `grid` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 10px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L191

```css
.deadline-task { display: flex; align-items: center; justify-content: space-between; gap: 20px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px 18px; box-shadow: 0 3px 12px rgba(31,41,51,.025); }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task`: คลาส deadline-task
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: center;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 20px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--card);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --card; ค่าที่ใช้จริงคือ `var(--card)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 1px solid var(--line);`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 16px 18px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 16px; ซ้ายขวา 18px; ค่าที่ใช้จริงคือ `16px 18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `box-shadow: 0 3px 12px rgba(31,41,51,.025);`: เงากล่อง อ่านเป็น x y ความฟุ้ง และสี rgba ตามลำดับ; ค่าที่ใช้จริงคือ `0 3px 12px rgba(31,41,51,.025)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L192

```css
.deadline-task-main { min-width: 0; flex: 1; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task-main`: คลาส deadline-task-main
- Declaration `min-width: 0;`: ความกว้างขั้นต่ำ; 0 อนุญาตลูก flex/grid หดต่ำกว่าความกว้างเนื้อหาขั้นต้น ช่วยลดปัญหาล้น; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L193

```css
.deadline-course { color: var(--maroon); font-size: 12px; font-weight: 700; letter-spacing: .035em; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-course`: คลาส deadline-course
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `letter-spacing: .035em;`: ช่องเพิ่มระหว่างอักขระ; em เทียบขนาดฟอนต์ปัจจุบัน; ค่าที่ใช้จริงคือ `.035em` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L194

```css
.deadline-task h3, .deadline-edit-card h3 { margin: 2px 0 5px; font-size: 17px; line-height: 1.3; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task h3`: คลาส deadline-task; แท็ก h3; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.deadline-edit-card h3`: คลาส deadline-edit-card; แท็ก h3; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 2px 0 5px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 2px; ซ้ายขวา 0; ล่าง 5px; ค่าที่ใช้จริงคือ `2px 0 5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 17px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `17px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `line-height: 1.3;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `1.3` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L195

```css
.deadline-meta { color: var(--muted); font-size: 13px; margin: 0; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-meta`: คลาส deadline-meta
- Declaration `color: var(--muted);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --muted; ค่าที่ใช้จริงคือ `var(--muted)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L196

```css
.deadline-progress { width: min(100%, 360px); margin-top: 12px; height: 8px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-progress`: คลาส deadline-progress
- Declaration `width: min(100%, 360px);`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; เลือกค่าน้อยกว่าระหว่างเต็มกล่องกับ 360px; ค่าที่ใช้จริงคือ `min(100%, 360px)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-top: 12px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `height: 8px;`: ความสูง; 100% อ้างความสูงแม่เมื่อมีฐานคำนวณได้; ค่าที่ใช้จริงคือ `8px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L197

```css
.deadline-task-actions { display: flex; flex-direction: column; align-items: end; gap: 9px; flex-shrink: 0; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task-actions`: คลาส deadline-task-actions
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 9px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `9px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-shrink: 0;`: 0 ห้าม item นี้หดเมื่อพื้นที่ flex ไม่พอ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L198

```css
.deadline-text-button { background: transparent; border: 0; padding: 2px 0; color: var(--maroon); text-decoration: underline; font: inherit; font-size: 12px; cursor: pointer; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-text-button`: คลาส deadline-text-button
- Declaration `background: transparent;`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; ค่าที่ใช้จริงคือ `transparent` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border: 0;`: เส้นขอบทุกด้าน: ความหนา ชนิดเส้น สี; none/0 ยกเลิกเส้นตามรูปแบบคำสั่ง; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 2px 0;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 2px; ซ้ายขวา 0; ค่าที่ใช้จริงคือ `2px 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-decoration: underline;`: none เอาเส้นตกแต่งออก; underline ใส่เส้นใต้เพื่อสื่อว่ากดได้; ค่าที่ใช้จริงคือ `underline` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font: inherit;`: shorthand ชุดคุณสมบัติฟอนต์; inherit รับจากแม่ ก่อน font-size ที่ตามมาจะกำหนดขนาดเฉพาะใหม่; ค่าที่ใช้จริงคือ `inherit` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 12px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `cursor: pointer;`: pointer เปลี่ยนตัวชี้เมาส์เป็นมือเหนือสิ่งกดได้; ค่าที่ใช้จริงคือ `pointer` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L199

```css
.deadline-footnote { margin-top: 15px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-footnote`: คลาส deadline-footnote
- Declaration `margin-top: 15px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `15px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L200

```css
.deadline-page-title { margin: 2px 0 22px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-page-title`: คลาส deadline-page-title
- Declaration `margin: 2px 0 22px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 2px; ซ้ายขวา 0; ล่าง 22px; ค่าที่ใช้จริงคือ `2px 0 22px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L201

```css
.deadline-page-title h1 { margin-top: 5px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-page-title h1`: คลาส deadline-page-title; แท็ก h1; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin-top: 5px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `5px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L202

```css
.deadline-form-layout { grid-template-columns: minmax(255px, .85fr) minmax(0, 1.4fr); }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-form-layout`: คลาส deadline-form-layout
- Declaration `grid-template-columns: minmax(255px, .85fr) minmax(0, 1.4fr);`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; ซ้ายขั้นต่ำ 255px รับ .85 ส่วน ขวาขั้นต่ำ 0 รับ 1.4 ส่วน; ค่าที่ใช้จริงคือ `minmax(255px, .85fr) minmax(0, 1.4fr)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L203

```css
.deadline-add-form { position: sticky; top: 16px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-add-form`: คลาส deadline-add-form
- Declaration `position: sticky;`: sticky เลื่อนจนถึงขอบกำหนดแล้วติดภายในขอบเขตกล่องครอบ; static กลับตำแหน่งปกติ; ค่าที่ใช้จริงคือ `sticky` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `top: 16px;`: ระยะจากขอบบนใน positioning; sticky ใช้ 16px เป็นระยะยึดจากขอบบน; ค่าที่ใช้จริงคือ `16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L204

```css
.deadline-add-form h2 { margin: 0 0 18px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-add-form h2`: คลาส deadline-add-form; แท็ก h2; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0 0 18px;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 0; ซ้ายขวา 0; ล่าง 18px; ค่าที่ใช้จริงคือ `0 0 18px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L205

```css
.deadline-add-form .field input { max-width: none; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-add-form .field input`: คลาส deadline-add-form; คลาส field; แท็ก input; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `max-width: none;`: ขอบบนของความกว้าง; none ยกเลิกเพดานความกว้างเดิม; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L206

```css
.deadline-edit-card { margin-bottom: 10px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-card`: คลาส deadline-edit-card
- Declaration `margin-bottom: 10px;`: ระยะนอกด้านล่าง; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L207

```css
.deadline-edit-heading { display: flex; justify-content: space-between; align-items: start; gap: 12px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-heading`: คลาส deadline-edit-heading
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `justify-content: space-between;`: จัดลูกตามแกนหลักของ flex หรือ inline axis ของ grid: space-between กระจายระหว่างรายการ, center กลาง, flex-end ท้ายแกน; ค่าที่ใช้จริงคือ `space-between` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 12px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L208

```css
.deadline-edit-card details { border-top: 1px solid var(--line); margin-top: 12px; padding-top: 10px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-card details`: คลาส deadline-edit-card; แท็ก details; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `border-top: 1px solid var(--line);`: เส้นขอบเฉพาะด้านบน; อ่านตัวแปร --line; ค่าที่ใช้จริงคือ `1px solid var(--line)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `margin-top: 12px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding-top: 10px;`: ระยะว่างภายในเฉพาะด้านบน; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L209

```css
.deadline-edit-card summary { color: var(--maroon); cursor: pointer; font-size: 13px; font-weight: 700; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-card summary`: คลาส deadline-edit-card; แท็ก summary; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `color: var(--maroon);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `cursor: pointer;`: pointer เปลี่ยนตัวชี้เมาส์เป็นมือเหนือสิ่งกดได้; ค่าที่ใช้จริงคือ `pointer` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-weight: 700;`: น้ำหนักตัวอักษร normal ปกติ 600 กึ่งหนา 700 หนา 800 หนามาก ขึ้นกับฟอนต์ที่มีจริง; ค่าที่ใช้จริงคือ `700` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L210

```css
.deadline-edit-form { margin-top: 16px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-form`: คลาส deadline-edit-form
- Declaration `margin-top: 16px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `16px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L211

```css
.deadline-edit-form .field { flex: 1; min-width: 120px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-form .field`: คลาส deadline-edit-form; คลาส field; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `flex: 1;`: การโต/หด/ฐานของ flex item; flex:1 รับพื้นที่ว่างตามส่วนแบ่งพร้อมฐานเริ่มต้นศูนย์ตาม shorthand; ค่าที่ใช้จริงคือ `1` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `min-width: 120px;`: ความกว้างขั้นต่ำ; 0 อนุญาตลูก flex/grid หดต่ำกว่าความกว้างเนื้อหาขั้นต้น ช่วยลดปัญหาล้น; ค่าที่ใช้จริงคือ `120px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L212

```css
.deadline-edit-form .field input { width: 100%; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-form .field input`: คลาส deadline-edit-form; คลาส field; แท็ก input; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L213

```css
.deadline-delete-form { margin-top: 14px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-delete-form`: คลาส deadline-delete-form
- Declaration `margin-top: 14px;`: ระยะนอกด้านบน; auto ใน flex column รับที่ว่างและผลักส่วนนี้ลงล่าง; ค่าที่ใช้จริงคือ `14px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L214

```css
.deadline-hours-form { display: flex; flex-wrap: wrap; align-items: end; gap: 12px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hours-form`: คลาส deadline-hours-form
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `align-items: end;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `end` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 12px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L215

```css
.deadline-hours-form .field { margin: 0; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hours-form .field`: คลาส deadline-hours-form; คลาส field; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `margin: 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; ค่าที่ใช้จริงคือ `0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L216

```css
.deadline-hours-form input { max-width: 210px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hours-form input`: คลาส deadline-hours-form; แท็ก input; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `max-width: 210px;`: ขอบบนของความกว้าง; none ยกเลิกเพดานความกว้างเดิม; ค่าที่ใช้จริงคือ `210px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L217

```css
.deadline-focus { display: flex; flex-direction: column; gap: 4px; padding: 20px 22px; border-radius: 12px; background: var(--maroon); color: #fff; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-focus`: คลาส deadline-focus
- Declaration `display: flex;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `flex` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 4px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `4px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `padding: 20px 22px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 20px; ซ้ายขวา 22px; ค่าที่ใช้จริงคือ `20px 22px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `border-radius: 12px;`: รัศมีมุมโค้ง; 999px ทำทรงแคปซูล; 50% ในกรอบจัตุรัสเป็นวงกลม; สี่ค่าเรียงซ้ายบน ขวาบน ขวาล่าง ซ้ายล่าง; ค่าที่ใช้จริงคือ `12px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `background: var(--maroon);`: พื้นหลังสีหรือ gradient; transparent ทำพื้นโปร่งใส; อ่านตัวแปร --maroon; ค่าที่ใช้จริงคือ `var(--maroon)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: #fff;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#fff` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L218

```css
.deadline-focus .deadline-eyebrow { color: #ffdc75; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-focus .deadline-eyebrow`: คลาส deadline-focus; คลาส deadline-eyebrow; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `color: #ffdc75;`: สีตัวอักษรหรือ currentColor ของ element; ค่าที่ใช้จริงคือ `#ffdc75` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L219

```css
.deadline-focus strong { font-size: 22px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-focus strong`: คลาส deadline-focus; แท็ก strong; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-size: 22px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `22px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L220

```css
.deadline-focus span:last-child { font-size: 13px; opacity: .9; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-focus span:last-child`: คลาส deadline-focus; แท็ก span; สถานะ/ตำแหน่ง :last-child ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `opacity: .9;`: ความทึบทั้ง element และเนื้อหาลูก 1 ทึบเต็ม ค่าน้อยลงยิ่งโปร่ง; ค่าที่ใช้จริงคือ `.9` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L221

```css
.deadline-plan-detail { margin: 9px 0 0; font-size: 13px; color: var(--ink); }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-plan-detail`: คลาส deadline-plan-detail
- Declaration `margin: 9px 0 0;`: ช่องว่างนอกกรอบ อ่านลำดับค่าตามพจนานุกรม; auto แนวนอนแบ่งพื้นที่ว่างสองข้างเพื่อจัดกลางเมื่อเงื่อนไขรองรับ; บน 9px; ซ้ายขวา 0; ล่าง 0; ค่าที่ใช้จริงคือ `9px 0 0` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `font-size: 13px;`: ขนาดฟอนต์ px คงที่หรือ clamp ปรับตาม viewport ภายในขอบเขต; ค่าที่ใช้จริงคือ `13px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `color: var(--ink);`: สีตัวอักษรหรือ currentColor ของ element; อ่านตัวแปร --ink; ค่าที่ใช้จริงคือ `var(--ink)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L222

```css
.deadline-home-hero { min-height: 260px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-home-hero`: คลาส deadline-home-hero
- Declaration `min-height: 260px;`: ความสูงขั้นต่ำ; 100vh อย่างน้อยเท่าความสูง viewport; ค่าที่ใช้จริงคือ `260px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L223

```css
.deadline-home-cards .card { min-height: 132px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-home-cards .card`: คลาส deadline-home-cards; คลาส card; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `min-height: 132px;`: ความสูงขั้นต่ำ; 100vh อย่างน้อยเท่าความสูง viewport; ค่าที่ใช้จริงคือ `132px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L224

```css
.deadline-home-cards .card-title { line-height: 1.35; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-home-cards .card-title`: คลาส deadline-home-cards; คลาส card-title; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `line-height: 1.35;`: ความสูงแต่ละบรรทัด ถ้าไม่มีหน่วยคูณ font-size แต่ px เป็นค่าคงที่; ค่าที่ใช้จริงคือ `1.35` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L225

```css
.deadline-task :focus-visible, .deadline-edit-card :focus-visible, .deadline-hero :focus-visible, .deadline-hours-form :focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task :focus-visible`: คลาส deadline-task; สถานะ/ตำแหน่ง :focus-visible ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.deadline-edit-card :focus-visible`: คลาส deadline-edit-card; สถานะ/ตำแหน่ง :focus-visible ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.deadline-hero :focus-visible`: คลาส deadline-hero; สถานะ/ตำแหน่ง :focus-visible ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Selector `.deadline-hours-form :focus-visible`: คลาส deadline-hours-form; สถานะ/ตำแหน่ง :focus-visible ตามพจนานุกรม; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `outline: 3px solid var(--gold);`: เส้นเน้นรอบ element เช่นการ focus ไม่เพิ่มขนาดกล่องเหมือน border; อ่านตัวแปร --gold; ค่าที่ใช้จริงคือ `3px solid var(--gold)` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `outline-offset: 3px;`: ระยะห่างเส้น outline ออกจากกรอบ element; ค่าที่ใช้จริงคือ `3px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L226

```css
@media (max-width: 720px) {
```

ส่วนเพิ่ม Deadline Compass

- Media query `@media (max-width: 720px)`: ใช้กฎด้านในเมื่อ viewport กว้างไม่เกิน 720 CSS px รวมเท่ากับค่านี้; วงเล็บครอบเงื่อนไข ปีกกาครอบกฎ

### L227

```css
  .deadline-form-layout { grid-template-columns: 1fr; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-form-layout`: คลาส deadline-form-layout
- Declaration `grid-template-columns: 1fr;`: กำหนดคอลัมน์ของ Grid ทั้งขนาด สัดส่วน หรือจำนวนซ้ำตาม repeat/minmax ในพจนานุกรม; ค่าที่ใช้จริงคือ `1fr` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L228

```css
  .deadline-add-form { position: static; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-add-form`: คลาส deadline-add-form
- Declaration `position: static;`: sticky เลื่อนจนถึงขอบกำหนดแล้วติดภายในขอบเขตกล่องครอบ; static กลับตำแหน่งปกติ; ค่าที่ใช้จริงคือ `static` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L229

```css
}
```

ส่วนเพิ่ม Deadline Compass

ปีกกาปิดจบบล็อก `@media max-width 720px` กฎถัดไปจึงอยู่นอกขอบเขตนี้

### L230

```css
@media (max-width: 640px) {
```

ส่วนเพิ่ม Deadline Compass

- Media query `@media (max-width: 640px)`: ใช้กฎด้านในเมื่อ viewport กว้างไม่เกิน 640 CSS px รวมเท่ากับค่านี้; วงเล็บครอบเงื่อนไข ปีกกาครอบกฎ

### L231

```css
  .deadline-hero { padding: 24px 20px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero`: คลาส deadline-hero
- Declaration `padding: 24px 20px;`: ระยะว่างภายในกรอบ ดูลำดับค่าบนขวาล่างซ้ายตามพจนานุกรม; บนล่าง 24px; ซ้ายขวา 20px; ค่าที่ใช้จริงคือ `24px 20px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L232

```css
  .deadline-hero-mark { display: none; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero-mark`: คลาส deadline-hero-mark
- Declaration `display: none;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `none` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L233

```css
  .deadline-hero .btn { display: block; width: 100%; text-align: center; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-hero .btn`: คลาส deadline-hero; คลาส btn; ช่องว่างเลือกตัวท้ายที่เป็นลูกหลานของส่วนหน้าในระดับใดก็ได้
- Declaration `display: block;`: รูปแบบกล่อง: flex ใช้ Flexbox; grid ใช้ Grid; block เป็นบล็อก; inline-block เป็นกล่องในบรรทัด; inline อยู่แนวข้อความ; none ซ่อนไม่ใช้พื้นที่แสดงผล; ค่าที่ใช้จริงคือ `block` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `width: 100%;`: ความกว้างกล่อง; 100% เทียบ containing block; px เป็น CSS pixels; ค่าที่ใช้จริงคือ `100%` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: center;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `center` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L234

```css
  .deadline-section-head { align-items: start; flex-direction: column; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-section-head`: คลาส deadline-section-head
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L235

```css
  .deadline-reminder-control { align-items: start; text-align: left; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-reminder-control`: คลาส deadline-reminder-control
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `text-align: left;`: จัดข้อความ/inline content: left ซ้าย right ขวา center กลาง; ค่าที่ใช้จริงคือ `left` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L236

```css
  .deadline-task { align-items: start; flex-direction: column; gap: 10px; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task`: คลาส deadline-task
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `gap: 10px;`: ช่องว่างระหว่างลูก flex/grid ไม่เพิ่มพื้นที่ขอบนอกของกลุ่ม; ค่าที่ใช้จริงคือ `10px` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L237

```css
  .deadline-task-actions { align-items: start; flex-direction: row; flex-wrap: wrap; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-task-actions`: คลาส deadline-task-actions
- Declaration `align-items: start;`: จัดลูกตามแกนขวางของ flex หรือแนว block ของ grid: center กลาง, start/end ขอบเริ่ม/ท้าย, flex-end ท้ายแกนขวาง; ค่าที่ใช้จริงคือ `start` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-direction: row;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `row` อ่านหน่วยและเครื่องหมายตามพจนานุกรม
- Declaration `flex-wrap: wrap;`: wrap ให้ flex item ขึ้นแถวใหม่เมื่อพื้นที่ไม่พอ; ค่าที่ใช้จริงคือ `wrap` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L238

```css
  .deadline-edit-heading { flex-direction: column; }
```

ส่วนเพิ่ม Deadline Compass

- Selector `.deadline-edit-heading`: คลาส deadline-edit-heading
- Declaration `flex-direction: column;`: ทิศแกนหลัก flex: column บนลงล่าง; row แนวนอนตามทิศภาษา; ค่าที่ใช้จริงคือ `column` อ่านหน่วยและเครื่องหมายตามพจนานุกรม

### L239

```css
}
```

ส่วนเพิ่ม Deadline Compass

ปีกกาปิดจบบล็อก `@media max-width 640px` กฎถัดไปจึงอยู่นอกขอบเขตนี้

## คำถาม Frontend ที่ควรซ้อมตอบ

**HTML กับ Python แบ่งงานกันอย่างไร?**  
Python อ่าน/คำนวณแล้วส่ง dict ให้ template Jinja แทรกค่าตามจุด HTML บอกโครงสร้าง CSS ตกแต่ง เช่น progress=50 จาก Python กลายเป็น width:50% ของแถบใน HTML

**ทำไมหน้า 2 มีหลาย form?**  
เพิ่ม แก้ไข และลบเป็นคำสั่งแยกกัน ส่ง hidden action คนละค่า ฟอร์มลบไม่ผูกกับ required ของฟอร์มแก้ไขเพราะเป็นคนละ form และ form เหล่านี้ไม่ซ้อนกัน

**hidden input ถือว่าปลอดภัยหรือไม่?**  
ซ่อนจากหน้าจอปกติ แต่แก้ใน request ได้ จึงต้องตรวจฝั่ง Python และ no ยังเป็นตำแหน่งแถว ไม่ใช่ ID ถาวร

**ทำไมงานบางชิ้นไม่มีปุ่มปฏิทิน?**  
แสดงเฉพาะชิ้นที่ remaining_hours > 0 และ days_left >= 0 งานเสร็จแล้วและงานเกินกำหนดจึงไม่มีปุ่มนั้น

**aria ช่วยอะไร?**  
เพิ่มข้อมูลให้เทคโนโลยีช่วยอ่าน เช่นชื่อและเปอร์เซ็นต์ของแถบความคืบหน้า ข้ามรูปตกแต่ง และประกาศข้อความที่เปลี่ยนตาม aria-live ไม่ใช่โค้ดที่เปิด Notification เอง

**เลข 28 มาจากไหน?**  
เป็นข้อความตกแต่งที่เขียนคงที่ วันส่งจริงอ่าน item.due_date หรือ task.due_date ไม่อธิบายว่า 28 คือวันปัจจุบัน

**เหตุใดไม่ติดตั้ง UI framework เพิ่ม?**  
โครงงานมี CSS component มาให้และข้อกำหนดห้ามเพิ่ม package จึงใช้ CSS เดิมร่วมกับ deadline-* ที่ท้ายไฟล์

**ปิดเว็บแล้ว browser เตือนต่อได้หรือไม่?**  
สคริปต์ทำงานในหน้า 1 ที่เปิดอยู่ ไม่มี background push ใน template ชุดนี้ การเตือนหลังปิดเว็บใช้ไฟล์ที่นำเข้าแอปปฏิทินและขึ้นกับแอปนั้น

**ค่าที่กรอกกับ min/max ของ HTML รับประกันข้อมูลถูกต้องหรือไม่?**  
HTML ช่วยผู้ใช้ทั่วไป แต่สามารถส่ง request ข้ามได้ Python จึงตรวจตัวเลข วันที่ ความยาว และความสัมพันธ์ของชั่วโมงซ้ำ

**รูปแบบมือถือทำอย่างไร?**  
ใช้ media query ที่ 720px และ 640px เปลี่ยนคอลัมน์และทิศ flex บางกลุ่ม รวมถึงซ่อนปฏิทินตกแต่ง ออกแบบให้เนื้อหาอ่านต่อได้โดยไม่ติดตั้งแพ็กเกจ

## การรักษาความตรงกันของเอกสาร

เอกสารบันทึก snippet ทุกบรรทัดของ source ขณะอ่าน พร้อม SHA-256 หากแก้ source ในอนาคต ต้องปรับหมายเลขและคำอธิบายที่เกี่ยวข้อง ไม่ควรใช้ผลทดสอบเก่าเป็นหลักฐานว่า source ใหม่ผ่านแล้ว การจัดทำเอกสารนี้ไม่ได้รันหรือเปลี่ยนชุดทดสอบอาจารย์
