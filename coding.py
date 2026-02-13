import time
import math


fila=5
columna=5
pos_gato=(0,0)
pos_raton=(fila-1,columna-1)


def crear_tablero():
    return [["_" for _ in range(columna)] for _ in range(fila)]

def mostrar_tablero(laboratorio):
    for f in laboratorio:
        print(" ".join(f))

def pos_validas(pos):
    f, c = pos
    return 0 <= f < fila and 0 <= c < columna

def actualizar_tablero():
    tablero= crear_tablero()
    if pos_validas(pos_raton):
        tablero[pos_raton[0]][pos_raton[1]]="R"
    else:
        print("El rato no existe")
    if pos_validas(pos_gato):
        tablero[pos_gato[0]][pos_gato[1]]="G"
    else:
        print("El gato no existe")
    return tablero


def movimientos(pos):
    f=pos[0]
    c=pos[1]
    mov=[(f-1,c),(f+1,c),(f,c-1),(f,c+1)]
    mov_validos=[]
    for m in mov:
        if 0<=m[0]<fila and 0<=m[1]<columna:
            mov_validos.append(m)
    return mov_validos




def minimax(p_gato, p_raton, profundidad, es_raton):
    # Si el gato atrapa al ratón, es el fin para el ratón
    if p_gato == p_raton:
        return -999 if es_raton else 999

        # Cuando dejamos de mirar el futuro, devolvemos la distancia
    if profundidad == 0:
        return abs(p_gato[0] - p_raton[0]) + abs(p_gato[1] - p_raton[1])

    if es_raton:
        mejor_v = -math.inf
        # El ratón prueba sus movimientos legales
        for mov in movimientos(p_raton):
            valor = minimax(p_gato, mov, profundidad - 1, False)
            mejor_v = max(mejor_v, valor)
        return mejor_v
    else:
        mejor_v = math.inf
        # El gato prueba sus movimientos legales
        for mov in movimientos(p_gato):
            valor = minimax(mov, p_raton, profundidad - 1, True)
            mejor_v = min(mejor_v, valor)
        return mejor_v


def IA_gato():
    global pos_gato  # Para poder cambiar la posición real
    opciones = movimientos(pos_gato)
    mejor_mov = pos_gato
    mejor_valor = math.inf  # El gato busca el valor más bajo (distancia pequeña)

    for mov in opciones:
        # Simulamos qué pasaría si el gato mueve aquí
        valor = minimax(mov, pos_raton, 4, True)
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    pos_gato = mejor_mov  # Aquí es donde el raton realmente se mueve
def IA_raton():
    global pos_raton  # Para poder cambiar la posición real
    opciones = movimientos(pos_raton)
    mejor_mov = pos_raton
    mejor_valor = -math.inf  # El raton busca el valor más alto (distancia pequeña)

    for mov in opciones:
        # Simulamos qué pasaría si el raton mueve aquí
        valor = minimax(pos_gato, mov, 2, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    pos_raton = mejor_mov
turnos=10


# Bucle simple de 10 turnos
for i in range(turnos):
    print(f"\nTurno {i + 1}")

    # 1. El Gato piensa y mueve
    IA_gato()
    if pos_gato == pos_raton:
        tablero_final = actualizar_tablero()
        mostrar_tablero(tablero_final)
        print("¡EL GATO ATRAPÓ AL RATÓN!")
        break
    IA_raton()

    # 2. Dibujamos el resultado
    tablero_actualizado = actualizar_tablero()
    mostrar_tablero(tablero_actualizado)
    time.sleep(0.5)
    # 3. Revisar si ganó
    if i>=turnos-1:
        print("el raton escapo")
