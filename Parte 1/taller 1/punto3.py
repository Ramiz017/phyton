lista= []
cant = 0
promedio = 0
seguir = False

def calculo():
    global lista, cant, promedio
    dolares =int(input("ingrese la cantidad de dolares a convertir: "))
    total = dolares * 4350
    lista.append(total)
    cant = cant + 1
    promedio = promedio + total
    print(f"La cantidad de {dolares} en dolares ha sido convertidos a {total} pesos")
    print()
    return lista, promedio, cant

def finalizar():
    global lista, seguir, cant, promedio
    print("Las conversiones que realizaron fueron las siguientes")
    lista.sort()
    lista.reverse()
    print(lista)
    print(f"La cantidad de converisones fueron de: {cant}")
    promedio = promedio / cant
    print(f"El promedio de las conversiones fue de: {promedio}")
    seguir = True
    return promedio, seguir


while seguir == False:
    print("bienvenido a la tasa de cambio de dolar a pesos")
    print("la tasa de cambio es de 4.350 pesos por cada dolar ingresado")
    ingreso = input("Desea convertir dolares? (si/no): ")

    if ingreso == "si":
        calculo()
    elif ingreso == "no":
        finalizar()
    else:
        print("Ingrese una opcion valida (si/no)")
        print("")
