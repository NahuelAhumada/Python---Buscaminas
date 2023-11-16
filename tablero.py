from celda import Celda
class Tablero():
    #Pre: Recibe un tamanio MxN en formato de tupla (M,N)
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.crearTablero()
    def crearTablero(self):
        self.matriz = []
        for i in range(self.tamanio[0]):
            fila=[]
            for j in range(self.tamanio[1]):
                celda = Celda()
                fila.append(celda)
            self.matriz.append(fila)
    def getDimensiones(self):
        return self.tamanio
    def getCelda(self,i,j):
        return self.matriz[i][j]
