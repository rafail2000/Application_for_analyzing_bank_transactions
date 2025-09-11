import os
from dotenv import load_dotenv
from pprint import pprint

import requests

load_dotenv()

api_key = os.environ.get("API_KEY")

data = requests.get(api_key).json()
pprint(data['Valute']['AMD'])
