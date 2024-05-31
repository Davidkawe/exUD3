import math

class EquiFigura:
    def __init__(self, longitudLados):
        self.__longitudLados = longitudLados

    def get_longitudLados(self):
        return self.__longitudLados

    def set_longitudLados(self, longitudLados):
        self.__longitudLados = longitudLados

    def __str__(self):
        return f"Figura con lados de longitud: {self.__longitudLados}"

class TrianguloEquilatero(EquiFigura):
    def getPerimetro(self):
        return 3 * self.get_longitudLados()

    def getArea(self):
        return (math.sqrt(3) * self.get_longitudLados()**2) / 4

class Cuadrado(EquiFigura):
    def getPerimetro(self):
        return 4 * self.get_longitudLados()

    def getArea(self):
        return self.get_longitudLados()**2

def getPerimetroFigura(figura):
    return figura.getPerimetro()

def getAreaFigura(figura):
    return figura.getArea()

te1 = TrianguloEquilatero(5)
cu1 = Cuadrado(5)

print("Triángulo Equilátero:")
print("Perímetro:", getPerimetroFigura(te1))
print("Área:", getAreaFigura(te1))

print("\nCuadrado:")
print("Perímetro:", getPerimetroFigura(cu1))
print("Área:", getAreaFigura(cu1))