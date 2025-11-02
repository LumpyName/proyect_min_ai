import pygame

from .vector2d import Vector2D

ESCALA_TANQUE = 0.6  # Ajustá este valor (1.0 = tamaño actual)

class Tanque:
    """Clase para dibujar y personalizar un tanque con vista aérea"""
    
    def __init__(self, color_cuerpo=(34, 139, 34), color_torreta=(50, 205, 50), 
                 color_orugas=(0, 0, 0), color_cañon=(128, 128, 128)):
        """
        Inicializa un tanque con colores personalizables
        
        Args:
            color_cuerpo: Color del cuerpo principal (RGB)
            color_torreta: Color de la torreta (RGB)
            color_orugas: Color de las orugas (RGB)
            color_cañon: Color del cañón (RGB)
        """
        self.color_cuerpo = color_cuerpo
        self.color_torreta = color_torreta
        self.color_orugas = color_orugas
        self.color_cañon = color_cañon
        self.color_borde = (0, 0, 0)

        self.angulo_torreta = 0.0
        self.velocidad_giro = 2.5

        self.pos_x = 

    def cambiar_tema(self, color_cuerpo=None, color_torreta=None, 
                     color_orugas=None, color_cañon=None):
        """
        Cambia los colores del tanque
        
        Args:
            color_cuerpo: Nuevo color del cuerpo (RGB) o None para mantener
            color_torreta: Nuevo color de la torreta (RGB) o None para mantener
            color_orugas: Nuevo color de las orugas (RGB) o None para mantener
            color_cañon: Nuevo color del cañón (RGB) o None para mantener
        """
        if color_cuerpo is not None:
            self.color_cuerpo = color_cuerpo
        if color_torreta is not None:
            self.color_torreta = color_torreta
        if color_orugas is not None:
            self.color_orugas = color_orugas
        if color_cañon is not None:
            self.color_cañon = color_cañon

    def draw(self, screen, x, y, angulo_torreta=0.0):
        s = ESCALA_TANQUE  # usa la constante global
        centro = Vector2D(x, y)

        # Orugas
        pygame.draw.rect(screen, self.color_orugas, (x - 45*s, y - 50*s, 15*s, 100*s))
        pygame.draw.rect(screen, self.color_orugas, (x + 30*s, y - 50*s, 15*s, 100*s))

        # Cuerpo
        body = [
            (x - 30*s, y - 50*s),
            (x + 30*s, y - 50*s),
            (x + 30*s, y + 50*s),
            (x - 30*s, y + 50*s)
        ]
        pygame.draw.polygon(screen, self.color_cuerpo, body)
        pygame.draw.polygon(screen, self.color_borde, body, 2)

        # === TORRETA ===
        puntos_torreta_locales = [
            Vector2D(-20*s, -10*s),
            Vector2D(-14*s, -20*s),
            Vector2D( 14*s, -20*s),
            Vector2D( 20*s, -10*s),
            Vector2D( 20*s,  10*s),
            Vector2D( 14*s,  20*s),
            Vector2D(-14*s,  20*s),
            Vector2D(-20*s,  10*s),
        ]

        turret = [(centro + p.rotate(angulo_torreta)).to_tuple() for p in puntos_torreta_locales]
        pygame.draw.polygon(screen, self.color_torreta, turret)
        pygame.draw.polygon(screen, self.color_borde, turret, 2)

        # === CAÑÓN ===
        puntos_canon_locales = [
            Vector2D(-5*s, -20*s),
            Vector2D( 5*s, -20*s),
            Vector2D( 5*s, -60*s),
            Vector2D(-5*s, -60*s),
        ]

        cannon = [(centro + p.rotate(angulo_torreta)).to_tuple() for p in puntos_canon_locales]
        pygame.draw.polygon(screen, self.color_cañon, cannon)
        pygame.draw.polygon(screen, self.color_borde, cannon, 2)

        # Escotilla (centro)
        pygame.draw.circle(screen, self.color_borde, centro.to_tuple(), 6*s)

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
print("Hola Mundo")
