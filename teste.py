import os
import json
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('SERPAPI_KEY')

params_ida = {
    "engine": "google_flights",
    "departure_id": "BSB",
    "arrival_id": "IBZ",
    "outbound_date": "2025-07-30",
    "currency": "BRL",
    "hl": "pt-br",
    "api_key": api_key,
    "type": 2
}

search_ida = GoogleSearch(params_ida)
results_ida = search_ida.get_dict()

with open("ida.json", "w", encoding="utf-8") as f:
    json.dump(results_ida, f, ensure_ascii=False, indent=2)


params_volta = {
    "engine": "google_flights",
    "departure_id": "IBZ",
    "arrival_id": "BSB",
    "outbound_date": "2025-08-07",  
    "currency": "BRL",
    "hl": "pt-br",
    "api_key": api_key,
    "type": 2
}

search_volta = GoogleSearch(params_volta)
results_volta = search_volta.get_dict()

with open("volta.json", "w", encoding="utf-8") as f:
    json.dump(results_volta, f, ensure_ascii=False, indent=2)

