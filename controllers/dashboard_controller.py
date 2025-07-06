from bottle import Bottle, request
from .base_controller import BaseController
from models.user import UserModel

dashboard_routes = Bottle()

class DashboardController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        # Protege a rota do dashboard com o decorator de login
        self.app.route('/dashboard', method='GET', callback=self.login_required(self.dashboard))

    def dashboard(self):
        # Obtém o ID do utilizador do cookie
        user_id = request.get_cookie("user_id", secret='your-very-secret-key')
        
        # Encontra o utilizador para obter o nome
        user_model = UserModel()
        user = user_model.get_by_id(int(user_id))
        
        # Renderiza a página do dashboard, passando o nome do utilizador
        return self.render('dashboard', user_name=user.name if user else "Utilizador")

# Inicializa o controlador
DashboardController(dashboard_routes)