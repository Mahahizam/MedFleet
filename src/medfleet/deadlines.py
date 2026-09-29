from datetime import date


def days_until_due(due_date: date, as_of_date: date) -> int:
    """Return the number of days from as_of_date until due_date.

    A negative result means the deadline is overdue.
    """
    return (due_date - as_of_date).days


def inspection_status(due_date: date, as_of_date: date) -> str:
    """Return the STK/MTK inspection status: "ok", "due_soon" or "overdue".

    An inspection due today (0 days) counts as "due_soon", not "overdue".
    """
    days = days_until_due(due_date, as_of_date)
    if days < 0:
        return "overdue"
    if days <= 14:
        return "due_soon"
    return "ok"
