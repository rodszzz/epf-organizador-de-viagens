from bottle import Bottle, request, response, redirect
from .base_controller import BaseController
from models.user import UserModel
from services.user_service import UserService

auth_routes = Bottle()


class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_model = UserModel()
        self._setup_routes()

    def _setup_routes(self):
        self.app.route('/login', method=['GET', 'POST'], callback=self.login)
        self.app.route('/logout', method='GET', callback=self.logout)
        self.app.route(
            '/register', method=['GET', 'POST'], callback=self.register)

    def login(self):
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')

            print(f"\n[DEBUG] Tentativa de login com email: {email}")

            user = self.user_model.get_by_email(email)

            if user:
                print(f"[DEBUG] Utilizador encontrado: {
                      user.name} (ID: {user.id})")

                password_is_correct = user.check_password(password)
                print(f"[DEBUG] A senha fornecida está correta? {
                      password_is_correct}")

            if user and user.check_password(password):
                response.set_cookie("user_id", str(
                    user.id), secret='your-very-secret-key')
                return redirect('/dashboard')
            else:
                print("[DEBUG] Utilizador com este email não foi encontrado.")

            print("[DEBUG] Login falhou. A recarregar a página de login com erro.")
            return self.render('login', error="Email ou senha inválidos.")

        return self.render('login', error=None)

    def logout(self):
        response.delete_cookie("user_id")
        return redirect('/login')

    def register(self):
        if request.method == 'POST':
            user_service = UserService()
            email = request.forms.get('email')
            password = request.forms.get('password')
            password_confirm = request.forms.get('password_confirm')

            if self.user_model.get_by_email(email):
                return self.render('register', error="Este email já está cadastrado.")
            if password != password_confirm:
                return self.render('register', error="As senhas não coincidem.")

            user_service.save()
            return redirect('/login')

        return self.render('register', error=None)


AuthController(auth_routes)
