# better-bets


## Setup


Create and activate a virtual environemt:

```sh
conda create -n betterbets-env python=3.8

conda activate betterbets-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an Odds API Key](https://the-odds-api.com/) from The Odds API (i.e. `ODDS_API_KEY`).

Also sign up for the [SendGrid Service](https://sendgrid.com/), verify your single sender address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API Key (i.e. `SENDGRID_API_KEY`).

Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

ODDS_API_KEY="_________"
SENDER_EMAIL_ADDRESS="you@example.com"
SENDGRID_API_KEY="__________"
```


## Usage

Show a full betting slate:

```sh
python -m app.odds
```

Show arbitrage lines:

```sh
python -m app.bestbets
```


### Email Sending

Run the email service to send an example email and see if everything is working:

```sh
python -m app.bestbets_email
```