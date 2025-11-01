class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = int(popularidad)

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, un artista de {self.genero} con una popularidad de {self.popularidad}.")

    def actuar(self):
        print(f"{self.nombre} está actuando en el escenario")

    def despedirse(self):
        print(f"{self.nombre} se despide de su audiencia")

class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su exito {self.cancion_mas_popular} con gran energia")

class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo_musical):
        super().__init__(nombre, genero, popularidad)
        self.estilo_musical = estilo_musical

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo_musical} haciendo vibrar al publico.")

class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")

def iniciar_festival(lista_artistas):
    print("\n El festival musical comienza ahora \n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación \n")

def main():
    print("Bienvenido al Festival de Música")
    num_artistas = int(input("¿Cuántos artistas participarán en el festival?"))
    lista_artistas = []

    for i in range(num_artistas):
        print(f"\n Artista numero {i+1}")
        opcion = input("Tipo de artista (Cantante, DJ o Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1-100): "))

        if opcion == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif opcion == "dj":
            estilo = input("Estilo musical: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        elif opcion == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print("Tipo de artista no válido. Intenta de nuevo.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)

if __name__ == "__main__":
    main()