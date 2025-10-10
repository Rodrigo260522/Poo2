class Planeta:
    total_planetas = 0

    def __init__(self, nombre, distancia_km):
        self.nombre = nombre
        self.distancia_km = distancia_km
        Planeta.total_planetas += 1
        print(f"Planeta registrado: {self.nombre}")

    def __del__(self):
        print(f"Planeta eliminado: {self.nombre}")
        Planeta.total_planetas -= 1

    @classmethod
    def contar_planetas(cls):
        return cls.total_planetas


class NaveEspacial:
    total_naves = 0

    def __init__(self, nombre, velocidad_kmh, *misiones, **recursos):
        self.nombre = nombre
        self.velocidad_kmh = velocidad_kmh
        self.destino = None
        self.misiones = misiones
        self.recursos = recursos
        NaveEspacial.total_naves += 1
        print(f"Nave registrada: {self.nombre}")

    def __del__(self):
        print(f"Nave destruida: {self.nombre}")
        NaveEspacial.total_naves -= 1

    @classmethod
    def contar_naves(cls):
        return cls.total_naves

    def asignar_destino(self, planeta):
        self.destino = planeta
        print(f"Destino asignado a {self.nombre}: {planeta.nombre}")

    def calcular_tiempo_viaje(self):
        if self.destino:
            horas = self.destino.distancia_km / self.velocidad_kmh
            print(f"Tiempo estimado de viaje: {horas:.2f} horas")
            return horas
        else:
            print("No se ha asignado destino.")
            return None

    def mostrar_info(self):
        print(f"\n Nave: {self.nombre}")
        print(f"Velocidad: {self.velocidad_kmh} km/h")
        if self.destino:
            print(f"Destino: {self.destino.nombre} ({self.destino.distancia_km} km)")
        else:
            print("Destino: No asignado")
        print(f"Misiones: {', '.join(self.misiones) if self.misiones else 'Ninguna'}")
        print(f"Recursos: {self.recursos if self.recursos else 'Ninguno'}")


planetas = []
naves = []

def menu():
    while True:
        print("\n Sistema de Viajes Interplanetarios")
        print("1. Registrar planeta")
        print("2. Registrar nave")
        print("3. Asignar destino")
        print("4. Calcular tiempo de viaje")
        print("5. Mostrar información")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del planeta: ")
            try:
                distancia = float(input("Distancia desde la Tierra (km): "))
                planetas.append(Planeta(nombre, distancia))
            except ValueError:
                print("[!] Ingresa un número válido para la distancia.")

        elif opcion == "2":
            nombre = input("Nombre de la nave: ")
            try:
                velocidad = float(input("Velocidad (km/h): "))
                misiones = input("Misiones (separadas por coma): ").split(",")
                recursos = {}
                while True:
                    clave = input("Nombre del recurso (o ENTER para terminar): ")
                    if clave == "":
                        break
                    valor = input(f"Cantidad de {clave}: ")
                    recursos[clave] = valor
                naves.append(NaveEspacial(nombre, velocidad, *misiones, **recursos))
            except ValueError:
                print("Ingresa un número válido para la velocidad.")

        elif opcion == "3":
            if not planetas or not naves:
                print("Registra al menos una nave y un planeta.")
                continue
            for i, nave in enumerate(naves):
                print(f"{i}. {nave.nombre}")
            try:
                idx_nave = int(input("Selecciona nave: "))
                for j, planeta in enumerate(planetas):
                    print(f"{j}. {planeta.nombre}")
                idx_planeta = int(input("Selecciona planeta: "))
                naves[idx_nave].asignar_destino(planetas[idx_planeta])
            except (ValueError, IndexError):
                print("Selección inválida.")

        elif opcion == "4":
            if not naves:
                print("No hay naves registradas.")
                continue
            for i, nave in enumerate(naves):
                print(f"{i}. {nave.nombre}")
            try:
                idx = int(input("Selecciona nave: "))
                naves[idx].calcular_tiempo_viaje()
            except (ValueError, IndexError):
                print("Selección inválida.")

        elif opcion == "5":
            print(f"\n Total de planetas: {Planeta.contar_planetas()}")
            print(f"Total de naves: {NaveEspacial.contar_naves()}")
            for nave in naves:
                nave.mostrar_info()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()