# cine_asientos.py
def crear_sala(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    print("\nSala de cine: ")
    for fila in sala:
        print(" ".join(fila))
    print()

def reservar_asiento(sala, fila, columna):
    if fila < 1 or fila > len(sala) or columna < 1 or columna > len(sala[0]):
        print("Ese asiento no existe")
        return
    f = fila - 1
    c = columna - 1
    if sala[f][c] == "X":
        print("El asiento ya esta ocupado")
    else:
        sala[f][c] = "X"
        print("Asiento reservado correctamente")

def liberar_asiento(sala, fila, columna):
    if fila < 1 or fila > len(sala) or columna < 1 or columna > len(sala[0]):
        print("Ese asiento no existe")
        return
    f = fila - 1
    c = columna - 1
    if sala[f][c] == "L":
        print("El asiento ya esta libre")
    else:
        sala[f][c] = "L"
        print("Asiento liberado correctamente")

def contar_asientos(sala):
    libres = sum(fila.count("L") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)
    print("\nEstadisticas de la sala: ")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")

def menu():
    filas = int(input("Numero de filas del cine: "))
    columnas = int(input("Numero de columnas (asientos por fila): "))
    sala = crear_sala(filas, columnas)

    while True:
        print("\nMenu del sistema de cine")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            reservar_asiento(sala, fila, columna)
        elif opcion == "3":
            fila = int(input("Fila (1-based): "))
            columna = int(input("Columna (1-based): "))
            liberar_asiento(sala, fila, columna)
        elif opcion == "4":
            contar_asientos(sala)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")

menu()