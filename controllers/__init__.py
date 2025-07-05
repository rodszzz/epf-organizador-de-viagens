from bottle import Bottle
from controllers.user_controller   import user_routes
from controllers.search_controller import search_routes
from controllers.flight_controller import flight_routes
from controllers.trip_controller   import trip_routes

def init_controllers(app: Bottle):
    # Se não usar mais users, basta remover a linha abaixo
    app.merge(user_routes)

    # Ordem: /search → /flights → /trips
    app.merge(search_routes)
    app.merge(flight_routes)
    app.merge(trip_routes)
