from tablero import Tablero
from juego import Juego

tablero = Tablero((9,9))
tamanioPantalla=(630,630)
juego=Juego(tablero,tamanioPantalla)
juego.correr()