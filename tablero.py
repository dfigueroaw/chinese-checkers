from configuraciones import colores

tablero = [
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"]
    ]
def imprimir_tablero():
    print("  A B C D E F G H")
    for i in range(len(tablero)):
        print(i+1, end = " ")
        for j in range(len(tablero[i])):
            print(tablero[i][j], end = " ")
        print(i+1)
    print("  A B C D E F G H")

def actualizar_tablero(fila: int, columna: int, ficha: str, color: str):
    tablero[fila][columna] = colores[color] + ficha + colores["blanco"]

def actualizar_multiples(lista_de_posiciones: list, ficha: str, color: str):
    for posicion_ficha in lista_de_posiciones:
        actualizar_tablero(posicion_ficha[0], posicion_ficha[1], ficha, color)

def limpiar_tablero():
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            limpiar_casilla(i, j)

def limpiar_casilla(fila: int, columna: int):
    tablero[fila][columna] = "-"

def inicializar_tablero(ficha_j1: str, ficha_j2: str, color_j1: str, color_j2: str):
    actualizar_multiples([[0, 1], [0, 3], [0, 5], [0, 7], [1, 0], [1, 2], [1, 4], [1, 6]], ficha_j1, color_j1)
    actualizar_multiples([[6, 1], [6, 3], [6, 5], [6, 7], [7, 0], [7, 2], [7, 4], [7, 6]], ficha_j2, color_j2)

def mover_ficha(jugada: str, ficha: str, color: str):

    letras_tablero = "ABCDEFGH"
    fila_original = int(jugada[1]) - 1
    columna_original = letras_tablero.index(jugada[0])
    fila_target = int(jugada[3]) - 1
    columna_target = letras_tablero.index(jugada[2])

    limpiar_casilla(fila_original, columna_original)
    actualizar_tablero(fila_target, columna_target, ficha, color)

def comprobar_casilla(fila: int, columna: int, ficha: str, color: str):
    if tablero[fila][columna] == colores[color] + ficha + colores["blanco"]: return True
    else: return False

def comprobar_multiples(lista_de_posiciones: list, ficha: str, color: str):
    for posicion_ficha in lista_de_posiciones:
        if not comprobar_casilla(posicion_ficha[0], posicion_ficha[1], ficha, color): return False
    return True

def jugadas_validas_ficha(fila, columna):
    movimientos_validos_ficha = []

    fila_original = fila
    columna_original = columna

    moves = [(fila_original + 1, columna_original + 1), (fila_original + 1, columna_original - 1), (fila_original - 1, columna_original + 1), (fila_original - 1, columna_original - 1), (fila_original + 2, columna_original + 2), (fila_original + 2, columna_original - 2), (fila_original - 2, columna_original + 2), (fila_original - 2, columna_original - 2)]
    moves_in_range = []
    for move in moves:
        if move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7: moves_in_range.append(move)

    for move in moves_in_range:

        valido = False
        fila_target = move[0]
        columna_target = move[1]

        if tablero[fila_target][columna_target] == "-":
            if abs(fila_original - fila_target) == 1 and abs(columna_original - columna_target) == 1: valido = True
            if fila_original - fila_target == 2 and columna_original - columna_target == 2 and tablero[fila_original - 1][columna_original - 1] != "-": valido = True
            if fila_original - fila_target == 2 and columna_original - columna_target == -2 and tablero[fila_original - 1][columna_original + 1] != "-": valido = True
            if fila_original - fila_target == -2 and columna_original - columna_target == 2 and tablero[fila_original + 1][columna_original - 1] != "-": valido = True
            if fila_original - fila_target == -2 and columna_original - columna_target == -2 and tablero[fila_original + 1][columna_original + 1] != "-": valido = True
        if valido == True:
            movimientos_validos_ficha.append(((fila_original, columna_original), (fila_target, columna_target)))

    return movimientos_validos_ficha