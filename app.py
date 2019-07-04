from bottle import route, run, template, static_file, post, request, get
import sqlite3

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='statics')

@route('/hello/<name>')
def hello(name):
    return template('<b>hola {{name}}</b>!', name=name)

@post('/crear')
def crear():
    nombre = request.forms.get('nombre')
    edad = int(request.forms.get('edad'))
    locals = {
        'nombre': nombre,
        'edad': edad,
        'juegos': [
            {
                'genero': 'Terror',
                'nombre': 'Resident Evil'
            },
            {
                'genero': 'Plataforma',
                'nombre': 'Crash Banticoot'
            },
        ],
    }
    return template('index', locals=locals)

@route('/')
def index():
    locals = {
        'nombre': 'Pepe',
        'edad': 3,
        'juegos': [
            {
                'genero': 'Terror',
                'nombre': 'Resident Evil'
            },
            {
                'genero': 'Plataforma',
                'nombre': 'Crash Banticoot'
            },
        ],
    }
    return template('index', locals=locals)

@get('/producto/listar')
def producto_listar():
    conn = sqlite3.connect('db/belcorp.db')
    c = conn.cursor()
    c.execute("SELECT * FROM producto")
    rs = c.fetchall()
    productos = []
    for r in rs:
        temp = {
            'id': r[0],
            'nombre': r[1],
            'precio': r[2],
            'imagen': r[3],
            'ficha': r[4],
        }
        productos.append(temp)
    locals = {
        'productos': productos,
    }
    return template('productos', locals=locals)

run(host='localhost', port=8080, debug=True, reloader=True)