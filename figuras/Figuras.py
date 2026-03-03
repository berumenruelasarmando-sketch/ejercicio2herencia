class Figura(object):
    
    def __init__(self):
        self.nombre = ""
        self.color = ""

    def leerDatosFiguras(self):
        self.nombre = input("Nombre: ")
        self.color = input("Color: ")

    def mostrarDatosFiguras(self):
        print(self.nombre, self.color)