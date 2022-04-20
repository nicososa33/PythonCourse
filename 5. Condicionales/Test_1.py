'''Ejercicios
Ejercicio 1
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

'''

letra = input("ingresa una letra: ") # la mejor opcion es usar el IN 

'''
if letra.lower () == "a":
    print("es una vocal")
else:
    if letra.lower () == "e":
        print("es una vocal")
    else:
        if letra.lower () == "i":
            print("es una vocal")
        else:
            if letra.lower () == "o":
                print("es una vocal")
            else: 
                if letra.lower () == "u":
                    print("es una vocal")
                else: 
                    print("No es vocal")
'''

if letra.lower () in "aeiou":
    print("es vocal")
else:
    print("No es vocal")
