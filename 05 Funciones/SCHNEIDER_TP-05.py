#Ejercicio 1
#def imprimir_hola_mundo():
#    print("Hola Mundo!")

#imprimir_hola_mundo()

#Ejercicio 2
#def saludar_usuario(nombre):
#    return f"Hola {nombre}, que bueno saber de vos!"

#saludo = input("Ingrese su nombre:")
#print(saludar_usuario(saludo))

#Ejercicio 3
#def informacion_personal(nombre, apellido, edad, residencia):
#    return f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

#nombre_usuario = input("Ingrese su nombre:")
#apellido_usuario = input("Ingrese su apellido:")
#edad_usuario = input("Ingrese su edad:")
#residencia_usuario = input("Ingrese su residencia:")

#print (informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario))

#Ejercicio 4
#defino funciones
#import math
#def calcular_area_circulo(radio):
#    return math.pi * radio ** 2
#def calcular_perimetro_circulo(radio):
#    return 2 * math.pi * radio

#programa principal
#radio = float(input("Ingrese el radio del circulo: "))
#area_usuario = calcular_area_circulo(radio)
#perimetro_usuario =calcular_perimetro_circulo (radio)
#print (f"El area del circulo es: {area_usuario} y el perimetro es: {perimetro_usuario}")

#Ejercicio 5 
#defino funciones
#def segungos_a_horas(segundos):
#    horas = segundos / 3600
#    return horas

#segundos=int(input("Ingrese la cantidad de segundos: "))
#horas=segungos_a_horas(segundos)
#print(f"La cantidad de horas que representan {segundos} segundos es: {horas}")

#Ejercicio 6:
#def tabla_multiplicar(numero):
#    for i in range(1,11):
#        resultado = numero * i
#        print(f"{numero} x {i} = {resultado}")
 
#numero=int(input("Ingrese el numero: "))
#tabla_multiplicar(numero)

#Ejercicio 7
"""
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    if b != 0:
       division=a/b
    else:
      print("ERROR. No se puede dividir por 0")
    return(suma, resta, multiplicacion,division)

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
resultado = operaciones_basicas(a,b)

print("Resultado de operaciones:")
print(f"Suma {a} + {b} = {resultado[0]}")
print(f"Resta: {a} - {b} = {resultado[1]}")
print(f"Multiplicacion: {a} x {b} = {resultado[2]}")
print(f"Division: {a} / {b} = {resultado[3]}")
"""

#Ejercicio 8
#def calcular_imc(peso,altura):
#    return peso / (altura ** 2)

#a= float(input("Ingrese su peso: "))
#b=float(input("Ingrese su altura: "))
#imc=calcular_imc(a,b)

#print(f"Su IMC es: {imc}")

#Ejecicio 9
#def celsius_a_fahrenheit(celsius):
#    return celsius *9 / 5 + 32

#celsius=float(input("Ingrese los grados celsius: "))
#fahrenheit=celsius_a_fahrenheit(celsius)

#print(f"{celsius} grados celsius en grados Fahrenheit equivale a: {fahrenheit}")

#Ejercicio 10
#def calcular_promedio(a,b,c):
#    return (a + b + c)/ 3

#a=float(input("Ingrese el primer numero: "))
#b=float(input("ingrese el segundo numero: "))
#c=float(input("Ingrese el tercer numero: "))

#promedio=calcular_promedio(a,b,c)
#print(f"El promedio de {a}, {b} y {c} es: {promedio}")




   


