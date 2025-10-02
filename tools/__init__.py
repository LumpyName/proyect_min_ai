from .vector2d import Vector2D

# Limites:
def limitar(x, y):
    if x < 0:
        x = 0
    elif x > 800:
        x = 800
    
    if y < 0:
        y = 0
    elif y > 600:
        y = 600
    
    return x, y

