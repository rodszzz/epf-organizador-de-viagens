from models.trip import Trip, TripModel
from services.flight_service import FlightService

class TripService:
    def __init__(self):
        self.trip_model = TripModel()

    def get_all_trips_for_user(self, user_id):
        return self.trip_model.get_trips_by_user_id(user_id)
    
    def delete_trip_for_user(self, user_id, trip_index):
        return self.trip_model.delete_trip_for_user(user_id, trip_index)

    def save_roundtrip_for_user(self, user_id, offer_idx):
        ida_offers = FlightService('ida').list_offers()
        volta_offers = FlightService('volta').list_offers()

        if offer_idx < 0 or offer_idx >= len(ida_offers):
            return None 

        ida_offer = ida_offers[offer_idx]
        volta_offer = volta_offers[offer_idx]

        total_price = ida_offer.price + volta_offer.price
        total_duration = ida_offer.total_duration + volta_offer.total_duration
        h, m = divmod(total_duration, 60)
        total_duration_hm = f"{h}h {m}m"

        new_trip = Trip(
            ida=ida_offer,
            volta=volta_offer,
            total_price=total_price,
            total_duration_hm=total_duration_hm
        )
        
        self.trip_model.add_trip_for_user(user_id, new_trip)
        
        return new_trip