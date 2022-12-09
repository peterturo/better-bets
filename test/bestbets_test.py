
from app.bestbets import plus_sign, fetch_odds, parse_data

def test_plus_sign():
    assert plus_sign(-5) == -5
    assert plus_sign(5) == "+5"
    assert plus_sign(0) == "PICK"


def test_fetch_odds():
    data = fetch_odds("americanfootball_nfl", "spreads", "")
    assert isinstance (data, list)


def test_parse_data():

    games = parse_data("americanfootball_nfl", "spreads", "")

    assert isinstance (games, list)

    for g in games: 
        title = g["sport_title"]
        assert isinstance (title, str)
        assert title == "NFL"   
        
        away_team = g["away_team"]
        assert isinstance (away_team, str)  
        
        best_a_spread = g["best_a_spread"][0]
        assert isinstance (best_a_spread, float)



