from bottle import run

import config.database
import config.routes

run(host="localhost", port=8080)
