import pygame
import os
import random
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

    def colocarMinas(self,click_x,click_y):
        minas_colocadas = 0
        while minas_colocadas < 10:
            coord_x = random.randint(0,self.tablero.getDimensiones()[0]-1)
            coord_y = random.randint(0,self.tablero.getDimensiones()[1]-1)
            celda = self.tablero.getCelda(coord_x,coord_y)
            if not celda.getContiene_mina() and not (coord_x == click_x and coord_y == click_y):
                celda.colocarMina()
                minas_colocadas+=1

    def obtenerImagen(self, celda):
        numero= 12 if celda.getContiene_mina() else 10
        return self.imagenes[numero]
    def dibujar(self):
        tupla = (0,0)
        for fila in range(self.tablero.getDimensiones()[0]):
            for columna in range(self.tablero.getDimensiones()[1]):
                imagen=self.obtenerImagen(self.tablero.getCelda(fila, columna))
                self.pantalla.blit(imagen, tupla)
                tupla = (tupla[0]+self.tamanioBloque[0], tupla[1])
            tupla = (0,tupla[1]+self.tamanioBloque[0])
    
    def obtener_coordenadas(self, pos):
        return (pos[1] // self.tamanioBloque[1] ,pos[0] // self.tamanioBloque[0] )
    def correr(self):
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    pos_tablero=self.obtener_coordenadas(pos)
                    if not self.minas_colocadas:
                        self.colocarMinas(pos_tablero[0],pos_tablero[1])
                        self.minas_colocadas=True
            self.dibujar()
            pygame.display.flip()
        pygame.quit()