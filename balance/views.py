from flask import render_template, request, redirect, url_for


from . import app
from .models import ListaMovimientos, Movimiento



@app.route('/')
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template(
        'inicio.html',
        movs=lista.movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en el archivo CSV
    """
    if request.method == 'GET':
        return render_template('nuevo.html')
    if request.method =='POST':
        mov =  Movimiento(request.form)
        lista = ListaMovimientos()
        lista.leer_desde_archivo()
        lista.agregar(mov)
        return redirect(url_for('home'))



@app.route('/modificar')
def update():
    """
    Permite editar los datos de un movimiento creado previamente.
    """
    return 'Actualizar movimiento'


@app.route('/borrar')
def delete():
    """
    Borra un movimiento existente.
    """
    return 'Borrar movimiento'