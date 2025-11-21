# festival_playlist.py
nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    cantidad = int(input("¿Cuantas canciones se van a agregar? "))
    for i in range(cantidad):
        print(f"\n---Canción {i+1}---")
        nombre = input("Nombre de la cancion: ")
        artista = input("Artista: ")
        duracion = float(input("Duracion en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

def ver_reportes():
    if not nombres:
        print("\nNo hay canciones registradas.")
        return
    
    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    max_pop = max(popularidades)
    min_pop = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones

    cancion_mas_popular = nombres[popularidades.index(max_pop)]
    cancion_menos_popular = nombres[popularidades.index(min_pop)]

    print("\nReportes de la Playlist")
    print(f"Total de canciones: {total_canciones}")
    print(f"Duracion total: {duracion_total:.2f} minutos")
    print(f"Cancion más popular: {cancion_mas_popular} ({max_pop})")
    print(f"Cancion menos popular: {cancion_menos_popular} ({min_pop})")
    print(f"Promedio de popularidad: {promedio_pop:.2f}")

def buscar_canciones():
    if not nombres:
        print("\nNo hay canciones registradas")
        return
    
    print("\nBuscar canciones")
    print("1. Por artista")
    print("2. Por rango de popularidad")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        artista = input("Nombre del artista: ")
        print(f"\nCanciones de {artista}:")
        for i in range(len(nombres)):
            if artistas[i].lower() == artista.lower():
                print(f"- {nombres[i]} ({popularidades[i]})")
    elif opcion == "2":
        min_pop = int(input("Popularidad minima: "))
        max_pop = int(input("Popularidad maxima: "))
        print(f"\nCanciones con popularidad entre {min_pop} y {max_pop}:")
        for i in range(len(nombres)):
            if min_pop <= popularidades[i] <= max_pop:
                print(f"- {nombres[i]} ({popularidades[i]})")
    else:
        print("Opción inválida")

def playlist_recomendada():
    if not nombres:
        print("\nNo hay canciones registradas")
        return
    
    promedio_pop = sum(popularidades) / len(popularidades)
    print("\nPlaylist Recomendada (popularidad > promedio)")
    for i in range(len(nombres)):
        if popularidades[i] > promedio_pop:
            print(f"- {nombres[i]} de {artistas[i]} ({popularidades[i]})")

def menu():
    while True:
        print("\nFestival Playlist")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intenta de nuevo")

menu()