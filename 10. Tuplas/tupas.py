# una tupla sus datos no se puede modificar

tupla = (1 , 2 , 3 , 4 , 5 )
tupla2 = (6 , 7 , 8 , 9 , 10)

print(tupla)
print(type(tupla))
print(tupla[2])
print(tupla[0 : 3])
print(tupla + tupla2)

tupla[2] = 10 #las tuplas no pueden modiciar su valor por eso esto falla
print(tupla)