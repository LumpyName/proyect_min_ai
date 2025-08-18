# tanque.py: Clase del tanque jugador, movimiento, rotación y atributos


import numpy as np

class Tanque:
    def __init__(self, x, y):
        self.pos = np.array([x, y], dtype=float)
        self.dir = np.array([0, -1], dtype=float)  # Apunta hacia arriba
        self.vel = 0.0
        self.ang = 0.0

    def rotar(self, angulo_rad):
        R = np.array([[np.cos(angulo_rad), -np.sin(angulo_rad)],
                      [np.sin(angulo_rad),  np.cos(angulo_rad)]])
        self.dir = R @ self.dir

    def mover(self):
        self.pos += self.dir * self.vel
