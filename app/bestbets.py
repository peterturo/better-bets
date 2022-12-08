# this is the "app/bestbets.py" file

import requests
import json
from operator import itemgetter

from app.alpha import API_KEY

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

# converting list of values to dictionary with key value pairs
# from: https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/


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
        
            away_dicts = []
            home_dicts = []

            for b in bookmakers:
                markets = b["markets"]

                for m in markets:
                    odds = m["outcomes"]

                    away_spread = [p["point"] for p in odds if p["name"] == away_team]
                    home_spread = [p["point"] for p in odds if p["name"] == home_team]
                    
                    
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
                    
                    #over = [p["point"] for p in odds if p["name"] == "Over"]
                    #away_ml = [p["price"] for p in odds if p["name"] == away_team]
                    #home_ml = [p["price"] for p in odds if p["name"] == home_team]

                    # collecting bookmaker names, spreads, and prices for each game
            
            
            sorted_away_dicts = sorted(away_dicts, key=itemgetter("spread", "price"), reverse=True)
            sorted_home_dicts = sorted(home_dicts, key=itemgetter("spread", "price"), reverse=True)

            #print(sorted_away_dicts)
            #print(sorted_home_dicts)



            away_artbitrage = (sorted_away_dicts[0])
            home_arbitrage = (sorted_home_dicts[0])

            best_away_book = away_artbitrage["sportsbook"]
            best_home_book = home_arbitrage["sportsbook"]

            best_a_spread = away_artbitrage["spread"]
            best_h_spread = home_arbitrage["spread"]

            best_a_price = away_artbitrage["price"]
            best_h_price = home_arbitrage ["price"]
                



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

        print (f"{g['away_team']}: {g['best_away_book']} ({plus_sign(g['best_a_spread'][0])}, {plus_sign(g['best_a_price'][0])})")
        print (f"{g['home_team']}: {g['best_home_book']} ({plus_sign(g['best_h_spread'][0])}, {plus_sign(g['best_h_price'][0])})")
        
        print("-----------")

    # looping through and printing arbitrage data in the main loop