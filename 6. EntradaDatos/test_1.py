'''Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''

from math import sqrt #importar libreria matematica con funcion de raiz cuadrada

A = int(input('Numero A: '))
B = int(input('Numero B: '))
C = int(input('Numero C: '))

x1 = 0
x2 = 0

if ((B**2)-(4*A*C)) < 0:
    print('no se puede sacar la raiz cuadrada si el valor es negativo')
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("la solucoin es: \nx1=",x1, "\nx2=",x2) 
    
    
#---------------------------------------------------------------------------------------------------------------------------------

