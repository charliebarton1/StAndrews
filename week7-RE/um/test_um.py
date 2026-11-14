from um import count

def test_um_start():
    assert count("um my name is") == 1
def test_no_um():
    assert count("Hi my name is")== 0
def test_um_inword():
    assert count("My name is yum")== 0
def test_um_end():
    assert count("My name is um") == 1
def test_random_um():
    assert count("um my name is um the") == 2
def test_capital():
    assert count("Um my name is") == 1
def test_no_um():
    assert count("Hi my name is") == 0 

