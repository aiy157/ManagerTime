"""A small model for one assignment in data.json."""

from datetime import date


class Assignment:
    def __init__(self, title, course, due_date, estimated_hours, done_hours):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.estimated_hours = estimated_hours
        self.done_hours = done_hours

    def remaining_hours(self):
        return max(0, self.estimated_hours - self.done_hours)

    def days_left(self):
        return (date.fromisoformat(self.due_date) - date.today()).days
