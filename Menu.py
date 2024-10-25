#Menu en python
opcion = -1

while opcion != 3:
    print("1.- Mostrar pacientes")
    print("2.- Introducir nuevo pacientes")
    print("3.- Cerrar secion")
    opcion = int(input("Introduce una opcion: "))
    
    match opcion:
        case 1:
            print("Mostrar pacientes")
        case 2:
            print("Introduciendo")
        case 3:
            print("Saliento")
        case _:
            print("Error opcion no registrada")
