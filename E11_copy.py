'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: copiar lista con copy()
'''
lista_original = [1,4,5,6,7]
lista_copia = lista_original.copy()
lista_original[2] = 'carro'
print(f'la lista copia es {lista_original}')
print(f'la lista copia es {lista_copia}')