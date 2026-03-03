from figuras.circulo import Circulo
from figuras.triangulo import Triangulo

def menuFiguras():
    while True:
        print("\n:: Menú de Figuras ::")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Salir")
        opcion = input("Ingrese la figura: ")

        if opcion == "1" or opcion.lower() == "círculo":
            c = Circulo()
            c.leerDatosCirculo()
            print("\n--- Datos del Círculo ---")
            c.mostrarDatosCirculo()

        elif opcion == "2" or opcion.lower() == "triángulo":
            t = Triangulo()
            t.leerDatosTriangulo()
            print("\n--- Datos del Triángulo ---")
            t.mostrarDatosTriangulo()

        elif opcion == "3" or opcion.lower() == "salir":
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida, intente de nuevo.")