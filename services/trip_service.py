import os, json
from config import Config

TRIPS_FILE = os.path.join(Config.DATA_PATH, 'trips.json')

class TripService:
    def __init__(self):
        try:
            with open(TRIPS_FILE, 'r', encoding='utf-8') as f:
                self.trips = json.load(f)
        except FileNotFoundError:
            self.trips = []

    def add_roundtrip(self, ida_offer, volta_offer):
        entry = {
            'type': 'roundtrip',
            'total_price': ida_offer.price + volta_offer.price,
            'total_duration': ida_offer.total_duration + volta_offer.total_duration,
            'legs': (
                [ { ... } for leg in ida_offer.legs ],
                [ { ... } for leg in volta_offer.legs ]
            )
        }
        self.trips.append(entry)
        with open(TRIPS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.trips, f, ensure_ascii=False, indent=2)

    def get_all(self):
        return self.trips
