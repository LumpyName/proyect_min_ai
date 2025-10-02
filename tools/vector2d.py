"""
Módulo Vector2D para operaciones de álgebra lineal en 2D
Autor: Tu nombre
Versión: 1.0
"""

import math
from typing import Union, Tuple

class Vector2D:
    """
    Clase para manejar vectores 2D con operaciones de álgebra lineal
    
    Attributes:
        x (float): Componente X del vector
        y (float): Componente Y del vector
    
    Example:
        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(1, 2)
        >>> v3 = v1 + v2
        >>> print(f"Resultado: {v3.x}, {v3.y}")
        Resultado: 4.0, 6.0
    """
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Inicializar vector 2D
        
        Args:
            x (float): Componente X, por defecto 0.0
            y (float): Componente Y, por defecto 0.0
        """
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Suma vectorial
        
        Args:
            other (Vector2D): Vector a sumar
            
        Returns:
            Vector2D: Resultado de la suma
        """
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """
        Resta vectorial
        
        Args:
            other (Vector2D): Vector a restar
            
        Returns:
            Vector2D: Resultado de la resta
        """
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: Union[int, float]) -> 'Vector2D':
        """
        Multiplicación por escalar
        
        Args:
            scalar (Union[int, float]): Escalar multiplicador
            
        Returns:
            Vector2D: Vector escalado
        """
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: Union[int, float]) -> 'Vector2D':
        """
        Multiplicación inversa por escalar (escalar * vector)
        
        Args:
            scalar (Union[int, float]): Escalar multiplicador
            
        Returns:
            Vector2D: Vector escalado
        """
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar: Union[int, float]) -> 'Vector2D':
        """
        División por escalar
        
        Args:
            scalar (Union[int, float]): Escalar divisor
            
        Returns:
            Vector2D: Vector dividido
            
        Raises:
            ZeroDivisionError: Si el escalar es cero
        """
        if scalar == 0:
            raise ZeroDivisionError("No se puede dividir un vector por cero")
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other: 'Vector2D') -> bool:
        """
        Igualdad entre vectores (con tolerancia para flotantes)
        
        Args:
            other (Vector2D): Vector a comparar
            
        Returns:
            bool: True si son iguales
        """
        if not isinstance(other, Vector2D):
            return False
        
        tolerance = 1e-10
        return (abs(self.x - other.x) < tolerance and 
                abs(self.y - other.y) < tolerance)
    
    def __repr__(self) -> str:
        """
        Representación string para debugging
        
        Returns:
            str: Representación del vector
        """
        return f"Vector2D({self.x:.3f}, {self.y:.3f})"
    
    def __str__(self) -> str:
        """
        Representación string para usuario
        
        Returns:
            str: Representación legible del vector
        """
        return f"({self.x:.2f}, {self.y:.2f})"
    
    def magnitude(self) -> float:
        """
        Magnitud del vector (norma euclidiana)
        
        Returns:
            float: Magnitud del vector
            
        Example:
            >>> v = Vector2D(3, 4)
            >>> v.magnitude()
            5.0
        """
        return math.sqrt(self.x**2 + self.y**2)
    
    def magnitude_squared(self) -> float:
        """
        Magnitud al cuadrado (más eficiente para comparaciones)
        
        Returns:
            float: Magnitud al cuadrado
        """
        return self.x**2 + self.y**2
    
    def normalize(self) -> 'Vector2D':
        """
        Normalizar vector (vector unitario)
        
        Returns:
            Vector2D: Vector normalizado
            
        Raises:
            ValueError: Si el vector es cero (no se puede normalizar)
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("No se puede normalizar un vector de magnitud cero")
        return Vector2D(self.x / mag, self.y / mag)
    
    def normalize_safe(self) -> 'Vector2D':
        """
        Normalizar vector de manera segura (retorna vector cero si magnitud es 0)
        
        Returns:
            Vector2D: Vector normalizado o vector cero
        """
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)
    
    def dot(self, other: 'Vector2D') -> float:
        """
        Producto punto entre vectores
        
        Args:
            other (Vector2D): Segundo vector
            
        Returns:
            float: Resultado del producto punto
        """
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector2D') -> float:
        """
        Producto cruz en 2D (retorna escalar)
        
        Args:
            other (Vector2D): Segundo vector
            
        Returns:
            float: Componente Z del producto cruz
        """
        return self.x * other.y - self.y * other.x
    
    def rotate(self, angle_radians: float) -> 'Vector2D':
        """
        Rotar vector usando matriz de rotación
        
        Args:
            angle_radians (float): Ángulo en radianes
            
        Returns:
            Vector2D: Vector rotado
        """
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        
        # Matriz de rotación aplicada al vector
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        
        return Vector2D(new_x, new_y)
    
    def angle_to(self, other: 'Vector2D') -> float:
        """
        Ángulo entre dos vectores
        
        Args:
            other (Vector2D): Segundo vector
            
        Returns:
            float: Ángulo en radianes
        """
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        
        if magnitudes == 0:
            return 0.0
        
        # Clamping para evitar errores de precisión flotante
        cos_angle = max(-1.0, min(1.0, dot_product / magnitudes))
        return math.acos(cos_angle)
    
    def distance_to(self, other: 'Vector2D') -> float:
        """
        Distancia entre dos puntos (vectores de posición)
        
        Args:
            other (Vector2D): Segundo punto
            
        Returns:
            float: Distancia euclidiana
        """
        return (self - other).magnitude()
    
    def lerp(self, other: 'Vector2D', t: float) -> 'Vector2D':
        """
        Interpolación lineal entre vectores
        
        Args:
            other (Vector2D): Vector destino
            t (float): Factor de interpolación [0, 1]
            
        Returns:
            Vector2D: Vector interpolado
        """
        return self + (other - self) * t
    
    def reflect(self, normal: 'Vector2D') -> 'Vector2D':
        """
        Reflejar vector respecto a una normal
        
        Args:
            normal (Vector2D): Vector normal (debe estar normalizado)
            
        Returns:
            Vector2D: Vector reflejado
        """
        return self - normal * (2 * self.dot(normal))
    
    def project_onto(self, other: 'Vector2D') -> 'Vector2D':
        """
        Proyectar este vector onto otro vector
        
        Args:
            other (Vector2D): Vector sobre el cual proyectar
            
        Returns:
            Vector2D: Vector proyectado
        """
        if other.magnitude_squared() == 0:
            return Vector2D(0, 0)
        
        scalar = self.dot(other) / other.magnitude_squared()
        return other * scalar
    
    def to_tuple(self) -> Tuple[int, int]:
        """
        Convertir a tupla de enteros (útil para pygame)
        
        Returns:
            Tuple[int, int]: Coordenadas como enteros
        """
        return (int(self.x), int(self.y))
    
    def to_tuple_float(self) -> Tuple[float, float]:
        """
        Convertir a tupla de flotantes
        
        Returns:
            Tuple[float, float]: Coordenadas como flotantes
        """
        return (self.x, self.y)
    
    @classmethod
    def from_angle(cls, angle_radians: float, magnitude: float = 1.0) -> 'Vector2D':
        """
        Crear vector desde ángulo y magnitud
        
        Args:
            angle_radians (float): Ángulo en radianes
            magnitude (float): Magnitud del vector
            
        Returns:
            Vector2D: Nuevo vector
        """
        return cls(math.cos(angle_radians) * magnitude, 
                  math.sin(angle_radians) * magnitude)
    
    @classmethod
    def random_unit(cls) -> 'Vector2D':
        """
        Crear vector unitario aleatorio
        
        Returns:
            Vector2D: Vector unitario aleatorio
        """
        import random
        angle = random.uniform(0, 2 * math.pi)
        return cls.from_angle(angle)

# Constantes útiles
ZERO = Vector2D(0, 0)
ONE = Vector2D(1, 1)
UP = Vector2D(0, -1)      # En pantalla, Y crece hacia abajo
DOWN = Vector2D(0, 1)
LEFT = Vector2D(-1, 0)
RIGHT = Vector2D(1, 0)

# Función utilitaria
def distance(point1: Vector2D, point2: Vector2D) -> float:
    """
    Función utilitaria para calcular distancia entre puntos
    
    Args:
        point1 (Vector2D): Primer punto
        point2 (Vector2D): Segundo punto
        
    Returns:
        float: Distancia entre puntos
    """
    return point1.distance_to(point2)

# Testing del módulo
if __name__ == "__main__":
    # Pruebas básicas
    print("=== Pruebas del módulo Vector2D ===")
    
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v2 = {3 * v2}")
    print(f"Magnitud v1 = {v1.magnitude()}")
    print(f"v1 normalizado = {v1.normalize()}")
    print(f"Producto punto = {v1.dot(v2)}")
    print(f"Ángulo entre vectores = {math.degrees(v1.angle_to(v2)):.1f}°")
    
    # Rotación
    v3 = Vector2D(1, 0)
    v4 = v3.rotate(math.pi/2)  # 90 grados
    print(f"(1,0) rotado 90° = {v4}")
    
    print("\n¡Módulo Vector2D funcionando correctamente!")
