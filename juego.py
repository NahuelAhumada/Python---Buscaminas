import pygame
import os
class Juego():
    def __init__(self, tablero, tamanioPantalla):
        pygame.init()
        self.minas_colocadas=False
        self.pantalla=pygame.display.set_mode(tamanioPantalla)
        self.tablero=tablero
        self.tamanioPantalla=tamanioPantalla
        self.tamanioBloque = (tamanioPantalla[0] // self.tablero.getDimensiones()[1], self.tamanioPantalla[1] // self.tablero.getDimensiones()[0])
        self.imagenes = []
        self.cargarImagenes()

    def cargarImagenes(self):
        for nombre_arhivo in os.listdir("img"):
            if (not nombre_arhivo.endswith(".png")):
                continue
            image = pygame.image.load(r"img/"+nombre_arhivo)
            image=pygame.transform.scale(image,(self.tamanioBloque[0],self.tamanioBloque[1]))
            self.imagenes.append(image)

    def colocarMinas(self):
        pass
    def obtenerImagen(self, celda):
        numero= 11 if celda.getContiene_mina() else 9
        return self.imagenes[numero]
    def dibujar(self):
        tupla = (0,0)
        for fila in range(self.tablero.getDimensiones()[0]):
            for columna in range(self.tablero.getDimensiones()[1]):
                self.pantalla.blit(self.imagenes[10], tupla)
                tupla = (tupla[0]+self.tamanioBloque[0], tupla[1])
            tupla = (0,tupla[1]+self.tamanioBloque[0])
    
     
    def correr(self):
        flag = True
        while flag:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    flag = False
            self.dibujar()
            pygame.display.flip()
        pygame.quit()