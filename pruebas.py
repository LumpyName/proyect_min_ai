import pygame
import sys
import numpy as np

from tools.tanque import Tanque, TEMA_DESIERTO 

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

# Posición inicial como vector NumPy
pos = np.array([WIDTH / 2, HEIGHT / 2], dtype=float)

# Constante de velocidad (pixeles por frame)
VELOCIDAD = 2.5

# Bucle principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.get_time() / 1000.0  # delta time en segundos

    # Dirección de movimiento (vector)
    vel = np.array([0.0, 0.0], dtype=float)
    keys = pygame.key.get_pressed()

    # Rotación de la torreta
    if keys[pygame.K_LEFT]:
        tanque1.angulo_torreta -= tanque1.velocidad_giro * dt
    if keys[pygame.K_RIGHT]:
        tanque1.angulo_torreta += tanque1.velocidad_giro * dt

    # Movimiento WASD
    if keys[pygame.K_w]:
        vel[1] -= 1
    if keys[pygame.K_s]:
        vel[1] += 1
    if keys[pygame.K_a]:
        vel[0] -= 1
    if keys[pygame.K_d]:
        vel[0] += 1

    # Normalizar el vector (mantener velocidad constante en diagonal)
    mag = np.linalg.norm(vel)
    if mag != 0:
        vel = (vel / mag) * VELOCIDAD

    # Actualizar posición
    pos += vel

    # Limitar dentro de la pantalla
    pos[0] = np.clip(pos[0], 0, WIDTH)
    pos[1] = np.clip(pos[1], 0, HEIGHT)

    # Dibujar
    screen.fill(WHITE)
    tanque1.draw(screen, pos[0], pos[1], tanque1.angulo_torreta)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

