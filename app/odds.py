# this is the "app/odds.py" file

import requests
import json

from app.alpha import API_KEY
from app.bestbets import fetch_odds, plus_sign


# printing betting odds data for spreads, h2h, and point totals


if __name__ == "__main__": 

    try:
    
        SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"
        WAGER_TYPE = input("Please input a wager type (spreads, h2h, totals) (default: 'spreads'): ") or "spreads"
        BOOK_KEY="&bookmakers=bovada"

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
                        
                        print(f"{sport_title}: {away_team} ({plus_sign(away_spread[0])}, {plus_sign(away_price[0])}) @ {home_team} ({plus_sign(home_spread[0])}, {plus_sign(home_price[0])})")

                    
                    elif WAGER_TYPE == "totals":
                        
                        over = [p["point"] for p in odds if p["name"] == "Over"]

                        print(f"{sport_title}: {away_team} @ {home_team}, O/U: {over[0]}")

                    
                    else:
                        
                        away_ml = [p["price"] for p in odds if p["name"] == away_team]
                        home_ml = [p["price"] for p in odds if p["name"] == home_team]

                        print(f"{sport_title}: {away_team} ({plus_sign(away_ml[0])}) @ {home_team} ({plus_sign(home_ml[0])})")

                    
                    print("-----------")
    except:
        print ("Could not find betting data, please input a different sport or wager.")