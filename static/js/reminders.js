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
