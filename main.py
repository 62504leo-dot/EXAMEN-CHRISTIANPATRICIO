from clases.areas import Triangulo, Rectangulo, Circulo

def main():
    print("Cálculo de áreas de figuras geométricas")
    print("1. Triángulo")
    print("2. Rectángulo")
    print("3. Círculo")

    opcion = input("Elija una opción (1, 2 o 3): ")

    if opcion == "1":
        figura = Triangulo()
    elif opcion == "2":
        figura = Rectangulo()
    elif opcion == "3":
        figura = Circulo()
    else:
        print("Opción no válida.")
        return

    figura.leer_datos()
    figura.calcular_area()
    figura.mostrar_resultado()


if __name__ == "__main__":
    main()

