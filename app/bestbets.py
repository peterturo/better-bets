# this is the "app/betterbets.py" file

import requests
import json

from app.alpha import API_KEY


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

# converting list of values to dictionary with key value pairs
# from: https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/



def generate_arbitrage(SPORT_KEY = "upcoming"):

    print(f"GENERATING {SPORT_KEY.upper()} ARBITRAGE BETS ...")
    print("-----------")

    request_url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/?regions=us&markets=spreads&oddsFormat=american&apiKey={API_KEY}"
    response = requests.get(request_url)

    data = json.loads(response.text)

    #print(type(data))
    #pprint(data)

    for d in data:
        away_team = d["away_team"]
        home_team = d["home_team"]
        bookmakers = d["bookmakers"]
        sport_title = d["sport_title"]
       
        #print(f"{away_team} @ {home_team}")
        #print(f"DATE: {d['commence_time'][11:19]}, {d['commence_time'][0:10]}")

        #markets = [b for b in bookmakers]

        a_spreads = []
        h_spreads = []

        a_prices = []
        h_prices = []

        for b in bookmakers:
            markets = b["markets"]

            for m in markets:
                odds = m["outcomes"]

                #for o in odds:
                    #print(f"{o['name']}: {o['point']}")
                    #print(f"{o['name'][1]}: {o['price'][1]}")
                    #print(m["outcomes"])

                away_spreads = [p["point"] for p in odds if p["name"] == away_team]
                home_spreads = [p["point"] for p in odds if p["name"] == home_team]
                away_spread = away_spreads[0]
                home_spread = home_spreads[0]

                    
                away_prices = [p["price"] for p in odds if p["name"] == away_team]
                home_prices = [p["price"] for p in odds if p["name"] == home_team]
                away_price = away_prices[0]
                home_price = home_prices[0]

                
                
                a_spreads.append(b["title"])
                a_spreads.append(away_spread)
                    
                h_spreads.append(b["title"])
                h_spreads.append(home_spread)

                
                a_prices.append(b["title"])
                a_prices.append(away_price)
                    
                h_prices.append(b["title"])
                h_prices.append(home_price)
                

        #sorted_books = sorted(odds, key=itemgetter("point"), reverse=True)
        #print(sorted_books)
        
        a_spreads_dict = (Convert(a_spreads))
        h_spreads_dict = (Convert(h_spreads))

        
        a_prices_dict = (Convert(a_prices))
        h_prices_dict = (Convert(h_prices))



        #sorted_away_odds = dict(sorted(a_odds_dict.items(), key=itemgetter(1)))
        #sorted_home_odds = dict(sorted(h_odds_dict.items(), key=itemgetter(1)))
        # from: https://www.askpython.com/python/dictionary/sort-a-dictionary-by-value-in-python#:~:text=itemgetter()%20method%20can%20be,m'%20values%20from%20the%20iterable.

        #print(sorted_away_odds)
        #print(sorted_home_odds)

        
        
        
        best_away_book = (max(a_spreads_dict, key=a_spreads_dict.get))
        best_home_book = (max(h_spreads_dict, key=h_spreads_dict.get))
        # from: https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
        

        
        
        print(f"{sport_title}: {away_team} @ {home_team}")
        print("")

        print("BEST BETS:")
       
        
        if a_spreads_dict[best_away_book] > 0:
            if a_prices_dict[best_away_book] > 0:
                print(f"{away_team}: {best_away_book} (+{a_spreads_dict[best_away_book]}, +{a_prices_dict[best_away_book]})")
            else:
                print(f"{away_team}: {best_away_book} (+{a_spreads_dict[best_away_book]}, {a_prices_dict[best_away_book]})")
        
        
        elif a_spreads_dict[best_away_book] == 0:
            if a_prices_dict[best_away_book] > 0:
                print(f"{away_team}: {best_away_book} (PICK, +{a_prices_dict[best_away_book]})")
            else:
                print(f"{away_team}: {best_away_book} (PICK, {a_prices_dict[best_away_book]})")
        
        else:
            if a_prices_dict[best_away_book] > 0:
                print(f"{away_team}: {best_away_book} ({a_spreads_dict[best_away_book]}, +{a_prices_dict[best_away_book]})")
            else:
                print(f"{away_team}: {best_away_book} ({a_spreads_dict[best_away_book]}, {a_prices_dict[best_away_book]})")
        
        
        
        if h_spreads_dict[best_home_book] > 0:
            if h_prices_dict[best_home_book] > 0:
                print(f"{home_team}: {best_home_book} (+{h_spreads_dict[best_home_book]}, +{h_prices_dict[best_home_book]})")
            else:
                print(f"{home_team}: {best_home_book} (+{h_spreads_dict[best_home_book]}, {h_prices_dict[best_home_book]})")
        
        elif h_spreads_dict[best_home_book] == 0:
            if h_prices_dict[best_away_book] > 0:
                print(f"{home_team}: {best_home_book} (PICK, +{h_prices_dict[best_home_book]})")
            else:
                print(f"{home_team}: {best_home_book} (PICK, {h_prices_dict[best_home_book]})")
        
        else:
            if h_prices_dict[best_home_book] > 0:
                print(f"{home_team}: {best_home_book} ({h_spreads_dict[best_home_book]}, +{h_prices_dict[best_home_book]})")
            else:
                print(f"{home_team}: {best_home_book} ({h_spreads_dict[best_home_book]}, {h_prices_dict[best_home_book]})")
        
        
        print("-----------")

    
generate_arbitrage()