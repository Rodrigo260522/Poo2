num=int(input("Ingresa un numero: "))
invertido=0
while num != 0:
    dig=num%10
    invertido=invertido*10+dig
    num=num//10
print("El numero invertido es: ", invertido)