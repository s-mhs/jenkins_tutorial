from src.add import add

def test_eight ():
    assert(add(3, 5)) == 8

def test_add_zero():
    assert(add(0, 0)) == 0

def test_negative_eight ():
    assert(add(-3, -5)) == -8