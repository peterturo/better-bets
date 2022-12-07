
from app.bestbets import plus_sign, Convert, fetch_arbitrage

def test_plus_sign():
    assert plus_sign(-5) == -5
    assert plus_sign(5) == "+5"
    assert plus_sign(0) == "PICK"


def test_Convert():
    list = ['a', 1, 'b', 2, 'c', 3]
    assert Convert(list) == {'a':1, 'b':2, 'c':3}

