class Celda:
    def __init__(self):
        self.bombas_alrededor=0
        self.click_izquierdo = False
        self.contiene_mina= False
        self.bandera_colocada = False
    def getBombas_alrededor(self):
        return self.bombas_alrededor
    def getContiene_mina(self):
        return self.contiene_mina
    def getClickeada(self):
        return self.click_izquierdo
    def getBandera_colocada(self):
        return self.bandera_colocada
    def colocarMina(self):
        self.contiene_mina=True
    def setVecinos(self,vecinos):
        self.vecinos = vecinos
        self.setBombas_alredador()
    def setBombas_alredador(self):
        self.bombas_alrededor=0
        for vecino in self.vecinos:
            if vecino.getContiene_mina():
                self.bombas_alrededor+=1
    def click_bandera(self):
        self.bandera_colocada=not self.bandera_colocada
    def hacer_click_izquiedo(self):
        self.click_izquierdo=True

        
    

