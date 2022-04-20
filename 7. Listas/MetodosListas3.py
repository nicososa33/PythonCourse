lista = ["python", 4, "rene", "nicolas", 12]

print(lista[3]) # busco el elemento a modificar con los []

lista[3]="Nicolas" #elijo el elemento a modificar y cambio 
print(lista)

#-------------------------------------------------------------------------------------

lista.pop() #quita el ultimo valor de la lista y se puede usar varias veces
print(lista)
lista.pop()
print(lista)

#--------------------------------------------------------------------------------------

lista.remove("python") # elimina de la lista el valor que elegimos
print(lista)