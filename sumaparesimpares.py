sumpares=0
sumimpares=0
num=int(input("Ingresa un numero: "))
for i in range(1,num+1):
    if i %2 == 0:
        sumpares=sumpares+i
    else:
        sumimpares=sumimpares+i
print("La suma de numeros pares es: ", sumpares)
print("La suma de los numeros impares es: ", sumimpares)