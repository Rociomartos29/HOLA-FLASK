from . import app

@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados
    """
    return 'Lista de movimientos'

@app.route('/nuevo')
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    return 'Agrega un movimiento nuevo'

@app.route('/modificar')
def update():
    """
    Nos permite editar los datos de un movimiento creado previamente
    """
    return 'Actualizar movimiento'

@app.route('/borrar')
def delete():
    """
    Borra un movimiento existente
    """
    return 'Borrar movimiento'