'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se usa el extend en las listas
'''
import modules.Fgenerales as fg
numeros = [1,2,3]
partes = []
nums = input('ingrese 3 numeros enteros separados por , ')
nums = nums.split(',')
for i in nums:
    partes.append(int(i))
numeros.extend(partes)
fg.limpiar_p()
print(partes)
print(numeros)