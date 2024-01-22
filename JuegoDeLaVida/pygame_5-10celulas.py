import random 
import copy
import os
import time


# def inicializador_tablero(filas, columnas, probabilidad_vida=0.2):
#     return [[1 if random.random() < probabilidad_vida else 0 for _ in range(columnas)] for _ in range(filas)]

# creamos la funcion iniciar tablero que le pasaremos el numero de filas i columnas
def inicializador_tablero(fila, columna): 
    num_celulas = random.randint(5, 10)
    tablero = [[0] * columna for _ in range(fila)]  # Inicializa un tablero con todas las células muertas

    for _ in range(num_celulas):
        num_aleatorio1 = random.randint(0, fila - 1)
        num_aleatorio2 = random.randint(0, columna - 1)

        tablero[num_aleatorio1][num_aleatorio2] = 1  # Establece una célula viva en la posición generada aleatoriamente

    return tablero
           

# Imprime el estado del tablero, ■ para celulas vivas y □ para celulas muertas
def imprimir_tablero(tablero, fila):
    for fila in tablero:
        print(''.join(['🟦 ' if celda else '⬜ ' for celda in fila]))


#cuenta el numero de celulas vivas alrededor de un posicion especifica en el tablero
#utiliza una  lista de coordenadas para representar a los vecinos
def contar_vecinos(tablero, fila, columna):
    filas, columnas = len(tablero), len(tablero[0])
    vecinos = [
        (fila + i, columna + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if i != 0 or j != 0
    ]

    contar = 0
    for f, c in vecinos:
        if 0 <= f < filas and 0 <= c < columnas and tablero[f][c] == 1:
            contar += 1

    return contar


# Función que aplica las reglas del Juego de la Vida para evolucionar el tablero a la siguiente generación.
# Utiliza una copia  del tablero para evitar modificar el tablero actual mientras se calcula el siguiente estado.
def evolucionar(tablero):
    nuevo_tablero = copy.deepcopy(tablero)
    filas, columnas = len(tablero), len(tablero[0])

    for fila in range(filas):
        for columna in range(columnas):
            
            vecinos_vivos = contar_vecinos(tablero, fila, columna)
            if tablero[fila][columna] == 1:  # Celda viva
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nuevo_tablero[fila][columna] = 0
                    
            else:  # Celda muerta
                if vecinos_vivos == 3:
                    nuevo_tablero[fila][columna] = 1

    return nuevo_tablero


# La condición if __name__ == "__main__": garantiza que este bloque se ejecute 
# solo si el script se ejecuta directamente y no si se importa como un módulo.
if __name__ == "__main__":
    fila, columna = 15, 15
    
    tablero = inicializador_tablero(fila, columna) #inicia tablero con las filas i columnas que declaramos

    generaciones = 100 #numero de veces que se actualizara el tablero

    for _ in range(generaciones): #bucle del juego con las generaciones que hemos declarao
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
        imprimir_tablero(tablero, fila) #imprime las celulas en el tablero que hemos iniciado
        tablero = evolucionar(tablero) #evoluciona el tablero anterior al nuevo
        time.sleep(0.07)  # Delay de medio segundo
