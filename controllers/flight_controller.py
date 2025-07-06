from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.trip_service import TripService

flight_routes = Bottle()

class FlightController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        # O método setup_routes agora está no BaseController, mas o mantemos para rotas específicas
        self.app.route('/flights', method='GET', callback=self.list_flights)
        # A rota de reserva agora guarda a viagem
        self.app.route('/flights/book', method='GET', callback=self.book_flight)

    def list_flights(self):
        # A lógica de list_flights do seu código original
        from services.flight_service import FlightService
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

    # Este método foi modificado para guardar a viagem
    def book_flight(self):
        # Primeiro, verificamos se o utilizador está logado
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        if not user_id:
            return redirect('/login')

        # Obtém o índice da oferta a partir da URL (?offer_idx=...)
        try:
            offer_idx = int(request.query.get('offer_idx', -1))
        except (ValueError, TypeError):
            return "Índice da oferta inválido."
        
        # Cria e guarda a viagem
        trip_service = TripService()
        saved_trip = trip_service.save_roundtrip_for_user(user_id, offer_idx)

        if saved_trip:
            # Redireciona para a página de viagens do utilizador para ele ver o que guardou
            return redirect('/trips')
        else:
            # Se a oferta não foi encontrada, volta para a listagem
            return redirect('/flights')


# Registra o controller
FlightController(flight_routes)