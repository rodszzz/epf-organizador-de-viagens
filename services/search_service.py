# services/search_service.py

import os
import json
import serpapi
from dotenv import load_dotenv
from config import Config

# carrega o arquivo .env que deve estar na raiz do projeto
load_dotenv()

# pega a chave da SerpAPI
API_KEY = os.getenv('SERPAPI_KEY')
if not API_KEY:
    raise RuntimeError("Por favor defina SERPAPI_KEY no seu .env")

def search_and_save(dep_id, arr_id, outbound_date, return_date,
                    currency='BRL', hl='pt-br'):
    """
    Faz a busca de voos de ida e volta no Google Flights via SerpAPI
    e salva os resultados em JSON em Config.DATA_PATH/data/{ida,volta}.json
    """
    base = {
        "api_key":      API_KEY,
        "engine":       "google_flights",
        "departure_id": dep_id,
        "arrival_id":   arr_id,
        "currency":     currency,
        "hl":           hl
    }

    # 1) busca ida
    params_ida  = { **base, "outbound_date": outbound_date }
    results_ida = serpapi.search(**params_ida)

    # 2) busca volta (inverte origem/destino e adiciona type=2)
    params_volta  = {
        **base,
        "departure_id":  arr_id,
        "arrival_id":    dep_id,
        "outbound_date": return_date,
        "type":          2
    }
    results_volta = serpapi.search(**params_volta)

    # 3) garante a pasta data/
    data_dir = os.path.join(Config.DATA_PATH, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # 4) grava em arquivos JSON
    ida_path   = os.path.join(data_dir, 'ida.json')
    volta_path = os.path.join(data_dir, 'volta.json')

    with open(ida_path,   'w', encoding='utf-8') as f:
        json.dump(results_ida,   f, ensure_ascii=False, indent=2)
    with open(volta_path, 'w', encoding='utf-8') as f:
        json.dump(results_volta, f, ensure_ascii=False, indent=2)
