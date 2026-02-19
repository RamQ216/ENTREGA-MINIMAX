import time #nos sirve para dar intervalos a lo que se muestra en pantalla

#declaramos el tamanho de nuestra matriz
FILA=5
COLUMNA=5
#le damos la coordenadas al gato y al raton
gato=[0,0]
raton=[FILA-1,COLUMNA-1]

#creamos el entorno mediante un for anidado
def crear():
    return[["_" for _ in range(COLUMNA)]for _ in range(FILA)]#es es una compresion de listas el for interno crea filas con "_" y el externo repite el proceso

#imprimimos la matriz filaxfila
def imprimir(imprimir):
    for i in imprimir:
        print(" ".join(i))#esto es fuadamental ya que nos permite imprimir fila por fila

#cada vez que se mueven los personajes lo hacen en un tablero limpio
def update():
    matriz=crear()
    if 0<=gato[0]<FILA and 0<=gato[1]<COLUMNA:
        matriz[gato[0]][gato[1]]= "G"
    if 0<=raton[0]<FILA and 0<=raton[1]<COLUMNA:
        matriz[raton[0]][raton[1]]= "R"
    return matriz
#definimos los movimientos posibles dentro de la matriz
def movimientos_p(pos):
    f=pos[0]
    c=pos[1]
    movi=[(f-1,c),(f+1,c),(f,c-1),(f,c+1)]
    valido=[]
    for m in movi:
        if 0<=m[0]<FILA and 0<=m[1]<COLUMNA:
            valido.append(m)
    return valido

#este es el cerebro de nuestro programa, es quien nos permite ver al futuro y tambien calcular la distancia mas cercana con manhattan
def minimax(p_gato,p_raton,profundidad,t_r):
    if p_gato==p_raton:#caso base
        return -999#es la peor situacion del raton el gato no tiene porque ya es redundante
    if profundidad==0:
        return abs(p_gato[0]-p_raton[0])+abs(p_gato[1]-p_raton[1])#aca se encuentra nuestr euristica que seria la distancia de manhattan
    if t_r==True:
        mejor_v=-1000000000#es nuestro punto de comparacion para poder ingresar los datos
        mov=movimientos_p(p_raton)
        for m in mov:
            valor=minimax(p_gato, m, profundidad-1, False)#aca se realiza nuestra recursividad 
            mejor_v=max(mejor_v, valor)
        return mejor_v
    else:
        mejor_v=1000000000#es nuestro punto de comparacion para poder ingresar los datos
        mov=movimientos_p(p_gato)
        for m in mov:
            valor=minimax(m, p_raton, profundidad-1, True)#aca se realiza nuestra recursividad 
            mejor_v=min(mejor_v, valor)
        return mejor_v
    
def IA_GATO():#aca le decimos a nuestro gato que se mueva a su mejor opcion mediante el minimax y la euristica que nos da el mejor movimiento
    global gato
    mejor_v=100000000
    mejor_mov=gato
    mov=movimientos_p(gato)
    for m in  mov:
        valor=minimax(m, raton, 5, True)
        if valor<mejor_v:
            mejor_v=valor
            mejor_mov=m
    gato=mejor_mov

def IA_RATON():#aca le decimos a nuestro raton que se mueva a su mejor opcion mediante el minimax y la euristica que nos da el mejor movimiento
    global raton
    mejor_v=-100000000
    mejor_mov=raton
    mov=movimientos_p(raton)
    for m in  mov:
        valor=minimax(gato, m, 2, False)
        if valor>mejor_v:
            mejor_v=valor
            mejor_mov=m
    raton=mejor_mov

#este seria nuestro motor que ietra e imprime en pantalla el tablero
turnos=10
for i in range(turnos):
    print(f"\nTURNOS {i+1}")
    IA_GATO()
    if gato==raton:
        print("el gato comio raton")
        break
    IA_RATON()
   
    imprimir(update())
    time.sleep(0.5)#nuestro intervalo de tiempo
if i==turnos-1:
    print("el raton escapo")

