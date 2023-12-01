import pygame
import os
from time import sleep
class Juego():
    #Pre: Recibe como parametro un objeto Tablero y una tupla de 2 valores numericos
    #representando las dimensiones en pixeles de la pantalla(ancho, alto) 
    def __init__(self, tablero, tamanioPantalla):
        pygame.init()
        self.fuente_de_texto = pygame.font.SysFont("Arial",36)
        self.minas_colocadas=False
        self.pantalla=pygame.display.set_mode(tamanioPantalla)
        self.tablero=tablero
        self.tamanioPantalla=tamanioPantalla
        self.tamanioBloque = (tamanioPantalla[0] // self.tablero.getDimensiones()[1], self.tamanioPantalla[1] // self.tablero.getDimensiones()[0])
        self.imagenes = {}
        self.cargarImagenes()
    #Pos: Lee los archivos de la carpeta "img" y guarda las imagenes dentro del diccionario
    # usando como clave el nombre del archivo 
    def cargarImagenes(self):
        for nombre_arhivo in os.listdir("img"):
            if (not nombre_arhivo.endswith(".png")):
                continue
            image = pygame.image.load(r"img/"+nombre_arhivo)
            image=pygame.transform.scale(image,(self.tamanioBloque[0],self.tamanioBloque[1]))
            self.imagenes[nombre_arhivo.split(".")[0]]= image

    #Pre: Recibe como parametro una instancia de la clase Celda
    #Pos: Obtinen del diccionario la imagen correspondiente de dicha celda
    def obtenerImagen(self, celda):
        archivo = None
        if celda.getClickeada():
            archivo= "bomb-at-clicked-block" if celda.getContiene_mina() else str(celda.getBombas_alrededor())
        else:        
            archivo ="flag" if celda.getBandera_colocada() else "empty-block"
        return self.imagenes[archivo]
    
    def dibujar(self):
        tupla = (0,0)
        for fila in range(self.tablero.getDimensiones()[0]):
            for columna in range(self.tablero.getDimensiones()[1]):
                imagen=self.obtenerImagen(self.tablero.getCelda(fila, columna))
                self.pantalla.blit(imagen, tupla)
                tupla = (tupla[0]+self.tamanioBloque[0], tupla[1])
            tupla = (0,tupla[1]+self.tamanioBloque[0])
    
    def hacer_click(self, indice, click_derecho):
        celda=self.tablero.getCelda(indice[0],indice[1])
        self.tablero.hacer_click(celda, click_derecho)
    def ganar(self):
        texto=self.fuente_de_texto.render("Has ganado",True,(0,255,255))
        self.pantalla.blit(texto, (242,315))
        sonido = pygame.mixer.Sound('winning.wav')
        sonido.play()
        pygame.display.flip()
        sleep(3)
    def correr(self):
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not(self.tablero.getHa_perdido()):
                        pos = pygame.mouse.get_pos()
                        click_derecho=pygame.mouse.get_pressed()[2]
                        indice = (pos[1] // self.tamanioBloque[1] ,pos[0] // self.tamanioBloque[0] )
                        if not self.minas_colocadas:
                            self.tablero.colocarMinas(indice[0],indice[1])
                            self.minas_colocadas=True
                        self.hacer_click(indice,click_derecho)   
            self.dibujar()
            pygame.display.flip()
            if self.tablero.checkear_victoria():
                    self.ganar()
                    flag = False
        pygame.quit()