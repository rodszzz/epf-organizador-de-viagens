from bottle import Bottle, request
from .base_controller import BaseController
from services.trip_service import TripService
from bottle import Bottle, request, redirect

trip_routes = Bottle()

class TripController(BaseController):
     
    def __init__(self, app):
        super().__init__(app)
        self.app.route('/trips', method='GET', callback=self.login_required(self.list_trips))
        self.app.route('/trips/delete/<trip_idx:int>', method='GET', callback=self.login_required(self.delete_trip))

    def delete_trip(self, trip_idx):
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        service = TripService()
        service.delete_trip_for_user(user_id, trip_idx)
        return redirect('/trips')

    def list_trips(self):
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        
        service = TripService()
        user_trips = service.get_all_trips_for_user(user_id)
        
        return self.render('trips', trips=user_trips)
    
TripController(trip_routes)