'''
Autor: Andres Forero
Fecha: 19/02/2025
Descripcion: uso de match y de las listas 
'''
import modules.Fgenerales as fg
lista = []
menu = 1
menu_principal = """    MENU PRINCIPAL  
1. Agregar tarea
2. Mostrar tarea
3. Eliminar tarea
4. Salir
Ingrese un numero segun la opcion que deseas realizar
> """

while menu != 4:
    menu = fg.validartipo(1,menu_principal)
    match menu:
        case 1:
            tarea = input('ingrese el nombre de la tarea y su descripcion')
            lista.append(tarea)
        case 2:
            for tareas in lista:
                print(f'- {tareas}\n')
        case 3:
            for tareas in lista:
                print(f'- {tareas}\n')
            tarea = input('ingrese la tarea que desea eliminar')
            indice = 0
            for tareas in lista:
                if tareas == tarea:
                    lista.remove(indice)
                    print(f'{tarea} eliminada de la lista')
                indice += 1
print('Saliste de la lista ')