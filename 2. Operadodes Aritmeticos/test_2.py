'''Ejercicio 2
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso total de toda la venta.

Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, se debe sumar.

'''
peso_payaso = 112
peso_muneca = 75
#cantidad_payaso = input('cantdad de payasos')
#cantidad_muneca = input('cantidad de muñecas')
cantidad_payaso = 23
cantidad_muneca = 54

pesogramos = ((peso_payaso * cantidad_payaso)+(peso_muneca * cantidad_muneca))

print("el peso tota en gramos es: ",pesogramos)