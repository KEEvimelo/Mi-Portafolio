# Importa la biblioteca Pygame
import pygame

# Definición de algunos colores en formato RGB
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

# Inicializa Pygame
pygame.init()

# Definición de las dimensiones de la ventana del juego
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Juego del Triangulo")

# Variable para controlar el bucle principal del juego
hecho = False

# Reloj para controlar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Posición inicial del rectángulo
rect_x = 50
rect_y = 50

# Velocidad de cambio del rectángulo en los ejes x e y
rect_cambio_x = 5
rect_cambio_y = 5

# Bucle principal del juego
while not hecho:
    # Captura eventos de pygame, como cerrar la ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # Actualiza la posición del rectángulo
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y

    # Si el rectángulo alcanza los bordes de la ventana, invierte su dirección
    if rect_y > 450 or rect_y < 0:
        rect_cambio_y = rect_cambio_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x * -1

    # Llena la pantalla con color NEGRO
    pantalla.fill(NEGRO)

    # Dibuja un rectángulo blanco en la posición actual del rectángulo
    pygame.draw.rect(pantalla, BLANCO, [rect_x, rect_y, 50, 50])

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de fotogramas (20 FPS en este caso)
    reloj.tick(100)

# Sale del bucle principal y cierra Pygame
pygame.quit()

