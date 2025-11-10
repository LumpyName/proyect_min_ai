import pygame
import numpy as np

ESCALA_TANQUE = 0.6  # Escala general del tanque

class Tanque:
    """Tanque modular con vista aérea, torreta y cuerpo independientes."""

    def __init__(self, color_cuerpo=(34, 139, 34), color_torreta=(50, 205, 50),
                 color_orugas=(0, 0, 0), color_cañon=(128, 128, 128)):
        self.color_cuerpo = color_cuerpo
        self.color_torreta = color_torreta
        self.color_orugas = color_orugas
        self.color_cañon = color_cañon
        self.color_borde = (0, 0, 0)

        self.angulo_torreta = 0.0
        self.angulo_cuerpo = 0.0
        self.velocidad_giro = 125.0

    # ===================== UTILIDAD =====================
    def _rotar_punto(self, punto, angulo_grados):
        """Rota un punto (x, y) alrededor del origen."""
        rad = np.radians(angulo_grados)
        rot = np.array([[np.cos(rad), -np.sin(rad)],
                        [np.sin(rad),  np.cos(rad)]])
        return rot @ punto

    # ===================== DIBUJO CUERPO =====================
    def _draw_cuerpo(self, screen, x, y):
        """Dibuja el cuerpo completo (orugas + cuerpo + marca delantera)."""
        s = ESCALA_TANQUE
        centro = np.array([x, y])

        # --- Forma base del cuerpo ---
        puntos_cuerpo_locales = np.array([
            [-30*s, -50*s],
            [ 30*s, -50*s],
            [ 30*s,  50*s],
            [-30*s,  50*s]
        ])

        cuerpo = [tuple(centro + self._rotar_punto(p, self.angulo_cuerpo)) for p in puntos_cuerpo_locales]
        pygame.draw.polygon(screen, self.color_cuerpo, cuerpo)
        pygame.draw.polygon(screen, self.color_borde, cuerpo, 2)

        # --- Orugas ---
        orugas_izq = np.array([[-45*s, -50*s], [-30*s, -50*s], [-30*s, 50*s], [-45*s, 50*s]])
        orugas_der = np.array([[30*s, -50*s], [45*s, -50*s], [45*s, 50*s], [30*s, 50*s]])

        oruga_izq_rot = [tuple(centro + self._rotar_punto(p, self.angulo_cuerpo)) for p in orugas_izq]
        oruga_der_rot = [tuple(centro + self._rotar_punto(p, self.angulo_cuerpo)) for p in orugas_der]

        pygame.draw.polygon(screen, self.color_orugas, oruga_izq_rot)
        pygame.draw.polygon(screen, self.color_orugas, oruga_der_rot)

        pygame.draw.polygon(screen, self.color_borde, oruga_izq_rot, 2)
        pygame.draw.polygon(screen, self.color_borde, oruga_der_rot, 2)

        # --- Marca delantera ---
        punta = np.array([0, -55*s])
        punta_rotada = centro + self._rotar_punto(punta, self.angulo_cuerpo)
        pygame.draw.circle(screen, (255, 0, 0), punta_rotada.astype(int), int(5*s))

    # ===================== DIBUJO TORRETA =====================
    def _draw_torreta(self, screen, x, y):
        """Dibuja la torreta y el cañón sobre el cuerpo."""
        s = ESCALA_TANQUE
        centro = np.array([x, y])

        # --- Torreta ---
        puntos_torreta_locales = np.array([
            [-20*s, -10*s],
            [-14*s, -20*s],
            [ 14*s, -20*s],
            [ 20*s, -10*s],
            [ 20*s,  10*s],
            [ 14*s,  20*s],
            [-14*s,  20*s],
            [-20*s,  10*s],
        ])
        turret = [tuple(centro + self._rotar_punto(p, self.angulo_torreta)) for p in puntos_torreta_locales]
        pygame.draw.polygon(screen, self.color_torreta, turret)
        pygame.draw.polygon(screen, self.color_borde, turret, 2)

        # --- Cañón ---
        puntos_canon_locales = np.array([
            [-5*s, -20*s],
            [ 5*s, -20*s],
            [ 5*s, -60*s],
            [-5*s, -60*s],
        ])
        cannon = [tuple(centro + self._rotar_punto(p, self.angulo_torreta)) for p in puntos_canon_locales]
        pygame.draw.polygon(screen, self.color_cañon, cannon)
        pygame.draw.polygon(screen, self.color_borde, cannon, 2)

        # --- Escotilla ---
        pygame.draw.circle(screen, self.color_borde, centro.astype(int), int(6*s))

    # ===================== DIBUJO COMPLETO =====================
    def draw(self, screen, x, y):
        """Dibuja todo el tanque."""
        self._draw_cuerpo(screen, x, y)
        self._draw_torreta(screen, x, y)

    # ===================== CONTROL DE ÁNGULOS =====================
    def rotar_torreta(self, delta):
        """Ajusta el ángulo de la torreta."""
        self.angulo_torreta = (self.angulo_torreta + delta) % 360

    def rotar_cuerpo(self, delta):
        """Ajusta el ángulo del cuerpo."""
        self.angulo_cuerpo = (self.angulo_cuerpo + delta) % 360

TEMA_VERDE = {
    'color_cuerpo': (34, 139, 34),
    'color_torreta': (50, 205, 50),
    'color_orugas': (0, 0, 0),
    'color_cañon': (128, 128, 128)
}

TEMA_AZUL = {
    'color_cuerpo': (30, 100, 180),
    'color_torreta': (70, 150, 220),
    'color_orugas': (20, 20, 60),
    'color_cañon': (150, 150, 180)
}

TEMA_ROJO = {
    'color_cuerpo': (180, 30, 30),
    'color_torreta': (220, 70, 70),
    'color_orugas': (60, 20, 20),
    'color_cañon': (180, 100, 100)
}

TEMA_DESIERTO = {
    'color_cuerpo': (194, 178, 128),
    'color_torreta': (210, 180, 140),
    'color_orugas': (101, 67, 33),
    'color_cañon': (139, 119, 101)
}
