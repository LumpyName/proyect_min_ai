import pygame
import sys

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

# Inicializar PyGame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanque Vista Aérea")

# Colores
WHITE = (255, 255, 255)
DARK_GREEN = (34, 139, 34)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Posición central del tanque
tank_x, tank_y = WIDTH // 2, HEIGHT // 2

# Función para dibujar el tanque desde arriba
def draw_tank_topdown(x, y):
    # Orugas (rectángulos a los lados)
    # Oruga izquierda
    pygame.draw.rect(screen, BLACK, (x - 45, y - 50, 15, 100))
    # Oruga derecha
    pygame.draw.rect(screen, BLACK, (x + 30, y - 50, 15, 100))
    
    # Cuerpo principal del tanque (rectángulo)
    body = [
        (x - 30, y - 50),  # superior izquierda
        (x + 30, y - 50),  # superior derecha
        (x + 30, y + 50),  # inferior derecha
        (x - 30, y + 50)   # inferior izquierda
    ]
    pygame.draw.polygon(screen, DARK_GREEN, body)
    pygame.draw.polygon(screen, BLACK, body, 2)
    
    # Torreta (octágono/círculo simplificado en el centro)
    turret = [
        (x - 20, y - 10),
        (x - 14, y - 20),
        (x + 14, y - 20),
        (x + 20, y - 10),
        (x + 20, y + 10),
        (x + 14, y + 20),
        (x - 14, y + 20),
        (x - 20, y + 10)
    ]
    pygame.draw.polygon(screen, GREEN, turret)
    pygame.draw.polygon(screen, BLACK, turret, 2)
    
    # Cañón (rectángulo apuntando hacia arriba)
    cannon = [
        (x - 5, y - 20),   # base izquierda
        (x + 5, y - 20),   # base derecha
        (x + 5, y - 60),   # punta derecha
        (x - 5, y - 60)    # punta izquierda
    ]
    pygame.draw.polygon(screen, GRAY, cannon)
    pygame.draw.polygon(screen, BLACK, cannon, 2)
    
    # Escotilla (círculo pequeño en la torreta)
    pygame.draw.circle(screen, BLACK, (x, y), 6)

# Bucle principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Velocidad
    por = 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        tank_y -= por
        tank_x, tank_y = limitar(tank_x, tank_y)
    if keys[pygame.K_DOWN]:
        tank_y += por
        tank_x, tank_y = limitar(tank_x, tank_y)
    if keys[pygame.K_LEFT]:
        tank_x -= por
        tank_x, tank_y = limitar(tank_x, tank_y)
    if keys[pygame.K_RIGHT]:
        tank_x += por
        tank_x, tank_y = limitar(tank_x, tank_y)
    # Dibujar fondo
    screen.fill(WHITE)
    
    # Dibujar el tanque
    draw_tank_topdown(tank_x, tank_y)
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
