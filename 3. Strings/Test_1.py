'''Ejercicio 1
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

Ejercicio 2
Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r'''

persona = 'Te quiero solo como amigo'
print(persona[0:2])
print(persona[-3:])
print(persona[: : 2])
print(persona[: : -1])
print(persona + persona[::-1])


#------------------------------------------------------------------

palabra = "separado"
print(palabra)
reemplazar = palabra.replace("",",")
print(reemplazar)


