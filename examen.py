# calificaciones.py

def leer_matriz(estudiantes, materias):
    matriz = []
    for e in range(estudiantes):
        fila = []
        print(f"\n--- Estudiante {e+1} ---")
        for m in range(materias):
            while True:
                try:
                    valor = float(input(f"Calificacion en materia {m+1} (0-100): "))
                    if 0 <= valor <= 100:
                        fila.append(valor)
                        break
                    else:
                        print("La calificacion debe estar entre 0 y 100.")
                except ValueError:
                    print("Entrada invalida, ingresa un numero.")
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    print("\nMatriz de calificaciones:")
    for fila in matriz:
        print(" ".join(f"{elem:6.2f}" for elem in fila))

def promedios_estudiantes(matriz):
    print("\nPromedio por estudiante:")
    for i, fila in enumerate(matriz, start=1):
        promedio = sum(fila) / len(fila)
        print(f"Estudiante {i}: {promedio:.2f}")

def promedios_materias(matriz):
    materias = len(matriz[0])
    print("\nPromedio por materia:")
    for m in range(materias):
        suma = 0
        for fila in matriz:
            suma += fila[m]
        promedio = suma / len(matriz)
        print(f"Materia {m+1}: {promedio:.2f}")

def max_min(matriz):
    maximo = matriz[0][0]
    minimo = matriz[0][0]
    for fila in matriz:
        for valor in fila:
            if valor > maximo:
                maximo = valor
            if valor < minimo:
                minimo = valor
    print(f"\nCalificacion mas alta: {maximo}")
    print(f"Calificacion mas baja: {minimo}")

estudiantes = int(input("Numero de estudiantes: "))
materias = int(input("Numero de materias: "))

matriz = leer_matriz(estudiantes, materias)

imprimir_matriz(matriz)
promedios_estudiantes(matriz)
promedios_materias(matriz)
max_min(matriz)