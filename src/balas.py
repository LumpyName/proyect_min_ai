# balas.py: Clase para los disparos del tanque y su movimientol


import numpy as np

class Bala:
    def __init__(self, pos, dir):
        self.pos = np.copy(pos)
        self.dir = np.copy(dir)
        self.vel = 5.0

    def mover(self):
        self.pos += self.dir * self.vel
