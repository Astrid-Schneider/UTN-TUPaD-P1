#Ejercicio 1
#def factorial(n):
    #if n == 0:
        #return 1
    #else:
        #recur = factorial (n - 1)
        #resultado = n * recur
        #return resultado 
#numero_usuario = int(input("Ingrese un numero: "))
#resultado_final = factorial (numero_usuario)
#print (f"El factorial de {numero_usuario} es: {resultado_final}")

#Ejercicio 2

#def fibonacci (n):
    #if n == 0 or n == 1:      
        #return n
    #else:    
        #return fibonacci (n - 1) + fibonacci (n - 2)
#print (fibonacci(10)

#Ejercicio 3
#def potencia(base,exponente):
    #if exponente == 0:
        #return 1
    #else:
        #return base * potencia (base, exponente - 1)
#print(potencia(5, 0))

#Ejercicio 4

#def a_binario (n):
    #if n == 0:
        #return ""
    #else:
        #return a_binario (n // 2) + str(n % 2)
#numero = 0
#resultado = a_binario(numero)
#print ("El numero ", numero, "en binario es: ", resultado or "0") 

#ejercicio 5

#def es_palindromo(palabra):
    #if len(palabra) <= 1:
        #return True
    #if palabra[0] != palabra [-1]:
        #return False
    #return es_palindromo(palabra[1:-1])
#print (es_palindromo ("oso"))
#print (es_palindromo ("hola"))

#ejercicio 6

#def suma_digitos(n):
    #if n < 10:
        #return n
    #else:
        #return (n % 10) + suma_digitos(n // 10)
#    
#print(suma_digitos(1234))

#ejercicio 7 
#def contar_bloques(n):
    #if n == 1:
        #return 1
    #else:
        #return n + contar_bloques (n - 1)
#print(contar_bloques(4))

#Ejercicio 8 
#def contar_digito(numero, digito):
    #if numero == 0:
        #return 0
    #if numero % 10 == digito:
        #return 1  + contar_digito(numero // 10, digito)
    #else:
        #return contar_digito(numero // 10, digito)
#print(contar_digito(101010,1))
    

    