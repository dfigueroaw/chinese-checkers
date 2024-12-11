historial = []
leer_archivo_historial = open('historial.txt','r')

for linea in leer_archivo_historial.readlines():
    partida = linea.strip().split(",")
    historial.append([partida[0], partida[1], partida[2], partida[3]])

def añadir_al_historial(jugador_1, jugador_2, tiempo, ganador):

    añadir_archivo_historial = open('historial.txt', 'a')

    historial.append([jugador_1, jugador_2, tiempo, ganador])
    añadir_archivo_historial.write(f"{jugador_1},{jugador_2},{tiempo},{ganador}\n")

def historial_de_juegos():

    print("ESTADÍSTICAS:")
    print(f"CANTIDAD DE PARTIDAS TOTAL: {len(historial)}")

    jugadores = {}
    #JUGADORES
    for partida in historial:
        if partida[0] not in jugadores:
            jugadores[partida[0]] = [0, 0, 0, 0, 0]
        if partida[1] not in jugadores:
            jugadores[partida[1]] = [0, 0, 0, 0, 0]

    for partida in historial:
        jugador_1 = partida[0]
        jugador_2 = partida[1]
        ganador = partida[3]

        jugadores[jugador_1][0] += 1
        jugadores[jugador_2][0] += 1

        jugadores[jugador_1][1] += 1 * (jugador_1 == ganador)
        jugadores[jugador_2][1] += 1 * (jugador_2 == ganador)

        jugadores[jugador_1][2] += 1 * (jugador_2 == ganador)
        jugadores[jugador_2][2] += 1 * (jugador_1 == ganador)

        jugadores[jugador_1][3] += 1 * (ganador == "CANCELADO")
        jugadores[jugador_2][3] += 1 * (ganador == "CANCELADO")

    ranks = []
    for jugador, stats in jugadores.items():
        ranks.append((jugador, 100 * stats[1] / (stats[1] + stats[2]) if stats[1] + stats[2] != 0 else 0))

    for tope in range(len(ranks) -1, 0, -1):
        for i in range(tope):
            if ranks[i][1] < ranks[i + 1][1]:
                ranks[i], ranks[i + 1] = ranks[i + 1], ranks[i]

    print(f"CANTIDAD DE PARTIDAS GANADAS POR LA IA: {jugadores["IA"][1] if "IA" in jugadores else 0}") #FALTO ESTO
    print("%10s %10s %10s %10s %10s %10s %10s"%("Ranking", "Jugador", "Partidas", "Victorias", "Derrotas", "Canceladas", "Tasa"))
    for i in range(len(ranks)):
        jugador = ranks[i]
        stats = jugadores[jugador[0]]
        print("%10s %10s %10s %10s %10s %10s %10s"%(i + 1, jugador[0], stats[0], stats[1], stats[2], stats[3], f"{100 * stats[1] / (stats[1] + stats[2]) if stats[1] + stats[2] != 0 else 0}%"))

    print("%4s %20s %28s %10s"%("Nro.", "Jugadores", "Fecha / Hora", "Ganador"))
    for partida in range(len(historial)):
        jugador_1 = historial[partida][0]
        jugador_2 = historial[partida][1]
        tiempo = historial[partida][2]
        ganador = historial[partida][3]

        print("%4s %20s %28s %10s"%(partida + 1, f"{jugador_1} vs {jugador_2}", tiempo, ganador))
    input("Presiona enter para salir del historial")