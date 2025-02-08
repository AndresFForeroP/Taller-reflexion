'''
Autor: Andres Forero
Fecha: 08/02/2025
Descripcion: uso for y if con listas
'''
def clasificar_num():
    for i in numeros:
        if i % 2 == 0:
            print(f'El numero {i} es par')
        else:
            print(f'El numero {i} es impar')
numeros = []
for i in range(0,5): 
    while True:
        try:
            num = int(input(f'Ingresa el numero #{i+1} para agregar a la lista '))
        except Exception:
            print('Ingrese solo numeros enteros')
        else:
            break
    numeros.append(num)
clasificar_num()