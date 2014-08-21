from bottle import route
from controllers import *

def setup_routes(app):
    app.route('/', 'GET', index)

