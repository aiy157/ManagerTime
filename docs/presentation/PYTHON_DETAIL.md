# คำอธิบาย Python ทุกบรรทัด

เอกสารนี้อธิบาย source จริงของ models.py และ page1.py ถึง page3.py ครบทุก physical line รวมบรรทัดว่าง เลขบรรทัดและ SHA-256 ผูกกับไฟล์ ณ วันที่จัดทำ เมื่อแก้โค้ดภายหลังให้ถือคำอธิบายเลขบรรทัดเป็นฉบับเก่าจนกว่าจะปรับตาม

## โครงสร้าง

    data.json -> storage.load -> models.Assignment
                              -> page1.build -> page1.html
                              -> page2.build/handle -> page2.html -> storage.save -> data.json
                              -> page3.build(query) -> page3.html

models.py เปรียบเหมือนแม่พิมพ์งานหนึ่งชิ้น หน้า1เป็นกระดานสรุป หน้า2เป็นเคาน์เตอร์รับแก้ข้อมูล หน้า3เป็นผู้ช่วยคำนวณแผน ทั้งสามหน้าใช้สูตรกลางร่วมกัน app.py และ storage.py เป็นไฟล์ที่อาจารย์ให้และห้ามแก้

## สูตร

| สูตร | ความหมาย |
|---|---|
| remaining = max(0, estimated - done) | ชั่วโมงคงเหลือไม่ติดลบ |
| days = due date - today | ติดลบคือเกินกำหนด ศูนย์คือวันนี้ |
| progress = min(100, int(done * 100 / estimated)) | เปอร์เซ็นต์แบบตัดเศษและไม่เกิน 100 |
| capacity = (days left + 1) * daily hours | เวลาที่ทำได้โดยรวมวันนี้ |
| gap = round(max(0, cumulative - capacity), 1) | ชั่วโมงขาดของภาระสะสม |
| hours per day = round(cumulative / (days left + 1), 1) | ค่าเฉลี่ยต่อวันที่ต้องทำ |

## ลำดับสำคัญ

หน้า1อ่านงาน สร้าง Assignment เติม remaining/days/progress แบ่งสถานะ สะสมตัวนับ แล้วใช้ selection loop ย้ายงานค้างขึ้นก่อนและเรียงวัน หน้า2ตรวจข้อมูลก่อนเพิ่ม/แก้ไข/ลบ และเขียน JSON ทั้ง list หน้า3คัดงานค้าง เรียงวัน บวกชั่วโมงสะสมก่อนประเมินแต่ละงาน แล้วเทียบกับเวลาว่างสะสม

soon count ในหน้า1นับเฉพาะส่งวันนี้ถึงอีกสามวัน ไม่รวมงานเกินกำหนด แต่ JavaScript notification ใช้ days <= 3 จึงรวมงานเกินกำหนดด้วย

## เครื่องหมายหลัก

การเยื้องสี่ช่องเป็นไวยากรณ์บอกบล็อก จุดใช้เข้าถึง attribute วงเล็บกลมใช้เรียกฟังก์ชัน วงเล็บเหลี่ยมใช้ list/index/key ปีกกาใช้ dict colon เปิดบล็อกหรือคั่น key กับ value comma คั่นสมาชิก เครื่องหมายเท่ากับหนึ่งตัวกำหนดค่า สองตัวเปรียบเทียบ และ hash เริ่ม comment

คำว่าอธิบายทุกตัวอักษรในเอกสารนี้หมายถึงแสดง source ทุกบรรทัดและแจกแจง token ทุกหน่วยที่ Python ตีความ ชื่อ remaining_hours เป็น identifier หนึ่งชื่อ ตัวอักษร r หรือ e แยกเดี่ยวไม่มีความหมายเป็นคำสั่ง

## ข้อจำกัดที่ต้องตอบตรง

- selection loop เป็น O(n squared) แต่ข้อมูลตัวอย่างมีเพียงเจ็ดรายการ
- วันต้องเป็น ISO ที่ถูกต้อง ข้อมูลแก้มือผิดอาจทำให้ days_left เกิด ValueError
- หน้า2ใช้ตำแหน่ง list เป็น no ไม่มี ID ถาวร หลายแท็บอาจทำให้ตำแหน่งเปลี่ยน
- isdigit รับตัวเลข Unicode บางแบบที่ int อาจแปลงไม่ได้ เป็น edge case ที่ยังไม่ครอบ
- JSON ถูกเขียนทั้งก้อนและไม่มี lock จึงเหมาะกับงานรายวิชาในเครื่อง
- หน้า3สมมติเวลาว่างเท่ากันทุกวัน และ gap ถูกปัดหนึ่งตำแหน่งก่อนตรวจ
- งานวันเดียวกันประเมินทีละแถว จึงอาจได้สถานะต่างกันตามลำดับเดิม

## คำอธิบายรายบรรทัด


## models.py — 18 บรรทัด

SHA-256: 085065c4aebb680472253967fe5bbda8f3086707eb32503e8c39a108f3b324e8

### L001

    """A small model for one assignment in data.json."""

หน้าที่: docstring อธิบายวัตถุประสงค์ของไฟล์สำหรับผู้อ่าน ไม่มีเงื่อนไขธุรกิจ

token และอักขระที่มีความหมาย:

- '"""A small model for one assignment in data.json."""' — docstring แบบสาม quote

### L002

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L003

    from datetime import date

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'from' — เลือกนำเข้าชื่อจากโมดูล
- 'datetime' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'import' — นำโมดูลหรือชื่อมาใช้
- 'date' — class วันที่ใน standard library

### L004

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L005

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L006

    class Assignment:

หน้าที่: ประกาศ class Assignment เป็นแม่แบบกลางของงานหนึ่งชิ้น

token และอักขระที่มีความหมาย:

- 'class' — ประกาศแม่แบบวัตถุ
- 'Assignment' — class แทนงานหนึ่งชิ้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L007

        def __init__(self, title, course, due_date, estimated_hours, done_hours):

หน้าที่: ประกาศฟังก์ชัน __init__: รับห้า field แล้วเก็บเป็น attribute ของ object

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- '__init__' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'self' — object Assignment ตัวที่กำลังทำงาน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'title' — identifier ของ ชื่องาน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'course' — identifier ของ ชื่อวิชา
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'estimated_hours' — identifier ของ ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'done_hours' — identifier ของ ชั่วโมงที่ทำแล้ว
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L008

            self.title = title

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'title' — identifier ของ ชื่องาน
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'title' — identifier ของ ชื่องาน

### L009

            self.course = course

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'course' — identifier ของ ชื่อวิชา
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'course' — identifier ของ ชื่อวิชา

### L010

            self.due_date = due_date

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD

### L011

            self.estimated_hours = estimated_hours

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'estimated_hours' — identifier ของ ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'estimated_hours' — identifier ของ ชั่วโมงทั้งหมดที่คาดว่าจะใช้

### L012

            self.done_hours = done_hours

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'done_hours' — identifier ของ ชั่วโมงที่ทำแล้ว
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'done_hours' — identifier ของ ชั่วโมงที่ทำแล้ว

### L013

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L014

        def remaining_hours(self):

หน้าที่: ประกาศฟังก์ชัน remaining_hours: คำนวณชั่วโมงคงเหลือ

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'remaining_hours' — identifier ของ ชั่วโมงที่ยังเหลือ
- '(' — เปิดกลุ่ม expression หรือ argument
- 'self' — object Assignment ตัวที่กำลังทำงาน
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L015

            return max(0, self.estimated_hours - self.done_hours)

หน้าที่: ลบชั่วโมงที่ทำแล้วจากชั่วโมงทั้งหมด แล้วใช้ max หนีบค่าต่ำสุดไว้ที่ศูนย์

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'max' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'estimated_hours' — identifier ของ ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- '-' — ลบหรือทำค่าติดลบ
- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'done_hours' — identifier ของ ชั่วโมงที่ทำแล้ว
- ')' — ปิดกลุ่ม expression หรือ argument

### L016

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L017

        def days_left(self):

หน้าที่: ประกาศฟังก์ชัน days_left: คำนวณจำนวนวันถึงกำหนด

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'days_left' — identifier ของ จำนวนวันถึงวันส่ง
- '(' — เปิดกลุ่ม expression หรือ argument
- 'self' — object Assignment ตัวที่กำลังทำงาน
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L018

            return (date.fromisoformat(self.due_date) - date.today()).days

หน้าที่: แปลงวันส่ง ISO ลบวันที่ระบบวันนี้ แล้วอ่านจำนวนวันเต็ม ค่าลบคือเกินกำหนด ศูนย์คือวันนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '(' — เปิดกลุ่ม expression หรือ argument
- 'date' — class วันที่ใน standard library
- '.' — เข้าถึง attribute หรือ method
- 'fromisoformat' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'self' — object Assignment ตัวที่กำลังทำงาน
- '.' — เข้าถึง attribute หรือ method
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- ')' — ปิดกลุ่ม expression หรือ argument
- '-' — ลบหรือทำค่าติดลบ
- 'date' — class วันที่ใน standard library
- '.' — เข้าถึง attribute หรือ method
- 'today' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- '.' — เข้าถึง attribute หรือ method
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท


## pages/page1.py — 63 บรรทัด

SHA-256: 0be8c1e56c4f38cbfa256c8493d3af70ed189dbfbaefd82674506802ecff0f23

### L001

    """Dashboard based on catalog/list and catalog/stats."""

หน้าที่: docstring อธิบายวัตถุประสงค์ของไฟล์สำหรับผู้อ่าน ไม่มีเงื่อนไขธุรกิจ

token และอักขระที่มีความหมาย:

- '"""Dashboard based on catalog/list and catalog/stats."""' — docstring แบบสาม quote

### L002

    import models

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'models' — โมดูลแบบจำลองของโครงการ

### L003

    import storage

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้

### L004

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L005

    TITLE = "ภาพรวมงาน"

หน้าที่: กำหนดชื่อหน้าให้ app.py ใช้ในเมนูและ title

token และอักขระที่มีความหมาย:

- 'TITLE' — ชื่อหน้าในเมนูและหัวเรื่อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"ภาพรวมงาน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L006

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L007

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L008

    def build():

หน้าที่: ประกาศฟังก์ชัน build: สร้าง context dict สำหรับ template ในคำขอ GET

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'build' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L009

        items = []

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '[' — เปิด list/index/key access
- ']' — ปิด list/index/key access

### L010

        open_count = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'open_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L011

        soon_count = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L012

        overdue_count = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'overdue_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L013

        remaining_total = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'remaining_total' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L014

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L015

        for row in storage.load():

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'row' — dict งานหนึ่งแถวจาก data.json
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'load' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L016

            task = models.Assignment(row["title"], row["course"], row["due_date"],

หน้าที่: เริ่มสร้าง Assignment จาก row; argument ยังต่อในบรรทัดถัดไป

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'models' — โมดูลแบบจำลองของโครงการ
- '.' — เข้าถึง attribute หรือ method
- 'Assignment' — class แทนงานหนึ่งชิ้น
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"title"' — string ชื่อ field: ชื่องาน
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"course"' — string ชื่อ field: ชื่อวิชา
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L017

                                     row["estimated_hours"], row["done_hours"])

หน้าที่: เข้าถึง field ใน dict row เป็นส่วนต่อเนื่องของ constructor ก่อนหน้า

token และอักขระที่มีความหมาย:

- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ']' — ปิด list/index/key access
- ')' — ปิดกลุ่ม expression หรือ argument

### L018

            remaining = task.remaining_hours()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'remaining_hours' — identifier ของ ชั่วโมงที่ยังเหลือ
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L019

            days = task.days_left()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'days_left' — identifier ของ จำนวนวันถึงวันส่ง
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L020

            item = dict(row)

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'dict' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- ')' — ปิดกลุ่ม expression หรือ argument

### L021

            item["remaining_hours"] = remaining

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท

### L022

            item["days_left"] = days

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท

### L023

            item["progress"] = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"progress"' — string ชื่อ field: เปอร์เซ็นต์ความคืบหน้า
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L024

            if row["estimated_hours"] > 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ']' — ปิด list/index/key access
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L025

                item["progress"] = min(100, int(row["done_hours"] * 100 / row["estimated_hours"]))

หน้าที่: คำนวณเปอร์เซ็นต์ ตัดทศนิยมด้วย int และจำกัดด้านบนที่ 100 โดยบรรทัดก่อนป้องกันหารศูนย์

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"progress"' — string ชื่อ field: เปอร์เซ็นต์ความคืบหน้า
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'min' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '100' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'int' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ']' — ปิด list/index/key access
- '*' — คูณ
- '100' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- '/' — หาร
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ']' — ปิด list/index/key access
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L026

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L027

            if remaining == 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '==' — เปรียบเทียบว่าเท่ากัน
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L028

                item["status"] = "เสร็จแล้ว"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"เสร็จแล้ว"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L029

                item["tone"] = "good"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"good"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L030

            else:

หน้าที่: เปิดกิ่งกรณีเงื่อนไขก่อนหน้าไม่ตรง

token และอักขระที่มีความหมาย:

- 'else' — รับกรณีที่เงื่อนไขก่อนหน้าไม่ตรง
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L031

                open_count = open_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'open_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'open_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L032

                remaining_total = remaining_total + remaining

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'remaining_total' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'remaining_total' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท

### L033

                if days < 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '<' — น้อยกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L034

                    overdue_count = overdue_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'overdue_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'overdue_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L035

                    item["status"] = "เกินกำหนด " + str(-days) + " วัน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"เกินกำหนด "' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'str' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '-' — ลบหรือทำค่าติดลบ
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '" วัน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L036

                    item["tone"] = "bad"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"bad"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L037

                elif days == 0:

หน้าที่: ตรวจเงื่อนไขถัดไปเฉพาะเมื่อกิ่งก่อนหน้าไม่ทำ

token และอักขระที่มีความหมาย:

- 'elif' — ตรวจเงื่อนไขถัดไปเมื่อกิ่งก่อนหน้าไม่ทำ
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '==' — เปรียบเทียบว่าเท่ากัน
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L038

                    soon_count = soon_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L039

                    item["status"] = "ส่งวันนี้"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"ส่งวันนี้"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L040

                    item["tone"] = "bad"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"bad"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L041

                elif days <= 3:

หน้าที่: ตรวจเงื่อนไขถัดไปเฉพาะเมื่อกิ่งก่อนหน้าไม่ทำ

token และอักขระที่มีความหมาย:

- 'elif' — ตรวจเงื่อนไขถัดไปเมื่อกิ่งก่อนหน้าไม่ทำ
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '<=' — น้อยกว่าหรือเท่ากับ
- '3' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L042

                    soon_count = soon_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L043

                    item["status"] = "อีก " + str(days) + " วัน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"อีก "' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'str' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '" วัน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L044

                    item["tone"] = "gold"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"gold"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L045

                else:

หน้าที่: เปิดกิ่งกรณีเงื่อนไขก่อนหน้าไม่ตรง

token และอักขระที่มีความหมาย:

- 'else' — รับกรณีที่เงื่อนไขก่อนหน้าไม่ตรง
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L046

                    item["status"] = "อีก " + str(days) + " วัน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"อีก "' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'str' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'days' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '" วัน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L047

                    item["tone"] = ""

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L048

            items.append(item)

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- ')' — ปิดกลุ่ม expression หรือ argument

### L049

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L050

        # Keep unfinished work nearest to its deadline at the top of the dashboard.

หน้าที่: comment อธิบายเจตนาของ algorithm Python ไม่ประมวลผลข้อความนี้

token และอักขระที่มีความหมาย:

- '# Keep unfinished work nearest to its deadline at the top of the dashboard.' — comment ถึงท้ายบรรทัด

### L051

        ordered = []

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'ordered' — list หลังเรียงลำดับ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '[' — เปิด list/index/key access
- ']' — ปิด list/index/key access

### L052

        while items:

หน้าที่: เริ่ม loop ที่ทำซ้ำขณะ list ยังไม่ว่าง และมีการ remove หนึ่งรายการต่อรอบ

token และอักขระที่มีความหมาย:

- 'while' — ทำซ้ำตราบใดที่เงื่อนไขจริง
- 'items' — list งานหลายรายการ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L053

            first = items[0]

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'items' — list งานหลายรายการ
- '[' — เปิด list/index/key access
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ']' — ปิด list/index/key access

### L054

            for item in items:

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'items' — list งานหลายรายการ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L055

                if first["remaining_hours"] == 0 and item["remaining_hours"] > 0:

หน้าที่: ถ้าตัวเลือกเดิมเสร็จแล้วแต่ผู้สมัครยังค้าง ให้ย้ายงานค้างขึ้นก่อน

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '==' — เปรียบเทียบว่าเท่ากัน
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'and' — ตรรกะและแบบหยุดก่อนเมื่อพบค่าเท็จ
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L056

                    first = item

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล

### L057

                elif item["remaining_hours"] > 0 and first["remaining_hours"] > 0 and item["due_date"] < first["due_date"]:

หน้าที่: เมื่อทั้งคู่ยังค้าง ให้เลือก due_date ที่เป็น ISO string น้อยกว่า ซึ่งคือวันก่อนกว่า

token และอักขระที่มีความหมาย:

- 'elif' — ตรวจเงื่อนไขถัดไปเมื่อกิ่งก่อนหน้าไม่ทำ
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'and' — ตรรกะและแบบหยุดก่อนเมื่อพบค่าเท็จ
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'and' — ตรรกะและแบบหยุดก่อนเมื่อพบค่าเท็จ
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- '<' — น้อยกว่า
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L058

                    first = item

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล

### L059

            ordered.append(first)

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'ordered' — list หลังเรียงลำดับ
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- ')' — ปิดกลุ่ม expression หรือ argument

### L060

            items.remove(first)

หน้าที่: ลบสมาชิกที่เลือกออกจาก pool เพื่อให้ selection loop เดินหน้าสู่จุดจบ

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '.' — เข้าถึง attribute หรือ method
- 'remove' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- ')' — ปิดกลุ่ม expression หรือ argument

### L061

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L062

        return {"items": ordered, "open_count": open_count, "soon_count": soon_count,

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '{' — เปิด dict
- '"items"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'ordered' — list หลังเรียงลำดับ
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"open_count"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'open_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"soon_count"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'soon_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L063

                "overdue_count": overdue_count, "remaining_total": remaining_total}

หน้าที่: ส่วนต่อเนื่องของ dict/string/คำสั่งหลายบรรทัดที่เริ่มก่อนหน้า ต้องอ่านรวมกัน

token และอักขระที่มีความหมาย:

- '"overdue_count"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'overdue_count' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"remaining_total"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'remaining_total' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '}' — ปิด dict


## pages/page2.py — 86 บรรทัด

SHA-256: c384dcb77d540e87134fe25fb638631d9c053e364b0260eff39cc73c0fa4f8e5

### L001

    """Add, edit, and delete assignments based on catalog/form."""

หน้าที่: docstring อธิบายวัตถุประสงค์ของไฟล์สำหรับผู้อ่าน ไม่มีเงื่อนไขธุรกิจ

token และอักขระที่มีความหมาย:

- '"""Add, edit, and delete assignments based on catalog/form."""' — docstring แบบสาม quote

### L002

    from datetime import date

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'from' — เลือกนำเข้าชื่อจากโมดูล
- 'datetime' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'import' — นำโมดูลหรือชื่อมาใช้
- 'date' — class วันที่ใน standard library

### L003

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L004

    import models

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'models' — โมดูลแบบจำลองของโครงการ

### L005

    import storage

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้

### L006

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L007

    TITLE = "จัดการงาน"

หน้าที่: กำหนดชื่อหน้าให้ app.py ใช้ในเมนูและ title

token และอักขระที่มีความหมาย:

- 'TITLE' — ชื่อหน้าในเมนูและหัวเรื่อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"จัดการงาน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L008

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L009

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L010

    def build():

หน้าที่: ประกาศฟังก์ชัน build: สร้าง context dict สำหรับ template ในคำขอ GET

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'build' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L011

        items = []

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '[' — เปิด list/index/key access
- ']' — ปิด list/index/key access

### L012

        position = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L013

        for row in storage.load():

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'row' — dict งานหนึ่งแถวจาก data.json
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'load' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L014

            item = dict(row)

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'dict' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- ')' — ปิดกลุ่ม expression หรือ argument

### L015

            item["no"] = position

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"no"' — string ชื่อ field: ตำแหน่งงานใน list
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์

### L016

            task = models.Assignment(row["title"], row["course"], row["due_date"],

หน้าที่: เริ่มสร้าง Assignment จาก row; argument ยังต่อในบรรทัดถัดไป

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'models' — โมดูลแบบจำลองของโครงการ
- '.' — เข้าถึง attribute หรือ method
- 'Assignment' — class แทนงานหนึ่งชิ้น
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"title"' — string ชื่อ field: ชื่องาน
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"course"' — string ชื่อ field: ชื่อวิชา
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L017

                                     row["estimated_hours"], row["done_hours"])

หน้าที่: เข้าถึง field ใน dict row เป็นส่วนต่อเนื่องของ constructor ก่อนหน้า

token และอักขระที่มีความหมาย:

- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ']' — ปิด list/index/key access
- ')' — ปิดกลุ่ม expression หรือ argument

### L018

            item["remaining_hours"] = task.remaining_hours()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'remaining_hours' — identifier ของ ชั่วโมงที่ยังเหลือ
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L019

            items.append(item)

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'item' — dict สำเนาที่เติมค่าคำนวณเพื่อแสดงผล
- ')' — ปิดกลุ่ม expression หรือ argument

### L020

            position = position + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L021

        return {"items": items, "count": len(items)}

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '{' — เปิด dict
- '"items"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'items' — list งานหลายรายการ
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"count"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'len' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'items' — list งานหลายรายการ
- ')' — ปิดกลุ่ม expression หรือ argument
- '}' — ปิด dict

### L022

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L023

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L024

    def read_hours(text):

หน้าที่: ประกาศฟังก์ชัน read_hours: แปลงข้อความชั่วโมงเป็น float ที่ใช้ได้หรือ None

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'read_hours' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'text' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L025

        try:

หน้าที่: เปิดบล็อกที่อาจเกิดข้อยกเว้น

token และอักขระที่มีความหมาย:

- 'try' — เริ่มส่วนที่อาจเกิดข้อยกเว้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L026

            value = float(text)

หน้าที่: พยายามแปลงข้อความเป็น float; nan และ infinity แปลงผ่านได้จึงมีด่านตรวจบรรทัดถัดไป

token และอักขระที่มีความหมาย:

- 'value' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'text' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument

### L027

        except (TypeError, ValueError):

หน้าที่: รับข้อยกเว้นที่ระบุแล้วใช้ค่าหรือข้อความสำรอง

token และอักขระที่มีความหมาย:

- 'except' — รับข้อยกเว้นชนิดที่ระบุ
- '(' — เปิดกลุ่ม expression หรือ argument
- 'TypeError' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'ValueError' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L028

            return None

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์

### L029

        if value != value or value in (float("inf"), float("-inf")):

หน้าที่: ตรวจ NaN ด้วยคุณสมบัติว่าไม่เท่ากับตัวเอง และปฏิเสธ infinity ทั้งบวกและลบ

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'value' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '!=' — เปรียบเทียบว่าไม่เท่ากัน
- 'value' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'value' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- '(' — เปิดกลุ่ม expression หรือ argument
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '"inf"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '"-inf"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L030

            return None

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์

### L031

        return value

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'value' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท

### L032

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L033

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L034

    def check(form):

หน้าที่: ประกาศฟังก์ชัน check: ตรวจและทำความสะอาดข้อมูลฟอร์ม

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'check' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L035

        title = form.get("title", "").strip()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'title' — identifier ของ ชื่องาน
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"title"' — string ชื่อ field: ชื่องาน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- '.' — เข้าถึง attribute หรือ method
- 'strip' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L036

        course = form.get("course", "").strip()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'course' — identifier ของ ชื่อวิชา
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"course"' — string ชื่อ field: ชื่อวิชา
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- '.' — เข้าถึง attribute หรือ method
- 'strip' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L037

        due_date = form.get("due_date", "")

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument

### L038

        estimate = read_hours(form.get("estimated_hours", ""))

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'read_hours' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L039

        done = read_hours(form.get("done_hours", "0"))

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'done' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'read_hours' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"0"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L040

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L041

        if title == "" or course == "":

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'title' — identifier ของ ชื่องาน
- '==' — เปรียบเทียบว่าเท่ากัน
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'course' — identifier ของ ชื่อวิชา
- '==' — เปรียบเทียบว่าเท่ากัน
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L042

            return None, "กรุณากรอกชื่องานและวิชา"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"กรุณากรอกชื่องานและวิชา"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L043

        if len(title) > 80 or len(course) > 40:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'len' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'title' — identifier ของ ชื่องาน
- ')' — ปิดกลุ่ม expression หรือ argument
- '>' — มากกว่า
- '80' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'len' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'course' — identifier ของ ชื่อวิชา
- ')' — ปิดกลุ่ม expression หรือ argument
- '>' — มากกว่า
- '40' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L044

            return None, "ชื่องานหรือวิชายาวเกินไป"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"ชื่องานหรือวิชายาวเกินไป"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L045

        try:

หน้าที่: เปิดบล็อกที่อาจเกิดข้อยกเว้น

token และอักขระที่มีความหมาย:

- 'try' — เริ่มส่วนที่อาจเกิดข้อยกเว้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L046

            date.fromisoformat(due_date)

หน้าที่: ตรวจว่าข้อความเป็นวันที่ ISO ที่มีจริง ผล date ไม่ต้องเก็บเพราะใช้เพียง validation

token และอักขระที่มีความหมาย:

- 'date' — class วันที่ใน standard library
- '.' — เข้าถึง attribute หรือ method
- 'fromisoformat' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- ')' — ปิดกลุ่ม expression หรือ argument

### L047

        except ValueError:

หน้าที่: รับข้อยกเว้นที่ระบุแล้วใช้ค่าหรือข้อความสำรอง

token และอักขระที่มีความหมาย:

- 'except' — รับข้อยกเว้นชนิดที่ระบุ
- 'ValueError' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L048

            return None, "กรุณาเลือกวันส่งที่ถูกต้อง"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"กรุณาเลือกวันส่งที่ถูกต้อง"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L049

        if estimate is None or estimate <= 0 or estimate > 200:

หน้าที่: กำหนดช่วง estimate มากกว่าศูนย์ถึง 200 และใช้ short circuit ป้องกันเปรียบเทียบ None

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'is' — คำสงวนของ Python
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '<=' — น้อยกว่าหรือเท่ากับ
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '>' — มากกว่า
- '200' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L050

            return None, "ชั่วโมงที่คาดว่าจะใช้ต้องมากกว่า 0 และไม่เกิน 200"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"ชั่วโมงที่คาดว่าจะใช้ต้องมากกว่า 0 และไม่เกิน 200"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L051

        if done is None or done < 0 or done > estimate:

หน้าที่: กำหนด done ตั้งแต่ศูนย์ถึง estimate รวมขอบ

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'done' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- 'is' — คำสงวนของ Python
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'done' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '<' — น้อยกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'done' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '>' — มากกว่า
- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L052

            return None, "ชั่วโมงที่ทำแล้วต้องอยู่ระหว่าง 0 ถึงชั่วโมงที่คาดว่าจะใช้"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"ชั่วโมงที่ทำแล้วต้องอยู่ระหว่าง 0 ถึงชั่วโมงที่คาดว่าจะใช้"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L053

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L054

        return {"title": title, "course": course, "due_date": due_date,

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '{' — เปิด dict
- '"title"' — string ชื่อ field: ชื่องาน
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'title' — identifier ของ ชื่องาน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"course"' — string ชื่อ field: ชื่อวิชา
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'course' — identifier ของ ชื่อวิชา
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L055

                "estimated_hours": estimate, "done_hours": done}, ""

หน้าที่: ส่วนต่อเนื่องของ dict/string/คำสั่งหลายบรรทัดที่เริ่มก่อนหน้า ต้องอ่านรวมกัน

token และอักขระที่มีความหมาย:

- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'estimate' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'done' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '}' — ปิด dict
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L056

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L057

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L058

    def handle(form):

หน้าที่: ประกาศฟังก์ชัน handle: เลือกคำสั่ง POST และบันทึกเมื่อผ่าน validation

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'handle' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L059

        action = form.get("action", "")

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'action' — identifier ของ คำสั่ง add update หรือ delete
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"action"' — string ชื่อ field: คำสั่ง add update หรือ delete
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument

### L060

        items = storage.load()

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'load' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L061

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L062

        if action == "add":

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'action' — identifier ของ คำสั่ง add update หรือ delete
- '==' — เปรียบเทียบว่าเท่ากัน
- '"add"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L063

            task, error = check(form)

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'check' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- ')' — ปิดกลุ่ม expression หรือ argument

### L064

            if error:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L065

                return "✗ " + error

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✗ "' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท

### L066

            items.append(task)

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'task' — Assignment หรือ dict งานตามบริบท
- ')' — ปิดกลุ่ม expression หรือ argument

### L067

            storage.save(items)

หน้าที่: ส่ง list ทั้งชุดให้ storage.py เขียนทับ data.json

token และอักขระที่มีความหมาย:

- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'save' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'items' — list งานหลายรายการ
- ')' — ปิดกลุ่ม expression หรือ argument

### L068

            return "✓ เพิ่มงานแล้ว"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✓ เพิ่มงานแล้ว"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L069

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L070

        position = form.get("no", "")

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"no"' — string ชื่อ field: ตำแหน่งงานใน list
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument

### L071

        if not position.isdigit() or int(position) >= len(items):

หน้าที่: ตรวจตำแหน่งเป็น digit และอยู่ใน list; short circuit ป้องกัน int เมื่อไม่ใช่ digit แต่ Unicode digit บางชนิดยังเป็น edge case

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'not' — กลับค่าความจริง
- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- '.' — เข้าถึง attribute หรือ method
- 'isdigit' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'int' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- ')' — ปิดกลุ่ม expression หรือ argument
- '>=' — มากกว่าหรือเท่ากับ
- 'len' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'items' — list งานหลายรายการ
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L072

            return "✗ ไม่พบงานนี้"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✗ ไม่พบงานนี้"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L073

        index = int(position)

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'index' — ตำแหน่ง list หลังแปลงเป็น int
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'int' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'position' — ตำแหน่ง list ที่เริ่มจากศูนย์
- ')' — ปิดกลุ่ม expression หรือ argument

### L074

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L075

        if action == "delete":

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'action' — identifier ของ คำสั่ง add update หรือ delete
- '==' — เปรียบเทียบว่าเท่ากัน
- '"delete"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L076

            items.pop(index)

หน้าที่: ลบสมาชิกตำแหน่ง index แล้วทำให้สมาชิกถัดไปเลื่อนตำแหน่ง

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '.' — เข้าถึง attribute หรือ method
- 'pop' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'index' — ตำแหน่ง list หลังแปลงเป็น int
- ')' — ปิดกลุ่ม expression หรือ argument

### L077

            storage.save(items)

หน้าที่: ส่ง list ทั้งชุดให้ storage.py เขียนทับ data.json

token และอักขระที่มีความหมาย:

- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'save' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'items' — list งานหลายรายการ
- ')' — ปิดกลุ่ม expression หรือ argument

### L078

            return "✓ ลบงานแล้ว"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✓ ลบงานแล้ว"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L079

        if action == "update":

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'action' — identifier ของ คำสั่ง add update หรือ delete
- '==' — เปรียบเทียบว่าเท่ากัน
- '"update"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L080

            task, error = check(form)

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'check' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'form' — ข้อมูลฟอร์ม POST แบบ mapping
- ')' — ปิดกลุ่ม expression หรือ argument

### L081

            if error:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L082

                return "✗ " + error

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✗ "' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'error' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท

### L083

            items[index] = task

หน้าที่: แทน dict เดิมทั้งก้อนด้วย dict ที่ผ่าน validation

token และอักขระที่มีความหมาย:

- 'items' — list งานหลายรายการ
- '[' — เปิด list/index/key access
- 'index' — ตำแหน่ง list หลังแปลงเป็น int
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท

### L084

            storage.save(items)

หน้าที่: ส่ง list ทั้งชุดให้ storage.py เขียนทับ data.json

token และอักขระที่มีความหมาย:

- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'save' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'items' — list งานหลายรายการ
- ')' — ปิดกลุ่ม expression หรือ argument

### L085

            return "✓ บันทึกการแก้ไขแล้ว"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✓ บันทึกการแก้ไขแล้ว"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L086

        return "✗ ไม่รู้จักคำสั่ง"

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '"✗ ไม่รู้จักคำสั่ง"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ


## pages/page3.py — 63 บรรทัด

SHA-256: 0cd4fb940f5572aef7d82536b44b9ddb04fad296094182f6f55f62b47f388666

### L001

    """Deadline order and workload estimate based on catalog/ranking and calculator."""

หน้าที่: docstring อธิบายวัตถุประสงค์ของไฟล์สำหรับผู้อ่าน ไม่มีเงื่อนไขธุรกิจ

token และอักขระที่มีความหมาย:

- '"""Deadline order and workload estimate based on catalog/ranking and calculator."""' — docstring แบบสาม quote

### L002

    import models

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'models' — โมดูลแบบจำลองของโครงการ

### L003

    import storage

หน้าที่: นำ dependency ในโครงการหรือ standard library มาใช้ ไม่มีการติดตั้ง package

token และอักขระที่มีความหมาย:

- 'import' — นำโมดูลหรือชื่อมาใช้
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้

### L004

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L005

    TITLE = "แผนก่อนวันส่ง"

หน้าที่: กำหนดชื่อหน้าให้ app.py ใช้ในเมนูและ title

token และอักขระที่มีความหมาย:

- 'TITLE' — ชื่อหน้าในเมนูและหัวเรื่อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"แผนก่อนวันส่ง"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L006

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L007

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L008

    def build(query):

หน้าที่: ประกาศฟังก์ชัน build: สร้าง context dict สำหรับ template ในคำขอ GET

token และอักขระที่มีความหมาย:

- 'def' — ประกาศฟังก์ชันหรือเมธอด
- 'build' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'query' — พารามิเตอร์ GET แบบ mapping
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L009

        notice = ""

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'notice' — identifier ของ ข้อความแจ้งค่าที่ไม่ถูกต้อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '""' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L010

        try:

หน้าที่: เปิดบล็อกที่อาจเกิดข้อยกเว้น

token และอักขระที่มีความหมาย:

- 'try' — เริ่มส่วนที่อาจเกิดข้อยกเว้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L011

            daily_hours = float(query.get("hours", "2"))

หน้าที่: อ่าน hours จาก URL และใช้ค่าเริ่มต้น 2 ก่อนแปลงเป็น float

token และอักขระที่มีความหมาย:

- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- 'query' — พารามิเตอร์ GET แบบ mapping
- '.' — เข้าถึง attribute หรือ method
- 'get' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '"hours"' — string ชื่อ field: พารามิเตอร์เวลาว่างต่อวัน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"2"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument

### L012

        except ValueError:

หน้าที่: รับข้อยกเว้นที่ระบุแล้วใช้ค่าหรือข้อความสำรอง

token และอักขระที่มีความหมาย:

- 'except' — รับข้อยกเว้นชนิดที่ระบุ
- 'ValueError' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L013

            daily_hours = 2

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '2' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L014

            notice = "ใช้ค่าเริ่มต้น 2 ชั่วโมงต่อวัน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'notice' — identifier ของ ข้อความแจ้งค่าที่ไม่ถูกต้อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"ใช้ค่าเริ่มต้น 2 ชั่วโมงต่อวัน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L015

        if daily_hours != daily_hours or daily_hours in (float("inf"), float("-inf")) or daily_hours <= 0 or daily_hours > 12:

หน้าที่: ปฏิเสธ NaN infinity ค่าที่ไม่เกินศูนย์ และค่ามากกว่า 12 แล้วใช้ค่าเริ่มต้น

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '!=' — เปรียบเทียบว่าไม่เท่ากัน
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- '(' — เปิดกลุ่ม expression หรือ argument
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '"inf"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'float' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '"-inf"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ')' — ปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '<=' — น้อยกว่าหรือเท่ากับ
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- 'or' — ตรรกะหรือแบบหยุดก่อนเมื่อพบค่าจริง
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '>' — มากกว่า
- '12' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L016

            daily_hours = 2

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '2' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L017

            notice = "กรุณาระบุเวลาว่างมากกว่า 0 และไม่เกิน 12 ชั่วโมงต่อวัน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'notice' — identifier ของ ข้อความแจ้งค่าที่ไม่ถูกต้อง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"กรุณาระบุเวลาว่างมากกว่า 0 และไม่เกิน 12 ชั่วโมงต่อวัน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L018

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L019

        remaining = []

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '[' — เปิด list/index/key access
- ']' — ปิด list/index/key access

### L020

        for row in storage.load():

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'row' — dict งานหนึ่งแถวจาก data.json
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'storage' — โมดูลอ่านเขียน JSON ที่อาจารย์ให้
- '.' — เข้าถึง attribute หรือ method
- 'load' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L021

            task = models.Assignment(row["title"], row["course"], row["due_date"],

หน้าที่: เริ่มสร้าง Assignment จาก row; argument ยังต่อในบรรทัดถัดไป

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'models' — โมดูลแบบจำลองของโครงการ
- '.' — เข้าถึง attribute หรือ method
- 'Assignment' — class แทนงานหนึ่งชิ้น
- '(' — เปิดกลุ่ม expression หรือ argument
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"title"' — string ชื่อ field: ชื่องาน
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"course"' — string ชื่อ field: ชื่อวิชา
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L022

                                     row["estimated_hours"], row["done_hours"])

หน้าที่: เข้าถึง field ใน dict row เป็นส่วนต่อเนื่องของ constructor ก่อนหน้า

token และอักขระที่มีความหมาย:

- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"estimated_hours"' — string ชื่อ field: ชั่วโมงทั้งหมดที่คาดว่าจะใช้
- ']' — ปิด list/index/key access
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'row' — dict งานหนึ่งแถวจาก data.json
- '[' — เปิด list/index/key access
- '"done_hours"' — string ชื่อ field: ชั่วโมงที่ทำแล้ว
- ']' — ปิด list/index/key access
- ')' — ปิดกลุ่ม expression หรือ argument

### L023

            if task.remaining_hours() > 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'remaining_hours' — identifier ของ ชั่วโมงที่ยังเหลือ
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L024

                remaining.append({"title": task.title, "course": task.course,

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- '{' — เปิด dict
- '"title"' — string ชื่อ field: ชื่องาน
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'title' — identifier ของ ชื่องาน
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"course"' — string ชื่อ field: ชื่อวิชา
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'course' — identifier ของ ชื่อวิชา
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L025

                                  "due_date": task.due_date, "days_left": task.days_left(),

หน้าที่: ส่วนต่อเนื่องของ dict/string/คำสั่งหลายบรรทัดที่เริ่มก่อนหน้า ต้องอ่านรวมกัน

token และอักขระที่มีความหมาย:

- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'due_date' — identifier ของ วันส่งรูป YYYY-MM-DD
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'days_left' — identifier ของ จำนวนวันถึงวันส่ง
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L026

                                  "remaining_hours": task.remaining_hours()})

หน้าที่: ส่วนต่อเนื่องของ dict/string/คำสั่งหลายบรรทัดที่เริ่มก่อนหน้า ต้องอ่านรวมกัน

token และอักขระที่มีความหมาย:

- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'task' — Assignment หรือ dict งานตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'remaining_hours' — identifier ของ ชั่วโมงที่ยังเหลือ
- '(' — เปิดกลุ่ม expression หรือ argument
- ')' — ปิดกลุ่ม expression หรือ argument
- '}' — ปิด dict
- ')' — ปิดกลุ่ม expression หรือ argument

### L027

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L028

        # Selection loop from catalog/ranking: nearest deadline comes first.

หน้าที่: comment อธิบายเจตนาของ algorithm Python ไม่ประมวลผลข้อความนี้

token และอักขระที่มีความหมาย:

- '# Selection loop from catalog/ranking: nearest deadline comes first.' — comment ถึงท้ายบรรทัด

### L029

        ordered = []

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'ordered' — list หลังเรียงลำดับ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '[' — เปิด list/index/key access
- ']' — ปิด list/index/key access

### L030

        while remaining:

หน้าที่: เริ่ม loop ที่ทำซ้ำขณะ list ยังไม่ว่าง และมีการ remove หนึ่งรายการต่อรอบ

token และอักขระที่มีความหมาย:

- 'while' — ทำซ้ำตราบใดที่เงื่อนไขจริง
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L031

            first = remaining[0]

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '[' — เปิด list/index/key access
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ']' — ปิด list/index/key access

### L032

            for task in remaining:

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'task' — Assignment หรือ dict งานตามบริบท
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L033

                if task["due_date"] < first["due_date"]:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- '<' — น้อยกว่า
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '[' — เปิด list/index/key access
- '"due_date"' — string ชื่อ field: วันส่งรูป YYYY-MM-DD
- ']' — ปิด list/index/key access
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L034

                    first = task

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท

### L035

            ordered.append(first)

หน้าที่: เพิ่มสมาชิกหนึ่งตัวท้าย list ในหน่วยความจำ

token และอักขระที่มีความหมาย:

- 'ordered' — list หลังเรียงลำดับ
- '.' — เข้าถึง attribute หรือ method
- 'append' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- ')' — ปิดกลุ่ม expression หรือ argument

### L036

            remaining.remove(first)

หน้าที่: ลบสมาชิกที่เลือกออกจาก pool เพื่อให้ selection loop เดินหน้าสู่จุดจบ

token และอักขระที่มีความหมาย:

- 'remaining' — ชั่วโมงคงเหลือหรือ list งานค้างตามบริบท
- '.' — เข้าถึง attribute หรือ method
- 'remove' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'first' — ตัวเลือกชั่วคราวที่ดีที่สุดใน selection loop
- ')' — ปิดกลุ่ม expression หรือ argument

### L037

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L038

        cumulative_hours = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'cumulative_hours' — ชั่วโมงคงเหลือสะสมถึงงานปัจจุบัน
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L039

        risk_count = 0

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L040

        for task in ordered:

หน้าที่: เริ่ม loop อ่านสมาชิกทีละตัวจากชุดด้านขวา บล็อกที่เยื้องจะทำซ้ำ

token และอักขระที่มีความหมาย:

- 'for' — วนรับสมาชิกทีละรายการ
- 'task' — Assignment หรือ dict งานตามบริบท
- 'in' — ระบุชุดสำหรับวนหรือตรวจสมาชิก
- 'ordered' — list หลังเรียงลำดับ
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L041

            cumulative_hours = cumulative_hours + task["remaining_hours"]

หน้าที่: บวกชั่วโมงงานปัจจุบันก่อนแบ่งกิ่ง จึงรวมงานเกินกำหนดไว้ในภาระของงานอนาคต

token และอักขระที่มีความหมาย:

- 'cumulative_hours' — ชั่วโมงคงเหลือสะสมถึงงานปัจจุบัน
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'cumulative_hours' — ชั่วโมงคงเหลือสะสมถึงงานปัจจุบัน
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access

### L042

            if task["days_left"] < 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ']' — ปิด list/index/key access
- '<' — น้อยกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L043

                task["status"] = "เกินกำหนด"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"เกินกำหนด"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L044

                task["tone"] = "bad"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"bad"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L045

                task["gap"] = task["remaining_hours"]

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"gap"' — string ชื่อ field: ชั่วโมงที่ขาดตามแผนสะสม
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"remaining_hours"' — string ชื่อ field: ชั่วโมงที่ยังเหลือ
- ']' — ปิด list/index/key access

### L046

                risk_count = risk_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L047

            else:

หน้าที่: เปิดกิ่งกรณีเงื่อนไขก่อนหน้าไม่ตรง

token และอักขระที่มีความหมาย:

- 'else' — รับกรณีที่เงื่อนไขก่อนหน้าไม่ตรง
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L048

                available_hours = (task["days_left"] + 1) * daily_hours

หน้าที่: รวมวันนี้ด้วยการบวกหนึ่ง แล้วคูณเวลาว่างต่อวันเป็น capacity สะสม

token และอักขระที่มีความหมาย:

- 'available_hours' — เวลาที่ทำได้สะสมถึงวันส่ง
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '(' — เปิดกลุ่ม expression หรือ argument
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ']' — ปิด list/index/key access
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ')' — ปิดกลุ่ม expression หรือ argument
- '*' — คูณ
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ

### L049

                task["gap"] = round(max(0, cumulative_hours - available_hours), 1)

หน้าที่: หาส่วนขาดสะสม ไม่ให้ติดลบ และปัดหนึ่งตำแหน่งก่อนนำ gap ไปตัดสินความเสี่ยง

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"gap"' — string ชื่อ field: ชั่วโมงที่ขาดตามแผนสะสม
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'round' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'max' — built-in function ของ Python
- '(' — เปิดกลุ่ม expression หรือ argument
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- 'cumulative_hours' — ชั่วโมงคงเหลือสะสมถึงงานปัจจุบัน
- '-' — ลบหรือทำค่าติดลบ
- 'available_hours' — เวลาที่ทำได้สะสมถึงวันส่ง
- ')' — ปิดกลุ่ม expression หรือ argument
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ')' — ปิดกลุ่ม expression หรือ argument

### L050

                task["hours_per_day"] = round(cumulative_hours / (task["days_left"] + 1), 1)

หน้าที่: หารงานสะสมด้วยจำนวนวันที่รวมวันนี้ แล้วปัดหนึ่งตำแหน่ง

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"hours_per_day"' — string ชื่อ field: ชั่วโมงเฉลี่ยต่อวันที่ต้องทำ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'round' — identifier: ชื่อตัวแปร ฟังก์ชัน method attribute หรือโมดูลตามบริบท
- '(' — เปิดกลุ่ม expression หรือ argument
- 'cumulative_hours' — ชั่วโมงคงเหลือสะสมถึงงานปัจจุบัน
- '/' — หาร
- '(' — เปิดกลุ่ม expression หรือ argument
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ']' — ปิด list/index/key access
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ')' — ปิดกลุ่ม expression หรือ argument
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ')' — ปิดกลุ่ม expression หรือ argument

### L051

                if task["gap"] > 0:

หน้าที่: ตรวจเงื่อนไข หากจริงจึงทำบล็อกที่เยื้องถัดไป

token และอักขระที่มีความหมาย:

- 'if' — ตรวจเงื่อนไขแรก
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"gap"' — string ชื่อ field: ชั่วโมงที่ขาดตามแผนสะสม
- ']' — ปิด list/index/key access
- '>' — มากกว่า
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L052

                    task["status"] = "เวลาไม่พอ"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"เวลาไม่พอ"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L053

                    task["tone"] = "bad"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"bad"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L054

                    risk_count = risk_count + 1

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- '+' — บวกตัวเลขหรือต่อข้อความตามชนิด
- '1' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น

### L055

                elif task["days_left"] <= 3:

หน้าที่: ตรวจเงื่อนไขถัดไปเฉพาะเมื่อกิ่งก่อนหน้าไม่ทำ

token และอักขระที่มีความหมาย:

- 'elif' — ตรวจเงื่อนไขถัดไปเมื่อกิ่งก่อนหน้าไม่ทำ
- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"days_left"' — string ชื่อ field: จำนวนวันถึงวันส่ง
- ']' — ปิด list/index/key access
- '<=' — น้อยกว่าหรือเท่ากับ
- '3' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L056

                    task["status"] = "ควรเริ่มตอนนี้"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"ควรเริ่มตอนนี้"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L057

                    task["tone"] = "gold"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"gold"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L058

                else:

หน้าที่: เปิดกิ่งกรณีเงื่อนไขก่อนหน้าไม่ตรง

token และอักขระที่มีความหมาย:

- 'else' — รับกรณีที่เงื่อนไขก่อนหน้าไม่ตรง
- ':' — เปิดบล็อกหรือคั่น key กับ value

### L059

                    task["status"] = "ตามแผน"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"status"' — string ชื่อ field: ข้อความสถานะ
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"ตามแผน"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L060

                    task["tone"] = "good"

หน้าที่: คำนวณหรืออ่านค่าด้านขวา แล้วกำหนดให้ตัวแปร field หรือสมาชิกด้านซ้าย

token และอักขระที่มีความหมาย:

- 'task' — Assignment หรือ dict งานตามบริบท
- '[' — เปิด list/index/key access
- '"tone"' — string ชื่อ field: ชื่อโทนสี CSS
- ']' — ปิด list/index/key access
- '=' — กำหนดค่าด้านขวาให้ด้านซ้าย
- '"good"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ

### L061

    

หน้าที่: บรรทัดว่างแบ่งกลุ่มความคิด ไม่มีคำสั่งทำงานและไม่สร้างค่า

token: ไม่มี เป็นบรรทัดว่างสำหรับจัดกลุ่มโค้ด

### L062

        return {"tasks": ordered, "daily_hours": daily_hours, "risk_count": risk_count,

หน้าที่: คืนผลให้ผู้เรียกและจบฟังก์ชันในเส้นทางนี้

token และอักขระที่มีความหมาย:

- 'return' — ส่งค่ากลับและจบการเรียก
- '{' — เปิด dict
- '"tasks"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'ordered' — list หลังเรียงลำดับ
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"daily_hours"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'daily_hours' — เวลาว่างต่อวันที่ผู้ใช้ระบุ
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"risk_count"' — string literal; quote เป็นขอบเขต ไม่เป็นส่วนของค่าข้อความ
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'risk_count' — จำนวนงานที่เกินกำหนดหรือเวลาไม่พอ
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล

### L063

                "focus": ordered[0] if ordered else None, "notice": notice}

หน้าที่: ส่วนต่อเนื่องของ dict/string/คำสั่งหลายบรรทัดที่เริ่มก่อนหน้า ต้องอ่านรวมกัน

token และอักขระที่มีความหมาย:

- '"focus"' — string ชื่อ field: งานแรกหรือ None
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'ordered' — list หลังเรียงลำดับ
- '[' — เปิด list/index/key access
- '0' — number literal สำหรับคำนวณ เปรียบเทียบ หรือกำหนดค่าเริ่มต้น
- ']' — ปิด list/index/key access
- 'if' — ตรวจเงื่อนไขแรก
- 'ordered' — list หลังเรียงลำดับ
- 'else' — รับกรณีที่เงื่อนไขก่อนหน้าไม่ตรง
- 'None' — ค่าไม่มีข้อมูล ไม่ใช่ข้อความและไม่ใช่ศูนย์
- ',' — คั่นสมาชิก argument หรือคู่ข้อมูล
- '"notice"' — string ชื่อ field: ข้อความแจ้งค่าที่ไม่ถูกต้อง
- ':' — เปิดบล็อกหรือคั่น key กับ value
- 'notice' — identifier ของ ข้อความแจ้งค่าที่ไม่ถูกต้อง
- '}' — ปิด dict

## ตัวอย่างค่าจริง ณ 29 กันยายน 2569

data.json มีงานเปิดเจ็ดงาน เหลือรวมยี่สิบเก้าชั่วโมง เกินกำหนดสามงาน และใกล้ส่งตามนิยามหน้า1หนึ่งงาน เมื่อหน้า3ใช้สองชั่วโมงต่อวัน ผลสะสมเป็นดังนี้:

| งาน | days left | ชั่วโมงงาน | ชั่วโมงสะสม | capacity | ผล |
|---|---:|---:|---:|---:|---|
| วงจร | -3 | 4 | 4 | ไม่คำนวณ | เกินกำหนด gap 4 |
| อนุพันธ์ | -2 | 4 | 8 | ไม่คำนวณ | เกินกำหนด gap 4 |
| สรุปแล็บ | -1 | 4 | 12 | ไม่คำนวณ | เกินกำหนด gap 4 |
| ภาษาอังกฤษ | 2 | 6 | 18 | 6 | ขาด 12 |
| โครงงาน | 5 | 6 | 24 | 12 | ขาด 12 |
| โปสเตอร์ | 7 | 3 | 27 | 16 | ขาด 11 |
| ทบทวน | 9 | 2 | 29 | 20 | ขาด 9 |

ผลนี้เปลี่ยนตามวันที่จริงและข้อมูลจริง ต้องชี้ค่าบนหน้าจอวันนำเสนอ

## คำถามทบทวน

1. Assignment ช่วยอะไร: รวม field กับสูตรกลาง ลดโอกาสแต่ละหน้าใช้กติกาไม่เหมือนกัน
2. dict(row) ช่วยอะไร: สำเนา dict ก่อนเติม field แสดงผล ไม่เติมลงข้อมูลต้นทางโดยตรง
3. เหตุใด ISO string เรียงตามวันได้: รูปปีเดือนไว้หน้าและเติมศูนย์ เมื่อตรวจรูปถูกต้องลำดับข้อความตรงลำดับวัน
4. เหตุใดตรวจทั้ง HTML และ Python: HTML ช่วยผู้ใช้แต่ request ถูกแก้ได้ Python จึงตรวจอีกครั้งก่อน save
5. value != value คืออะไร: NaN เป็นค่าพิเศษที่ไม่เท่ากับตัวเอง
6. เหตุใดงานเกินกำหนดกระทบงานอนาคต: cumulative ถูกบวกก่อน if days left ติดลบ
7. คะแนนอัตโนมัติ 60 เต็ม 60 พิสูจน์สูตรทั้งหมดหรือไม่: ไม่ ตัวตรวจดูหน้าเปิดได้และพื้นฐานโครงสร้าง สูตรและ edge case ต้องทดสอบแยก

## Coverage

| ไฟล์ | อธิบาย | SHA-256 |
|---|---:|---|
| models.py | 18/18 | 085065c4aebb680472253967fe5bbda8f3086707eb32503e8c39a108f3b324e8 |
| pages/page1.py | 63/63 | 0be8c1e56c4f38cbfa256c8493d3af70ed189dbfbaefd82674506802ecff0f23 |
| pages/page2.py | 86/86 | c384dcb77d540e87134fe25fb638631d9c053e364b0260eff39cc73c0fa4f8e5 |
| pages/page3.py | 63/63 | 0cd4fb940f5572aef7d82536b44b9ddb04fad296094182f6f55f62b47f388666 |

รวม 230 physical lines ทุกบรรทัดแสดง source หน้าที่ และ token หรือระบุว่าเป็นบรรทัดว่าง
