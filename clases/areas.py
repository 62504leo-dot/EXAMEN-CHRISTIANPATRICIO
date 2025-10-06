import math  # Necesario para usar pi

class Figura:
    def __init__(self):
        self.area = 0

    def leer_datos(self):
        """Se sobrescribe en cada figura según sus datos"""
        pass

    def calcular_area(self):
        """Se sobrescribe en cada figura"""
        pass

    def mostrar_resultado(self):
        print(f"El área es: {self.area:.2f}")


class Triangulo(Figura):
    def __init__(self):
        super().__init__()
        self.base = 0
        self.altura = 0

    def leer_datos(self):
        self.base = float(input("Ingrese la base del triángulo: "))
        self.altura = float(input("Ingrese la altura del triángulo: "))

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def mostrar_resultado(self):
        print(f"El área del triángulo es: {self.area:.2f}")


class Rectangulo(Figura):
    def __init__(self):
        super().__init__()
        self.base = 0
        self.altura = 0

    def leer_datos(self):
        self.base = float(input("Ingrese la base del rectángulo: "))
        self.altura = float(input("Ingrese la altura del rectángulo: "))

    def calcular_area(self):
        self.area = self.base * self.altura

    def mostrar_resultado(self):
        print(f"El área del rectángulo es: {self.area:.2f}")


class Circulo(Figura):
    def __init__(self):
        super().__init__()
        self.radio = 0

    def leer_datos(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def calcular_area(self):
        self.area = math.pi * (self.radio ** 2)

    def mostrar_resultado(self):
        print(f"El área del círculo es: {self.area:.2f}")
