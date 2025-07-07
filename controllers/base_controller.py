from bottle import static_file

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def _setup_base_routes(self):
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        self.app.route('/outraCoisa',
                       method=['GET'], callback=self.outra_func)

        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def outra_func(self):
        return self.render('outro_arquivo')

    def home_redirect(self):
        return self.redirect('/login')

    def helper(self):
        return self.render('helper-final')

    def serve_static(self, filename):
        return static_file(filename, root='./static')

    def render(self, template, **context):
        from bottle import template as render_template
        return render_template(template, **context)

    def redirect(self, path):
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)

    def login_required(self, callback):
        from bottle import request, redirect
        def wrapper(*args, **kwargs):
            user_id = request.get_cookie("user_id", secret='your-very-secret-key')
            if user_id:
                return callback(*args, **kwargs)
            return redirect('/login')
        return wrapper