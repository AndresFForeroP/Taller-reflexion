'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar el indice de una variable de la lista usando index()
'''
colores = ['rojo','azul','verde','amarrilo','negro']
color = input('Ingresa el color del cual quieres saber su poscicion ').lower()
while color.isalpha == False:
    color = input('Ingresa el color del cual quieres saber su poscicion ').lower()
try:
    ind = colores.index(color)
except Exception:
    print('El color no esta en la lista')
else:
    print(f'El indice del color {color} es el {ind}')
    print(colores)