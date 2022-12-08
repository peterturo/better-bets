# this is the "app/bestbets_email.py" file

# sending email with arbitrage betting lines

from app.email_service import send_email
from app.bestbets import plus_sign, parse_data

if __name__ == "__main__":

    print("ARBITRAGE EMAIL...")
    
    SPORT_KEY = input("Please input a sport (default: 'americanfootball_nfl'): ") or "americanfootball_nfl"
    WAGER_TYPE = "spreads"
    BOOK_KEY = ""

    print(f"GENERATING {SPORT_KEY.upper()} ARBITRAGE BETS ...")
    print("-----------") 


    games = parse_data(SPORT_KEY, WAGER_TYPE, BOOK_KEY)

    #html_content = []

    for g in games:
        html_content = f"""
        <h3>{f"{g['sport_title'].upper()}"} Arbitrage Bets</h3>
        <p> {f"{g['sport_title']}: {g['away_team']} ({plus_sign(g['away_spread'][0])}) @ {g['home_team']}"} ({plus_sign(g['home_spread'][0])}) </p>
        <p>BEST BETS: </p>
        <p> </p>
        <p>{f"{g['away_team']}: {g['best_away_book']} ({plus_sign(g['best_a_spread'])}, {plus_sign(g['best_a_price'])}"} </p>
        <p>{f"{g['home_team']}: {g['best_home_book']} ({plus_sign(g['best_h_spread'])}, {plus_sign(g['best_h_price'])}"} </p>
        """

        #html_content.append[html_contents]

    send_email(subject= f"{SPORT_KEY.upper()} Arbitrage Bets", html=html_content)
