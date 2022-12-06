
from app.bestbets import plus_sign

def test_plus_sign():
    assert plus_sign(-5) == -5
    assert plus_sign(5) == "+5"
    assert plus_sign(0) == "PICK"