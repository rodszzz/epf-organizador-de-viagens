# models/flights.py
import os, json
from config import Config

class FlightLeg:
    def __init__(self, dep, arr, duration, airline, flight_number, travel_class, airplane):
        # dep/arr são dicts com keys: name, id, time
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

class FlightOffer:
    def __init__(self, raw: dict):
        # raw vem do JSON, por ex: raw['flights'], raw['price'], raw['total_duration'], raw['booking_token'], etc.
        self.legs           = [
            FlightLeg(
                leg['departure_airport'],
                leg['arrival_airport'],
                leg['duration'],
                leg['airline'],
                leg.get('flight_number',''),
                leg.get('travel_class',''),
                leg.get('airplane','')
            ) for leg in raw['flights']
        ]
        self.total_duration = raw.get('total_duration')
        self.price          = raw.get('price')
        self.type           = raw.get('type')
        self.airline_logo   = raw.get('airline_logo')
        self.booking_token  = raw.get('booking_token')

class FlightModel:
    def __init__(self, direction='ida'):
        filename = 'ida.json' if direction == 'ida' else 'volta.json'
        path = os.path.join(Config.DATA_PATH, filename)
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        self.raw_offers = data.get('best_flights', [])

    def get_all(self):
        return [FlightOffer(raw) for raw in self.raw_offers]
