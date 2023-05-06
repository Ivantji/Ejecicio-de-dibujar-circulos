import pygame
import math


# inicializar pygame
pygame.init()

# crear la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Círculos")

# definir colores
azul = (0, 0, 255)
verde = (0, 255, 0)

# definir radios y posiciones iniciales
radius1 = 50
x1, y1 = width//2 - 200, height//2 # se establecen las cordenadas del centro
angulo1 = 0

radius2 = 70
x2, y2 = width//2 + 200, height//2
angulo2 = math.pi

# definir velocidades angulares
Vangular1 = 0.75 # en radianes por segundo
Vangular2 = -0.75

# definir reloj para calcular el tiempo transcurrido
clock = pygame.time.Clock()

# bucle principal
running = True
while running:
    # Se manejan los eventos
    for event in pygame.event.get(): #recupera una lista de eventos que han ocurrido desde la última vez que se llamó a la función.
        if event.type == pygame.QUIT: #este se activa cuando el usuario intenta cerrar la ventana del juego.
            running = False

    # calcular el tiempo transcurrido desde la última actualización
    tt = clock.tick(60) / 1000.0 # en segundos

    # actualizar ángulos
    #tt, representa el tiempo transcurrido desde el último cuadro en segundos.
    angulo1 += Vangular1 * tt # actualiza los valores de angulo1 y angulo2 multiplicando sus respectivas velocidades angulares (Vangular1 y Vangular2) por el tiempo tt.
    angulo2 += Vangular2 * tt

    # calcular nuevas posiciones
    x1 = int(width//2 - 200 + radius1 * math.cos(angulo1)) #int devuelve un número entero despues que la mitad del ancho del lienzo menos 200
    #y luego se sume el radius1 y el math.cos del angulo1
    y1 = int(height//2 + radius1 * math.sin(angulo1))

    x2 = int(width//2 + 200 + radius2 * math.cos(angulo2))
    y2 = int(height//2 + radius2 * math.sin(angulo2))

    # dibujar los círculos
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, azul, (x1, y1), radius1)
    pygame.draw.circle(screen, verde, (x2, y2), radius2)
    pygame.display.flip()

# salir de pygame
pygame.quit()
