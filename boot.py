import config.database
from bottle import Bottle, run
from config.routes import *

app = Bottle()

setup_routes(app)
run(app, host="localhost", port=8080)
