# observaciones.py: Funciones para generar el vector de observación de la IA


import numpy as np

def generar_observacion(tanque, enemigos, balas):
    obs = []
    # Distancia y dirección a enemigos
    for e in enemigos:
        vec = e.pos - tanque.pos
        dist = np.linalg.norm(vec)
        dir = vec / (dist + 1e-5)
        obs.extend([dist, dir[0], dir[1]])
    # Información de balas cercanas
    for b in balas:
        vec = b.pos - tanque.pos
        dist = np.linalg.norm(vec)
        dir = vec / (dist + 1e-5)
        obs.extend([dist, dir[0], dir[1]])
    # Velocidad y dirección propia
    obs.extend([tanque.vel, tanque.dir[0], tanque.dir[1]])
    return np.array(obs)
