from seasons import Date
import pytest

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
        Date("2024-22-21")
        Date("1982-09-41")
def test_invalid_inputs():
    with pytest.raises(SystemExit):
        Date("Hi")
        Date("22nd of June 1985")
        Date("2022-4-25")

def test_date_converter():
    d = ["1999-01-01", "1995-01-01", "1998-06-20"]
    ans = ["Five hundred twenty-five thousand, six hundred minutes", "Two million, six hundred twenty-nine thousand, four hundred forty minutes","Eight hundred six thousand, four hundred minutes"]
    fixed = "2000-01-01"
    for i in range(len(d)):
        test = Date(d[i],fixed)
        assert test.mins == ans[i]

