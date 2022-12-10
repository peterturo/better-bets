# this is the "web_app/routes/bestbets_routes.py" file ...
# from https://github.com/s2t2/unemployment-inclass-2022

from flask import Blueprint, request, render_template, redirect, flash

from app.bestbets import parse_data

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


        flash("Fetched Latest Betting Data!", "success")
        return render_template("bestbets_dashboard.html",
            sport_title=sport_title,
            games=games
        )
    except Exception as err:
        print('OOPS', err)

        flash("Betting Data Error. There are currently no available bets for your selected sport!", "danger")
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