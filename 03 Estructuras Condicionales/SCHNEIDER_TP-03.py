# EJERCICIO 1
#edad = int(input("Indique su edad:"))
#if edad > 18:
#    print ("Eres mayor de edad")
#else:
#    print ("Eres menor de edad")

# EJERCICIO 2
#nota= int(input("Indique su nota, por favor:"))
#if nota >= 6:
#    print ("Esta aprobado!")
#else:
#    print("Desaprobado")

# EJERCICIO 3
#numero= int(input("Por favor ingrese un numero:"))
#if numero % 2 == 0:
#    print("Ingreso un numero par!")
#else:
#    print("Ingreso un numero impar!")

#EJERCICIO 4
#edad=int(input("Ingrese su edad, por favor:"))
#if edad < 12:
#    print ("Es un niño!")
#elif edad >= 12 and edad < 18:
#    print ("Es adolescente!")
#elif edad >= 18 and edad < 30:
#    print("Es adulto/a joven!")
#else:
#    print("Es adulto/a")

#EJERCICIO 5
#contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres:")
#if len(contraseña) >= 8 and len(contraseña) <= 14:
#    print("Contraseña correcta")
#else:
#    print("Por favor ingrese una contraseña entre 8 y 14 caracteres.")

#EJERCICIO 6
#import random
#from statistics import mode, median, mean
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#moda= mode (numeros_aleatorios)
#mediana= median (numeros_aleatorios)
#media = mean(numeros_aleatorios)
#print(f"Numeros aleatorios:{numeros_aleatorios}")
#print(f"moda:{moda}")
#print(f"Mediana:{mediana}")
#print(f"Media:{media}")

#if media > mediana > moda:
#    print("Sesgo positivo")
#elif media < mediana < moda:
#    print("Sesgo negativo")
#else:
#    ("sin Sesgo")

# EJERCICIO 7 
#palabra = input("Ingrese una palabra o frase:")
#if palabra [-1] in "aeiou":
#    palabra = palabra + "!"
#print (palabra)

#EJERCICIO 8
#nombre=input("Por favor ingrese su nombre:")
#print("Elija una opcion:")
#print("1 - Si desea su nombre en mayuscula")
#print("2 - Si quiere su nombre en minuscula")
#print("3 - Si quiere su nombre con la primera letra mayuscula")
#opcion= input ("Elija opcion 1, 2 o 3:")

#if opcion == "1":
#    respuesta=nombre.upper()
#elif opcion == "2":
#    respuesta=nombre.lower()
#elif opcion == "3":
#    respuesta=nombre.title
#else:
#    respuesta = "Opcion no valida."
#print("respuesta:", respuesta)

#EJERCICIO 9
#magnitud=float(input("Ingrese la magnitud del terremoto segun escala de Richter:"))

#if magnitud < 3 :
#    categoria = "Muy leve, imperceptible"
#elif magnitud >=4 and magnitud < 5:
#    categoria = "Moderado, sentido por personas pero generalmente no causa daños"
#elif magnitud >=5 and magnitud < 6:
#    categoria = "Fuerte, puede causar daños en estructuras debiles"
#elif magnitud >= 6 and magnitud < 7:
#    categoria = "Muy fuerte, puede causar daños significativos"
#else:
#    categoria = "Extremo, puede causar daños graves a gran escala"

#print(f"El terremoto con magnitud {magnitud} es: {categoria}")

#EJERCICIO 10
#hemisferio = input("En qué hemisferio te encuentras? (n para norte, s para sur): ")
#mes = int(input ("Que mes del año es? (1 para Enero, 2 Febrero, 3 Marzo, 4 Abril, 5 Mayo, 6 Junio, 7 Julio, 8 Agosto, 9 Septiembre, 10 Octubre, 11 Noviembre y 12 Diciembre):"))
#dia = int(input("Qué día del mes es? (1 al 31 dependiendo del mes): "))

#if hemisferio == "n":
#    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
#        estacion = "Invierno"
#    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes ==5) or (mes == 6 and dia <= 20):
#        estacion = "Primavera"
#    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
#        estacion = "Verano"
#    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
#        estacion = "Otoño"

#elif hemisferio == "s":
#    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
#        estacion = "Verano"
#    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
#        estacion = "Otoño"
#    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
#        estacion = "Invierno"
#    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
#        estacion = "Primavera"

#else:
#    estacion = "Hemisferio no valido"

#print(f"Segun la fecha te encuentras en la estacion: {estacion}")
    

