kilometros = 0
act = True

while act == True:
    print("Hola has ingresado a alquilar un vehiculo!")
    kilometros = int(input("Ingrese los kilometros que consumio el vehiculo alquilado: "))

    if kilometros <= 300:
        montokilometros = 300000

    elif kilometros > 300 & kilometros <= 1000:
        montokilometros = 500000
        exceso = kilometros - 300
        adicion = exceso * 15000
        montokilometros = montokilometros + adicion

    elif kilometros > 1000: 
        montokilometros = 700000
        exceso = kilometros - 1000
        adicion = exceso * 20000
        montokilometros = montokilometros + adicion

    else:
        print("Ingrese una cantidad valida de kilometros, vuelva a ingresar")
        act = False

    print("1 = Mazda")
    print("2 = Honda")
    print("3 = Toyota")
    print("4 = Lamborgini")
    modelo = int(input("Ingrese el modelo del vehiculo: "))
    ano = int(input("Ingrese el año de modelo del vehiculo: "))

    if modelo == 1:
        if ano <= 2010:
            montokilometros = montokilometros * 0.95
        elif ano > 2010 & ano <= 2017:
            montokilometros = montokilometros * 0.98
        elif ano > 2017:
            montokilometros = montokilometros * 1.08

    elif modelo >= 2 & modelo <= 4:
        print("El modelo o año no aplica para ningun cargo o sobrecargo")

    else:
        print("Ingrese un modelo valido (Opcion del 1 al 4)")
        act = False

    print(f"El total para pagar el numero de {kilometros} kilometros recorridos en el auto alquilado es de")
    print(f"un total de {montokilometros}")
    act = False