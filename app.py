from bottle import route, run, template, static_file, post, request

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

run(host='localhost', port=8080, debug=True, reloader=True)