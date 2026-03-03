from figuras.Figuras import Figura

class Triangulo(Figura):

    def __init__(self):
        super().__init__()
        self.base = 0
        self.altura = 0

    def leerDatosTriangulo(self):
        self.nombre = "Triángulo"
        self.color = input("Color: ")
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

    def calcularArea(self):
        return (self.base * self.altura) / 2

        
    def mostrarDatosTriangulo(self):
            print("Forma:", self.nombre)
            print("Color:", self.color)
            print("Base:", self.base)
            print("Altura:", self.altura)
            print("Área:", self.calcularArea())