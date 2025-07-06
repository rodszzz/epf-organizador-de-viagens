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
        self.app.route('/register', method=['GET', 'POST'], callback=self.register)

    # (Mantenha os outros imports e o código da classe)

    def login(self):
        if request.method == 'POST':
            email = request.forms.get('email')
            password = request.forms.get('password')

            # --- Início do Diagnóstico ---
            print(f"\n[DEBUG] Tentativa de login com email: {email}")
            
            user = self.user_model.get_by_email(email)

            if user:
                print(f"[DEBUG] Utilizador encontrado: {user.name} (ID: {user.id})")
                
                # Vamos verificar a senha
                password_is_correct = user.check_password(password)
                print(f"[DEBUG] A senha fornecida está correta? {password_is_correct}")

            if user and user.check_password(password):
                # ... (código de debug, se ainda existir)
                response.set_cookie("user_id", str(user.id), secret='your-very-secret-key')
                return redirect('/dashboard') # Alterado de '/search' para '/dashboard'
            else:
                print("[DEBUG] Utilizador com este email não foi encontrado.")
            # --- Fim do Diagnóstico ---

            # Se o código chegar aqui, o login falhou
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

            # Validação
            if self.user_model.get_by_email(email):
                return self.render('register', error="Este email já está cadastrado.")
            if password != password_confirm:
                return self.render('register', error="As senhas não coincidem.")

            # Se tudo estiver ok, salva o usuário
            user_service.save()
            return redirect('/login')

        # Para o método GET, mostra o formulário de registro
        return self.render('register', error=None)

# Inicializa o controlador
AuthController(auth_routes)