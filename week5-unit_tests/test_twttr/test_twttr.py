from twttr import shorten
import pytest
def test_lower_str():
    assert shorten("aeuoijklemdh") == "jklmdh"

def test_upper_str():
    assert shorten("AEKHDEK") == "KHDK"

def test_num():
    assert shorten("1234") == "1234"

def test_int_error():
    with pytest.raises(TypeError):
        shorten(12)

def test_special_char():
    assert shorten("Hi, My name is:!?=") == "H, My nm s:!?="


