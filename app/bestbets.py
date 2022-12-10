# this is the "app/bestbets.py" file

import requests
import json
from operator import itemgetter

from app.alpha import API_KEY


def plus_sign(number):
    if number > 0:
        return(f"+{number}")
    elif number == 0:
        return("PICK")
    else:
        return(number)

# function that inserts a '+' in front of a positive number and turns a 0 into 'PICK' (for odds notation).



def fetch_odds(SPORT_KEY, WAGER_TYPE, BOOK_KEY):

    request_url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/?regions=us&markets={WAGER_TYPE}&oddsFormat=american&apiKey={API_KEY}{BOOK_KEY}"

    response = requests.get(request_url)

    data = json.loads(response.text)

    return data

# fetches data from The Odds API using user inputs/credentials
# also converts json file into a python dictionary


def parse_data(sport_key, wager_type, book_key):
    
    try:
   
        
        data = fetch_odds(sport_key, wager_type, book_key)

        games = []
        

        # looping through datasets list of dictionaries, storing variables along the way

        for d in data:
            away_team = d["away_team"]
            home_team = d["home_team"]
            bookmakers = d["bookmakers"]
            sport_title = d["sport_title"]
            start_time = d["commence_time"][0:10]
        
            away_dicts = []
            home_dicts = []

            for b in bookmakers:
                markets = b["markets"]

                for m in markets:
                    odds = m["outcomes"]

                    away_spread = [p["point"] for p in odds if p["name"] == away_team]
                    #away_spread = [f'+{a_spread}' if a_spread > 0 else f'{a_spread}' for a_spread in away_spreads]

                    home_spread = [p["point"] for p in odds if p["name"] == home_team]
                    #home_spread = [f'+{h_spread}' if h_spread > 0 else f'{h_spread}' for h_spread in home_spreads]
                    
                    
                    away_price = [p["price"] for p in odds if p["name"] == away_team]
                    home_price = [p["price"] for p in odds if p["name"] == home_team]
                    

                    away_dict = {
                        "sportsbook": b["title"],
                        "spread": away_spread,
                        "price": away_price
                    }

                    
                    away_dicts.append(away_dict)

                    
                    home_dict = {
                        "sportsbook": b["title"],
                        "spread": home_spread,
                        "price": home_price
                    }

                    home_dicts.append(home_dict)
                    

                    # collecting bookmaker names, spreads, and prices for each game
                    # putting them in a dictionary
                    # appending them to an empty list
            
            
            sorted_away_dicts = sorted(away_dicts, key=itemgetter("spread", "price"), reverse=True)
            sorted_home_dicts = sorted(home_dicts, key=itemgetter("spread", "price"), reverse=True)

            away_artbitrage = (sorted_away_dicts[0])
            home_arbitrage = (sorted_home_dicts[0])

            best_away_book = away_artbitrage["sportsbook"]
            best_home_book = home_arbitrage["sportsbook"]

            best_a_spreads = away_artbitrage["spread"]
            best_a_spread = [f'+{ba_spread}' if ba_spread > 0 else f'{ba_spread}' for ba_spread in best_a_spreads]

            best_h_spreads = home_arbitrage["spread"]
            best_h_spread = [f'+{bh_spread}' if bh_spread > 0 else f'{bh_spread}' for bh_spread in best_h_spreads]

            best_a_prices = away_artbitrage["price"]
            best_a_price = [f'+{ba_price}' if ba_price > 0 else f'{ba_price}' for ba_price in best_a_prices]

            best_h_prices = home_arbitrage ["price"]
            best_h_price = [f'+{bh_price}' if bh_price > 0 else f'{bh_price}' for bh_price in best_h_prices]
            
            # sorting dictionary by spread, and then price to get the best betting line for each team



            game = {
                "sport_title": sport_title,
                "home_team": home_team,
                "away_team": away_team,
                "best_away_book": best_away_book, 
                "best_home_book": best_home_book,
                "best_a_spread": best_a_spread,
                "best_h_spread": best_h_spread,
                "best_a_price": best_a_price,
                "best_h_price": best_h_price,
                "away_spread": away_spread,
                "home_spread": home_spread,
                "start_time": start_time
            }


            games.append(game)

            # creating dictionary of necessary variables collected throughout loop
            # appending these variables to an empty list

        return games
              
    except:
        print ("Could not find betting data, please input a valid sport key.")
        return None




if __name__ == "__main__":

    SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"
    WAGER_TYPE= "spreads"
    BOOK_KEY = ""

    print(f"GENERATING ARBITRAGE BETS FOR {SPORT_KEY.upper()}...")
    print("-----------")


    games = parse_data(SPORT_KEY, WAGER_TYPE, BOOK_KEY)

    for g in games:
        print (f"{g['sport_title']}: {g['away_team']} ({plus_sign(g['away_spread'][0])}) @ {g['home_team']} ({plus_sign(g['home_spread'][0])})")
        print ("")

        print("BEST BETS:")

        print (f"{g['away_team']}: {g['best_away_book']} ({g['best_a_spread'][0]}, {g['best_a_price'][0]})")
        print (f"{g['home_team']}: {g['best_home_book']} ({g['best_h_spread'][0]}, {g['best_h_price'][0]})")
        
        print("-----------")

    # looping through and printing arbitrage data in the main loop