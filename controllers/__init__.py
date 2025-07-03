from bottle import Bottle
from controllers.user_controller   import user_routes
from controllers.flight_controller import flight_routes
from controllers.trip_controller   import trip_routes

def init_controllers(app: Bottle):
    # se não usar mais usuários, basta comentar/remover user_routes
    app.merge(user_routes)
    app.merge(flight_routes)
    app.merge(trip_routes)
