import serpapi
from serpapi import GoogleSearch
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')

# TODO: fazer hash table pra dar um grep no json
params = {
    "engine": "google_flights",
    "departure_id": "BSB",
    "arrival_id": "GRU",
    "outbound_date": "2025-06-30",
    "return_date": "2025-07-07",
    "currency": "BRL",
    "hl": "pt-br",
    "api_key": api_key
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
