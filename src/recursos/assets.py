import os
import pygame

# Ruta absoluta a la carpeta assets
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

class Image:
    def __init__(self, tipo, variante=None, *args):
        self.tipo = tipo
        self.variante = variante
        self.args = args  # otros parámetros como tamaño, grosor, etc.

    def load(self):
        if self.tipo == "tanque":
            nombre_archivo = f"{self.tipo}_{self.variante}.png"
            ruta = os.path.join(ASSETS_DIR, nombre_archivo)
            return pygame.image.load(ruta)
        elif self.tipo == "linea":
            # Generar imagen por código según args
            pass
        elif self.tipo == "punto":
            # Generar punto negro tamaño fijo
            pass
