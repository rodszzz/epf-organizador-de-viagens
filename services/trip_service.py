from models.trip import Trip, TripModel
from services.flight_service import FlightService

class TripService:
    def __init__(self):
        self.trip_model = TripModel()

    def get_all_trips_for_user(self, user_id):
        """ Obtém todas as viagens guardadas por um utilizador. """
        return self.trip_model.get_trips_by_user_id(user_id)
    
    def delete_trip_for_user(self, user_id, trip_index):
        """ Pede ao modelo para apagar uma viagem específica. """
        return self.trip_model.delete_trip_for_user(user_id, trip_index)

    def save_roundtrip_for_user(self, user_id, offer_idx):
        """ Encontra a oferta de voo e guarda-a para o utilizador. """
        ida_offers = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()

        # Verifica se o índice da oferta é válido
        if offer_idx < 0 or offer_idx >= len(ida_offers):
            return None # Oferta não encontrada

        ida_offer = ida_offers[offer_idx]
        volta_offer = volta_offers[offer_idx]

        total_price = ida_offer.price + volta_offer.price
        total_duration = ida_offer.total_duration + volta_offer.total_duration
        h, m = divmod(total_duration, 60)
        total_duration_hm = f"{h}h {m}m"

        # Cria um objeto Trip
        new_trip = Trip(
            ida=ida_offer,
            volta=volta_offer,
            total_price=total_price,
            total_duration_hm=total_duration_hm
        )
        
        # Guarda a viagem para o utilizador
        self.trip_model.add_trip_for_user(user_id, new_trip)
        
        return new_trip