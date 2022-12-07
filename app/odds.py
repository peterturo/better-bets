# this is the "app/odds.py" file

import requests
import json

from app.alpha import API_KEY
from app.bestbets import fetch_odds, plus_sign


if __name__ == "__main__": 

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

                    away_spreads = [p["point"] for p in odds if p["name"] == away_team]
                    home_spreads = [p["point"] for p in odds if p["name"] == home_team]
                    away_spread = away_spreads[0]
                    home_spread = home_spreads[0]

                    away_prices = [p["price"] for p in odds if p["name"] == away_team]
                    home_prices = [p["price"] for p in odds if p["name"] == home_team]
                    away_price = away_prices[0]
                    home_price = home_prices[0]

                     
                    
                    print(f"{sport_title}: {away_team} ({plus_sign(away_spread)}, {plus_sign(away_price)}) @ {home_team} ({plus_sign(home_spread)}, {plus_sign(home_price)})")



                elif WAGER_TYPE == "totals":
                    
                    overs = [p["point"] for p in odds if p["name"] == "Over"]
                    over = overs[0]

                    print(f"{sport_title}: {away_team} @ {home_team}, O/U: {over}")

                else:
                    
                    away_mls = [p["price"] for p in odds if p["name"] == away_team]
                    home_mls = [p["price"] for p in odds if p["name"] == home_team]
                    away_ml = away_mls[0]
                    home_ml = home_mls[0]

                    print(f"{sport_title}: {away_team} ({plus_sign(away_ml)}) @ {home_team} ({plus_sign(home_ml)})")


                
                #print(f"Odds from {b['title']}")    
                print("-----------")