class Celda:
    def __init__(self):
        self.clickeada = False
        self.contiene_bomba= False
        self.bandera_colocada = False
    def getContiene_bomba(self):
        return self.bandera_colocada
    def getClickeada(self):
        return self.clickeada
    def getBandera_colocada(self):
        return self.bandera_colocada
    

