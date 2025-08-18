import pygame

# Inicializar Pygame
pygame.init()

# Cargar la imagen original
imagen_original = pygame.image.load("assets/tanque_azul.png")

# Definir nuevo tamaño (por ejemplo, 800x600)
nuevo_tamano = (200, 200)

# Redimensionar la imagen
imagen_redimensionada = pygame.transform.scale(imagen_original, nuevo_tamano)

# Mostrar en pantalla (opcional)
pantalla = pygame.display.set_mode(nuevo_tamano)
pantalla.blit(imagen_redimensionada, (0, 0))
pygame.display.flip()

# Esperar unos segundos antes de cerrar
pygame.time.wait(3000)
pygame.quit()
