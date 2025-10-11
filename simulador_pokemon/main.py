from clases.pokemon import Pokemon
pokemones = []
def capturar_pokemon():
    nombre = input("Nombre del Pokemon: ")
    print("\n Existen 18 tipos de pokemones: Fuego, Agua, Planta, Electrico, Normal, Lucha, Veneno, Tierra, Volador, Psiquico, Bicho, Roca, Fantasma, Hielo, Dragon, Acero, Siniestro y Hada")
    tipo = input("Escribe el tipo del Pokemon: ")
    try:
        ataque = int(input("Ataque: "))
        defensa = int(input("Defensa: "))
        salud = int(input("Salud: "))
    except ValueError:
        print("Entrada invalida. Usa solo numeros.")
        return
    nuevo = Pokemon(nombre, tipo, ataque, defensa, salud)
    pokemones.append(nuevo)

def entrenar_pokemon():
    if not pokemones:
        print("No hay Pokemones para entrenar")
        return
    for i, p in enumerate(pokemones):
        print(f"{i+1}. {p.nombre}")
    try:
        idx = int(input("Selecciona el Pokemon a entrenar: ")) - 1
        pokemon = pokemones[idx]
    except (ValueError, IndexError):
        print("Selección invalida.")
        return
    print("Entrenamiento personalizado: ")
    try:
        ataque = int(input("Mejora de ataque (0 si no aplica): "))
        defensa = int(input("Mejora de defensa (0 si no aplica): "))
        salud = int(input("Mejora de salud (0 si no aplica): "))
    except ValueError:
        print("Entrada invalida. Se usaran mejoras al azar")
        ataque, defensa, salud = 2, 3, 5
    pokemon.entrenar(ataque, defensa, salud)

def mostrar_todos():
    if not pokemones:
        print("No hay Pokemones registrados")
    for p in pokemones:
        p.mostrar_info()

def liberar_pokemon():
    if not pokemones:
        print("No hay Pokemon para liberar")
        return
    for i, p in enumerate(pokemones):
        print(f"{i+1}. {p.nombre}")
    idx = int(input("Selecciona el Pokemon a liberar: ")) - 1
    liberado = pokemones.pop(idx)
    del liberado

def menu():
    while True:
        print("\n Simulador Pokemon")
        print("1. Capturar nuevo Pokemon")
        print("2. Entrenar Pokemon")
        print("3. Ver todos los Pokemon")
        print("4. Ver total de Pokemon")
        print("5. Liberar un Pokemon")
        print("6. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            Pokemon.total_pokemones()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()