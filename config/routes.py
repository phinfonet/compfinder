from bottle import route, Bottle

app = Bottle()
app.route('/', 'GET', callback=index)

