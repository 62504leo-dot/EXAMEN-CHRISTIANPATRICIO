from clases.areas import Triangulo, Rectangulo

def main():
    print("Cálculo de áreas de figuras geométricas")
    print("1. Triángulo")
    print("2. Rectángulo")

    opcion = input("Elija una opción (1 o 2): ")

    if opcion == "1":
        figura = Triangulo()
    elif opcion == "2":
        figura = Rectangulo()
    else:
        print("Opción no válida.")
        return

    figura.leer_datos()
    figura.calcular_area()
    figura.mostrar_resultado()


if __name__ == "__main__":
    main()
