numero = int(input("Ingresa un numero: "))
contador=0
if numero==0:
    contador=1
else:
    numero=int(numero)
    if numero<0:
        numero=-numero 
    while numero > 0:
        numero=numero // 10  
        contador=contador+1          
print("El numero tiene" , contador, "digitos")