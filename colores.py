for i in range(108):
    print(f"\033[{i}mEstoy probando el color {i}")

colores = {"blanco": "\033[0m", "rojo": "\033[91m", "verde": "\033[92m", "amarillo": "\033[93m", "azul": "\033[94m", "rosa": "\033[95m", "cian": "\033[96m"}
for color, clave in colores.items():
    print(clave + f"este es el color {color}")