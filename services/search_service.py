import os
import json
import serpapi
from dotenv import load_dotenv
from config import Config

load_dotenv()

API_KEY = os.getenv('SERPAPI_KEY')


def search_and_save(dep_id, arr_id, outbound_date, return_date,
                    currency='BRL', hl='pt-br'):
    base = {
        "api_key":      API_KEY,
        "engine":       "google_flights",
        "departure_id": dep_id,
        "arrival_id":   arr_id,
        "currency":     currency,
        "hl":           hl
    }

    params_ida = {**base, "outbound_date": outbound_date, "type": "2"}
    raw_ida = serpapi.search(**params_ida)
    results_ida = raw_ida.as_dict()

    params_volta = {
        **base,
        "departure_id":  arr_id,
        "arrival_id":    dep_id,
        "outbound_date": return_date,
        "type":          "2"
    }
    raw_volta = serpapi.search(**params_volta)
    results_volta = raw_volta.as_dict()
    data_dir = Config.DATA_PATH
    os.makedirs(data_dir, exist_ok=True)

    ida_path = os.path.join(data_dir, 'ida.json')
    volta_path = os.path.join(data_dir, 'volta.json')

    with open(ida_path,   'w', encoding='utf-8') as f:
        json.dump(results_ida,   f, ensure_ascii=False, indent=2)

    with open(volta_path, 'w', encoding='utf-8') as f:
        json.dump(results_volta, f, ensure_ascii=False, indent=2)
