from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.user_service import UserService

user_routes = Bottle()

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_service = UserService()
        self.app.route('/account', method='GET', callback=self.login_required(self.show_account))
        self.app.route('/account', method='POST', callback=self.login_required(self.update_account))

    def show_account(self):
        """ Mostra o formulário com os dados do utilizador logado. """
        user_id = int(request.get_cookie("user_id", secret='your-very-secret-key'))
        user = self.user_service.get_by_id(user_id)
        
        return self.render('account_form', user=user, success=request.query.get('success'))

    def update_account(self):
        """ Atualiza os dados do utilizador. """
        user_id = int(request.get_cookie("user_id", secret='your-very-secret-key'))
        user = self.user_service.get_by_id(user_id)
        self.user_service.edit_user(user)
        return redirect('/account?success=true')

UserController(user_routes)