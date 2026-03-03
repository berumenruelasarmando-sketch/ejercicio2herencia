from figuras.Circulo import Circulo
from figuras.Triangulo import Triangulo

def main():
    
    print("\n********Circulo***********")
    c = Circulo()
    c.leerDatosCirculo()
    
    print("\n*******************")
    c.mostrarDatosCirculo()

    print("\n********Triangulo***********")
    t = Triangulo()
    t.leerDatosTriangulo()
    
    print("\n*******************")
    t.mostrarDatosTriangulo()


if __name__ == "__main__":
    main()