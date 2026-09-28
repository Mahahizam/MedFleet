from datetime import date

from medfleet.deadlines import days_until_due


def test_due_in_future_returns_positive_days():
    assert days_until_due(date(2026, 10, 15), date(2026, 10, 1)) == 14


def test_due_today_returns_zero():
    assert days_until_due(date(2026, 10, 1), date(2026, 10, 1)) == 0


def test_overdue_returns_negative_days():
    assert days_until_due(date(2026, 9, 25), date(2026, 10, 1)) == -6
    