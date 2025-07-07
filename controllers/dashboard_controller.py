from bottle import Bottle, request
from .base_controller import BaseController
from models.user import UserModel

dashboard_routes = Bottle()

class DashboardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.app.route('/dashboard', method='GET', callback=self.login_required(self.dashboard))

    def dashboard(self):
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        
        user_model = UserModel()
        user = user_model.get_by_id(int(user_id))
        
        return self.render('dashboard', user_name=user.name if user else "Utilizador")

DashboardController(dashboard_routes)