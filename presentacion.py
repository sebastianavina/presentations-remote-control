from bottle import route, get, post, run, request, template, static_file, redirect

import os
import commands

import funciones_xdo
from lecture import lecture


# Static dir for serving styles and stuff.
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

# Main page
@get('/')
def index():
    xdo = ""
    if "xdo" in request.query:
        xdo = request.query["xdo"]
        funciones_xdo.go_presentation_mode(xdo)
    ventanas = commands.getstatusoutput("xdotool search \"evince\"",)
    import re
    grupos = re.findall(r"([0-9]{8})", str(ventanas))
    return template("views/principal.htm", name="hola", ventanas = grupos ,xdo = xdo)

@post('/')
def index():
    archivo = request.forms.get("presentacion")
    xdo = request.forms.get("xdo")
    instruccion = "convert -density 300 %s -resize 200 static/thumbs/%s " % \
                  (str(archivo), "filminas.png")
    os.popen(instruccion)
    redirect("/run/y?file=%s&xdo=%s" % (archivo,xdo))

@route('/prepare/<name>')
def prepare(name):
    funciones_xdo.go_presentation_mode("27262979")
    return template('<b>Prepare {{name}}</b>!', name=name)

@get('/run/<pagina>')
def run_presentation(pagina):
    if "goto" in request.query:
        xdo = request.query["xdo"]
        pagina =request.query["goto"]
        funciones_xdo.change_evince_page(pagina,xdo)

    files = []
    #funciones_xdo.change_evince_page(pagina,"27262979")
    filenames = next(os.walk("static/thumbs/"))[2]

    return template("views/mostrar.htm", name=pagina, \
                    archivos = filenames, \
                    xdo = request.query["xdo"], \
                    ventanas = "")

run(host='0.0.0.0', port=8080)
