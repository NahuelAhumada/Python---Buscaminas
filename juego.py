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
        self.imagenes = {}
        self.cargarImagenes()

    def cargarImagenes(self):
        for nombre_arhivo in os.listdir("img"):
            if (not nombre_arhivo.endswith(".png")):
                continue
            image = pygame.image.load(r"img/"+nombre_arhivo)
            image=pygame.transform.scale(image,(self.tamanioBloque[0],self.tamanioBloque[1]))
            self.imagenes[nombre_arhivo.split(".")[0]]= image

    

    def obtenerImagen(self, celda, primer_click):
        archivo = "empty-block"
        if primer_click:
            archivo ="unclicked-bomb" if celda.getContiene_mina() else str(celda.getBombas_alrededor())
        return self.imagenes[archivo]
    def dibujar(self, minas_colocadas):
        tupla = (0,0)
        for fila in range(self.tablero.getDimensiones()[0]):
            for columna in range(self.tablero.getDimensiones()[1]):
                imagen=self.obtenerImagen(self.tablero.getCelda(fila, columna),minas_colocadas)
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
                        self.tablero.colocarMinas(pos_tablero[0],pos_tablero[1])
                        self.minas_colocadas=True
            self.dibujar(self.minas_colocadas)
            pygame.display.flip()
        pygame.quit()