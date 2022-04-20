from pickle import DICT


diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 6 : 7}

print (diccionario.values())

#diccionario.pop (3) ELIJO VALOR A BORRAR

#diccionario.clear() BORRA TODO EL diccionario

#diccionario.get(2) #devuelve el valor
#print(diccionario.get(2))

#diccionario.setdefault #recibe el valor de la key y su valor

diccionario.update(diccionario2) # CREA UN SOLO DICCIONARIO, LOS JUNTA

print(diccionario)
