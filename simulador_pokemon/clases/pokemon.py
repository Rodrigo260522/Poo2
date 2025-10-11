class Pokemon:
    contador_pokemones = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.contador_pokemones += 1
        print(f"{self.nombre} ha sido capturado")

    def __del__(self):
        print(f"{self.nombre} ha sido liberado")
        Pokemon.contador_pokemones -= 1

    def entrenar(self, ataque=0, defensa=0, salud=0):
        self.nivel += 1
        self.ataque += ataque
        self.defensa += defensa
        self.salud += salud
        print(f"{self.nombre} subio de nivel")

    def mostrar_info(self):
        print(f"{self.nombre} / Tipo: {self.tipo} / Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque} / Defensa: {self.defensa} / Salud: {self.salud}")

    def atacar(self, objetivo):
        daño = self.ataque - objetivo.defensa
        if daño < 0:
            daño = 0
        objetivo.salud -= daño
        print(f"{self.nombre} atacó a {objetivo.nombre} causando {daño} de daño")
        if objetivo.salud <= 0:
            print(f"{objetivo.nombre} ha sido derrotado")

    @classmethod
    def total_pokemones(cls):
        print(f"Hay {cls.contador_pokemones} Pokemones registrados")