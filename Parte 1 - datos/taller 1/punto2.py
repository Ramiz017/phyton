# diccionario para almacenar los contactos
agenda_telefonica = {}

opcion = ""

while opcion != "salir":
    print()
    print("Opciones disponibles:")
    print("1. Registrar nuevo contacto")
    print("2. Listar contactos")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("Para salir del programa escriba: salir")
    print()
    
    opcion = input("Ingrese la opción deseada: ")
    print()

    if opcion == "1":
        nombre = input("Ingrese el nombre y apellidos del contacto: ")
        num = input("Ingrese el Numero telefónico del contacto: ")
        ubicacion = input("Ingrese la ubicación del contacto: ")
        agenda_telefonica[nombre] = {

            "num": num,
            "ubicacion": ubicacion
        }
        
        print(f"Contacto {nombre} registrado con exito.")
    
    elif opcion == "2":
        if not agenda_telefonica:
            print("No hay contactos registrados en la agenda telefonica.")

        else:
            for nombre, datos in agenda_telefonica.items():
                print(f"Nombre: {nombre}, Numero: {datos['num']}, Ubicación: {datos['ubicacion']}")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
        if nombre in agenda_telefonica:
            nuevo_num = input("Ingrese el nuevo Numero telefónico: ")
            nueva_ubicacion = input("Ingrese la nueva ubicación: ")
            agenda_telefonica[nombre]["num"] = nuevo_num
            agenda_telefonica[nombre]["ubicacion"] = nueva_ubicacion
            print(f"Contacto {nombre} actualizado con exito.")
        else:
            print(f"Contacto {nombre} no encontrado en la agenda telefonica.")
    
    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        if nombre in agenda_telefonica:
            del agenda_telefonica[nombre]
            print(f"Contacto {nombre} eliminado con exito.")
        else:
            print(f"Contacto {nombre} no encontrado en la agenda telefonica.")
    
    elif opcion == "salir":
        confirmar = ""
        while confirmar != "no":
            confirmar = input("¿Está seguro que desea salir? (si/no): ")
            if confirmar == "si":
                print("Gracias por usar la agenda telefonica.")
                break
            elif confirmar == "no":
                print()
                break
            else:
                print("Error, por favor ingrese 'si' o 'no'")
    
    else:
        print("No se ha ingresado una opción válida, inténtelo nuevamente.")
        print()
