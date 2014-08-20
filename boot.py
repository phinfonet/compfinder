from bottle import run

import controllers
import config.database
import config.routes

run(app, host="localhost", port=8080)
