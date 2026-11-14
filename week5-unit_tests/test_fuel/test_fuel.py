from fuel import convert, gauge
import pytest

def test_format():
    assert convert("3/4")==75
    with pytest.raises(ValueError):
        convert("4-6")
        convert("5 5")
def test_negatives():
    # assert convert("5/5")==100
    with pytest.raises(ValueError):
        convert("-4/7")
    with pytest.raises(ValueError):
        convert("5/-5")
    with pytest.raises(ValueError):
        convert("-5/-6")

def test_rounding():
    assert convert("2/3")== 67
    assert convert("9/10") == 90
    assert convert("3/7") == 43

def test_isint():
    with pytest.raises(ValueError):
        convert("X/7")
        convert("5/Z")
        convert("X/Y")
def test_0division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
        convert("1/0")

def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
def test_gauge_F():
    assert gauge(99) == "F"
def test_gauge():
    assert gauge(88) == "88%"









