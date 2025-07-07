from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.search_service import search_and_save

search_routes = Bottle()


class SearchController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/search', method='GET',
                       callback=self.login_required(self.form))
        self.app.route('/search', method='POST',
                       callback=self.login_required(self.do_search))

    def form(self):
        return self.render('search')

    def do_search(self):
        dep = request.forms.get('departure_id')
        arr = request.forms.get('arrival_id')
        out = request.forms.get('outbound_date')
        ret = request.forms.get('return_date')

        search_and_save(dep, arr, out, ret)
        return redirect('/flights')


SearchController(search_routes)
