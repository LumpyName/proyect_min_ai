import pygame
import sys
import numpy as np
from tools.tanque import Tanque, TEMA_DESIERTO

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanque Vista Aérea")

WHITE = (255, 255, 255)

tanque1 = Tanque(**TEMA_DESIERTO)
pos = np.array([WIDTH / 2, HEIGHT / 2], dtype=float)
VELOCIDAD = 2.5  # píxeles por frame

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # === CONTROL DE TORRETA ===
    if keys[pygame.K_k]:
        # Girar torreta 1° antihorario
        tanque1.angulo_torreta = (tanque1.angulo_torreta - 1) % 360
    elif keys[pygame.K_l]:
        # Girar torreta 1° horario
        tanque1.angulo_torreta = (tanque1.angulo_torreta + 1) % 360

    # === CONTROL DEL CUERPO ===
    # Rotación manual en 1° por frame
    if keys[pygame.K_a]:
        tanque1.rotar_cuerpo(-1)
        tanque1.angulo_torreta = (tanque1.angulo_torreta - 1) % 360

    elif keys[pygame.K_d]:
        tanque1.rotar_cuerpo(1)
        tanque1.angulo_torreta = (tanque1.angulo_torreta + 1) % 360

    # Avance según el ángulo del cuerpo (sin radianes)
    if keys[pygame.K_w] or keys[pygame.K_s]:
        # Dirección: frente o atrás (en grados)
        signo = -1 if keys[pygame.K_s] else 1

        # Convertir el ángulo del cuerpo a un vector de dirección
        angulo = np.radians(tanque1.angulo_cuerpo)
        dx = np.sin(angulo)
        dy = -np.cos(angulo)

        pos[0] += dx * VELOCIDAD * signo
        pos[1] += dy * VELOCIDAD * signo

    # Limitar posición dentro de pantalla
    pos[0] = np.clip(pos[0], 0, WIDTH)
    pos[1] = np.clip(pos[1], 0, HEIGHT)

    # === DIBUJAR ===
    screen.fill(WHITE)
    tanque1.draw(screen, pos[0], pos[1])
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()

