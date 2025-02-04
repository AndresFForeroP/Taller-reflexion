'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se remueven datos de las listas con pop()
'''
numeros = [1,2,3,4,5]
menu = 1
while menu != 3:
    print("""       MENU 
1.Hacer pop sin indice (pop al final)
2.Hacer pop con indice
3.Salir
 """)
    try:
        menu = int(input('Ingrese un numero del menu (1-3) '))
    except Exception:
        print('solo ingrese numeros segun la opcion del menu')
    match menu:
        case 1:
            print(f'Se eliminio {numeros.pop()} de la lista')
            print(numeros)
        case 2:
            indice = int(input('Ingresa el indice que desea eliminar de la lista '))
            print(numeros.pop(indice))
            print(numeros)
