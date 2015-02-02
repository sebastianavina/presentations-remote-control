from bottle import route, run, template, static_file

import funciones_xdo
from lecture import lecture

# Static dir for serving styles and stuff.
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# Main page
@route('/')
def index()
:
    return template("views/principal.htm", name="hola")

@route('/prepare/<name>')
def prepare(name):
    funciones_xdo.go_presentation_mode("27262979")
    return template('<b>Prepare {{name}}</b>!', name=name)

@route('/run/<pagina>')
def run_presentation(pagina):
    funciones_xdo.change_evince_page(pagina,"27262979")
    return template('<b>Run {{name}}</b>!', name=name)

run(host='0.0.0.0', port=8080)
