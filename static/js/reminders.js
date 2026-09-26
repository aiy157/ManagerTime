// Browser reminders while the dashboard is open, plus calendar files for later alerts.
const reminderData = document.getElementById("reminder-data");
const reminderButton = document.getElementById("enable-reminders");
const reminderStatus = document.getElementById("reminder-status");

if (reminderData && reminderButton && reminderStatus) {
  const tasks = JSON.parse(reminderData.textContent);
  let lastShownKey = "";

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
    if (!("Notification" in window) || !window.isSecureContext) {
      reminderStatus.textContent = "เบราว์เซอร์นี้ไม่รองรับการแจ้งเตือนในหน้านี้";
      reminderButton.disabled = true;
    } else if (Notification.permission === "granted") {
      reminderStatus.textContent = "เปิดแล้ว · เตือนเมื่อหน้านี้เปิดอยู่";
      reminderButton.textContent = "🔔 เปิดการแจ้งเตือนแล้ว";
    } else if (Notification.permission === "denied") {
      reminderStatus.textContent = "เบราว์เซอร์ปิดกั้นการแจ้งเตือน โปรดเปลี่ยนในการตั้งค่าเว็บไซต์";
      reminderButton.disabled = true;
    } else {
      reminderStatus.textContent = "กดเพื่ออนุญาตให้เบราว์เซอร์เตือน";
    }
  }

  function checkReminders() {
    if (!("Notification" in window) || Notification.permission !== "granted") return;
    const urgent = tasks.filter((task) => task.remaining_hours > 0 && daysUntil(task.due_date) <= 3);
    if (urgent.length === 0) return;
    const key = "deadline-reminder-" + todayKey();
    if (lastShownKey === key) return;
    try {
      if (localStorage.getItem(key) === "shown") return;
    } catch (_) {
      // The notification can still appear if browser storage is unavailable.
    }
    const body = urgent.length === 1
      ? urgent[0].title + " · ส่ง " + urgent[0].due_date
      : "มี " + urgent.length + " งานที่ใกล้ส่งหรือเกินกำหนด · เริ่มจาก " + urgent[0].title;
    try {
      const notification = new Notification("ตรวจเดดไลน์วันนี้", { body });
      notification.onclick = () => window.focus();
      lastShownKey = key;
      try { localStorage.setItem(key, "shown"); } catch (_) { /* storage is optional */ }
    } catch (_) {
      reminderStatus.textContent = "เบราว์เซอร์ไม่สามารถแสดงการแจ้งเตือนได้";
    }
  }

  reminderButton.addEventListener("click", async () => {
    if (!("Notification" in window)) return;
    try {
      await Notification.requestPermission();
      updateStatus();
      checkReminders();
    } catch (_) {
      reminderStatus.textContent = "ไม่สามารถขออนุญาตแจ้งเตือนได้ในเบราว์เซอร์นี้";
    }
  });

  updateStatus();
  checkReminders();
  window.setInterval(checkReminders, 60000);
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
