import sys
import os

print("--- INFORMAÇÃO DE DIAGNÓSTICO ---")
print(f"Executável Python a ser usado: {sys.executable}")
print("\nCaminhos que o Python está a verificar (sys.path):")
for path in sys.path:
    print(f"  - {path}")
print("--- FIM DO DIAGNÓSTICO ---\n\n")


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
