opcion = 1

while opcion != 0: 
    print("==reserva de vuelos")
    print("1) listar")
    print("2) reservar")
    print("3) modificar")
    print("4) eliminar")
    print("0) salir")
    print("ingrese opcion")
    opcion = int(input())

    match opcion:
        case 1:
            print("==vuelo de codigos==")
            print("1) santiago - brasil")
            print("2) santiago - argentina")
            print("3) santiago - canada")
        case 2:
            print("==reservar==")
            print("1) santiago - brasil")
            print("2) santiago - argentina")
            print("3) santiago - canada")
            print("ingrese vuelo a reservar")
            vuelo = int(input())
            print("ingrese el nombre del pasajero")
            nombre = input()
            print (f"reservar realizada para nombre")
        case 3:
            print("==modificar==")
            print("1) santiago - brasil")
            print("2) santiago - argentina")
            print("3) santiago - canada")
            print("ingrese vuelo a modificar")
            vuelo = int(input())
        case 4:
            print("==eliminar==")
            print("!adios!")
            vuelo = 0
        case 0:
            print("!adios!")
            mensaje = input("vuelva pronto")
        case _:
            print("ingrese opcion correcta")        