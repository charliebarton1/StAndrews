from numb3rs import validate

def test_valid_ip():
    assert validate("222.23.245.243") == True
    assert validate("1.12.1.1") == True
def test_start_0():
    assert validate("011.11.11.1") == False
    assert validate("001.1.11.1") == False
def test_above255():
    assert validate("265.12.12.12") == False
    assert validate("245.12.12.256") == False
    assert validate("245.22.296.12") == False
    assert validate("245.262.12.12") == False




def test_format():
    assert validate("200.14.14.14.") == False
    assert validate("200 100 14 14") == False
    assert validate("155-155-155-155") == False
def test_invalid_input():
    assert validate("My IP is: 233.233.233.233")== False



