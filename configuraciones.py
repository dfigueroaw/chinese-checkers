color_j1 = "rojo"
color_j2 = "azul"
ficha_j1 = "O"
ficha_j2 = "X"
colores = {"blanco": "\033[0m", "rojo": "\033[91m", "verde": "\033[92m", "amarillo": "\033[93m", "azul": "\033[94m", "rosa": "\033[95m", "cian": "\033[96m"}
#seleccion de turno, tablero forma, tablero tamaño
#comprobar que las fichas no son iguales

def imprimir_menu_configuracion():
    print("Configuración del programa")
    print("1 | Cambiar color de fichas")
    print("2 | Cambiar forma de fichas")
    print("3 | Regresar")
    return input("Seleccione una opción: ")

def imprimir_menu_configuracion_color():
    print("Cambiar color de fichas")
    print("1 | Cambiar color del jugador 1")
    print("2 | Cambiar color del jugador 2")
    print("3 | Regresar")
    return input("Seleccione una opción: ")

def cambiar_color():

    global color_j1, color_j2

    cambiando_color = True

    while cambiando_color:
        seleccion = imprimir_menu_configuracion_color()

        if seleccion == "1":

            nuevo_color = ""
            while nuevo_color not in colores or nuevo_color == color_j2:
                print(f"Color actual del jugador 1: {colores[color_j1] + color_j1 + colores["blanco"]}")
                print("Colores disponibles: ")
                for color in colores:
                    print(f"- {colores[color] + color + colores["blanco"]}")
                nuevo_color = input("Ingrese el nombre del color al que desee cambiar: ")
                if nuevo_color in colores and nuevo_color != color_j2:
                    color_j1 = nuevo_color

        elif seleccion == "2":

            nuevo_color = ""
            while nuevo_color not in colores or nuevo_color == color_j1:
                print(f"Color actual del jugador 2: {colores[color_j2] + color_j2 + colores["blanco"]}")
                print("Colores disponibles: ")
                for color in colores:
                    print(f"- {colores[color] + color + colores["blanco"]}")
                nuevo_color = input("Ingrese el nombre del color al que desee cambiar: ")
                if nuevo_color in colores and nuevo_color != color_j1:
                    color_j2 = nuevo_color

        elif seleccion == "3":
            cambiando_color = False

def imprimir_menu_configuracion_forma():
    print("Cambiar forma de fichas")
    print("1 | Cambiar forma del jugador 1")
    print("2 | Cambiar forma del jugador 2")
    print("3 | Regresar")
    return input("Seleccione una opción: ")

def cambiar_forma():

    global ficha_j1, ficha_j2

    cambiando_forma = True

    while cambiando_forma:
        seleccion = imprimir_menu_configuracion_forma()

        if seleccion == "1":

            nueva_forma = ""
            while len(nueva_forma) != 1 or nueva_forma == ficha_j2:
                print(f"Forma actual del jugador 1: {ficha_j1}")
                nueva_forma = input("Ingrese la nueva forma de sus fichas (1 caracter): ")
                if len(nueva_forma) == 1 and nueva_forma != ficha_j2:
                    ficha_j1 = nueva_forma

        elif seleccion == "2":

            nueva_forma = ""
            while len(nueva_forma) != 1 or nueva_forma == ficha_j1:
                print(f"Forma actual del jugador 2: {ficha_j2}")
                nueva_forma = input("Ingrese la nueva forma de sus fichas (1 caracter): ")
                if len(nueva_forma) == 1 and nueva_forma != ficha_j1:
                    ficha_j2 = nueva_forma


        elif seleccion == "3":
            cambiando_forma = False

def configurar():
    configurando = True

    while configurando:
        seleccion = imprimir_menu_configuracion()

        if seleccion == "1":
            cambiar_color()

        elif seleccion == "2":
            cambiar_forma()

        elif seleccion == "3":
            configurando = False