# this is the "app/alpha.py" file

# import secret credentials from .env file

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ODDS_API_KEY")