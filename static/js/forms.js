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
