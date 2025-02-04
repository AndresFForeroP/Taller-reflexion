'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se remueven datos todos de las listas con clear()
'''
def limpiar_lista(lista):
    lista.clear()
lista = [1,2,'3','hola mundo','comunismo',3.1415]
print(lista)
limpiar_lista(lista)
print(lista)