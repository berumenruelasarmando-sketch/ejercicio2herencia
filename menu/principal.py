from figuras.Circulo import Circulo
from figuras.Triangulo import Triangulo

def menuPrincipal():
    while True:
        print("\n:---- Menú de Figuras-----")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Salir")
        
        op= int(input("Elejir opcion: "))
        print()
        
        match(op):
            case 1:
                c = Circulo()
                c.leerDatosFiguras()
                c.leerDatosCirculo()
                c.mostrarDatosCirculo()
                print("Circulo creado")
                
            case 2:
                t = Triangulo()
                t.leerDatosFiguras()
                t.leerDatosTriangulo()
                t.mostrarDatosTriangulo()
                print("triangulo creado")
            
            case 3:
                print("Adios")
                break
            
            case _:
                print("Opcion invalida")
if __name__ == "__main__":
    menuPrincipal()