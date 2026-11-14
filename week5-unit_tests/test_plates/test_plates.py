import plates


def test_start_letter():
    assert plates.is_valid("AB") == True
    assert plates.is_valid("12AB")==False
    assert plates.is_valid("1ABCD")==False
    assert plates.is_valid("A123")==False


def test_len():
    assert plates.is_valid("ABCD") == True
    assert plates.is_valid("ABCDEFG") == False


def test_num_place():
    assert plates.is_valid("AB12") == True
    assert plates.is_valid("ABC132") == True
    assert plates.is_valid("AA12B") == False
    assert plates.is_valid("123AB") == False
    assert plates.is_valid("12B1AB") == False
    assert plates.is_valid("B13AB") == False
    assert plates.is_valid("AB012") == False




def test_special():
    assert plates.is_valid("AB12,") == False
    assert plates.is_valid("!AB12") == False
    assert plates.is_valid("!AB-2") == False



