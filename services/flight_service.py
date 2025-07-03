from models.flights import FlightModel

class FlightService:
    def __init__(self, direction='ida'):
        self.model = FlightModel(direction)

    def list_offers(self):
        return self.model.get_all()
