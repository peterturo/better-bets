# this is the "app/bestbets.py" file

import requests
import json

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



def fetch_odds(SPORT_KEY, WAGER_TYPE, BOOK_KEY):

    request_url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/?regions=us&markets={WAGER_TYPE}&oddsFormat=american&apiKey={API_KEY}{BOOK_KEY}"

    response = requests.get(request_url)

    data = json.loads(response.text)

    return data


def parse_data(sport_key, wager_type, book_key):
    
    try:

        print(f"GENERATING {sport_key.upper()} ARBITRAGE BETS ...")
        print("-----------")   
        
        data = fetch_odds(sport_key, wager_type, book_key)

        games = []
        

        for d in data:
            away_team = d["away_team"]
            home_team = d["home_team"]
            bookmakers = d["bookmakers"]
            sport_title = d["sport_title"]
        
            a_spreads = []
            h_spreads = []

            a_prices = []
            h_prices = []

            for b in bookmakers:
                markets = b["markets"]

                for m in markets:
                    odds = m["outcomes"]

                    away_spread = [p["point"] for p in odds if p["name"] == away_team]
                    home_spread = [p["point"] for p in odds if p["name"] == home_team]

                    a_spreads.append(b["title"])
                    a_spreads.append(away_spread[0])
                        
                    h_spreads.append(b["title"])
                    h_spreads.append(home_spread[0])
                    
                    
                    away_price = [p["price"] for p in odds if p["name"] == away_team]
                    home_price = [p["price"] for p in odds if p["name"] == home_team]
                    
                    a_prices.append(b["title"])
                    a_prices.append(away_price[0])
                        
                    h_prices.append(b["title"])
                    h_prices.append(home_price[0])

                    # collecting bookmaker name, spread, and price for each game
                    
            
            
            a_spreads_dict = (Convert(a_spreads))
            h_spreads_dict = (Convert(h_spreads))
            
            a_prices_dict = (Convert(a_prices))
            h_prices_dict = (Convert(h_prices))

            # converting lists of bookmaker and spreads/prices into dictionary with key = bookmaker and value = spread/price

            
            best_away_book = max(a_spreads_dict, key=a_spreads_dict.get)
            best_home_book = max(h_spreads_dict, key=h_spreads_dict.get)

            best_a_spread = max(a_spreads_dict.values())
            best_h_spread = max(h_spreads_dict.values())

            best_a_price = a_prices_dict[best_away_book]
            best_h_price = h_prices_dict[best_home_book]

            # from: https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary             
                



            game = {
                "sport_title": sport_title,
                "home_team": home_team,
                "away_team": away_team,
                "best_away_book": best_away_book, 
                "best_home_book": best_home_book,
                "best_a_spread": best_a_spread,
                "best_h_spread": best_h_spread,
                "best_a_price": best_a_price,
                "best_h_price": best_h_price
            }


            games.append(game)

        return games
              
    except:
        print ("Could not find betting data, please input a valid sport key.")
        return None




if __name__ == "__main__":

    SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"
    WAGER_TYPE="spreads" 
    BOOK_KEY=""


    games = parse_data(SPORT_KEY, WAGER_TYPE, BOOK_KEY)

    for g in games:
        print (f"{g['sport_title']}: {g['away_team']} @ {g['home_team']}")
        print ("")

        print("BEST BETS:")

        print (f"{g['away_team']}: {g['best_away_book']} ({plus_sign(g['best_a_spread'])}, {plus_sign(g['best_a_price'])}")
        print (f"{g['home_team']}: {g['best_home_book']} ({plus_sign(g['best_h_spread'])}, {plus_sign(g['best_h_price'])}")
        
        
        print("-----------")