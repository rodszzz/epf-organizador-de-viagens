# controllers/flight_controller.py

from bottle import Bottle, request, redirect
from .base_controller      import BaseController
from services.flight_service import FlightService

flight_routes = Bottle()

class FlightController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        # Listagem de ofertas
        self.app.route('/flights',      method='GET', callback=self.list_flights)
        # Redirecionamento para o deep_link (ida ou volta)
        self.app.route('/flights/book', method='GET', callback=self.book_flight)

    def list_flights(self):
        ida_offers   = FlightService('ida').list_offers()
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
        # Lê o índice e a perna (ida ou volta)
        idx = int(request.query.get('offer_idx', 0))
        leg = request.query.get('leg', 'ida')

        # Recarrega as ofertas para selecionar a correta
        ida_offers   = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()
        offer = ida_offers[idx] if leg == 'ida' else volta_offers[idx]

        # Usa o deep_link diretamente
        link = getattr(offer, 'deep_link', None)
        if link:
            return redirect(link)

        # Fallback: volta para a listagem se não tiver link
        return redirect('/flights')

# Registra o controller
FlightController(flight_routes)
