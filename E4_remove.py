'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se remueven datos de las listas con remove()
'''
animales = ['perro','gato','elefante','tigre']
print(animales)
while True:
    nombrea = input('ingrese el nombre del animal que desea eliminar de la lista ')
    nombrea = nombrea.lower()
    if nombrea not in animales:
        print('El animal no esta en la lista')
    else:
        print(f'{nombrea} eliminado con exito')
        animales.remove(nombrea)
        break
print(animales)