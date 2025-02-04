'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: contar cuantas veces esta el elemento en la lista count()
'''
frutas = ['manzana','pera','manzana','naranja','manzana']
fruta = input('Ingrese la fruta que desea saber cuantas veces esta en la lista')
while fruta.isalpha() == False:
    fruta = input('Ningua fruta lleva numeros,ingrese el nombre de la fruta')
if frutas.count(fruta) > 0:
    print(f'La {frutas} esta {frutas.count(fruta)} ')
else:
    print('No esta en la lista la fruta')