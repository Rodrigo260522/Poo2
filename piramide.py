alt=int(input("Ingresa la altura: "))
for i in range (1,alt+1):
    espacios = " " * (alt - i)         
    asteriscos = "*" * (2 * i - 1)   
    print(espacios + asteriscos)