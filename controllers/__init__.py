from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.search_controller import search_routes
from controllers.flight_controller import flight_routes
from controllers.trip_controller import trip_routes
from controllers.auth_controller import auth_routes  
from controllers.dashboard_controller import dashboard_routes

def init_controllers(app: Bottle):
    app.merge(auth_routes)
    app.merge(dashboard_routes) 
    app.merge(user_routes)
    app.merge(search_routes)
    app.merge(flight_routes)
    app.merge(trip_routes)
