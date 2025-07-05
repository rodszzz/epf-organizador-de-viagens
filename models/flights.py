# models/flights.py

import os
import json
from config import Config

class FlightLeg:
    def __init__(self, dep, arr, duration, airline, flight_number, travel_class, airplane):
        # dep e arr são dicts: {'name': ..., 'id': ..., 'time': ...}
        self.departure_airport_name = dep['name']
        self.departure_airport_code = dep['id']
        self.departure_time         = dep['time']
        self.arrival_airport_name   = arr['name']
        self.arrival_airport_code   = arr['id']
        self.arrival_time           = arr['time']
        self.duration               = duration
        self.airline                = airline
        self.flight_number          = flight_number
        self.travel_class           = travel_class
        self.airplane               = airplane

    @property
    def duration_hm(self):
        h, m = divmod(self.duration, 60)
        return f"{h}h {m}m" if h else f"{m}m"

class FlightOffer:
    def __init__(self, raw: dict):
        # mapeia cada perna (leg)
        self.legs           = [
            FlightLeg(
                leg['departure_airport'],
                leg['arrival_airport'],
                leg['duration'],
                leg['airline'],
                leg.get('flight_number', ''),
                leg.get('travel_class', ''),
                leg.get('airplane', '')
            )
            for leg in raw.get('flights', [])
        ]
        self.total_duration = raw.get('total_duration', 0)
        self.price          = raw.get('price', 0)
        self.type           = raw.get('type', '')
        self.airline_logo   = raw.get('airline_logo', '')
        self.booking_token  = raw.get('booking_token', '')
        # **novo**: link direto para reserva
        self.deep_link      = raw.get('deep_link', '')

    @property
    def total_duration_hm(self):
        h, m = divmod(self.total_duration, 60)
        return f"{h}h {m}m"

    @property
    def booking_link(self):
        """
        Retorna o deep_link, caso exista,
        para ser usado no template.
        """
        return self.deep_link


class FlightModel:
    def __init__(self, direction='ida'):
        filename = 'ida.json' if direction == 'ida' else 'volta.json'
        path = os.path.join(Config.DATA_PATH, filename)
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        # supondo que o JSON tenha a chave 'best_flights'
        self.raw_offers = data.get('best_flights', [])

    def get_all(self):
        # aqui sim passamos cada raw para o construtor
        return [FlightOffer(raw) for raw in self.raw_offers]
