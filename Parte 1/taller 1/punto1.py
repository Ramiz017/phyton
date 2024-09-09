cantestu = 0
cantemple = 0 # cantidad por cada tipo
cantextran= 0

totalestu = []
totalemple = [] # el que dio mas
totalextran = []

elegir = ""

while elegir != "salir":
    print()
    print("Tipos de usuarios:")
    print("estudiante")
    print("empleado")
    print("extranjero")
    print("Para salir del programa escriba:  salir")
    print()
    elegir = input("Ingrese su tipo de usuario: ")
    print()

    if elegir == "estudiante":
        print("El precio es de $1.500 COP por cada ticket para estudiantes")
        tickets = int(input("Ingrese la cantidad de tickets a comprar para estudiante: "))
        print()
        total = tickets * 1500

        print(f"El total de tickets que compro fue de: {tickets}")
        print(f"por un valor de: {total}")
        totalestu.append(total)
        cantestu= cantestu + 1

    elif elegir == "empleado":
        print("El precio es de $2.500 COP por cada ticket para empleados")
        tickets = int(input("Ingrese la cantidad de tickets a comprar para empleado: "))
        print()
        total = tickets * 2500

        print(f"El total de tickets que compro fue de: {tickets}")
        print(f"por un valor de: {total}")
        totalemple.append(total)
        cantemple= cantemple + 1

    elif elegir == "extranjero":
        print("El precio es de $4.500 COP por cada ticket para empleados")
        tickets = int(input("Ingrese la cantidad de tickets a comprar para extranjero: "))
        print()
        total = tickets * 4500

        print(f"El total de tickets que compro fue de: {tickets}")
        print(f"por un valor de: {total}")
        totalextran.append(total)
        cantextran= cantextran + 1

    elif elegir == "salir":
        confirmar = ""
        while confirmar != "no":
            confirmar= input("Esta seguro que desea salir? (si/no): ")
            if confirmar == "si":
                print("Gracias por su visita")
            elif confirmar == "no":
                print()
                break
            else:
                print("Error, por favor ingrese si o no")

    else:
        print("No se ha ingresado un tipo de usuario valido, intentelo nuevamente")
        print()

print("El numero de ventas por cada usuario fueron")
print(f"Estudiantes: {cantestu}")
print(f"Empleados: {cantemple}")
print(f"Extrangeros: {cantextran}")
print()

print("El total de las ventas fueron")
print(f"Estudiantes: {sum(totalestu)}")
print(f"Empleados: {sum(totalemple)}")
print(f"Extrangeros: {sum(totalextran)}")




