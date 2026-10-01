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
