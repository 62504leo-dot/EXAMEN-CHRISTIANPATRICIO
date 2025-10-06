class Figura:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.area = 0

    def leer_datos(self):
        """Método para leer datos desde el teclado"""
        self.base = float(input("Ingrese la base: "))
        self.altura = float(input("Ingrese la altura: "))

    def calcular_area(self):
        """Método que será sobrescrito en cada figura"""
        pass

    def mostrar_resultado(self):
        """Muestra el área calculada"""
        print(f"El área es: {self.area:.2f}")


class Triangulo(Figura):
    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def mostrar_resultado(self):
        print(f"El área del triángulo es: {self.area:.2f}")


class Rectangulo(Figura):
    def calcular_area(self):
        self.area = self.base * self.altura

    def mostrar_resultado(self):
        print(f"El área del rectángulo es: {self.area:.2f}")
