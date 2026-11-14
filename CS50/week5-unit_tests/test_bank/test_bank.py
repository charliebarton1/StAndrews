from bank import value
import pytest

def test_hello():
    assert value("Hello") == 0

def test_h_start():
    assert value("hi how are you? ") == 20

def test_any_letter():
    assert value("Bonjour") == 100

