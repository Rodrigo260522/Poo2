import os
import pickle

archivo_texto = "coleccion_libros.txt"
archivo_binario = "datos_libros.bin"

def crear_archivo_texto():
    if not os.path.exists(archivo_texto):
        with open(archivo_texto, "w") as f:
            f.write("Biblioteca de libros que quiero leer este ano\n")

def guardar_elemento(nombre, categoria, anio, autor, calificacion):
    try:
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        with open(archivo_texto, "a") as f:
            f.write(f"{nombre},{categoria},{anio},{autor},{calificacion}\n")
    except Exception as e:
        print("Error al guardar el elemento:", e)

def mostrar_coleccion():
    try:
        with open(archivo_texto, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("El archivo de coleccion no existe")

def buscar_elemento(nombre):
    try:
        with open(archivo_texto, "r") as f:
            encontrado = False
            for linea in f:
                if nombre.lower() in linea.lower():
                    print("Elemento encontrado:", linea.strip())
                    encontrado = True
            if not encontrado:
                print("No se encontro el elemento")
    except FileNotFoundError:
        print("El archivo de coleccion no existe")

def guardar_datos_binarios(nombre, popularidad, rareza):
    try:
        datos = {}
        if os.path.exists(archivo_binario):
            with open(archivo_binario, "rb") as f:
                datos = pickle.load(f)
        datos[nombre] = {"popularidad": popularidad, "rareza": rareza}
        with open(archivo_binario, "wb") as f:
            pickle.dump(datos, f)
    except Exception as e:
        print("Error al guardar datos binarios:", e)

def mostrar_datos_binarios():
    try:
        with open(archivo_binario, "rb") as f:
            datos = pickle.load(f)
            for nombre, info in datos.items():
                print(f"{nombre} -> Popularidad: {info['popularidad']}, Rareza: {info['rareza']}")
    except FileNotFoundError:
        print("El archivo binario no existe")
    except Exception as e:
        print("Error al leer datos binarios:", e)

def menu():
    crear_archivo_texto()
    while True:
        print("===== MI COLECCION DIGITAL =====")
        print("1. Agregar elemento")
        print("2. Mostrar coleccion completa")
        print("3. Buscar elemento por nombre")
        print("4. Mostrar datos binarios")
        print("5. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del libro: ")
                categoria = input("Categoria: ")
                anio = input("Anio: ")
                autor = input("Autor: ")
                calificacion = input("Calificacion: ")
                guardar_elemento(nombre, categoria, anio, autor, calificacion)

                popularidad = int(input("Popularidad (numero entero): "))
                rareza = int(input("Rareza (1-100): "))
                if rareza < 1 or rareza > 100:
                    raise ValueError("La rareza debe estar entre 1 y 100")
                guardar_datos_binarios(nombre, popularidad, rareza)
            except ValueError as ve:
                print("Error de validacion:", ve)
            finally:
                print("Proceso de agregado finalizado")

        elif opcion == "2":
            mostrar_coleccion()

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            buscar_elemento(nombre)

        elif opcion == "4":
            mostrar_datos_binarios()

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida")

menu()