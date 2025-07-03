from bottle import Bottle
from .base_controller import BaseController
from services.trip_service import TripService

trip_routes = Bottle()

class TripController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/trips', method='GET', callback=self.list_trips)

    def list_trips(self):
        trips = TripService().get_all()
        return self.render('trips', trips=trips)

TripController(trip_routes)
