class Celda:
    def __init__(self):
        self.clickeada = False
        self.contiene_mina= False
        self.bandera_colocada = False
    def getContiene_mina(self):
        return self.contiene_mina
    def getClickeada(self):
        return self.clickeada
    def getBandera_colocada(self):
        return self.bandera_colocada
    def colocarMina(self):
        self.contiene_mina=True
    

