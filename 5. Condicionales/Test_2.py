'''
Ejercicio 2
Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
'''

numero = int(input("ingresa numero entero: "))

if numero > 0:
    print("el valor absoluto de {} es: {}".format(numero, numero))
else:
    print("el valor absoluto de {} es: ".format(numero), abs(numero)) 
    #ABS realiza la multiplicacion de un numero negativo * -1