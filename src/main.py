# main.py: Loop principal del juego y renderizado del mundo 2Dl

import pygame
from config import *
from tanque import Tanque
from balas import Bala

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

jugador = Tanque(ANCHO//2, ALTO//2)
balas_lista = []

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Ejemplo simple de movimiento manual
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        jugador.vel = 5
    else:
        jugador.vel = 0
    if teclas[pygame.K_LEFT]:
        jugador.rotar(-0.1)
    if teclas[pygame.K_RIGHT]:
        jugador.rotar(0.1)
    if teclas[pygame.K_SPACE]:
        balas_lista.append(Bala(jugador.pos, jugador.dir))

    jugador.mover()
    for bala in balas_lista:
        bala.mover()

    # Renderizar
    pantalla.fill((0,0,0))
    pygame.draw.circle(pantalla, (0,255,0), jugador.pos.astype(int), 15)
    for bala in balas_lista:
        pygame.draw.circle(pantalla, (255,0,0), bala.pos.astype(int), 5)
    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()
