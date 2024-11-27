import pygame
import pygame.mixer as mixer
from biblioteca_de_imágenes_y_sonido import cargar_imagen

pygame.font.init() #INICIALIZA LA FUENTE QUE SE USARA EN EL JUEGO PARA ESCRIBIR TEXTO 
# from Biblioteca import *

# Cargar variable de entorno de la ruta del archivo .env
ruta_imagenes = "Parcial_Buscaminas/Imagenes/"
ruta_fuentes = "Parcial_Buscaminas/Fuentes/"
ruta_sonidos = "Parcial_Buscaminas/Sonidos/"

# Cargar variable de la ruta del archivo .json
archivo_puntajes = "puntajes.json"

    #CONSTANTES PANTALLA
ANCHO_SCREEN = 500
ALTO_SCREEN = 600
RESOLUCION_SCREEN = (ANCHO_SCREEN, ALTO_SCREEN)

    #CONSTANTES DE COLORES
COLOR_PANTALLA_INICIO = (137, 138, 128)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS = (120, 120, 120)
COLOR_ROJO = (255, 0, 0)
COLOR_BLANCO = (255, 255, 255)
BG_COLOR = (140, 141, 145)
BG_COLOR2 = (162, 164, 168)
UNA_MINA = (15, 15, 252)
DOS_MINAS = (2, 99, 23)
TRES_MINAS = (230, 5, 16)
CUATRO_MINAS = (1, 6, 56)
CINCO_MINAS = (145, 11, 1)
SEIS_MINAS = (115, 5, 107)
SIETE_MINAS = (1, 71, 77)
OCHO_MINAS = (0, 0, 0)

    #CONSTANTES DE FUENTES(Letra)
FUENTE_TITULOS = pygame.font.Font(ruta_fuentes + "Broken Console Bold.otf", 50)
FUENTE_OPCIONES = pygame.font.Font(ruta_fuentes + "Bitend DEMO.otf", 30)
FUENTE_NUMEROS = pygame.font.Font(ruta_fuentes + "Digital Dismay.otf", 80)
FUENTE_MARCADOR = pygame.font.SysFont("Segoe MDL2 Assets", 30)
FUENTE_RESULTADO = pygame.font.Font(ruta_fuentes + "GameBubleDEMO.otf", 50)
FUENTE_NOMBRE_RESULTADO = pygame.font.Font(ruta_fuentes + "GameBubleDEMO.otf", 20)

    #CONSTANTES TIEMPO
UN_SEGUNDO = 1000

    # Cantidad filas, cantidad columnas, cantidad minas
MATRIZ_FACIL = (8, 8, 10)
MATRIZ_MEDIO = (16, 16, 40)
MATRIZ_DIFICIL = (24, 24, 90)

#-------------------------------------------------CONFIGS VARIABLES--------------------------------------------------#
instancia_pantalla = "MENU"
matriz_a_crear = 0
validacion_jugar = 0
Empezo = False
game_over = False
ganador = False
alto_marcador = 120
tamaño_bloque = 25

    # imagen
imagen_fondo_menu = cargar_imagen(ruta_imagenes + "fondo.jpg", RESOLUCION_SCREEN) # Cargar una imagen
imagen_fondo_niveles = cargar_imagen(ruta_imagenes + "fondo_niveles.jpg", RESOLUCION_SCREEN) # Cargar una imagen
imagen_fondo_puntajes = cargar_imagen(ruta_imagenes + "confeti.jpg", RESOLUCION_SCREEN) # Cargar una imagen
imagen_bomba = cargar_imagen(ruta_imagenes + "bomba_explota.png", (700, 700))
imagen_trofeo = cargar_imagen(ruta_imagenes + "trofeo1.png", (500, 500))
imagen_podio = cargar_imagen(ruta_imagenes + "trofeos.png", (800, 400))
imagen_inicio = cargar_imagen(ruta_imagenes + "inicio.png", (40, 40))
imagen_reset = cargar_imagen(ruta_imagenes + "reset.png", (40, 40))

    # Sonidos
explosion = mixer.Sound(ruta_sonidos + "explosion.mp3")

#   Datos jugador
ingreso_nombre = False
nombre_usuario = ""
Score = {
    'Jugador': nombre_usuario,
    'Puntaje': 0,
    'Tiempo': 0
}

#----------HERRAMIENTAS DEL MENU PRINCIPAL-----------#
#TITULO
titulo_juego = "BUSCAMINAS"
superficie_titulo = FUENTE_TITULOS.render(titulo_juego, True, (COLOR_NEGRO))
ancho_titulo = superficie_titulo.get_width()
ubicacion_x_titulo = ((ANCHO_SCREEN - ancho_titulo) / 2) + 1
ubicacion_Y_titulos = 60
ubicacion_xy_titulo = (ubicacion_x_titulo, ubicacion_Y_titulos)
mensaje_perdiste = "Perdiste!"
mensaje_ganaste = "Ganaste"
mensaje_ingreso_nombre = "Ingresa tu nombre"
nombre_ingresado = ""
jugadores = {}
jugador = {}

#OPCIONES
inicio_ubicacion_x_opciones = 130
ancho_rectangulo = 30
sombra_ancho = ancho_rectangulo + 5
alto_rectangulo = 30
sombra_alto = alto_rectangulo +5

#--------------HERRAMIENTAS OPCION NIVEL-------------#
opcion_nivel = "Nivel"
superficie_nivel = FUENTE_OPCIONES.render(opcion_nivel, False, (COLOR_NEGRO))

#UNA VEZ DENTRO DE OPCION NIVEL
nivel_titulo = "DIFICULTAD"
superficie_nivel_titulo =FUENTE_TITULOS.render(nivel_titulo, True, (COLOR_NEGRO))
ancho_nivel_titulo = superficie_nivel_titulo.get_width()
ubicacion_x__nivel_titulo = ((ANCHO_SCREEN - ancho_nivel_titulo) / 2) + 1
ubicacion_xy_nivel_titulo = (ubicacion_x__nivel_titulo, ubicacion_Y_titulos)

opcion_nivel_facil = "Facil"
superficie_nivel_facil = FUENTE_OPCIONES.render(opcion_nivel_facil, False, (COLOR_NEGRO))

opcion_nivel_medio = "Medio"
superficie_nivel_medio = FUENTE_OPCIONES.render(opcion_nivel_medio, False, (COLOR_NEGRO))

opcion_nivel_dificil = "Dificil"
superficie_nivel_dificil = FUENTE_OPCIONES.render(opcion_nivel_dificil, False, (COLOR_NEGRO))

opcion_nivel_salir = "Salir"
superficie_nivel_salir = FUENTE_OPCIONES.render(opcion_nivel_salir, False, (COLOR_NEGRO))

#--------------HERRAMIENTAS OPCION JUGAR-------------#
opcion_jugar = "Jugar"
superficie_jugar = FUENTE_OPCIONES.render(opcion_jugar, False, (COLOR_NEGRO))
puntaje = str(Score['Puntaje'])

#CREACION MARCADOR
ubicacion_xy_marcador = (ANCHO_SCREEN, 120)
marcador = pygame.Surface(ubicacion_xy_marcador)
tablero22 = pygame.Surface((0 + ubicacion_xy_marcador[0],0))
tablero22.fill(COLOR_BLANCO)
marcador.fill(COLOR_GRIS)

#UBICACIONES EN MARCADOR
alto_marcador = marcador.get_height()
ancho_marcador = marcador.get_width()
ancho_botones = 30
alto_botones = 30
ubicacion_X_botones = (ancho_marcador / 2) - (ancho_botones/2)
ubicacion_Y_botones = (alto_marcador / 2)
ubicación_Y_abandonar = ubicacion_Y_botones - 40
ubicacion_Y_reiniciar = ubicacion_Y_botones + 10
punto_y_contadores_del_marcador = 5
ubicacion_x_cronometro = (ubicacion_X_botones + 100)

#------------HERRAMIENTAS OPCION PUNTAJES------------#
opcion_puntajes = "Ver Puntajes"
superficie_puntajes = FUENTE_OPCIONES.render(opcion_puntajes, False, (COLOR_NEGRO))
#UNA VEZ DENTRO DE OPCION PUNTAJE
puntajes_titulo = "PUNTAJES"
superficie_puntajes_titulo = FUENTE_TITULOS.render(puntajes_titulo, True, (COLOR_NEGRO))
ancho_puntajes_titulo = superficie_nivel_titulo.get_width()
ubicacion_x_puntajes_titulo = ((ANCHO_SCREEN - ancho_puntajes_titulo) / 2) + 3
ubicacion_xy_puntajes_titulo = (ubicacion_x_puntajes_titulo, ubicacion_Y_titulos)

puntajes_volver = "Volver"
superficie_puntajes_volver = FUENTE_OPCIONES.render(puntajes_volver, True, (COLOR_NEGRO))

#--------------HERRAMIENTAS OPCION SALIR-------------#
opcion_salir = "Salir"
superficie_salir = FUENTE_OPCIONES.render(opcion_salir, False, (COLOR_NEGRO))

#CRONOMETRO DEL MARCADOR
evento_cronometro = pygame.USEREVENT + 1
segundos = 0
minutos = 0
horas= 0
