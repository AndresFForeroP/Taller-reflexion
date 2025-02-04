'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: ordenar numeros con short()
'''
numeros = [3,8,1,7,2]
numeros.sort()
print(numeros)
while True:
    try:
        orden = int(input(""" ORDEN
        1.ascendente
        2.decreciente
        Ingrese el numero de la opcion """))
    except Exception:
        print('Ingresa solo numeros')
    if orden == 2:
        numeros.sort(reverse=True)
        break
    elif orden == 1:
        break
print(numeros)