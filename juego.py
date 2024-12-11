from datetime import datetime
from historial import *
from tablero import *

def validar_input(jugada: str):

    letras_tablero = "ABCDEFGH"
    nums_tablero = "12345678"
    if len(jugada) != 4: return False
    if jugada[0] not in letras_tablero: return False
    if jugada[2] not in letras_tablero: return False
    if jugada[1] not in nums_tablero: return False
    if jugada[3] not in nums_tablero: return False

    return True

def comprobar_movimiento(jugada: str):

    letras_tablero = "ABCDEFGH"
    fila_original = int(jugada[1]) - 1
    columna_original = letras_tablero.index(jugada[0])
    fila_target = int(jugada[3]) - 1
    columna_target = letras_tablero.index(jugada[2])

    if tablero[fila_target][columna_target] == "-":
        if abs(fila_original - fila_target) == 1 and abs(columna_original - columna_target) == 1: return True
        if fila_original - fila_target == 2 and columna_original - columna_target == 2 and tablero[fila_original - 1][columna_original - 1] != "-": return True
        if fila_original - fila_target == 2 and columna_original - columna_target == -2 and tablero[fila_original - 1][columna_original + 1] != "-": return True
        if fila_original - fila_target == -2 and columna_original - columna_target == 2 and tablero[fila_original + 1][columna_original - 1] != "-": return True
        if fila_original - fila_target == -2 and columna_original - columna_target == -2 and tablero[fila_original + 1][columna_original + 1] != "-": return True

    return False

def comprobar_ficha_del_jugador(jugada: str, ficha: str, color: str):

    letras_tablero = "ABCDEFGH"
    fila_original = int(jugada[1]) - 1
    columna_original = letras_tablero.index(jugada[0])

    return comprobar_casilla(fila_original, columna_original, ficha, color)

def comprobar_ganador(ficha_j1: str, ficha_j2: str, color_j1: str, color_j2: str):
    j1_ganador = comprobar_multiples([[6, 1], [6, 3], [6, 5], [6, 7], [7, 0], [7, 2], [7, 4], [7, 6]], ficha_j1, color_j1)
    j2_ganador = comprobar_multiples([[0, 1], [0, 3], [0, 5], [0, 7], [1, 0], [1, 2], [1, 4], [1, 6]], ficha_j2, color_j2)
    return j1_ganador or j2_ganador

def jugar_turno(jugador: str, ficha: str, color: str):

    imprimir_tablero()

    jugada_valida = False

    while not jugada_valida:

        jugada = input(f"{jugador} ? ").upper()

        if jugada == "-1": return "CANCELADO"

        if validar_input(jugada) and comprobar_movimiento(jugada) and comprobar_ficha_del_jugador(jugada, ficha, color): jugada_valida = True

    mover_ficha(jugada, ficha, color)

    return

def jugadas_validas(ficha: str, color: str):

    movimientos_validos = [] # LISTA CON TUPLAS A RETORNAR

    posiciones_ficha = []

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if comprobar_casilla(fila, columna, ficha, color) == True:
                posiciones_ficha.append((fila, columna))

    for ficha in posiciones_ficha:

        movimientos_validos_ficha = jugadas_validas_ficha(ficha[0], ficha[1])

        for valido in movimientos_validos_ficha:
            movimientos_validos.append(valido)

    return movimientos_validos

def jugada_ia(jugadas_posibles: list):

    capas = {2: [], 1: [], -1: [], -2: []}

    for jugada in jugadas_posibles:
        capas[jugada[0][0] - jugada[1][0]].append(jugada)

    capa_target = [] # SOLO SELECCIONAR ENTRE LAS FICHAS QUE PUEDEN MOVERSE LA MAYOR CANTIDAD DE CASILLAS HACIA ADELANTE

    if capas[2] != []: capa_target = capas[2]
    elif capas[1] != []: capa_target = capas[1]
    elif capas[-1] != []: capa_target = capas[-1]
    else: capa_target = capas[-2]

    ultima_fila = 0

    for jugada in capa_target:
        if jugada[0][0] > ultima_fila:
            ultima_fila = jugada[0][0]

    fila_target = [] # SOLO SELECCCIONAR ENTRE LAS FICHAS QUE SE ENCUENTREN MAS ATRAS EN EL TABLERO (MOVIMIENTO EN MASA)

    for jugada in capa_target:
        if jugada[0][0] == ultima_fila:
            fila_target.append(jugada)

    #PRIORIZAR LA FICHA QUE SE VAYA A UNA POSICION MAS CENTRICA
    for jugada in fila_target:
        if jugada[0][1] == 0 or jugada[0][1] == 7:
            return jugada

    for jugada in fila_target:
        if jugada[0][1] == 1 or jugada[0][1] == 6:
            return jugada

    for jugada in fila_target:
        if jugada[0][1] == 2 or jugada[0][1] == 5:
            return jugada

    for jugada in fila_target:
        return jugada

    return

def turno_maquina(ficha: str, color: str):

    imprimir_tablero()

    jugadas_posibles = jugadas_validas(ficha, color)

    jugada = jugada_ia(jugadas_posibles)

    limpiar_casilla(jugada[0][0], jugada[0][1])
    actualizar_tablero(jugada[1][0], jugada[1][1], ficha, color)

    letras_tablero = "ABCDEFGH"
    return print(f"IA ? {letras_tablero[jugada[0][1]]}{jugada[0][0] + 1}{letras_tablero[jugada[1][1]]}{jugada[1][0] + 1}")

def juego():

    from configuraciones import color_j1, color_j2, ficha_j1, ficha_j2

    jugador_1 = input("Ingresar el nombre del jugador 1: ")
    jugador_2 = input("Ingresar el nombre del jugador 2: ")
    fecha_y_hora = datetime.now().strftime("%c")
    inicializar_tablero(ficha_j1, ficha_j2, color_j1, color_j2)

    while True:
        turno = jugar_turno(jugador_1, ficha_j1, color_j1)
        if turno == "CANCELADO": return añadir_al_historial(jugador_1, jugador_2, fecha_y_hora, "CANCELADO")
        fin_del_juego = comprobar_ganador(ficha_j1, ficha_j2, color_j1, color_j2)
        if fin_del_juego == True:
            print(f"{jugador_1} ha ganado el juego!")
            return añadir_al_historial(jugador_1, jugador_2, fecha_y_hora, jugador_1)

        turno = jugar_turno(jugador_2, ficha_j2, color_j2)
        if turno == "CANCELADO": return añadir_al_historial(jugador_1, jugador_2, fecha_y_hora, "CANCELADO")
        fin_del_juego = comprobar_ganador(ficha_j1, ficha_j2, color_j1, color_j2)
        if fin_del_juego == True:
            print(f"{jugador_2} ha ganado el juego!")
            return añadir_al_historial(jugador_1, jugador_2, fecha_y_hora, jugador_2)

def juego_maquina():
    from configuraciones import color_j1, color_j2, ficha_j1, ficha_j2

    jugador_1 = input("Ingresar el nombre del jugador 1: ")

    primer_t = ""
    while primer_t != "y" and primer_t != "n":
        primer_t = input("Desea empezar el juego? (y/n): ").lower()

    fecha_y_hora = datetime.now().strftime("%c")
    inicializar_tablero(ficha_j1, ficha_j2, color_j1, color_j2)

    if primer_t == "n": turno_maquina(ficha_j2, color_j2)

    while True:
        turno = jugar_turno(jugador_1, ficha_j1, color_j1)
        if turno == "CANCELADO": return añadir_al_historial(jugador_1, "IA", fecha_y_hora, "CANCELADO")
        fin_del_juego = comprobar_ganador(ficha_j1, ficha_j2, color_j1, color_j2)
        if fin_del_juego == True:
            print(f"{jugador_1} ha ganado el juego!")
            return añadir_al_historial(jugador_1, "IA", fecha_y_hora, jugador_1)

        turno_maquina(ficha_j2, color_j2)
        fin_del_juego = comprobar_ganador(ficha_j1, ficha_j2, color_j1, color_j2)
        if fin_del_juego == True:
            print(f"La IA ha ganado el juego!")
            return añadir_al_historial(jugador_1, "IA", fecha_y_hora, "IA")