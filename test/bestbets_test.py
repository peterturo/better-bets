
from app.bestbets import plus_sign, Convert, parse_data

def test_plus_sign():
    assert plus_sign(-5) == -5
    assert plus_sign(5) == "+5"
    assert plus_sign(0) == "PICK"


def test_Convert():
    list = ['a', 1, 'b', 2, 'c', 3]
    assert Convert(list) == {'a':1, 'b':2, 'c':3}


def test_parse_data():
    
    games = parse_data(sport_key = "americanfootball_nfl", wager_type = "spreads", book_key = "" )
    
    #assert isinstance (games, list)
    
    for g in games:

        title = g["sport_title"]
        assert isinstance (title, str)
        assert title == "NFL"

        away_team = g["away_team"]
        assert isinstance (away_team, str)

        best_a_spread = g["best_a_spread"]
        assert isinstance (best_a_spread, float)



