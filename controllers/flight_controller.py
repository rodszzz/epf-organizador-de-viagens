from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.trip_service import TripService

flight_routes = Bottle()


class FlightController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.app.route('/flights', method='GET', callback=self.list_flights)
        self.app.route('/flights/book', method='GET',
                       callback=self.book_flight)

    def list_flights(self):
        from services.flight_service import FlightService
        ida_offers = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()

        combined = []
        for i, (ida, volta) in enumerate(zip(ida_offers, volta_offers)):
            total_price = ida.price + volta.price
            total_duration = ida.total_duration + volta.total_duration
            h, m = divmod(total_duration, 60)
            combined.append({
                'idx':               i,
                'ida':               ida,
                'volta':             volta,
                'total_price':       total_price,
                'total_duration_hm': f"{h}h {m}m"
            })

        return self.render('flights', offers=combined)

    def book_flight(self):
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        if not user_id:
            return redirect('/login')

        try:
            offer_idx = int(request.query.get('offer_idx', -1))
        except (ValueError, TypeError):
            return "Índice da oferta inválido."

        trip_service = TripService()
        saved_trip = trip_service.save_roundtrip_for_user(user_id, offer_idx)

        if saved_trip:
            return redirect('/trips')
        else:
            return redirect('/flights')


FlightController(flight_routes)
