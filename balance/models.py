import csv
from datetime import date

from . import RUTA_FICHERO

CLAVES_IGNORADAS = ['errores']

class Movimiento:
    def __init__(self, dict_datos):

        self.errores = []
        self.fecha = dict_datos.get('fecha', '')
        self.concepto = dict_datos.get('concepto', 'Gastos Varios')
        self.tipo = dict_datos.get('tipo')
        self.cantidad = dict_datos.get('cantidad')
        try:
            self.fecha = date.fromisoformat(self.fecha)
        except ValueError:
            self.fecha = None
            self.errores.append(f'La fecha {self.fecha} no es una fecha válida')


    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}\n'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        self.movimientos = []

    def leer_desde_archivo(self):
        self.movimientos = []
        with open(RUTA_FICHERO, 'r') as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(fila)
                self.movimientos.append(movimiento)

    def agregar(self, movimiento):
        if not isinstance(movimiento, Movimiento):
            raise ValueError('No pouedes agregar eso, no es un movimiento')
        
        self.movimientos.append(movimiento)
        self.guardar()

    def guardar(self):

        with open(RUTA_FICHERO, 'w') as csvfile:

            '''
            cabecera = ['fecha', 'concepto', 'tipo', 'cantidad']
            writer = csv.writer(csvfile)
            writer.writerow((cabecera))
            '''
            cabeceras = list(self.movimientos[0].__dict__.keys())

            for clave in CLAVES_IGNORADAS:
                cabeceras.remove(clave)

            writer = csv.DictWriter(csvfile, fieldnames=cabeceras)
            writer.writeheader()
            for mov in self.movimientos:
                mov_dict = mov.__dict__
                for clave in CLAVES_IGNORADAS:
                    mov.__dict__.pop(clave)
                writer.writerow(mov_dict)
   
   
   
   
   
   
   
    def __str__(self):
        result = ''
        for mov in self.movimientos:
            result += f'\n{mov}'
        return result

    def __repr__(self):
        return self.__str__()