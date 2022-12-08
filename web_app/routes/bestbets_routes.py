# this is the "web_app/routes/bestbets_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.bestbets import parse_data, plus_sign

bestbets_routes = Blueprint("bestbets_routes", __name__)

@bestbets_routes.route("/bestbets/form")
def bestbets_form():
    print("ARBITRAGE FORM...")
    return render_template("bestbets_form.html")

@bestbets_routes.route("/bestbets/dashboard", methods=["GET", "POST"])
def bestbets_dashboard():
    print("ARBITRAGE DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    sport_key = request_data.get("sport_key") or "americanfootball_nfl"
    
    try:
        games = parse_data(sport_key=sport_key, wager_type="spreads", book_key="")
    
        for g in games:
            sport_title = g["sport_title"]
            away_team = g["away_team"]
            home_team = g["home_team"]
            away_spread = plus_sign(g["away_spread"][0])
            home_spread = plus_sign(g["home_spread"][0])
            best_away_book = g["best_away_book"]
            best_home_book = g["best_home_book"]
            best_a_spread = plus_sign(g["best_a_spread"])
            best_h_spread = plus_sign(g["best_h_spread"])
            best_a_price = plus_sign(g["best_a_price"])
            best_h_price = plus_sign(g["best_h_price"])


        flash("Fetched Latest Betting Data!", "success")
        return render_template("bestbets_dashboard.html",
            sport_key=sport_key,
            sport_title=sport_title,
            away_team=away_team,
            home_team=home_team,
            away_spread=away_spread,
            home_spread=home_spread,
            best_away_book=best_away_book,
            best_home_book=best_home_book,
            best_a_spread=best_a_spread,
            best_h_spread=best_h_spread,
            best_a_price=best_a_price,
            best_h_price=best_h_price
        )
    except Exception as err:
        print('OOPS', err)

        flash("Betting Data Error. Please check your sport and wager and try again!", "danger")
        return redirect("/bestbets/form")

#
# API ROUTES
#

@bestbets_routes.route("/api/bestbets.json")
def bestbets_api():
    print("BETTING DATA (API)...")

    # for data supplied via GET request, url params are in request.args:
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)
    sport_key = url_params.get("sport_key") or "americanfootball_nfl"

    try:
        games = parse_data(sport_key=sport_key, wager_type="spreads", book_key="")
        return games
    except Exception as err:
        print('OOPS', err)
        return {"message":"Betting Data Error. Please try again."}, 404