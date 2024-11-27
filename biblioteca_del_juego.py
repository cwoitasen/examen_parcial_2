import random
import pygame
# import pygame.mixer as mixer
import json
from variables import *

def inicializar_matriz(tamaño:tuple, parametro:any)->list:
    '''
    inicializa una matriz vacia de x*y y N nro de mins
    recibe 1 tupla con 3 int (cant filas, cantidad columnas y cantidad de minas)
    devuelve la matriz
    '''
    matriz = []
    for _ in range(tamaño[0]):
        matriz += [[parametro] * tamaño[1]] # Cargamos la matriz limpia
    return matriz

def cargar_minas(matriz:list, matriz_area:list, parametros:tuple)->None:
    '''
    Carga las minas en la matriz.
    Recibe una matriz y una tupla con 3 números de tipo int, que corresponden a la cantidad de filas, 
    la cantidad de columnas y la cantidad de minas.
    No tiene retorno.
    '''
    minas = 0
    while minas < parametros[2]: # parametro[2] es la cantidad de minas definida
        i = random.randint(0,parametros[0]-1) # hacemos random entre 0 y la cantidad de filas para tener una coordenada aleatoria
        j = random.randint(0,parametros[1]-1) # hacemos random entre 0 y la cantidad de columnas para tener una coordenada aleatoria
        if matriz[i][j] == 0 and matriz_area[i][j] == False: # si esa coordenada que creamos tiene 0, le ponemos -1 (mina) y subimos el contaador de minas
            matriz[i][j] = -1 
            minas += 1

def definir_valores_campos(matriz:list)->None:
    '''
    Establece los valores de las cantidades de minas contiguas al casillero.
    Recibe una matriz
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])): #Recorro la matriz normalmente
            if matriz[i][j] == 0:       # Si el campo es 0, es porque no hay mina, tengo que revisar cuantos casilleros de minas tiene alrededor
                cant_minas = recorrer_casillas_contiguas(matriz,i,j) # llamo la funcion que evalua eso
                matriz[i][j] = cant_minas # Cambio el 0 por la cantidad de minas que tiene alrededor

def recorrer_casillas_contiguas(matriz:list,fila:int,columna:int)->int:
    '''
    Recorre las casillas contiguas a la casilla pasada por parametro y devuelve la cantidad de minas que tiene alrededor.
    Recibe una matriz, una fila y una columna.
    Devuelve un entero con la cantidad de minas que tiene alrededor.
    '''
    contador_minas = 0
    for i in range(fila - 1, fila + 2): # hago que revise 1 fila anterior a la que le paso (osea la fila de arriba) y una posterior (la fila de abajo)
        if i >= 0 and i < len(matriz):  # me fijo que este en rango, que el la fila (i) no sea menor a 0 y que a su vez no se pase de la len de las filas de la matriz
            for j in range(columna - 1, columna + 2): # lo mismo para columnas, desde la anterior hasta la siguiente
                if j >= 0 and j < len(matriz[i]): # lo mismo para columnas, que no se vaya de rango, y que no vaya a columna - 1
                    if matriz[i][j] == -1: # si hay 1 mina
                            contador_minas += 1  # le sumo al contador
    return contador_minas

def imprimir_matriz(matriz:list)->None:
    '''
    Imprime la matriz de 2*X
    Recibe una matriz
    No tiene retorno
    '''
    vacio = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == None:
                print(f"{vacio:3}", end=" ")
            else:
                print(f"{matriz[i][j]:3}", end=" ")
        print("")

def crear_condicion_victoria(matriz:list,matriz_descu:bool,condicion:any, parametro:any, parametro2:any)->None:
    '''
    Crea una matriz de booleanos con la condicion de victoria
    Recibe una matriz, una matriz de booleanos, una condicion, un parametro y un parametro2
    No tiene retorno
    '''
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == condicion:
                matriz_descu[i][j] = parametro
            else:
                matriz_descu[i][j] = parametro2

def ir_a_jugar(validacion_jugar:int)-> str:
    '''
    Cambia la instancia de pantalla a JUGAR si la validacion es 1, sino la cambia a MENU
    Recibe una validacion
    Devuelve la instancia de pantalla
    '''
    if validacion_jugar == 1:
        instancia_pantalla = "JUGAR" 
    else:
        instancia_pantalla = "MENU"      
    return instancia_pantalla

def clickeo_casilla(matriz:list,matriz_descu:list, matriz_bandera:list, fila:int, columna:int)-> bool:
    '''
    Evalua si la casilla clickeada es una mina o no
    Recibe una matriz, una matriz de booleanos, una matriz de banderas, una fila y una columna
    Devuelve un booleano
    '''
    game_over = False
    if matriz_bandera[fila][columna] == False:
        if matriz[fila][columna] == -1:  # si es una mina
            matriz[fila][columna] = -2   # le mando -2 para mostrar mina con cruz
            game_over = True
        mostrar_celda(matriz, matriz_descu, matriz_bandera, fila, columna) 
    return game_over
    
def mostrar_celda(matriz:list, matriz_parametro:list, matriz_bandera:list, fila:int, columna:int)-> None:
    '''
    Muestra la celda clickeada
    Recibe una matriz, una matriz de booleanos, una matriz de banderas, una fila y una columna
    No tiene retorno
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    if matriz_parametro[fila][columna] or matriz_bandera[fila][columna]:
        return
    matriz_parametro[fila][columna] = True
    if matriz[fila][columna] == 0:
        # Con una funcion recursiva revela las celdas que tienen valor 0
        for dir in directions:
            nf = fila + dir[0]
            nc = columna + dir[1]
            if 0 <= nf < len(matriz) and 0 <= nc < len(matriz[0]) and not matriz_parametro[nf][nc]: # que no se vaya de rango ni ya este descubierto
                mostrar_celda(matriz, matriz_parametro, matriz_bandera, nf, nc)

def calcular_puntaje(matriz_descubierto:list, marcador:dict, fin:bool=False, parametro_matriz:tuple=(0,0,0))-> None:
    '''
    Calcula el puntaje del jugador
    Recibe una matriz de booleanos, un diccionario, un booleano para saber si es el fin del juego, y una tupla con los parametros de la matriz de juego
    No tiene retorno
    '''
    puntos = 0
    if fin:
        puntos = (parametro_matriz[0] * parametro_matriz[1]) - parametro_matriz[2]
    else:
        for fila in range(len(matriz_descubierto)):
            for columna in range(len(matriz_descubierto[fila])):
                if matriz_descubierto[fila][columna]:
                    puntos += 1
    marcador['Puntaje'] = puntos

def definir_area_primer_click(matriz_area:list, fila:int, columna:int)->None:
    '''
    Define el area a descubrir en el primer click
    Recibe una matriz de booleanos, una fila y una columna
    No tiene retorno
    '''
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    if matriz_area[fila][columna] == False:
        matriz_area[fila][columna] = True
        for dir in directions:
            nf = fila + dir[0]
            nc = columna + dir[1]
            if nf <= len(matriz_area) - 1 and nc <= len(matriz_area[0]) - 1:
                matriz_area[nf][nc] = True

def colocar_bandera(matriz:list,fila:int,columna:int) -> None:
    '''
    Coloca una bandera en la casilla clickeada
    Recibe una matriz, una fila y una columna
    No tiene retorno
    '''
    if matriz[fila][columna] == True:
        matriz[fila][columna] = False
    else:
        matriz[fila][columna] = True

def controlar_victoria(matriz_comparacion:list, matriz_parametro:list)-> bool:
    '''
    Controla si el jugador gano
    Recibe una matriz de comparacion y una matriz parametro
    Devuelve un booleano
    '''
    ganador = False

    if matriz_comparacion == matriz_parametro:
        ganador = True
    return ganador

def dibujar_tablero(screen:any, buscaminas:list, tamaño_bloque:int, font:any, imagen_mina:any, imagen_cruz:any)->None:
    '''
    Dibuja el tablero
    Recibe la pantalla, el tablero, el tamaño del bloque, la fuente y las imagenes de mina y cruz
    No tiene retorno
    '''
    # Armar el tablero
    for fila in range(len(buscaminas)):
        for columna in range(len(buscaminas[fila])):
            valor = buscaminas[fila][columna]

            # Coordenada del bloque
            y = fila * (tamaño_bloque) + alto_marcador # le agrego los pixel del marcador
            x = columna * (tamaño_bloque) + 10

            # Valor del bloque
            pygame.draw.rect(screen, BG_COLOR, (x+1, y+1, tamaño_bloque, tamaño_bloque))
            pygame.draw.rect(screen, (0,0,0), (x+1, y+1, tamaño_bloque, tamaño_bloque), width=1)

            match valor:
                case 0:
                    numero = font.render(str(valor), True, BG_COLOR)
                case 1:
                    numero = font.render(str(valor), True, UNA_MINA)
                case 2:
                    numero = font.render(str(valor), True, DOS_MINAS)
                case 3:
                    numero = font.render(str(valor), True, TRES_MINAS)
                case 4:
                    numero = font.render(str(valor), True, CUATRO_MINAS)
                case 5:
                    numero = font.render(str(valor), True, CINCO_MINAS)
                case 6:
                    numero = font.render(str(valor), True, SEIS_MINAS)
                case 7:
                    numero = font.render(str(valor), True, SIETE_MINAS)
                case 8:
                    numero = font.render(str(valor), True, OCHO_MINAS)
            
            if valor == -1:
            # Muestro mina
                # imagen_mina = cargar_imagen(ruta_imagenes + "mina.png", (tamaño_bloque*0.8, tamaño_bloque*0.8)) 
                imagen_rect_mina = imagen_mina.get_rect(center=(x + tamaño_bloque / 2, y + tamaño_bloque / 2)) # get_rect -> coordenadas
                screen.blit(imagen_mina, imagen_rect_mina)
            elif valor == -2:
            # Muestro mina con cruz y reproduzco el sonido de la explosion una sola vez
                # explosion.play(0)
                # imagen_mina = cargar_imagen(ruta_imagenes + "mina.png", (tamaño_bloque*0.8, tamaño_bloque*0.8)) # Cargar una imagen
                imagen_rect_mina = imagen_mina.get_rect(center=(x + tamaño_bloque / 2, y + tamaño_bloque / 2)) # get_rect -> coordenadas
                # imagen_cruz = cargar_imagen(ruta_imagenes + "cruz.png", (tamaño_bloque*0.8, tamaño_bloque*0.8)) # Cargar una imagen
                imagen_rect_cruz = imagen_cruz.get_rect(center=(x + tamaño_bloque / 2, y + tamaño_bloque / 2)) # get_rect -> coordenadas
                screen.blit(imagen_mina, imagen_rect_mina)
                screen.blit(imagen_cruz, imagen_rect_cruz)
                
            else:
            # Muestro numeros      
                # Creo la coordenada para el numero          
                numero_rect = numero.get_rect(center=(x + tamaño_bloque / 2, y + tamaño_bloque / 2)) # get_rect -> coordenadas
                screen.blit(numero, numero_rect)

def dibujar_tablero_vacio(screen:any, buscaminas:list, descubierto:list, tamaño_bloque:int)->None:
    '''
    Dibuja el tablero vacio
    Recibe la pantalla, el tablero, la matriz de booleanos y el tamaño del bloque
    No tiene retorno
    '''
    for fila in range(len(buscaminas)):
        for columna in range(len(buscaminas[fila])):
            rect = pygame.Rect(columna * tamaño_bloque + 10, fila * tamaño_bloque + alto_marcador, tamaño_bloque, tamaño_bloque) # casillero en una variable - le sumo tamaño de cabecera a fila
            if descubierto[fila][columna] == False: # Si no es un casillero ya clickeado, le dibuja el casillero que "cubre" el numero
                pygame.draw.rect(screen, BG_COLOR2, rect) # cuadrado
                pygame.draw.rect(screen, COLOR_NEGRO, rect, 1) # borde

def dibujar_tablero_bandera(screen:any, buscaminas:list, matriz_bandera:list, tamaño_bloque:int, imagen_bandera:any)->None:
    '''
    Dibuja el tablero con banderas
    Recibe la pantalla, el tablero, la matriz de banderas, el tamaño del bloque y la imagen de la bandera
    No tiene retorno
    '''
    for fila in range(len(buscaminas)):
        for columna in range(len(buscaminas[fila])):
            if matriz_bandera[fila][columna] == True:
                # imagen_bandera = cargar_imagen(ruta_imagenes + "bandera.png", (tamaño_bloque*0.8, tamaño_bloque*0.8)) # Cargar una imagen
                screen.blit(imagen_bandera, (columna * tamaño_bloque + 10, fila * tamaño_bloque + alto_marcador )) # le sumo los pixels de la cabecera en fila

def simular_cronometro(segundos:int, contador_minutos:int, contador_horas:int) ->list:
    ''' 
    Simula un cronometro
    Recibe segundos, minutos y horas
    Devuelve segundos, minutos y horas
    '''

    segundos += 1
    
    if segundos >= 60:
        contador_minutos += 1
        segundos = 0
    if contador_minutos >= 60:
        contador_horas += 1
        contador_minutos = 0
        segundos = 0
    
    return [segundos, contador_minutos, contador_horas]

def leer_jugadores(archivo_puntajes:str)->dict:
    '''
    Lee los jugadores del archivo puntajes.json
    Recibe un archivo
    Devuelve un diccionario
    '''
    try:
        with open(archivo_puntajes, 'r') as archivo:
            jugadores = json.load(archivo)
        archivo.close()
    except FileNotFoundError:
        jugadores = []
        for i in range(1,4):
            jugador = {"Jugador": 'Ricky', "Puntaje":i}
            jugadores.append(jugador)

        with open(archivo_puntajes,"w") as archivo:
            json.dump(jugadores, archivo, indent=4)
            
    # except json.JSONDecodeError:
    return jugadores

def escribir_y_ordenar_jugadores(archivo_puntajes:str, jugador:dict)->None:
    '''
    Escribe los jugadores en el archivo puntajes.json
    Recibe un archivo y un diccionario
    No tiene retorno
    '''
    jugadores = leer_jugadores(archivo_puntajes)
    jugadores.append(jugador)
    jugadores.sort(key=lambda jugador: int(jugador['Puntaje']), reverse=True)
    with open(archivo_puntajes, 'w') as archivo:
        json.dump(jugadores, archivo, indent=4)
    archivo.close()

# def mostrar_podio(jugadores_ordenados:dict)->list:
#     '''
#     Muestra los puntajes de los jugadores
#     Recibe un diccionario
#     No tiene retorno
#     '''
#     podio = []
#     contador = 0
#     for jugador in jugadores_ordenados:
#         if contador < 3:
#             podio.append(jugador)
#             contador += 1
#         else:
#             break
#     return podio

def pantalla_podio(jugador: dict, clave:str, posicion: int) -> None:
    '''
    Carga los renders de los datos de los puntajes
    Recibe un diccionario, la clave y la pos del archivo
    '''
    fuente_podio = pygame.font.Font(ruta_fuentes + "Bitend DEMO.otf", 30)
    superficie_podio_jugador = fuente_podio.render(str(jugador[posicion][clave]), True, (COLOR_NEGRO))

    return superficie_podio_jugador