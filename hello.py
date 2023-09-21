from flask import Flask

# Instanciamos Flask, tenemos que pasar un nombre de aplicacion

app = Flask(__name__)
@app.route('/')

def hola():
    return 'Hola, soy Flask. ¿Cómo te llamas?'

@app.route('/adios')

def adios():
    return 'Te dejo, que tengo hambre'

@app.route('/new')
def nueva():
    return 'Esta ruta es nueva, Cuidado con los bandidos'
