# HERRAMIENTAS BASE
import pygame
import pygame.mixer as mixer
from biblioteca_del_juego import *
#---------------------------------------------------INICIALIZADORES--------------------------------------------------#
pygame.init()
pygame.font.init() #INICIALIZA LA FUENTE QUE SE USARA EN EL JUEGO PARA ESCRIBIR TEXTO
mixer.init()
    #Fuente para los numeros
font = pygame.font.SysFont("Arial", tamaño_bloque)

#-------------------------------------------------CONFIG MAIN SCREEN-------------------------------------------------#
screen = pygame.display.set_mode(RESOLUCION_SCREEN)

#---------------------------------------------DESARROLLO MENÚ PRINCIPAL----------------------------------------------#
#--------------------------------------------------CONFIGS VARIAS----------------------------------------------------#

pygame.display.set_caption("BUSCAMINAS")
pygame.time.set_timer(evento_cronometro, UN_SEGUNDO)

#--------------------------------------------------SONIDOS--------------------------------------------------------#
mixer.music.load(ruta_sonidos + "musica_de_fondo.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

#--------------------------------------------------PUNTAJES-------------------------------------------------------#
jugadores = leer_jugadores(archivo_puntajes)

# ═════════════════════════════════════════════════DESARROLLO IN GAME═════════════════════════════════════════════════#
encendido = True
while encendido == True:

#═══════════════════════════════════════════════VISUAL MENU PRINCIPAL════════════════════════════════════════════════#
    if instancia_pantalla == "MENU":
        #Imagen de fondo
        screen.blit(imagen_fondo_menu, (0, 0)) 

        #Textos
        screen.blit(superficie_titulo, (ubicacion_xy_titulo))
        screen.blit(superficie_nivel, (inicio_ubicacion_x_opciones, 158))
        screen.blit(superficie_jugar, (inicio_ubicacion_x_opciones, 258))
        screen.blit(superficie_puntajes, (inicio_ubicacion_x_opciones, 358))
        screen.blit(superficie_salir, (inicio_ubicacion_x_opciones, 458))

        #Botones al lado del texto
        boton_nivel = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x_titulo, 160, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x_titulo, 160, sombra_ancho, sombra_alto), width=5)

        boton_jugar = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x_titulo, 260, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x_titulo, 260, sombra_ancho, sombra_alto), width=5)

        boton_puntajes = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x_titulo, 360, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x_titulo, 360, sombra_ancho, sombra_alto), width=5)

        boton_salir = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x_titulo, 460, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x_titulo, 460, sombra_ancho, sombra_alto), width=5)

        pygame.draw.rect(screen, (COLOR_NEGRO), (0, 0, ANCHO_SCREEN, ALTO_SCREEN), width=5)

#═════════════════════════════════════════════VISUAL DE PANTALLA NIVEL═══════════════════════════════════════════════#
    elif instancia_pantalla == "NIVEL":
        screen.blit(imagen_fondo_niveles, (0, 0))
        screen.blit(superficie_nivel_titulo, ubicacion_xy_nivel_titulo)
        screen.blit(superficie_nivel_facil, (inicio_ubicacion_x_opciones+40, 165))
        screen.blit(superficie_nivel_medio, (inicio_ubicacion_x_opciones+40, 265))
        screen.blit(superficie_nivel_dificil, (inicio_ubicacion_x_opciones+40, 365))
        screen.blit(superficie_nivel_salir, (inicio_ubicacion_x_opciones+40, 465))

        boton_nivel_facil = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x__nivel_titulo, 160, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x__nivel_titulo, 160, sombra_ancho, sombra_alto), width=5)

        boton_nivel_medio = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x__nivel_titulo, 260, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x__nivel_titulo, 260, sombra_ancho, sombra_alto), width=5)

        boton_nivel_dificil = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x__nivel_titulo, 360, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x__nivel_titulo, 360, sombra_ancho, sombra_alto), width=5)

        boton_nivel_volver = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x__nivel_titulo, 460, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x__nivel_titulo, 460, sombra_ancho, sombra_alto), width=5)

        pygame.draw.rect(screen, (COLOR_NEGRO), (0, 0, ANCHO_SCREEN, ALTO_SCREEN), width=5)

#═════════════════════════════════════════════VISUAL DE PANTALLA JUGAR═══════════════════════════════════════════════#
    elif instancia_pantalla == "JUGAR":
        if matriz_a_crear == 0:
            validacion_jugar = 1
            instancia_pantalla = "NIVEL"

        else:
            screen.fill(COLOR_NEGRO)

            #INVOCACION DE MARCADOR Y TABLERO
            screen.blit(marcador, (0,0))
            superficie_score = FUENTE_NUMEROS.render(puntaje, False, COLOR_ROJO)
            puntaje = str(Score['Puntaje']).zfill(3)
            screen.blit(superficie_score, (70,punto_y_contadores_del_marcador+16))
            dibujar_tablero(screen, buscaminas, tamaño_bloque, font, imagen_mina, imagen_cruz)
            dibujar_tablero_vacio(screen, buscaminas, descubierto, tamaño_bloque)
            dibujar_tablero_bandera(screen, buscaminas, matriz_bandera, tamaño_bloque, imagen_bandera)

            #INVOCACION DE BOTONES CON SUS CORRESPONDIENTES HITBOX
            hitbox_abandonar = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_X_botones, ubicación_Y_abandonar, 40, 40), width=100)
            screen.blit(imagen_inicio, (ubicacion_X_botones-10,ubicación_Y_abandonar-10))

            hitbox_reiniciar = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_X_botones, ubicacion_Y_reiniciar, 40, 40), width=100)
            screen.blit(imagen_reset, (ubicacion_X_botones-10, ubicacion_Y_reiniciar))

            #INVOCACION DE CONTADORES
            screen.blit(superficie_cronometro, ((ubicacion_X_botones + 65), punto_y_contadores_del_marcador+16))
            bordes_pantalla = pygame.draw.rect(screen, (COLOR_NEGRO), (0, 0, ANCHO_SCREEN, ALTO_SCREEN), width=5)
            bordes_marcador = pygame.draw.rect(screen, (COLOR_NEGRO), (0, 0, ancho_marcador, alto_marcador), width=5)

            if ganador and ingreso_nombre == False:
                mensaje = FUENTE_RESULTADO.render(mensaje_ganaste, True, COLOR_NEGRO)
                screen.blit(imagen_trofeo, (0,100))
                if nombre_usuario != "":
                    screen.blit(nombre_usuario, (210, 520))
                mensaje_nombre = FUENTE_NOMBRE_RESULTADO.render(mensaje_ingreso_nombre, True, COLOR_NEGRO)
                nombre_usuario = FUENTE_NOMBRE_RESULTADO.render(nombre_ingresado, True, COLOR_NEGRO)
                screen.blit(mensaje_nombre, (170, 260))
                screen.blit(mensaje, (159,191))

            elif game_over and ingreso_nombre == False:
                mensaje = FUENTE_RESULTADO.render(mensaje_perdiste, True, COLOR_BLANCO)
                screen.blit(imagen_bomba, (-140,30))
                if nombre_usuario != "":
                    screen.blit(nombre_usuario, (209, 426))
                mensaje_nombre = FUENTE_NOMBRE_RESULTADO.render(mensaje_ingreso_nombre, True, COLOR_BLANCO)
                nombre_usuario = FUENTE_NOMBRE_RESULTADO.render(nombre_ingresado, True, COLOR_BLANCO)
                screen.blit(mensaje_nombre, (168, 375))
                screen.blit(mensaje, (150,300))


#════════════════════════════════════════════VISUAL DE PANTALLA PUNTAJE══════════════════════════════════════════════#
    elif instancia_pantalla == "PUNTAJE":
        screen.blit(imagen_fondo_puntajes, (0,0))
        screen.blit(imagen_podio, (-150,70))
        if len(jugadores) > 0:
            superficie_podio_jugador = pantalla_podio(jugadores, "Jugador", 0)
            superficie_podio_puntaje = pantalla_podio(jugadores, "Puntaje", 0)
            screen.blit(superficie_podio_jugador, (220,283))
            screen.blit(superficie_podio_puntaje, (240,324))
            superficie_podio_jugador = pantalla_podio(jugadores, "Jugador", 1)
            superficie_podio_puntaje = pantalla_podio(jugadores, "Puntaje", 1)
            screen.blit(superficie_podio_jugador, (20,352))
            screen.blit(superficie_podio_puntaje, (82,386))
            superficie_podio_jugador = pantalla_podio(jugadores, "Jugador", 2)
            superficie_podio_puntaje = pantalla_podio(jugadores, "Puntaje", 2)
            screen.blit(superficie_podio_jugador, (364,354))
            screen.blit(superficie_podio_puntaje, (390,390))
        screen.blit(superficie_puntajes_titulo, ubicacion_xy_puntajes_titulo)
        screen.blit(superficie_puntajes_volver, (inicio_ubicacion_x_opciones+30, 460))

        boton_puntaje_volver = pygame.draw.rect(screen, (COLOR_GRIS), (ubicacion_x_puntajes_titulo, 460, ancho_rectangulo, alto_rectangulo), width=100)
        pygame.draw.rect(screen, (COLOR_NEGRO), (ubicacion_x_puntajes_titulo, 460, sombra_ancho, sombra_alto), width=5)

        pygame.draw.rect(screen, (COLOR_NEGRO), (0, 0, ANCHO_SCREEN, ALTO_SCREEN), width=5)

#════════════════════════════════════════════════════OPCION SALIR════════════════════════════════════════════════════#
    else:
        encendido = False

#═══════════════════════════════════════════════════════EVENTOS══════════════════════════════════════════════════════#
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            encendido = False

#══════════EVENTO CLICK DE MOUSE IZQUIERDO══════════#
        if evento.type == pygame.MOUSEBUTTONDOWN:
            XY_CLICK = list(pygame.mouse.get_pos())
            #══════════EVENTO CLICK DE MOUSE IZQUIERDO EN PANTALLA PRINCIPAL══════════#
            if instancia_pantalla == "MENU":

                if boton_nivel.collidepoint(XY_CLICK):
                    instancia_pantalla = "NIVEL"

                elif boton_jugar.collidepoint(XY_CLICK):
                    instancia_pantalla = "JUGAR"

                elif boton_puntajes.collidepoint(XY_CLICK):
                    instancia_pantalla = "PUNTAJE"

                elif boton_salir.collidepoint(XY_CLICK):
                    instancia_pantalla = "SALIR"

            #════════════EVENTO CLICK DE MOUSE IZQUIERDO EN PANTALLA NIVEL════════════#
            elif instancia_pantalla == "NIVEL":

                if boton_nivel_facil.collidepoint(XY_CLICK):
                    matriz_a_crear = MATRIZ_FACIL
                    instancia_pantalla = ir_a_jugar(validacion_jugar)

                elif boton_nivel_medio.collidepoint(XY_CLICK):
                    matriz_a_crear = MATRIZ_MEDIO
                    instancia_pantalla = ir_a_jugar(validacion_jugar)

                elif boton_nivel_dificil.collidepoint(XY_CLICK):
                    matriz_a_crear = MATRIZ_DIFICIL
                    instancia_pantalla = ir_a_jugar(validacion_jugar)                 
            
                elif boton_nivel_volver.collidepoint(XY_CLICK):
                    instancia_pantalla = "MENU"

                # Inicializamos todas las matrices
                if matriz_a_crear != 0:
                    tamaño_bloque = ((ALTO_SCREEN-120) / matriz_a_crear[1])
                    imagen_mina = cargar_imagen(ruta_imagenes + "mina.png", (tamaño_bloque, tamaño_bloque)) # Cargar una imagen
                    imagen_cruz = cargar_imagen(ruta_imagenes + "cruz.png", (tamaño_bloque, tamaño_bloque)) # Cargar una imagen
                    imagen_bandera = cargar_imagen(ruta_imagenes + "bandera.png", (tamaño_bloque, tamaño_bloque)) # Cargar una imagen
                    buscaminas = inicializar_matriz(matriz_a_crear,0)
                    descubierto = inicializar_matriz(matriz_a_crear,False)
                    victoria_bandera = inicializar_matriz(matriz_a_crear,False)
                    victoria_evitar_minas = inicializar_matriz(matriz_a_crear,False)
                    matriz_bandera = inicializar_matriz(matriz_a_crear,False)
                    matriz_area = inicializar_matriz(matriz_a_crear,False)

            #══════════EVENTO CLICK DE MOUSE IZQUIERDO EN PANTALLA PUNTAJES═══════════#
            elif instancia_pantalla == "PUNTAJE":
# agregar puntajes

                if boton_puntaje_volver.collidepoint(XY_CLICK):
                    instancia_pantalla = "MENU"

            #════════════EVENTO CLICK DE MOUSE IZQUIERDO EN PANTALLA JUGAR════════════#
            elif instancia_pantalla == "JUGAR":
                if hitbox_abandonar.collidepoint(XY_CLICK):
                    instancia_pantalla = "MENU"
                    segundos = 0
                    minutos = 0
                    horas = 0
                    Score['Puntaje'] = 0
                    Empezo = False
                    game_over = False
                    ganador = False
                    ingreso_nombre = False
                    nombre_ingresado = ""
                    buscaminas = inicializar_matriz(matriz_a_crear,0)
                    descubierto = inicializar_matriz(matriz_a_crear,False)
                    matriz_bandera = inicializar_matriz(matriz_a_crear,False)
                    matriz_area = inicializar_matriz(matriz_a_crear,False)

                elif hitbox_reiniciar.collidepoint(XY_CLICK):
                    segundos = 0
                    minutos = 0
                    horas = 0
                    Score['Puntaje'] = 0
                    Empezo = False
                    game_over = False
                    ganador = False
                    ingreso_nombre = False
                    nombre_ingresado = ""
                    buscaminas = inicializar_matriz(matriz_a_crear,0)
                    descubierto = inicializar_matriz(matriz_a_crear,False)
                    matriz_bandera = inicializar_matriz(matriz_a_crear,False)
                    matriz_area = inicializar_matriz(matriz_a_crear,False)

                mouse_pos_click = pygame.mouse.get_pos()

                fila = int((mouse_pos_click[1] - alto_marcador) // tamaño_bloque) # le resto los pixeles del marcador antes de dividir
                columna = int((mouse_pos_click[0] - 10) // tamaño_bloque)

                if evento.button == 1 and (fila < len(buscaminas) and columna < len(buscaminas[0])) and (game_over == False and ganador == False) and bordes_marcador.collidepoint(XY_CLICK) == False: 
                    if Empezo == False:
                        definir_area_primer_click(matriz_area, fila, columna)
                        cargar_minas(buscaminas, matriz_area, matriz_a_crear)
                        crear_condicion_victoria(buscaminas, victoria_bandera, -1, True, False) # crea condicion de victoria por minas
                        crear_condicion_victoria(buscaminas, victoria_evitar_minas,  0, True, False) # crea condicion de victoria por banderas
                        definir_valores_campos(buscaminas)
                        Empezo = True
                        game_over = False
                        ganador = False

                    game_over = clickeo_casilla(buscaminas, descubierto, matriz_bandera, fila, columna)
                    if game_over:
                        crear_condicion_victoria(buscaminas, descubierto, -1, True, True)
                        matriz_bandera = inicializar_matriz(matriz_a_crear,False)
                    else:
                        calcular_puntaje(descubierto, Score)

                elif evento.button == 3 and (fila < len(buscaminas) and columna < len(buscaminas[0])) and (game_over == False and ganador == False and Empezo == True) and bordes_marcador.collidepoint(XY_CLICK) == False: 
                    if descubierto[fila][columna] == False:
                        colocar_bandera(matriz_bandera,fila,columna)

                if Empezo:
                    if (controlar_victoria(matriz_bandera, victoria_bandera) or controlar_victoria(descubierto, victoria_evitar_minas)):
                        matriz_bandera = inicializar_matriz(matriz_a_crear,False)
                        descubierto = inicializar_matriz(matriz_a_crear, True)
                        calcular_puntaje(descubierto, Score, True, matriz_a_crear)
                        tiempo_total = segundos + minutos * 60 + horas * 3600
                        resta_puntos = 150 - tiempo_total
                        Score['Tiempo'] = tiempo_total
                        if resta_puntos > 0:
                            Score['Puntaje'] += resta_puntos 
                        ganador = True

        if evento.type == evento_cronometro and ganador == False and game_over == False:
            superficie_cronometro = FUENTE_NUMEROS.render((f"{'0'.zfill(2)}:{'0'.zfill(2)}"), False, (255,0,0))
            if instancia_pantalla == "JUGAR":
                tiempo = simular_cronometro(segundos, minutos, horas)
                segundos = tiempo[0]
                minutos = tiempo[1]
                horas = tiempo[2]
                if horas == 0:
                    superficie_cronometro = FUENTE_NUMEROS.render((f"{str(minutos).zfill(2)}:{str(segundos).zfill(2)}"), False, (255,0,0))
                else:
                    superficie_cronometro = FUENTE_NUMEROS.render((f"{horas}:{str(minutos).zfill(2)}:{str(segundos).zfill(2)}"), False, (255,0,0))
                ancho_superficie_cronometro = superficie_cronometro.get_width()
                alto_superficie_cronometro = superficie_cronometro.get_height() 
        
        if evento.type == pygame.KEYDOWN and (ganador or game_over):
            if evento.key == pygame.K_RETURN:
                jugador = {
                    "Jugador": nombre_ingresado.capitalize(),
                    "Puntaje": int(puntaje)
                }
                escribir_y_ordenar_jugadores(archivo_puntajes, jugador)
                jugadores = leer_jugadores(archivo_puntajes)
                ingreso_nombre = True
                nombre_ingresado = ""
            elif evento.key == pygame.K_BACKSPACE:
                nombre_ingresado = nombre_ingresado[0:-1]
            elif len(nombre_ingresado) < 8:
                nombre_ingresado += evento.unicode

    pygame.display.update()