print("Has ingresado al credito para autos")
inicial = int(input("Ingrese el credito que necesitas para el auto: "))

if inicial <= 25000000:
    cuota = inicial / 4
    mensualidadtotal = cuota * 3
    mensualidades = mensualidadtotal / 18

    print(f"La cuota inicial para el credito debe ser de {cuota} para aprobar el credito")
    print(f"Y el resto de la mensualidad que es de {mensualidadtotal} pesos")
    print(f"que debe pagarse en 18 cuotas de {mensualidades} pesos cada una")    
    print(f"El total a pagar sera de {inicial}") 

    confirmar = input("Desea confiramr este credito? ( si / no ): ")

    if confirmar == "si":
        print("El credito ha sido generado")
    else:
        print("El credito ha sido cancelado")


if inicial > 25000000:
    cuota = inicial * 0.35
    mensualidadtotal = inicial - cuota
    mensualidades = mensualidadtotal / 24

    print(f"La cuota inicial para el credito debe ser de {cuota} para aprobar el credito")
    print(f"Y el resto de la mensualidad que es de {mensualidadtotal} pesos")
    print(f"que debe pagarse en 18 cuotas de {mensualidades} pesos cada una")    
    print(f"El total a pagar sera de {inicial}")  

    confirmar = input("Desea confiramr este credito? ( si / no ): ")

    if confirmar == "si":
        print("El credito ha sido generado")
    else:
        print("El credito ha sido cancelado")