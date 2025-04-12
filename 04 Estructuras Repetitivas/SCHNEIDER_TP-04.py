#EJERCICIO 1
#for num in range (101):
#    print (num)

#EJERCICIO 2

#numero = (input("ingrese un numero entero: "))
#if numero[0] == "-":
#    cantidad_digitos = len(numero) - 1
#else:
#    cantidad_digitos = len(numero)
#print (f"El numero tiene {cantidad_digitos} digitos.")

#EJERCICIO 3

#numero_uno= int(input("Ingrese el primer numero: "))
#numero_dos= int(input("Ingrese el segundo numero: "))
#suma = 0
#for i in range(numero_uno + 1, numero_dos):
#    suma += i
#print(f"La suma de los numeros {numero_uno} y numero {numero_dos} es: {suma}")

#EJERCICIO 4
"""
total=0
while True:
    numero_usuario=int(input("Ingrese un numero (0 para detenerse):"))
    if numero_usuario == 0:
     break
    total += numero_usuario

print(f"El total acumulado es {total}")
"""

#EJERCICIO 5
"""
import random
numero_aleatorio = random.randint(0,9)
intentos=0
while True:
    numero_usuario = int(input("Adivina un numero entre 0 y 9, introduce tu primer intento: "))
    intentos += 1

    if intentos == numero_usuario:
        print(f"Correcto! el numero era {numero_aleatorio}.")
        print(f"Lo adivinaste en {intentos} intentos!.")
    else:
        print("Incorrecto! intenta otra vez: ")
                         """

#EJERCICIO 6
#for numero in range (100,-1,-1):
#    if numero % 2 == 0:
#        print(numero)

#EJERCICIO 7
#numero_usuario=int(input("Ingrese un numero entero positivo: "))
#suma = 0
#for i in range(0,numero_usuario + 1):
#    suma = suma + i

#print(f"La suma desde 0 hasta {numero_usuario} es {suma}! ")

#EJERCICIO 8:
"""
par=0
impar=0
positivo=0
negativo=0

for i in range(100):
    numero_usuario=int(input("Ingrese los numeros: "))

    if numero_usuario % 2 == 0:
        par= par + 1
    else:
        impar= impar + 1

    if numero_usuario > 0:
        positivo = positivo + 1
    elif numero_usuario < 0:
        negativo = negativo + 1


print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")
print(f"Numeros positivos: {positivo}")
print(f"Numeros negativos: {negativo}")
"""

#EJERCICIO 9
#suma=0
#for i in range(100):
#    numero = int(input("Ingrese numeros:"))
#    suma = suma + numero
#media = suma / 100
#print(f"La media de los numeros ingresados es : {media}")

#EJERCICIO 10
#numero_usuario=(input("Ingrese un numero: "))
#numero_invertido = numero_usuario [::-1]
#print(f"El numero original es: {numero_usuario}")
#print(f"El numero original invertido es: {numero_invertido}")




