from seasons import Date
import pytest
from datetime import date
def test_valid_dates():
    Date("2002-02-02")
    Date("2025-02-21")
    Date("1982-09-02")
    Date("1982-11-23")
    Date("2019-12-13")
    Date("1972-10-24")
def test_invalid_dates():
    with pytest.raises(SystemExit):
        Date("2032-02-02")
    with pytest.raises(SystemExit):
        Date("2024-22-21")
    with pytest.raises(SystemExit):
        Date("1982-09-41")
def test_invalid_inputs():
    with pytest.raises(SystemExit):
        Date("Hi")
    with pytest.raises(SystemExit):
       Date("22nd of June 1985")
    with pytest.raises(SystemExit):
        Date("2022-4-25")

def test_date_converter(monkeypatch):
    monkeypatch.setattr(Date, "today", date(2000, 1, 1))

    births = ["1999-01-01", "1995-01-01", "1998-06-20"]
    answers = [525600, 2629440, 806400]

    for birth, expected in zip(births, answers):
        assert Date(birth).days() == expected

