from working import convert
import pytest 
def test_basic():
    assert convert("9 AM to 9 PM") == "09:00 to 21:00"
    assert convert("5 AM to 6 PM") == "05:00 to 18:00"
def test_complex():
    assert convert("9:00 AM to 9:00 PM") == "09:00 to 21:00"
def test_basic_complex():
    assert convert("9:00 AM to 9 PM") == "09:00 to 21:00"
    assert convert("9 AM to 9:00 PM") == "09:00 to 21:00"

def test_above10():
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("5 AM to 11 PM") == "05:00 to 23:00"
def test_decimal():
    assert convert("11:30 AM to 9:12 PM") == "11:30 to 21:12"
def test_PM_start():
    assert convert("5 PM to 11 AM") == "17:00 to 11:00"
def test_midday_midnight():
    assert convert("12 AM to 12 PM")=="00:00 to 12:00"
def test_no_to():
     with pytest.raises(ValueError):
        convert("12 AM 2 PM")
def test_incorrect_times():
     with pytest.raises(ValueError):
        convert("12:64 AM to 2:52 PM")
