'''
Autor: Andres Forero
Fecha: 19/02/2025
Descripcion: uso de match
'''
import modules.Fgenerales as fg
while opcion != 1 and opcion != 2:
    opcion = fg.validartipo(1,'Ingrese 1 o 2')
match opcion:
    case 1:
        print('ingresaste la opcion 1')
    case 2:
        print('opcion invalida')