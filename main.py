from bottle import Bottle, run
from config import Config
from controllers import init_controllers

app = Bottle()
init_controllers(app)

if __name__ == '__main__':
    run(app,
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG,
        reloader=Config.RELOADER)
