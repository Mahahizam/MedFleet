from datetime import date

import pytest

from medfleet.deadlines import inspection_status


def test_due_in_nine_days_is_due_soon():
    assert inspection_status(date(2026, 10, 10), date(2026, 10, 1)) == "due_soon"


def test_due_date_as_text_raises_type_error():
    with pytest.raises(TypeError):
        inspection_status("2026-10-10", date(2026, 10, 1))
