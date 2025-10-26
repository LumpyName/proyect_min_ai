import pygame

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

    def draw(self, screen, x, y):
        s = ESCALA_TANQUE  # usa la constante global

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

        # Torreta
        turret = [
            (x - 20*s, y - 10*s),
            (x - 14*s, y - 20*s),
            (x + 14*s, y - 20*s),
            (x + 20*s, y - 10*s),
            (x + 20*s, y + 10*s),
            (x + 14*s, y + 20*s),
            (x - 14*s, y + 20*s),
            (x - 20*s, y + 10*s)
        ]
        pygame.draw.polygon(screen, self.color_torreta, turret)
        pygame.draw.polygon(screen, self.color_borde, turret, 2)

        # Cañón
        cannon = [
            (x - 5*s, y - 20*s),
            (x + 5*s, y - 20*s),
            (x + 5*s, y - 60*s),
            (x - 5*s, y - 60*s)
        ]
        pygame.draw.polygon(screen, self.color_cañon, cannon)
        pygame.draw.polygon(screen, self.color_borde, cannon, 2)

        # Escotilla
        pygame.draw.circle(screen, self.color_borde, (x, y), 6*s)

# Temas predefinidos
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
