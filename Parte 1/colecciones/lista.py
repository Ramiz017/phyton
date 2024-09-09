import random

def ingresar():
    lista = []
    num = int(input("Ingrese el número de datos que tendrá la lista: "))
    for _ in range(num):
        lista.append(random.randint(0, 50))
    print(lista)
    return lista

def buscar(lista):
    buscando = False
    buscar = int(input("Ingrese el dato que busca: "))
    for valor in lista:
        if buscar == valor:
            buscando = True
            break
    return buscando, buscar

def reemplazar(lista):
    print(f"los datos de la lista son: {lista}")
    buscar = int(input("Ingrese el dato que desea reemplazar: "))
    reemplazo = int(input("Ingrese el nuevo dato: "))
    for i in range(len(lista)):
        if lista[i] == buscar:
            lista[i] = reemplazo
    else:
            print("El dato no se encuentra en la lista")
    print(lista)

cont = 0
arreglo = []

while cont == 0:
    print("Menu de lista - prueba de case")
    print("1. Ingresar datos")
    print("2. Mostrar los datos de la lista")
    print("3. Ordenar los datos de la lista")
    print("4. Buscar un dato en la lista")
    print("5. Reemplazar un dato en la lista")
    print("0. Para salir")

    opcion = int(input("Ingrese una opción de la lista: "))

    match opcion:
        case 1:
            arreglo = ingresar()
        case 2:
            print(arreglo)
        case 3:
            arreglo.sort()
        case 4:
            esta, num = buscar(arreglo)
            if esta:
                print(f"El valor {num} fue encontrado")
            else:
                print("El valor no fue encontrado")
        case 5:
            reemplazar(arreglo)
        case 0: 
            cont = 1
            print("Has salido del programa")
        case _:
            print("Opción inválida")
