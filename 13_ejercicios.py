#Esta funcion encuentra el valor absoluto de cualquier numero
def val_absoluto(a):
    if(a < 0):
        return val_absoluto(a + 1) + 1
    elif(a > 0):
        return val_absoluto(a - 1) + 1
    else:
        return 0

#Esta funcion encuentra el factorial de un numero n
def facorial(n):
    if(n == 0):
        return 1
    else:
        return n * facorial(n-1)

#Esta funcion encuentra el enesimo numero de la seria de fibonacci
def fibonacci(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Esta funcion encuentra la potencia de un numero n elevado a la m
def potencia(n, m):
    if(m == 0):
        return 1
    else:
        return n * potencia(n, m-1)

#Esta funcion permite encontrar la multiplicacion de dos numeros por medio de la suma
def multi_sumando(n, m):
    if(m == 0):
        return 0
    else:
        return n + multi_sumando(n, m-1)

#Esta funcion permite endontrar la division de dos numeros por medio de la resta
def div_restando(n, m):
    if(n <= m):
        return 0
    else:
        return div_restando(n - m, m) + 1

#Esta funcion permite saber si una palabra es palindroma o no
def palindromo(palabra):
    if(palabra[0] != palabra[-1]):
        return False
    elif(len(palabra) < 2):
        return True
    else:
        return palindromo(palabra[1:-1])

#Esta funcion permite encontrar el maximo comun divisor de 2 numeros
def MCD(a,b):
    if(b == 0):
        return a
    else:
        return MCD(b,a%b)

#Esta funcion permite encontrar la suma de los digitos de un numero
def suma_numero(n):
    if(n == 0):
        return n
    else:
        return n%10 + suma_numero(n/10)

#Esta funcion permite encontrar el binario de un numero
def abase2(n,b):
	if (n==0):
	   return""
	elif (n<2):
	   return str(n%b)
	elif (n>=2):
	   return abase2(n/b,b) + str(n%b)


#Funcion que permite invertir una lista
def invertir(lista):
    if(len(lista) == 1):
        return lista
    else:
        return lista[len(lista)- 1:] + invertir(lista[:len(lista) - 1])

#Funcion  que permite encontrar el numero menor de una lista
def menor_lista(lista):
    if(len(lista) == 1):
        return lista[0]
    elif(lista[len(lista) - 1] > lista[len(lista) - 2]):
        return menor_lista(lista[:len(lista) - 1])
    else:
        return menor_lista(lista[::-1])

def menor_listas(lista):
    if(len(lista) == 1):
        return lista
    else:
        return menor_lista(lista[len(lista) - 1:]) + menor_lista(lista[len(lista) - 1:])



