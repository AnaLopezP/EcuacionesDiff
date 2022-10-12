import ecuacion1
import ecuacion2
import ecuacion3
import ecuacion4
import ecuaciones.helpers as helpers


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("QUE EJERCICIO QUIERES VER:")
        print("[1] Ejercicio 1")
        print("[2] Ejercicio 2")
        print("[3] Ejercicio 3")
        print("[4] Ejercicio 4")
        print("[5] Ninguno")

        decision = input("> ")
        helpers.limpiar_pantalla()

        if decision == '1':
            print("--------------------------------ECUACION 1----------------------------------")
            ecuacion1.ecuacion1()

        if decision == '2':
            print("--------------------------------ECUACION 2----------------------------------")
            ecuacion2.ecuacion2()

        if decision == '3':
            print("--------------------------------ECUACION 3----------------------------------")
            ecuacion3.ecuacion3()

        if decision == '4':
            print("--------------------------------ECUACION 4----------------------------------")
            ecuacion4.ecuacion4()
        
        if decision == '5':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER  para continuar")
