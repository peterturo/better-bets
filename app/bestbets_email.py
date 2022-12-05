from app.email_service import send_email
from app.bestbets import generate_arbitrage, plus_sign, Convert

if __name__ == "__main__":

    print("ARBITRAGE EMAIL...")
    SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"

    print(f"GENERATING {SPORT_KEY.upper()} ARBITRAGE BETS ...")
    print("-----------")   

    data = generate_arbitrage(SPORT_KEY)

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
                
        
        
        a_spreads_dict = (Convert(a_spreads))
        h_spreads_dict = (Convert(h_spreads))
        
        a_prices_dict = (Convert(a_prices))
        h_prices_dict = (Convert(h_prices))

        try:
        
            best_away_book = (max(a_spreads_dict, key=a_spreads_dict.get))
            best_home_book = (max(h_spreads_dict, key=h_spreads_dict.get))


            html_content = f"""
                <h3>Arbitrage Bets</h3>
                <p>{f"{sport_title}: {away_team} @ {home_team}"} </p>
                <p> </p>
                <p>BEST BETS: </p>
                <p>{f"{away_team}: {best_away_book} ({plus_sign(a_spreads_dict[best_away_book])}, {plus_sign(a_prices_dict[best_away_book])})"} </p>
                <p>{f"{home_team}: {best_home_book} ({plus_sign(h_spreads_dict[best_home_book])}, {plus_sign(h_prices_dict[best_home_book])})"} </p>
                <p>---------- </p>
            """


            send_email(subject="Arbitrage Bets", html=html_content)

        except:
            break
