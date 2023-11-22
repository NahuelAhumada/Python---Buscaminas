from celda import Celda
import random
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
    
    def colocarVecinos(self):
        for fila in range(self.tamanio[0]):
            for columna in range(self.tamanio[1]):
                celda = self.getCelda(fila,columna)
                vecinos = self.obtenerListaDeVecinos((fila, columna))
                celda.setVecinos(vecinos)

    def obtenerListaDeVecinos(self, indice):
        vecinos=[]
        for i in range(-1,2):
            for j in range(-1,2):
                pos_x=indice[0]+i
                pos_y=indice[1]+j
                if not (pos_x<=0 or pos_x<self.tamanio[0] or pos_y>=0 or pos_y<self.tamanio[0]):
                    if i!=0 and j!=0:
                        vecinos.append(self.matriz[pos_x][pos_y])
        return vecinos

    def getCelda(self,i,j):
        return self.matriz[i][j]
    
    def colocarMinas(self,pos_x,pos_y):
        minas_colocadas = 0
        while minas_colocadas < 10:
            coord_x = random.randint(0,self.tamanio[0]-1)
            coord_y = random.randint(0,self.tamanio[1]-1)
            celda = self.getCelda(coord_x,coord_y)
            if not celda.getContiene_mina() and not (coord_x == pos_x and coord_y == pos_y):
                celda.colocarMina()
                minas_colocadas+=1