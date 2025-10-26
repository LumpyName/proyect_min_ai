import pygame
import sys

from tools.tanque import Tanque, TEMA_DESIERTO
from tools.vector2d import Vector2D  # Asegúrate de importar tu clase

# Inicializar PyGame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanque Vista Aérea")

# Colores
WHITE = (255, 255, 255)

# Crear tanque
tanque1 = Tanque(**TEMA_DESIERTO)

# Posición inicial (como vector)
pos = Vector2D(WIDTH / 2, HEIGHT / 2)

# Constante de velocidad (pixeles por frame)
VELOCIDAD = 2.5

# Bucle principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dirección de movimiento (vector)
    vel = Vector2D(0, 0)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        vel.y -= 1
    if keys[pygame.K_DOWN]:
        vel.y += 1
    if keys[pygame.K_LEFT]:
        vel.x -= 1
    if keys[pygame.K_RIGHT]:
        vel.x += 1

    # Normalizar el vector (mantener velocidad constante en diagonal)
    if vel.magnitude() != 0:
        vel = vel.normalize() * VELOCIDAD

    # Actualizar posición
    pos += vel

    # Limitar dentro de la pantalla
    pos.x = max(0, min(WIDTH, pos.x))
    pos.y = max(0, min(HEIGHT, pos.y))

    # Dibujar
    screen.fill(WHITE)
    tanque1.draw(screen, pos.x, pos.y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

