from figuras.Figuras import Figura
import math

class Circulo(Figura):

    def __init__(self):
        super().__init__()
        self.radio = 0

    def leerDatosCirculo(self):
        self.nombre = "Círculo"
        self.color = input("Color: ")
        self.radio = float(input("Radio: "))

    def calcularArea(self):
        return math.pi * (self.radio ** 2)
            
    def mostrarDatosCirculo(self):
        print("Forma:", self.nombre)
        print("Color:", self.color)
        print("Radio:", self.radio)
        print("Área:", round(self.calcularArea(), 2))