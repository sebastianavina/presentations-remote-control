from bottle import route, run, template, static_file

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=8080)
