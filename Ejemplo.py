while True:  # Bucle infinito que se repetirá hasta que rompamos con break
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    print("\nSeleccione la operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = input("Ingrese el numero de la operacion: ")

    if opcion == "1":
        resultado = num1 + num2
        print("El resultado es:", resultado)

    elif opcion == "2":
        resultado = num1 - num2
        print("El resultado es:", resultado)

    elif opcion == "3":
        resultado = num1 * num2
        print("El resultado es:", resultado)

    elif opcion == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado es:", resultado)
        else:
            print("No se puede dividir entre cero.")

    elif opcion == "5":  # Opción para salir del programa
        print("Saliendo de la calculadora...")
        break  # Rompe el bucle y termina el programa

    else:
        print("Opcion invalida")

    print("\n--- Nueva operación ---\n")
