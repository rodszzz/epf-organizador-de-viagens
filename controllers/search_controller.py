# controllers/search_controller.py

from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.search_service import search_and_save

search_routes = Bottle()

class SearchController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        # Formulário de busca
        self.app.route('/search', method='GET',  callback=self.form)
        # Processa submissão
        self.app.route('/search', method='POST', callback=self.do_search)

    def form(self):
        # Renderiza views/search.tpl
        return self.render('search')

    def do_search(self):
        # Lê campos do formulário
        dep = request.forms.get('departure_id')
        arr = request.forms.get('arrival_id')
        out = request.forms.get('outbound_date')
        ret = request.forms.get('return_date')

        # Executa busca e salva JSON em data/
        search_and_save(dep, arr, out, ret)

        # Redireciona para a listagem de voos
        return redirect('/flights')

# Monta as rotas
SearchController(search_routes)
