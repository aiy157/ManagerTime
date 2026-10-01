"""Build source-grounded study documents; does not modify app or task data."""
import ast
import hashlib
import html
from html.parser import HTMLParser
import io
import json
import keyword
from pathlib import Path
import re
import tokenize

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "current"
META = json.loads((HERE / "study_metadata.json").read_text(encoding="utf-8"))
SYMBOLS = json.loads((HERE / "study_symbols.json").read_text(encoding="utf-8"))
GROUPS = json.loads((HERE / "study_questions.json").read_text(encoding="utf-8"))
FN = SYMBOLS["functions"]
NAMES = SYMBOLS["names"]
DAY = "30 กันยายน 2569 (2026-09-30)"
BT = chr(96)

OPS = {
    "=": "กำหนดค่า/default/keyword argument ไม่ใช่การเปรียบเทียบ",
    "==": "เปรียบเทียบเท่ากัน", "!=": "เปรียบเทียบไม่เท่ากัน",
    ">": "มากกว่า", "<": "น้อยกว่า", ">=": "มากกว่าหรือเท่ากับ",
    "<=": "น้อยกว่าหรือเท่ากับ", "+": "บวกเลข/ต่อข้อความตามชนิด",
    "-": "ลบ/เครื่องหมายติดลบ", "*": "คูณ/ทำซ้ำข้อความ/ขยาย argument ตามตำแหน่ง",
    "/": "หาร; กับ pathlib.Path เป็นการต่อ path", "**": "ขยาย keyword arguments หรือยกกำลังตามบริบท",
    ".": "เข้าถึง attribute/method ของชื่อด้านซ้าย", ",": "คั่นสมาชิก/argument",
    ":": "เริ่ม block หรือคั่น key:value ใน dict ตามบริบท",
    "(": "เปิดกลุ่มนิพจน์/argument/tuple", ")": "ปิดกลุ่มที่เปิดด้วย (",
    "[": "เปิด list หรือการอ้าง index/key", "]": "ปิด list/การอ้าง index/key",
    "{": "เปิด dict/set ตามบริบท", "}": "ปิด dict/set", "@": "เริ่ม decorator ในชุดทดสอบ",
}
FIELDS = {
    "title": "ชื่องาน", "course": "วิชาที่เกี่ยวข้อง", "due_date": "วันส่งรูปแบบ YYYY-MM-DD",
    "estimated_hours": "ชั่วโมงรวมที่คาดว่าจะใช้", "done_hours": "ยอดชั่วโมงความคืบหน้าสะสม",
    "priority": "ความสำคัญ high/normal/low", "details": "รายละเอียดซ้อนของงาน",
    "owner": "รหัสสมาชิกผู้รับผิดชอบ; ว่างหมายถึงไม่มอบหมาย",
    "started": "boolean ว่าเริ่มงานแล้ว", "subtasks": "list ขั้นตอนย่อย",
    "history": "list ประวัติกิจกรรม/เวลา", "created_on": "วันที่สร้าง; ว่างเมื่อไม่รู้ของข้อมูลเดิม",
    "progress_on": "วันที่อัปเดตกิจกรรม; ว่างเมื่อยังไม่มีข้อมูล",
    "before_complete": "ยอดก่อนกดปิดเพื่อเปิดกลับ", "completed_on": "วันที่ปิดงาน",
    "date": "วันที่ของประวัติ", "hours": "ชั่วโมงตามชนิดรายการ",
    "kind": "ชนิด work/adjustment/complete/reopen", "note": "หมายเหตุ",
    "done": "boolean ว่างานย่อยถูกติ๊กเสร็จหรือไม่", "daily_hours": "งบเวลาว่างรายวัน",
    "group": "ข้อมูลกลุ่ม", "members": "รายการสมาชิก", "name": "ชื่อกลุ่ม/สมาชิกตาม path",
    "section": "ข้อความกลุ่มหรือ section ที่ผู้ใช้ให้", "topic": "หัวข้อโครงการ",
    "description": "คำอธิบายหัวข้อ", "id": "รหัสสมาชิกแบบ string", "role": "บทบาทในรายวิชา",
    "task": "ส่วนของโครงงานรายวิชาที่รับผิดชอบ",
}
ATTRS = {
    "class": "ชื่อ class ที่ CSS ใช้เลือกตกแต่ง", "id": "ชื่อเฉพาะ DOM/anchor/label",
    "name": "key ที่ส่งไปใน form", "value": "ค่าที่ส่ง/ค่าเริ่มต้น; ไม่ใช่ชื่อ key",
    "type": "ชนิดช่องหรือปุ่ม", "method": "วิธีส่ง form (post ไป handle)",
    "action": "URL ปลายทาง form", "href": "ปลายทางลิงก์/anchor",
    "for": "id ของช่องที่ label อธิบาย", "required": "ให้เบราว์เซอร์บังคับค่าตามชนิด",
    "min": "ค่าต่ำสุดที่ช่องรับในเบราว์เซอร์", "max": "ค่าสูงสุดที่ช่องรับในเบราว์เซอร์",
    "step": "ขั้นค่าที่เบราว์เซอร์ใช้ตรวจตัวเลข", "maxlength": "จำนวนอักขระสูงสุดในช่อง",
    "placeholder": "ตัวอย่างก่อนกรอก ไม่ได้ส่งเป็นค่าโดยตัวมันเอง",
    "hidden": "ซ่อนตาม HTML/กฎ CSS; ยังไม่ใช่สิทธิ์เข้าถึง",
    "role": "บทบาทเชิงความหมายให้เครื่องมือเข้าถึง",
    "aria-label": "คำอธิบายสำหรับเครื่องมืออ่านหน้าจอ",
    "aria-labelledby": "id ของข้อความที่ตั้งชื่อส่วนนี้",
    "aria-describedby": "id ของข้อความช่วยอธิบาย",
    "aria-hidden": "กำหนดว่าตัดส่วนนี้ออกจาก accessibility tree",
    "aria-live": "ให้แจ้งข้อความที่เปลี่ยนอย่างสุภาพตามค่าที่กำหนด",
    "aria-pressed": "สถานะกดของปุ่ม toggle ไม่ใช่ชั่วโมงทำงาน",
    "aria-valuenow": "ค่าปัจจุบันของ progressbar",
    "aria-valuemin": "ขอบล่าง progressbar", "aria-valuemax": "ขอบบน progressbar",
    "datetime": "วันที่มาตรฐานของ time", "rows": "ความสูง textarea เป็นบรรทัด",
    "tabindex": "ลำดับ/ความสามารถรับ focus จากคีย์บอร์ด",
    "style": "CSS เฉพาะ element; progress เป็นเปอร์เซ็นต์ที่ Python คำนวณ",
    "onsubmit": "JavaScript เมื่อส่ง form; confirm ลบข้อมูล",
    "src": "ไฟล์ script ที่โหลด", "defer": "รัน script ภายนอกหลังแยก HTML เสร็จ",
    "selected": "option ที่เลือกตอนสร้าง HTML",
    "data-assignment-form": "marker ให้ forms.js ผูก validation",
    "data-today": "วันที่อ้างอิงจาก Python ให้ forms.js",
    "data-original-date": "วันเดิมเพื่อไม่ยืนยันอดีตเดิมซ้ำ",
    "data-past-warning": "marker กล่องยืนยันวันที่อดีต",
    "data-subtask-template": "id textarea เป้าหมายของขั้นตอนตัวอย่าง",
    "data-calendar-title": "ชื่อสำหรับไฟล์ปฏิทิน",
    "data-calendar-course": "วิชาสำหรับไฟล์ปฏิทิน",
    "data-calendar-date": "วันส่งสำหรับไฟล์ปฏิทิน",
}
TAGS = {
    "section": "ส่วนเนื้อหาที่มีหัวข้อ", "div": "กลุ่ม layout",
    "span": "ข้อความย่อยในบรรทัด", "h1": "หัวข้อหลักหน้า", "h2": "หัวข้อส่วน",
    "h3": "หัวข้องาน/การ์ด", "h4": "หัวข้อย่อยในรายละเอียด",
    "p": "ย่อหน้าหรือคำอธิบาย", "a": "ลิงก์", "button": "ปุ่มกระทำ",
    "form": "ชุดข้อมูลที่จะส่ง", "input": "ช่องรับ/ค่าซ่อน",
    "label": "ชื่อ/คำอธิบายของช่อง", "small": "ข้อความประกอบ",
    "strong": "ข้อความที่เน้น", "article": "การ์ดงาน/สมาชิกหนึ่งรายการ",
    "details": "ส่วนยุบ/เปิดได้", "summary": "ตัวควบคุมเปิดรายละเอียด",
    "ul": "รายการแบบไม่มีเลข", "li": "สมาชิกในรายการ",
    "select": "ตัวเลือก", "option": "ตัวเลือกหนึ่งค่า", "textarea": "ข้อความหลายบรรทัด",
    "time": "ข้อมูลวันที่ที่มีความหมาย", "table": "ตาราง",
    "thead": "หัวตาราง", "tbody": "เนื้อตาราง", "tr": "แถว",
    "th": "ชื่อคอลัมน์", "td": "ช่องข้อมูล", "br": "ขึ้นบรรทัดใน HTML", "script": "script/JSON ตาม type",
}
CSS = {
    "display": "วิธีจัดวาง/การแสดง", "flex": "สัดส่วนและพฤติกรรม flex item",
    "flex-direction": "ทิศทางของ flex", "flex-wrap": "ให้ flex ขึ้นบรรทัดใหม่",
    "align-items": "แนวจัดวางบนแกนขวาง", "align-self": "แนวจัดวางเฉพาะ item",
    "justify-content": "จัดพื้นที่บนแกนหลัก", "gap": "ช่องว่างระหว่าง item",
    "grid-template-columns": "จำนวน/สัดส่วนคอลัมน์ grid",
    "width": "ความกว้าง", "height": "ความสูง", "min-width": "ความกว้างต่ำสุด",
    "max-width": "ความกว้างสูงสุด", "min-height": "ความสูงต่ำสุด",
    "margin": "ระยะภายนอก", "margin-top": "ระยะนอกด้านบน", "margin-bottom": "ระยะนอกด้านล่าง",
    "padding": "ระยะภายใน", "padding-top": "ระยะในด้านบน", "padding-left": "ระยะในซ้าย",
    "padding-right": "ระยะในขวา", "color": "สีตัวอักษร", "background": "พื้นหลัง/gradient",
    "background-color": "สีพื้นหลัง", "font-size": "ขนาดอักษร", "font-weight": "น้ำหนักอักษร",
    "font-family": "ชุดฟอนต์ตามลำดับ", "font": "รูปแบบฟอนต์แบบย่อ",
    "font-variant-numeric": "รูปแบบตัวเลข เช่นกว้างเท่ากัน",
    "line-height": "ระยะบรรทัด", "text-align": "แนวข้อความ", "text-transform": "รูปแบบตัวพิมพ์",
    "letter-spacing": "ช่องห่างอักขระ", "text-decoration": "รูปแบบเส้นตกแต่งข้อความ",
    "text-underline-offset": "ระยะเส้นใต้", "border": "เส้นขอบแบบย่อ",
    "border-top": "เส้นขอบบน", "border-bottom": "เส้นขอบล่าง",
    "border-color": "สีเส้นขอบ", "border-radius": "ความโค้งมุม",
    "border-bottom-color": "สีขอบล่าง", "border-bottom-width": "ความหนาขอบล่าง",
    "overflow": "การจัดการส่วนล้น", "overflow-x": "การจัดการส่วนล้นแนวนอน",
    "overflow-wrap": "การตัดข้อความยาว", "white-space": "การรักษา/ตัดช่องว่างและบรรทัด",
    "position": "รูปแบบตำแหน่ง", "top": "ตำแหน่งจากบน",
    "cursor": "รูปตัวชี้", "box-shadow": "เงา", "transform": "แปลงตำแหน่ง/หมุน",
    "transition": "การเปลี่ยนลักษณะระหว่างสถานะ", "opacity": "ความทึบ",
    "flex-shrink": "การหดตัว flex item", "resize": "ทิศที่ผู้ใช้ปรับ textarea ได้",
    "outline": "เส้น focus ที่ไม่ใช้พื้นที่ layout", "outline-offset": "ระยะของเส้น focus",
    "scroll-margin-top": "ระยะเมื่อเลื่อนมาที่ anchor", "vertical-align": "แนวข้อมูลใน table",
    "object-fit": "วิธีวางภาพในกรอบ", "box-sizing": "วิธีรวม padding/border ในขนาด",
    "border-collapse": "การรวมเส้นขอบตาราง", "accent-color": "สี control ตาม browser",
    "list-style": "รูป marker ของรายการ",
}

def code(value):
    return BT + str(value).replace(BT, "&#96;").replace("\n", "\\n") + BT

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def doc_path(relative):
    return OUT / "files" / (relative + ".md")

def doc_link(relative, prefix=""):
    return prefix + "files/" + relative + ".md"

def expr(node):
    if node is None:
        return "ไม่มีค่า"
    if isinstance(node, ast.Name):
        return code(node.id)
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "None (ไม่มีค่าที่ใช้ได้)"
        return code(repr(node.value))
    if isinstance(node, ast.Attribute):
        return code(ast.unparse(node))
    if isinstance(node, ast.Subscript):
        return code(ast.unparse(node)) + " (อ่าน key/index)"
    if isinstance(node, ast.Compare):
        meanings = {ast.Eq:"เท่ากับ",ast.NotEq:"ไม่เท่ากับ",ast.Lt:"น้อยกว่า",
                    ast.Gt:"มากกว่า",ast.LtE:"ไม่เกิน",ast.GtE:"อย่างน้อย",
                    ast.Is:"เป็น object เดียวกับ",ast.IsNot:"ไม่เป็น object เดียวกับ",
                    ast.In:"อยู่ใน",ast.NotIn:"ไม่อยู่ใน"}
        parts = [expr(node.left)]
        for op, right in zip(node.ops, node.comparators):
            parts += [meanings.get(type(op), "เปรียบเทียบ"), expr(right)]
        return " ".join(parts)
    if isinstance(node, ast.BoolOp):
        joiner = " และ " if isinstance(node.op, ast.And) else " หรือ "
        return joiner.join(expr(v) for v in node.values)
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.Not):
            return "ไม่เป็นจริง: " + expr(node.operand)
        return code(ast.unparse(node))
    if isinstance(node, ast.Dict):
        return "dict ที่มี key " + ", ".join(expr(k) for k in node.keys if k is not None)
    if isinstance(node, (ast.List, ast.Set, ast.Tuple)):
        label = {ast.List:"list",ast.Set:"set",ast.Tuple:"tuple"}[type(node)]
        if len(node.elts) <= 4:
            return label + " [" + ", ".join(expr(x) for x in node.elts) + "]"
        return label + " จำนวน " + str(len(node.elts)) + " สมาชิกตามโค้ด"
    if isinstance(node, ast.Call):
        name = ast.unparse(node.func)
        tail = name.rsplit(".",1)[-1]
        if name == "storage.load":
            return "อ่านรายการงานล่าสุดผ่าน storage.load()"
        if name == "storage.save":
            return "เขียนรายการงานทั้งไฟล์ผ่าน storage.save()"
        if tail in ("append","push"):
            return "เพิ่ม " + expr(node.args[0]) + " ไปท้าย " + expr(node.func.value)
        if tail in ("remove","pop"):
            return "เอาสมาชิก/key ออกจาก " + expr(node.func.value) + " ตาม argument ในโค้ด"
        if tail == "get":
            return "อ่าน " + expr(node.args[0]) + " จาก " + expr(node.func.value) + " พร้อม default เมื่อไม่มี"
        if tail == "setdefault":
            return "เติม " + expr(node.args[0]) + " ใน " + expr(node.func.value) + " เฉพาะเมื่อ key หาย"
        if tail in FN:
            return "เรียก " + code(name) + ": " + FN[tail]
        if tail in ("min","max","len","round","int","float","str","dict","list","abs"):
            return code(name) + "(" + ", ".join(expr(a) for a in node.args) + ")"
        return "เรียก " + code(name) + " ด้วย argument ที่แสดงในโค้ด"
    if isinstance(node, ast.BinOp):
        label = {ast.Add:"บวก/ต่อ",ast.Sub:"ลบ",ast.Mult:"คูณ/ทำซ้ำ",ast.Div:"หาร/ต่อ Path",
                 ast.Mod:"หารเอาเศษ",ast.Pow:"ยกกำลัง"}.get(type(node.op), "คำนวณ")
        return "(" + expr(node.left) + " " + label + " " + expr(node.right) + ")"
    return code(ast.unparse(node))

def statement(node):
    if isinstance(node, ast.ClassDef):
        return "ประกาศ class " + code(node.name) + " เป็นแบบแทนงาน; ไม่ได้สร้าง object จนกว่าจะเรียก constructor"
    if isinstance(node, ast.FunctionDef):
        note = FN.get(node.name)
        if node.name in ("build","handle"):
            note = "build เตรียม context จาก GET" if node.name == "build" else "handle รับฟอร์ม POST และคืนข้อความ"
        return "ประกาศฟังก์ชัน " + code(node.name) + ": " + (note or "ทำงานเมื่อมีผู้เรียกตาม body ด้านล่าง")
    if isinstance(node, (ast.Import,ast.ImportFrom)):
        return "นำเข้าชื่อ/module ที่ใช้ในไฟล์: " + code(ast.unparse(node))
    if isinstance(node, ast.Assign):
        targets = ", ".join(code(ast.unparse(x)) for x in node.targets)
        return "เก็บผล " + expr(node.value) + " ลง " + targets
    if isinstance(node, ast.AugAssign):
        return "ปรับค่า " + expr(node.target) + " ด้วย " + expr(node.value) + " ตาม operator"
    if isinstance(node, ast.Return):
        return "คืนให้ผู้เรียกและจบฟังก์ชันรอบนี้: " + expr(node.value)
    if isinstance(node, ast.If):
        return "ตรวจเงื่อนไข: " + expr(node.test) + "; เมื่อจริงจึงทำ body ที่ย่อหน้าต่อไป"
    if isinstance(node, (ast.For, ast.AsyncFor)):
        return "วน " + expr(node.iter) + " ให้ " + expr(node.target) + " รับสมาชิกทีละรอบ"
    if isinstance(node, ast.While):
        return "ทำซ้ำขณะ " + expr(node.test) + " เป็นจริง; body ต้องเปลี่ยนข้อมูลจนจบรอบได้"
    if isinstance(node, ast.With):
        return "ใช้ resource ใน with: " + "; ".join(expr(x.context_expr) for x in node.items) + "; ออกจาก block แล้วปิด resource ตาม context manager"
    if isinstance(node, ast.Try):
        return "ลองคำสั่งใน try; หากเกิด exception ที่ระบุจึงเข้า except"
    if isinstance(node, ast.ExceptHandler):
        return "รับ exception " + (expr(node.type) if node.type else "ตามที่ระบุ") + " แล้วทำ branch นี้"
    if isinstance(node, ast.Assert):
        return "ตรวจคำตอบใน test: ต้องให้ " + expr(node.test) + " เป็นจริง มิฉะนั้น test ไม่ผ่าน"
    if isinstance(node, ast.Delete):
        return "ลบ key/รายการ " + ", ".join(expr(t) for t in node.targets) + " ในข้อมูลทดสอบ"
    if isinstance(node, ast.Expr):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return "ข้อความ docstring อธิบาย module/function ไม่ใช่คำสั่งบันทึกงาน"
        return expr(node.value)
    if isinstance(node, ast.Continue):
        return "ข้ามส่วนที่เหลือของรอบนี้และไปสมาชิกถัดไป"
    if isinstance(node, ast.Break):
        return "ออกจาก loop ที่ครอบคำสั่งนี้"
    if isinstance(node, ast.Raise):
        return "ส่ง exception/exit ตามค่าที่ระบุ ไม่ใช่ return context"
    return "คำสั่ง " + code(type(node).__name__) + " ตามโค้ดจริง"

def python_notes(source):
    tree = ast.parse(source)
    nodes = [n for n in ast.walk(tree) if isinstance(n,(ast.stmt,ast.ExceptHandler))]
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    byline = {}
    names = set()
    for t in tokens:
        byline.setdefault(t.start[0], []).append(t)
        if t.type == tokenize.NAME and not keyword.iskeyword(t.string):
            names.add(t.string)
    funcs = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef,ast.ClassDef)):
            funcs.append((n.lineno,n.end_lineno,n.name,statement(n)))
    funcs.sort()
    result = []
    for line_no,line in enumerate(source.splitlines(),1):
        stripped = line.strip()
        notes = []
        if not stripped:
            notes.append("บรรทัดว่าง แยกส่วนให้คนอ่าน ไม่มีคำสั่งทำงาน")
        elif stripped.startswith("#"):
            notes.append("comment สำหรับผู้อ่าน: " + stripped[1:].strip())
        elif stripped.startswith("@"):
            notes.append("decorator ของ pytest; fixture/parametrize จัดการข้อมูลชั่วคราวหรือขยายกรณีทดสอบ ไม่ใช่ route ของแอป")
        elif stripped in ("else:","finally:"):
            notes.append("else: ทำทางเลือกเมื่อเงื่อนไขก่อนหน้าไม่จริง" if stripped == "else:" else "finally: ทำเสมอหลัง try เพื่อปิด/คืนสภาพ resource")
        else:
            matches = [n for n in nodes if n.lineno <= line_no <= n.end_lineno]
            starts = [n for n in matches if n.lineno == line_no]
            choices = starts or matches
            if choices:
                node = min(choices,key=lambda n:(n.end_lineno-n.lineno, -n.lineno))
                if node.lineno != line_no:
                    notes.append("ส่วนต่อ/ปิดนิพจน์ของคำสั่งเริ่ม L" + str(node.lineno) + ": " + statement(node))
                else:
                    notes.append(statement(node))
            else:
                notes.append("ส่วนของนิพจน์/รายการ argument ที่เปิดจากบรรทัดก่อนหน้า อ่านต่อรวมเป็นคำสั่งเดียว")
        ts = byline.get(line_no,[])
        operators = list(dict.fromkeys(t.string for t in ts if t.type == tokenize.OP))
        if operators:
            notes.append("เครื่องหมาย: " + "; ".join(code(op) + " " + OPS.get(op,"ตาม syntax Python") for op in operators))
        used = list(dict.fromkeys(t.string for t in ts if t.type == tokenize.NAME and t.string in NAMES))
        if used:
            notes.append("ชื่อที่ต้องรู้: " + "; ".join(code(n) + " = " + NAMES[n] for n in used))
        indent = len(line) - len(line.lstrip(" "))
        if indent and stripped:
            notes.append("ย่อหน้า " + str(indent) + " ช่องว่าง: อยู่ใน block ที่เปิดก่อนหน้า; Python ใช้ indentation จัดโครงสร้าง")
        result.append(notes)
    return result,funcs,sorted(names)

JINJA = re.compile(r"({{.*?}}|{%.*?%}|{#.*?#})",re.S)
def jinja_note(token):
    if token.startswith("{{"):
        inside = token[2:-2].strip()
        if "url_for(" in inside:
            return "สร้าง URL ผ่าน route เดิม: " + code(inside)
        if "|tojson" in inside:
            return "serialize ข้อมูลเป็น JSON สำหรับ script data: " + code(inside)
        if "row_fields(" in inside:
            return "เรียก macro ใส่ no/version ซ่อนใน form: " + code(inside)
        if "quick_actions(" in inside:
            return "เรียก macro ปุ่ม start/complete/reopen ตาม item และหน้า: " + code(inside)
        if "task_card(" in inside:
            return "เรียก macro การ์ดงานร่วม: " + code(inside)
        return "แสดงค่าจาก context/นิพจน์ Jinja: " + code(inside)
    if token.startswith("{#"):
        return "comment Jinja ไม่ถูกส่งเป็นข้อความหน้าเว็บ"
    inside = token[2:-2].strip()
    kind = inside.split()[0] if inside else ""
    notes = {
        "extends":"ใช้โครงแม่ base.html", "block":"เปิดส่วนที่แม่แบบแม่อนุญาตให้แทน",
        "endblock":"จบ block content/scripts", "from":"นำเข้า macro ย่อย",
        "import":"นำเข้าแม่แบบย่อย", "macro":"นิยาม macro รับ argument แล้วสร้างชิ้น HTML",
        "endmacro":"จบ macro", "for":"วน list จาก context",
        "endfor":"จบ for", "if":"ตรวจเงื่อนไขก่อนแสดง HTML", "elif":"ตรวจเงื่อนไขทางเลือก",
        "else":"ทางเลือกของ if หรือกรณี for ไม่มีสมาชิก ต้องดู block ที่ครอบ",
        "endif":"จบเงื่อนไข", "set":"กำหนดค่าภายใน template",
    }
    return notes.get(kind,"คำสั่ง Jinja") + ": " + code(inside)

class HtmlNotes(HTMLParser):
    def __init__(self, restore):
        super().__init__(convert_charrefs=False)
        self.notes = {}
        self.restore = restore
    def add(self,text):
        self.notes.setdefault(self.getpos()[0],[]).append(text)
    def restore_text(self,text):
        for marker,value in self.restore.items():
            text = text.replace(marker,value)
        return text
    def handle_starttag(self,tag,attrs):
        self.add("เปิด " + code("<"+tag+">") + ": " + TAGS.get(tag,"element HTML"))
        for key,val in attrs:
            val = self.restore_text(val or "")
            self.add(code(key) + ("="+code(val) if val else "") + ": " + ATTRS.get(key,"attribute ตาม HTML/DOM ที่ส่วนนี้ใช้งาน"))
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        self.add("tag นี้ปิดในตัว ไม่เปิด container ให้ลูก")
    def handle_endtag(self,tag):
        self.add("ปิด " + code("</"+tag+">") + " ที่เปิดไว้ก่อนหน้า")
    def handle_data(self,data):
        value = self.restore_text(data).strip()
        if value and not value.startswith("{{") and not value.startswith("{%"):
            self.add("ข้อความ/ข้อมูลในส่วนนี้ตามโค้ด: " + code(value))
    def handle_entityref(self,name):
        self.add("HTML entity "+code("&"+name+";")+" แทนอักขระเมื่อตีความ HTML")
    def handle_charref(self,name):
        self.add("HTML character reference "+code("&#"+name+";")+" เช่น &#10; เป็นขึ้นบรรทัด")
    def handle_comment(self,data):
        self.add("comment HTML สำหรับผู้อ่าน")

def html_notes(source):
    restore={}
    def mask(match):
        marker = "JINJA_MARK_"+str(len(restore))+"_END"
        restore[marker]=match.group(0)
        # Existing templates have their expressions/blocks on single lines.
        return marker + "\n" * match.group(0).count("\n")
    masked=JINJA.sub(mask,source)
    parser=HtmlNotes(restore)
    parser.feed(masked)
    result=[]
    for i,line in enumerate(source.splitlines(),1):
        notes=[jinja_note(t) for t in JINJA.findall(line)]
        notes += parser.notes.get(i,[])
        if not line.strip():
            notes=["บรรทัดว่าง แยกส่วนของ template ไม่มี element เพิ่ม"]
        if not notes:
            notes=["ส่วนต่อของ HTML/ข้อความที่เปิดก่อนหน้า อ่านตาม container ที่ครอบ"]
        result.append(list(dict.fromkeys(notes)))
    return result,[],[]

def css_notes(source):
    result=[]
    stack=[]
    for line in source.splitlines():
        stripped=line.strip()
        notes=[]
        if not stripped:
            notes=["บรรทัดว่างแบ่งกลุ่มกฎ ไม่มีผลตกแต่ง"]
        elif stripped.startswith("/*"):
            notes=["comment บอกส่วนของ stylesheet: "+stripped]
        else:
            for match in re.finditer(r"([^{}]+)\{",line):
                selector=match.group(1).strip()
                if selector.startswith("@media"):
                    notes.append("เงื่อนไขขนาดจอ: "+code(selector)+" กฎภายในใช้เมื่อเข้าเงื่อนไข")
                else:
                    notes.append("selector "+code(selector)+" เลือก element/class ตามที่เขียน; descendant/child/pseudo-selector ขึ้นกับเครื่องหมาย")
                stack.append(selector)
            # Properties occur after { or at the start of a multiline rule.
            for prop,value in re.findall(r"(?:^|[;{])\s*([-\w]+)\s*:\s*([^;{}]+)",line):
                if prop.startswith("--"):
                    meaning="นิยามตัวแปร CSS ให้ var(...) อ้างใช้"
                else:
                    meaning=CSS.get(prop,"property CSS ของกฎที่เลือก")
                notes.append(code(prop)+": "+meaning+" = "+code(value.strip()))
            for _ in range(line.count("}")):
                notes.append("} จบ block ของกฎ/เงื่อนไข"+(" "+code(stack.pop()) if stack else ""))
            if ":focus-visible" in line:
                notes.append("focus-visible ช่วยเห็นตำแหน่งคีย์บอร์ด ไม่ใช่สถานะงาน")
            if "[hidden]" in line:
                notes.append("selector ใช้ attribute hidden ร่วม display:none ของส่วนเตือน")
            if "var(" in line:
                notes.append("var(...) อ่าน CSS custom property; สีมาจาก :root หรือค่าที่กำหนด")
        result.append(notes or ["ส่วนต่อของกฎ CSS ที่เปิดก่อนหน้า"])
    return result,[],[]

JS_METHODS = {
    "querySelectorAll":"เลือก DOM ที่ตรง selector ทั้งชุด",
    "querySelector":"เลือก DOM ที่ตรง selectorหนึ่ง element",
    "getElementById":"หา element ด้วย id", "addEventListener":"ผูกฟังก์ชันกับ event",
    "setCustomValidity":"ตั้ง/ล้างข้อความ validation ของช่อง",
    "setAttribute":"เปลี่ยน attribute ใน DOM", "checkValidity":"ตรวจ form ตาม constraint",
    "reportValidity":"ให้ browser แสดงจุดผิด", "preventDefault":"หยุดการส่ง form ปกติ",
    "filter":"เลือกสมาชิกที่เงื่อนไขจริง", "map":"สร้าง array ใหม่จากสมาชิก",
    "forEach":"ทำ callback ต่อสมาชิก", "split":"แยกข้อความ", "join":"ต่อรายการเป็นข้อความ",
    "padStart":"เติมอักขระข้างหน้าให้ความยาวครบ", "parseFromString":"อ่าน HTML snapshot ที่ fetch ได้",
    "requestPermission":"ขอสิทธิ์ Notification จากการกดของผู้ใช้",
    "setInterval":"ตั้งงานตรวจข้อมูลซ้ำ 60000 ms", "setTimeout":"ตั้ง timeout สำหรับ fetch/คืน URL",
    "clearTimeout":"ยกเลิก timeout ที่เสร็จแล้ว",
    "getItem":"อ่าน signature จาก localStorage", "setItem":"จำ signature ลง localStorage",
    "createObjectURL":"สร้าง URL ชั่วคราวของ Blob", "revokeObjectURL":"คืนทรัพยากร URL หลังใช้",
    "closest":"หา element นี้หรือบรรพบุรุษที่ตรง marker",
    "focus":"ย้าย focus ไป element/หน้าต่าง", "scrollIntoView":"เลื่อนให้เห็นการ์ด",
    "replace":"แทนข้อความตามรูปแบบ", "slice":"ตัดช่วงข้อความ",
    "remove":"เอาลิงก์ดาวน์โหลดชั่วคราวออกจาก DOM",
    "appendChild":"เพิ่มลิงก์ดาวน์โหลดชั่วคราวใน DOM", "click":"กระตุ้นดาวน์โหลดตามลิงก์",
    "abort":"ยกเลิก fetch ที่ใช้เวลานาน",
    "runInNewContext":"รัน source ในส่วนจำลอง Node vm ไม่ใช่ browser จริง",
    "readFileSync":"อ่าน reminders.js สำหรับ Node test",
    "equal":"assert ค่าเท่ากันใน test", "match":"assert ข้อความตรง regex", "ok":"assert เป็นจริง",
}
def js_notes(source):
    result=[]
    functions=[]
    for no,line in enumerate(source.splitlines(),1):
        s=line.strip()
        notes=[]
        if not s:
            notes=["บรรทัดว่างแบ่งฟังก์ชัน/เหตุการณ์ ไม่ทำคำสั่ง"]
        elif s.startswith("//") or s.startswith("/*"):
            notes=["comment สำหรับคนอ่าน: "+s]
        else:
            match=re.search(r"(?:async\s+)?function\s+(\w+)\s*\((.*?)\)",s)
            if match:
                functions.append((no,no,match.group(1),"ฟังก์ชัน JavaScript ตามส่วนนี้"))
                notes.append("ประกาศ "+code(match.group(1))+" รับ "+code(match.group(2))+"; body ทำงานเมื่อเรียก")
            if re.match(r"(const|let|var)\s+",s):
                name=re.match(r"(const|let|var)\s+(\w+)",s)
                if name:
                    notes.append("สร้างตัวแปร "+code(name.group(2))+" ด้วย "+name.group(1)+
                                 (" (ไม่เปลี่ยน binding; object ยังแก้สมาชิกได้)" if name.group(1)=="const" else " (เปลี่ยนค่าภายหลังได้)"))
            if s.startswith("if"):
                notes.append("ตรวจเงื่อนไขก่อนทำคำสั่ง; return ใน guard จบรอบฟังก์ชันนี้")
            if s.startswith("else") or "else if" in s:
                notes.append("ทำทางเลือกของเงื่อนไขก่อนหน้า")
            if s.startswith("try"):
                notes.append("ลองส่วนที่อาจผิดพลาด เช่นสิทธิ์ storage/network")
            if "catch" in s:
                notes.append("รับข้อผิดพลาดตาม block นี้เพื่อไม่ให้สคริปต์หยุดทั้งหมด")
            if s.startswith("finally"):
                notes.append("ทำ cleanup แม้คืนก่อนหรือมี error")
            if s.startswith("return"):
                notes.append("คืนคำตอบหรือจบฟังก์ชันตามนิพจน์ในบรรทัด")
            if "=>" in s:
                notes.append("arrow function เป็น callback/ตัวแปลงสมาชิก ไม่ได้เรียก body ทุกส่วนทันที")
            if "await " in s:
                notes.append("รอผล Promise ภายใน async ก่อนทำขั้นตอนถัดไป โดยไม่บล็อก browser event loop ทั้งหมด")
            for method in dict.fromkeys(re.findall(r"\.(\w+)\s*\(",s)):
                if method in JS_METHODS:
                    notes.append(code(method+"()")+": "+JS_METHODS[method])
            if "JSON.parse" in s:
                notes.append("parse ข้อความ JSON เป็นค่าข้อมูล ไม่ใช่การรันโค้ดผู้ใช้")
            if "JSON.stringify" in s:
                notes.append("serialize ข้อมูลเพื่อ snapshot/signature/การเทียบ")
            if "new Notification" in s:
                notes.append("สร้าง Notification เฉพาะเมื่อเงื่อนไขและสิทธิ์ผ่าน; ใน Node harness เป็น class จำลอง")
            if "new Blob" in s:
                notes.append("รวมข้อความ ICS เป็นไฟล์ text/calendar UTF-8 ในหน่วยความจำ")
            if "fetch(" in s:
                notes.append("GET หน้า Overview เดิมเพื่ออ่าน reminder-data ล่าสุด; ไม่ส่งการแก้งาน")
            if ".textContent" in s and "=" in s:
                notes.append("อ่าน/ตั้งข้อความ DOM; textContent ไม่ตีความค่าที่ตั้งเป็นแท็ก HTML")
            if any(x in s for x in (".hidden =", ".disabled =", ".required =", ".checked =", ".open =")):
                notes.append("ปรับสถานะ control/ส่วนยุบในเบราว์เซอร์ ไม่เขียน data.json")
            if "60000" in s:
                notes.append("60000 ms = 60 วินาที; browser อาจหน่วง timer เมื่อแท็บพัก")
            if "10000" in s:
                notes.append("10000 ms = 10 วินาทีสำหรับตัดการดึงข้อมูล")
            if "86400000" in s:
                notes.append("86400000 ms = หนึ่งวัน; หารผล UTC ของวันเพื่อเทียบ deadline")
            if re.match(r"^[\]})]+[);,]*$",s):
                notes.append("ปิด block/array/call ที่เปิดในบรรทัดก่อน ตามเครื่องหมาย")
            if not notes:
                notes.append("ส่วนต่อของนิพจน์/ข้อมูล/การกำหนดค่าตามโค้ดและ block ที่ครอบ")
            marks=re.findall(r"===|!==|=>|&&|\|\||[{}\[\]();]",s)
            if marks:
                notes.append("เครื่องหมายที่พบ: "+", ".join(code(x) for x in dict.fromkeys(marks))+
                             "; ===/!== เทียบค่าและชนิด, &&/|| รวมเงื่อนไข, => callback, วงเล็บจัดกลุ่ม")
        result.append(notes)
    return result,functions,[]

def json_notes(source):
    json.loads(source)
    matches=list(re.finditer(r'"(?:\\.|[^"\\])*"|-?\d+(?:\.\d+)?(?:[Ee][+-]?\d+)?|true|false|null|[{}\[\]:,]',source))
    notes={}
    cursor=0
    def add(token,text):
        line=source.count("\n",0,token.start())+1
        notes.setdefault(line,[]).append(text)
    def parse(path):
        nonlocal cursor
        token=matches[cursor]; word=token.group(); cursor+=1
        if word=="{":
            add(token,"เปิด object "+code(path)+" เก็บ key:value")
            while matches[cursor].group()!="}":
                key_token=matches[cursor]; key=json.loads(key_token.group()); cursor+=1
                assert matches[cursor].group()==":"; cursor+=1
                add(key_token,"key "+code(key)+": "+FIELDS.get(key,"ค่าของโครงสร้างนี้"))
                parse(path+"."+key)
                if matches[cursor].group()==",": cursor+=1
                else: break
            add(matches[cursor],"ปิด object "+code(path));cursor+=1
        elif word=="[":
            add(token,"เปิด array "+code(path)+" เก็บหลายรายการเรียงลำดับ")
            index=0
            while matches[cursor].group()!="]":
                parse(path+"["+str(index)+"]");index+=1
                if matches[cursor].group()==",":cursor+=1
                else:break
            add(matches[cursor],"ปิด array "+code(path)+" จำนวน "+str(index)+" รายการ");cursor+=1
        else:
            value=json.loads(word)
            meaning="string" if isinstance(value,str) else "boolean" if isinstance(value,bool) else "null" if value is None else "number"
            extra=""
            if value=="": extra="; ค่าว่างตามข้อมูลนี้ ไม่เดาประวัติ/ผู้รับผิดชอบใหม่"
            add(token,code(path)+" = "+code(word)+" ("+meaning+")"+extra)
    parse("$")
    result=[]
    for i,line in enumerate(source.splitlines(),1):
        extra="comma คั่นสมาชิก และ colon คั่น key:value ตาม JSON; ห้าม trailing comma/comment"
        result.append(notes.get(i,["ส่วนคั่น/บรรทัดว่างของ JSON ตามโครงสร้าง"]) + ([extra] if "," in line or ":" in line else []))
    return result,[],[]

BAT_NOTES=[
    "ปิดการแสดงคำสั่งแต่ยังแสดงผลลัพธ์ เพื่อลดความรก terminal",
    "เปลี่ยน code page เป็น UTF-8 แล้วซ่อนข้อความคำสั่งด้วย >nul",
    "ย้าย drive/โฟลเดอร์เป็นตำแหน่งสคริปต์จาก %~dp0",
    "หากไม่มี Python ใน .venv ให้บอกทำ setup, pause และ exit /b 1",
    "ตั้ง encoding ของ stdout/stderr Python เป็น UTF-8",
    "เรียกตัวตรวจอาจารย์ซึ่งตรวจคะแนน/hash และอาจ reset data จาก sample",
    "แสดงบรรทัดว่าง",
    "แสดงหัวข้อ pytest",
    "รัน pytest -q ผ่าน Python ใน .venv รวม test file ที่พบ",
    "pause รอผู้ใช้ดูผลก่อนปิดหน้าต่าง",
]
def other_notes(source,relative):
    result=[]
    for i,line in enumerate(source.splitlines(),1):
        s=line.strip()
        if relative=="check.bat":
            text=BAT_NOTES[i-1]
        elif not s:
            text="บรรทัดว่างแยกย่อหน้า"
        elif s.startswith("#"):
            text="หัวข้อ Markdown: "+s.lstrip("#").strip()
        elif "[x]" in s:
            text="รายการตรวจที่เอกสารระบุว่าสำเร็จ ต้องอ้างหลักฐานจริง ไม่ใช่โค้ดตรวจ"
        elif "[ ]" in s:
            text="รายการที่ยังไม่ยืนยันสำเร็จ เช่น commit/ทีม"
        else:
            text="ข้อความกำกับ/ข้อมูลโครงการสำหรับผู้อ่าน ไม่ถูก app ใช้เป็น logic: "+code(s)
        result.append([text])
    return result,[],[]

def analyze(source,relative):
    suffix=Path(relative).suffix
    if suffix==".py":return python_notes(source)
    if suffix==".html":return html_notes(source)
    if suffix==".css":return css_notes(source)
    if suffix in (".js",".cjs"):return js_notes(source)
    if suffix==".json":return json_notes(source)
    return other_notes(source,relative)

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text.rstrip()+"\n",encoding="utf-8")

def build_file(relative,meta):
    path=ROOT/relative
    raw=path.read_bytes()
    source=raw.decode("utf-8").replace("\r\n","\n")
    lines=source.splitlines()
    notes,funcs,names=analyze(source,relative)
    assert len(notes)==len(lines)
    suffix=path.suffix
    language={".py":"python",".html":"html",".css":"css",".js":"javascript",".cjs":"javascript",".json":"json",".bat":"bat",".md":"markdown"}.get(suffix,"text")
    out=[
        "# "+relative+" — "+meta["title"],"",
        "อ้างอิงไฟล์ปัจจุบัน "+DAY+"; "+str(len(lines))+" physical lines (รวมบรรทัดว่าง)","",
        "**SHA-256 ของไฟล์จริง:** "+code(hashlib.sha256(raw).hexdigest()),"",
        "**ผู้ศึกษา/บทบาท:** "+meta["owner"],"",
        "## 1. หน้าที่และการเชื่อมต่อ","",
        meta["purpose"],"",
        "- **รับเข้า:** "+meta["input"],
        "- **ผลลัพธ์:** "+meta["output"],"",
        "**เกี่ยวข้องกับ:** "+("; ".join(meta["depends"]) or "เป็นข้อความประกอบ repository"),"",
        "## 2. ลำดับทำงาน","",
    ]
    out += [str(i)+". "+step for i,step in enumerate(meta["steps"],1)]
    out += ["","## 3. จุดที่ต้องอธิบายให้ถูก",""]
    out += ["- "+x for x in meta["cautions"]]
    if suffix==".css":
        marker=next((i for i,l in enumerate(lines,1) if "your own styles below" in l),None)
        out += ["","**ขอบเขตส่วนเดิม:** marker "+code("your own styles below")+" อยู่ L"+str(marker)+
                " ส่วนก่อน marker เป็น component ที่อาจารย์ให้ ส่วนหลังเป็นกฎโครงการ การอธิบายทุกบรรทัดไม่ได้อ้างว่าแก้ส่วนเดิม"]
    out += ["","## 4. คำถามซ้อมตอบที่เกี่ยวกับไฟล์",""]
    qid=0
    count=0
    for group in GROUPS:
        for row in group["rows"]:
            qid+=1
            if relative in row["files"]:
                question_path=OUT/"TEACHER_QUESTIONS.md"
                from_path=doc_path(relative).parent
                rel_question=str(Path(__import__("os").path.relpath(question_path,from_path))).replace("\\","/")
                out.append("- [Q"+str(qid).zfill(3)+": "+row["q"]+"]("+rel_question+"#q"+str(qid).zfill(3)+")")
                count+=1
    if not count:
        out.append("- อธิบายว่าไฟล์นี้เป็นข้อมูล/เครื่องมือประกอบอะไร และถูกอ่านที่ใด")
    if funcs:
        out += ["","## 5. ฟังก์ชัน/คลาสและตำแหน่ง","",
                "| ชื่อ | บรรทัดจริง | หน้าที่ |","|---|---|---|"]
        for start,end,name,desc in funcs:
            position="เริ่ม L"+str(start) if language=="javascript" else "L"+str(start)+"–L"+str(end)
            out.append("| "+code(name)+" | "+position+" | "+desc.replace("|","&#124;")+" |")
    if names:
        out += ["","## 6. ชื่อและคำศัพท์ที่พบใน Python","",
                "ชื่อที่เป็น local variable ให้ดูคำสั่งที่กำหนดค่าในบรรทัดจริง ตัวแปรชื่อเดียวกันต่างฟังก์ชันไม่จำเป็นต้องหมายถึง object เดียวกัน","",
                "| ชื่อ | ความหมาย |","|---|---|"]
        for name in names:
            note=NAMES.get(name,FN.get(name,"ชื่อที่ประกาศ/นำเข้า/เข้าถึงใน source; ตรวจตำแหน่งนิยามและ argument ในโค้ดด้านล่าง"))
            out.append("| "+code(name)+" | "+note.replace("|","&#124;")+" |")
    out += ["","## 7. โค้ดปัจจุบันครบทั้งไฟล์","",
            "คัดลอกเพื่ออ่านประกอบเท่านั้น ไม่ใช้สำเนานี้ทับ source โดยไม่ตรวจ SHA ถ้าไฟล์จริงเปลี่ยนเลขบรรทัดอาจไม่ตรง LF/CRLF แสดงเป็นการขึ้นบรรทัดในเอกสาร แต่ SHA คำนวณจาก bytes จริง","",
            "§§§"+language,source.rstrip("\n"),"§§§","",
            "## 8. คำอธิบายทุกบรรทัด","",
            "สตริง ชื่อ และเครื่องหมายอยู่ครบใน code block แต่ละบรรทัดด้านล่าง ชื่อ identifier เป็นหนึ่งหน่วย ไม่แยกอักษรของชื่อเดียวกันเป็นความหมายใหม่ ช่องว่างใน Python กำหนด block ส่วนช่องว่างในข้อความ/HTML ให้ดูชนิดส่วนที่ครอบ",""]
    for no,(line,detail) in enumerate(zip(lines,notes),1):
        out += ["### L"+str(no),""]
        if line:
            out += ["§§§"+language,line,"§§§",""]
        else:
            out += ["(บรรทัดว่าง)",""]
        out += ["- "+n for n in detail]
        out += [""]
    content="\n".join(out).replace("§§§",BT*3)
    write(doc_path(relative),content)
    return content,{"source":relative,"detail":"files/"+relative+".md",
                    "sha256":hashlib.sha256(raw).hexdigest(),"lines":len(lines),
                    "characters":len(source),"line_explanations":len(notes)}

def build_questions():
    text=["# คำถามที่อาจารย์อาจถาม พร้อมแนวคำตอบ 100 ข้อ","",
          "โครงการเดดไลน์ไม่ชนกัน · CodeMind กลุ่ม 6 · "+DAY,"",
          "ชุดนี้เป็นแนวซ้อมจาก source และข้อกำหนดจริง ไม่รับประกันว่าอาจารย์จะถามทุกข้อ ตอบตามสิ่งที่มีในโค้ด ไม่อ้างว่ามี login, push, database หรือ commit ของทุกคนหากยังไม่มีหลักฐาน","",
          "## ลำดับอ่านแนะนำ","",
          "- ทุกคน: Q001–Q010, Q014–Q020 และ Q091–Q100",
          "- นายวายุ: Q011–Q030, Q051–Q060 และ Q081–Q090",
          "- นางสาวลักขณา: Q031–Q040 และ Q073–Q079",
          "- นายไกรวิชญ์: Q041–Q050 และ Q061–Q072",
          "- นายธีรเดช: Q051–Q060, Q091–Q100 และอ่าน Node/fixture ประกอบ","",
          "## 20 ข้อที่ควรตอบได้ก่อนนำเสนอ","",
          "Q001, Q003, Q005, Q008, Q011, Q012, Q015, Q021, Q022, Q027, Q030, Q032, Q037, Q043, Q046, Q054, Q055, Q077, Q092, Q093",""]
    qid=0
    for group in GROUPS:
        text+=["## "+group["title"],"","**ผู้ซ้อมหลัก:** "+group["who"],""]
        for row in group["rows"]:
            qid+=1
            label="Q"+str(qid).zfill(3)
            text+=['<a id="'+label.lower()+'"></a>',"",
                   "### "+label+" — "+row["q"],"",
                   "**แนวคำตอบ:** "+row["a"],""]
            if row["files"]:
                text+=["**เปิดประกอบ:** "+", ".join("["+f+"]("+doc_link(f)+")" for f in row["files"]),""]
    assert qid==100
    text+=["## วิธีซ้อมให้ตอบจากความเข้าใจ","",
           "1. อ่านคำถามก่อน โดยยังไม่ดูคำตอบ","2. ตอบสั้น ๆ 20–40 วินาทีและชี้ฟังก์ชันหรือ field ที่ใช้จริง",
           "3. หากเป็นสูตร ให้เขียนตัวเลขตัวอย่างก่อนเทียบหน้าจอ","4. ให้เพื่อนถามต่อว่า ถ้ารายการว่าง/ข้อมูลผิด/ปิดหน้า จะเกิดอะไร",
           "5. ถ้าเป็นข้อจำกัดให้ตอบตรง ไม่เติมคุณสมบัติที่ยังไม่มี","",
           "อ่าน [สารบัญรายไฟล์](README.md), [คู่มือรวมพร้อมโค้ดทุกไฟล์](PROJECT_DETAIL_ALL.md) และ [ผังงานปัจจุบัน](../FLOWCHARTS.md)"]
    write(OUT/"TEACHER_QUESTIONS.md","\n".join(text))

def main():
    before={relative:digest(ROOT/relative) for relative in META}
    manifest=[]
    documents=[]
    for relative,meta in META.items():
        content,record=build_file(relative,meta)
        documents.append((relative,content))
        manifest.append(record)
    build_questions()
    total=sum(r["lines"] for r in manifest)
    index=["# คู่มือศึกษาและซ้อมตอบ — โค้ดปัจจุบัน","",
           "เดดไลน์ไม่ชนกัน · CodeMind กลุ่ม 6 · "+DAY,"",
           "## เริ่มอ่านจากสามส่วนนี้","",
           "1. [คำถามอาจารย์พร้อมแนวคำตอบ 100 ข้อ](TEACHER_QUESTIONS.md)",
           "2. [คู่มือรวมทุกไฟล์พร้อมโค้ดและคำอธิบาย](PROJECT_DETAIL_ALL.md)",
           "3. รายละเอียดเฉพาะไฟล์ในตารางด้านล่าง","",
           "ครอบคลุม "+str(len(manifest))+" ไฟล์โค้ด/ข้อมูล/เครื่องมือประกอบ รวม "+str(total)+
           " physical lines แต่ละไฟล์มีหน้าที่ ข้อมูลรับเข้า/ส่งออก ความสัมพันธ์ ลำดับทำงาน จุดที่ต้องระวัง โค้ดครบ และคำอธิบายรายบรรทัดพร้อม SHA-256","",
           "**ชื่อไฟล์จริง:** หน้าแรกใช้ templates/home.html ไม่มี index.html ในโครงการนี้","",
           "**ขอบเขต:** อธิบายไฟล์ของโครงการครบ รวมหน้าแรกและข้อมูลทีมที่มีอยู่ก่อนรอบล่าสุด และอธิบาย check.bat เดิมเป็นบริบท QA ไม่กล่าวว่าแก้ไฟล์เดิมทั้งหมด ไฟล์เอกสาร/ภาพประกอบมีรายการกำกับในคู่มือรวม ไม่วนอธิบายเอกสารที่กำลังสร้างเอง","",
           "## สารบัญรายไฟล์","",
           "| ไฟล์จริง | รายละเอียด | บรรทัด | หน้าที่ |","|---|---|---:|---|"]
    for record in manifest:
        relative=record["source"]
        index.append("| "+code(relative)+" | [เปิดอ่าน]("+doc_link(relative)+") | "+str(record["lines"])+" | "+META[relative]["title"]+" |")
    index+=["","## อ่านตามหน้าที่","",
            "- **วายุ:** models.py, data/sample/settings/team JSON และสูตร Plan",
            "- **ลักขณา:** page1.py/page1.html, macro การ์ด และ reminders.js",
            "- **ไกรวิชญ์:** page2.py/page2.html, style.css, forms.js และ macro",
            "- **ธีรเดช:** page3.py/page3.html, test_planner_features.py, check.bat, fixture และ Node tests",
            "- **ทุกคน:** home.html, Team, ข้อจำกัด และการเดินทางของข้อมูล GET/POST","",
            "## เอกสารประกอบที่ยังใช้ได้","",
            "- [ผังงานแต่ละหน้า](../FLOWCHARTS.md)",
            "- [บทนำเสนอแบ่งสมาชิก](../PRESENTATION_SCRIPT.md)",
            "- [สรุปผู้ทดสอบ](../TESTER_SUMMARY.md)",
            "- [สูตรและกติกาปัจจุบัน](../UPGRADE_DETAILS.md)",
            "- [รายงานตรวจจริง](../../qa/QA_REPORT.md)","",
            "คู่มือ PYTHON_DETAIL/FRONTEND_DETAIL/JAVASCRIPT_DATA_DETAIL เดิมเป็นประวัติฉบับแรก สำหรับเลขบรรทัดปัจจุบันให้อ่านชุด current นี้",
            "",
            "## การตรวจความตรงกับ source","",
            "source_manifest.json เก็บชื่อไฟล์ จำนวนบรรทัด SHA และจำนวนคำอธิบาย ต้องเทียบ SHA ใหม่เมื่อแก้ source ก่อนใช้เลขบรรทัดตอบอาจารย์ เอกสาร snapshot ไม่เปลี่ยนเองเมื่อผู้ใช้แก้ data หรือเพิ่มงานผ่านเว็บไซต์","",
            "การสร้างชุดนี้ตรวจ source/hash/JSON/แม่แบบและความครบถ้วนของเอกสาร ไม่ใช่การรันทดสอบการทำงานทั้งหมดซ้ำ ผล 42 passed/60 คะแนนให้ดูวันตรวจใน QA_REPORT",""]
    write(OUT/"README.md","\n".join(index))
    write(OUT/"source_manifest.json",json.dumps({"date":"2026-09-30","files":manifest,
                                             "total_source_lines":total,"questions":100},
                                            ensure_ascii=False,indent=2))
    merged=[
        "# รายละเอียดรวมทุกไฟล์ — โค้ดปัจจุบัน","",
        "เดดไลน์ไม่ชนกัน · CodeMind กลุ่ม 6 · "+DAY,"",
        "เอกสารนี้รวมบทจากคู่มือรายไฟล์ครบ "+str(len(manifest))+" ไฟล์ จำนวน "+str(total)+
        " บรรทัดจริง ไม่แก้โค้ดเพื่อประกอบเอกสาร เริ่มอ่านตามส่วนรับผิดชอบ หากเอกสารยาวเกินควรใช้ [สารบัญแยกรายไฟล์](README.md)","",
        "## ภาพรวมการเดินทางของข้อมูล","",
        "ผู้ใช้ → app.py เดิม → GET/build หรือ POST/handle → models/storage → template Jinja → HTML/CSS/JavaScript → ผู้ใช้","","§§§mermaid",
        "flowchart LR"," U[ผู้ใช้] --> A[app.py เดิม]"," A --> G[GET: build]"," A --> P[POST: handle]",
        " G --> M[models: คำนวณ]"," P --> V[ตรวจข้อมูลและ version]",
        " V --> S[storage.save]"," S --> D[(data.json)]"," D --> M",
        " M --> T[HTML/Jinja]"," T --> B[CSS และ JavaScript]"," B --> U",
        " P --> R[redirect กลับ GET]"," R --> G","§§§","",
        "## สูตรที่ต้องใช้ร่วมกัน","",
        "- remaining = max(0, estimate−done); progress = int(done×100/estimate) จำกัด 0–100",
        "- วันคงเหลือ = due−วันนี้; วันทำได้ = วันคงเหลือ+1 สำหรับกำหนดที่ยังไม่ผ่าน",
        "- cumulative = ผลรวม remaining ของ pending ที่ due ก่อนหรือเท่ากับวันตรวจ รวมงานค้าง",
        "- spent = min(งบต่อวัน, work ที่บันทึกวันนี้จากทุกงาน); capacity = days×hours−spent",
        "- required = (cumulative+spent)/days; gap = max(0,cumulative−capacity)",
        "- shortfall/day = max(0,required−hours); ปัดค่าแสดงส่วนขาดขึ้น 0.1 หลังตัดสินความเสี่ยง",
        "- today budget = max(0,hours−work วันนี้จริง); จัดสรรด้วย min(remaining,budget) แล้วลด budget",
        "- work เท่านั้นรวม actual_total; adjustment/complete/reopen แสดงเหตุการณ์แต่ไม่เพิ่มเวลาจริง","",
        "## แผนที่เชื่อมหน้า","",
        "| หน้า | Python | Template | JavaScript |",
        "|---|---|---|---|",
        "| หน้าแรก / | app.py เดิม | home.html | ไม่มีเฉพาะหน้า |",
        "| Overview | page1.py | page1.html + _task_card.html | reminders.js |",
        "| Manage | page2.py | page2.html + _task_card.html | forms.js |",
        "| Plan | page3.py | page3.html + _task_card.html | ไม่มี script เฉพาะหน้า |",
        "| Team | team.py | team.html | ไม่มี script เฉพาะหน้า |","",
        "## ไฟล์เดิมที่ห้ามแก้และใช้เป็นบริบท","",
        "| ไฟล์ | หน้าที่ | สถานะ |","|---|---|---|",
        "| app.py | route โหลด page/เรียก build/handle/render/redirect | ไม่แก้ |",
        "| storage.py | load/save/reset ของรายการ JSON | ไม่แก้ |",
        "| templates/base.html | header/nav/footer และ block | ไม่แก้ |",
        "| templates/_not_built.html | หน้าอธิบายข้อผิดพลาด | ไม่แก้ |",
        "| check_project.py | ตรวจคะแนนพื้นฐานและ hash | ไม่แก้ |",
        "| test_pages.py | ชุดทดสอบอาจารย์ 4 กรณี | ไม่แก้ |","",
        "## สิ่งที่มีจริงและข้อจำกัด","",
        "ใช้ JSON ในเครื่อง ไม่มี login/database transaction/permanent task ID/service worker/push สถานะทีมไม่ใช่หลักฐาน commit ใช้ SHA ตรวจฟอร์มเก่าแต่ไม่มี file lock การแจ้งเตือนทำงานขณะเปิด Overview และ server",
        "",
        "## เอกสารและภาพที่สร้าง/ปรับปรุงประกอบโครงการ","",
        "| รายการ | หน้าที่ |","|---|---|",
        "| PROJECT_DETAIL.md, PYTHON_DETAIL.md, FRONTEND_DETAIL.md, JAVASCRIPT_DATA_DETAIL.md | ประวัติ source ฉบับแรก มีข้อความนำไปชุด current |",
        "| UPGRADE_DETAILS.md | กติกาและความสามารถตามการปรับปรุง 14 ข้อ |",
        "| TESTER_SUMMARY.md | สูตร/กรณีตรวจ/บทพูดของผู้ทดสอบ |",
        "| PRESENTATION_SCRIPT.md | บทพูดแยกสมาชิก |",
        "| FLOWCHARTS.md | ผังงาน GET/POST และแต่ละหน้า |",
        "| docs/qa/QA_REPORT.md | ผลตรวจและขอบเขตที่ยังไม่ยืนยัน |",
        "| docs/qa/overview-desktop.jpg, overview-mobile.jpg | ภาพจากข้อมูลตัวอย่างจริง |",
        "| docs/qa/overview-mobile-fixture.jpg, history-mobile-fixture.jpg | ภาพจากข้อมูลทดสอบชั่วคราว |",
        "| study_metadata.json, study_symbols.json, study_questions.json | แหล่งคำอธิบาย/คำถามที่เขียนประกอบ source สำหรับสร้างชุดนี้ |",
        "| build_current_details.py | เครื่องมือสร้าง snapshot docs; ไม่ใช่ส่วนที่ app.py โหลด |",
        "| current/README.md, TEACHER_QUESTIONS.md, files/, source_manifest.json | สารบัญ คำถาม รายไฟล์ และข้อมูลตรวจความครบ |","",
        "## วิธีตรวจและใช้งานเอกสาร","",
        "1. อ่าน README เลือกไฟล์ของตนและตรวจ SHA หากมีการแก้ source",
        "2. ซ้อมคำถามแล้วเปิด line ที่เกี่ยวข้อง ไม่จำเฉพาะข้อความ",
        "3. ดูเว็บด้วย run.bat ที่พอร์ตที่เครื่องแจ้ง หากรัน check.bat ให้สำรอง data แยกก่อน",
        "4. ใช้ pytest/Node/fixture ตาม TESTER_SUMMARY เพื่อทดสอบเพิ่มเติม ไม่แก้ไฟล์ห้ามแตะ",
        "5. ตรวจ git log และ commit งานของตนจริงตามกติกา ไม่อ้างว่าคู่มือทำให้คะแนนทีมครบ","",
        "## สารบัญบททุกไฟล์",""
    ]
    for i,(relative,_) in enumerate(documents,1):
        merged.append(str(i)+". ["+relative+"](#file-"+str(i)+")")
    merged+=[""]
    for i,(relative,content) in enumerate(documents,1):
        merged+=['<a id="file-'+str(i)+'"></a>',"", "## ไฟล์ "+str(i)+": "+relative,""]
        # Links in each source chapter go up from nested files; in the merged file point here.
        content=re.sub(r"\]\((?:\.\./)+TEACHER_QUESTIONS.md","](TEACHER_QUESTIONS.md",content)
        chapter=[]
        in_code=False
        for line in content.splitlines():
            if line.startswith(BT*3):
                in_code=not in_code
            if not in_code and line.startswith("#"):
                line="#"+line
            chapter.append(line)
        merged+=chapter+["","---",""]
    write(OUT/"PROJECT_DETAIL_ALL.md","\n".join(merged).replace("§§§",BT*3))
    for relative,sha in before.items():
        assert digest(ROOT/relative)==sha,relative
    print(json.dumps({"files":len(manifest),"source_lines":total,
                      "line_explanations":sum(r["line_explanations"] for r in manifest),
                      "questions":100,"source_unchanged":True},ensure_ascii=False))

if __name__=="__main__":
    main()
