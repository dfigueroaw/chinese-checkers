from juego import *
from historial import *
from configuraciones import *

jugando = True

def imprimir_menu():
    print("Menu principal")
    print("1 | Jugar contra otro jugador")
    print("2 | Jugar contra la maquina")
    print("3 | Historial")
    print("4 | Configuración")
    print("5 | Salir")
    return input("Seleccione una opción: ")

while jugando:
    seleccion = imprimir_menu()

    if seleccion == "1":
        juego()

    if seleccion == "2":
        juego_maquina()

    elif seleccion == "3":
        historial_de_juegos()

    elif seleccion == "4":
        configurar()

    elif seleccion == "5":
        jugando = False