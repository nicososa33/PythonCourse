"""
Ejercicio 1
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

Ejercicio 2
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa
"""

meses = ('enero' , 'febrero' , 'marzo' , 'abril' , 'mayo' , 'junio' , 'julio' , 'agosto' , 'septiembre' , 'octubre' , 'noviembre' , 'diciembre')

OpcionMes = int(input("ingrese su mes: "))

print("tu mes es: ", meses[OpcionMes-1])