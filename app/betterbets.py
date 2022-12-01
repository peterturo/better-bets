def generate_odds(SPORT_KEY = "americanfootball_nfl"):

    #WAGER_TYPE = (input("Please enter a type of wager (spreads, h2h, totals): "))

    print(f"GENERATING ODDS FOR {SPORT_KEY.upper()}...")
    print("-----------")

    request_url = f"https://api.the-odds-api.com/v4/sports/{SPORT_KEY}/odds/?regions=us&markets=spreads&oddsFormat=american&apiKey={API_KEY}&bookmakers=bovada"
    response = requests.get(request_url)

    data = json.loads(response.text)

    #print(type(data))
    #pprint(data)

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

                     
                    
                    if away_spread > home_spread:
                        print(f"{sport_title}: {away_team} (+{away_spread}, {away_price}) @ {home_team} ({home_spread}, {home_price})")
        
                    else:
                        print(f"{sport_title}: {away_team} ({away_spread}, {away_price}) @ {home_team} (+{home_spread}, {home_price})")



                elif WAGER_TYPE == "totals":
                    
                    overs = [p["point"] for p in odds if p["name"] == "Over"]
                    over = overs[0]

                    print(f"{sport_title}: {away_team} @ {home_team}, O/U: {over}")

                else:
                    
                    away_mls = [p["price"] for p in odds if p["name"] == away_team]
                    home_mls = [p["price"] for p in odds if p["name"] == home_team]
                    away_ml = away_mls[0]
                    home_ml = home_mls[0]

                    if away_ml > home_ml:
                        print(f"{sport_title}: {away_team} (+{away_ml}) @ {home_team} ({home_ml})")
        
                    else:
                        print(f"{sport_title}: {away_team} ({away_ml}) @ {home_team} (+{home_ml})")


                
                print(f"SPORTSBOOK: {b['title']}")    
                print("-----------")

generate_odds()