from datetime import date


def days_until_due(due_date: date, as_of_date: date) -> int:
    """Return the number of days from as_of_date until due_date.

    A negative result means the deadline is overdue.
    """
    return (due_date - as_of_date).days