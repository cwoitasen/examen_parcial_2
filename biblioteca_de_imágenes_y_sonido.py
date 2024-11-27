import pygame

pygame.mixer.init()

def cargar_imagen(ruta:str, tamaño=(20, 20))->None:
    '''
    Carga una imagen y la escala de la misma
    recibe la ruta de la imagen y puede recibir el tamaño 
    Retorna una superficie
    '''
    imagen = pygame.image.load(ruta) # Cargar una imagen
    imagen = pygame.transform.scale(imagen, tamaño) # Escalar la imagen

    return imagen

# def cargar_sonido(ruta:str, tiempo:int)->None:
#     '''
#     Carga un sonido y lo reproduce
#     '''
#     sonido = pygame.mixer.music.load(ruta)
#     sonido = pygame.mixer.music.play(tiempo)

#     return sonido