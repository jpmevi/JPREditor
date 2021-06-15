from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo


class Asignacion(Instruccion):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if(self.expresion=='++'):
            simbolo = Simbolo(self.identificador, "INCREMENTO", self.fila, self.columna, 1)
        elif(self.expresion=='--'):
            simbolo = Simbolo(self.identificador, "DECREMENTO", self.fila, self.columna, -1)
        else:    
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Excepcion): return value

            simbolo = Simbolo(self.identificador, self.expresion.tipo, self.fila, self.columna, value)

        result = table.actualizarTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None
