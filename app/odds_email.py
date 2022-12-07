from app.email_service import send_email
from app.odds import fetch_odds, plus_sign

if __name__ == "__main__": 

    print("ODDS EMAIL...")
    
    SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"
    WAGER_TYPE = input("Please input a wager type (spreads, h2h, totals) (default: 'spreads'): ") or "spreads"
    BOOK_KEY='&bookmakers=bovada'


    print(f"GENERATING {WAGER_TYPE.upper()} FOR {SPORT_KEY.upper()}...")
    print("-----------")
    
    data = fetch_odds(SPORT_KEY, WAGER_TYPE, BOOK_KEY)
    
    for d in data:
        away_team = d["away_team"]
        home_team = d["home_team"]
        bookmakers = d["bookmakers"]
        sport_title = d["sport_title"]
       


        for b in bookmakers:
            markets = b["markets"]

            for m in markets:
                odds = m["outcomes"]


                if WAGER_TYPE == "spreads":

                    away_spread = [p["point"] for p in odds if p["name"] == away_team]
                    home_spread = [p["point"] for p in odds if p["name"] == home_team]

                    away_price = [p["price"] for p in odds if p["name"] == away_team]
                    home_price = [p["price"] for p in odds if p["name"] == home_team]

                    
                    html_content = f"""
                    <h3>{f"{sport_title.upper()}"} Bets</h3>
                    <p>{f"{sport_title}: {away_team} ({plus_sign(away_spread[0])}, {plus_sign(away_price[0])}) @ {home_team} ({plus_sign(home_spread[0])}, {plus_sign(home_price[0])})"} </p>
                    """


                elif WAGER_TYPE == "totals":
                    
                    over = [p["point"] for p in odds if p["name"] == "Over"]


                    html_content = f"""
                    <h3>{f"{sport_title.upper()}"} Bets</h3>
                    <p>{f"{sport_title}: {away_team} @ {home_team}, O/U: {over[0]}"} </p>
                    """

                else:
                    
                    away_ml = [p["price"] for p in odds if p["name"] == away_team]
                    home_ml = [p["price"] for p in odds if p["name"] == home_team]


                    html_content = f"""
                    <h3>{f"{sport_title.upper()}"} Bets</h3>
                    <p>{f"{sport_title}: {away_team} ({plus_sign(away_ml[0])}) @ {home_team} ({plus_sign(home_ml[0])})"} </p>
                    """


                
                send_email(subject= f"{sport_title.upper()} Bets", html=html_content)

                