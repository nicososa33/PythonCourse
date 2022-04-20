'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]

print("valores actuales de la lista: ",lista)

pagina = int(input("ingrese numero de pagina: "))
ejercicio = int(input("ingrese el numero de ejercicio: "))

lista[0] = pagina
lista[1] = ejercicio

print(lista)