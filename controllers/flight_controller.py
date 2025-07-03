from bottle import Bottle, request
from .base_controller import BaseController
from services.flight_service import FlightService
from services.trip_service   import TripService

flight_routes = Bottle()

class FlightController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/flights',      method='GET',  callback=self.list_flights)
        self.app.route('/flights/book', method='POST', callback=self.book_flight)

    def list_flights(self):
        ida_offers   = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()

        combined = []
        for i, (ida, volta) in enumerate(zip(ida_offers, volta_offers)):
            combined.append({
                'idx': i,
                'ida': ida,
                'volta': volta,
                'total_price': ida.price + volta.price,
                'total_duration': ida.total_duration + volta.total_duration
            })

        return self.render('flights', offers=combined)

    def book_flight(self):
        idx = int(request.forms.get('offer_idx'))
        ida_offers   = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()
        ida, volta   = ida_offers[idx], volta_offers[idx]

        TripService().add_roundtrip(ida, volta)
        return self.redirect('/trips')

FlightController(flight_routes)
