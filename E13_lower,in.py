'''
Autor: Andres Forero
Fecha: 08/02/2025
Descripcion: uso de lower y de in en diccionarios 
'''
import modules.Fgenerales as fg
def agregar_contactos():
    nombre = input('ingrese el nombre del contacto ').lower()
    while True:
        try:
            telefono = int(input(f'Ingrese el numero de telefono de {nombre} ')) 
        except Exception:
            print('ERROR,solo ingrese numeros')
        else:
            break
    nContacto = {nombre,telefono}
    contactos.append(nContacto)
    print('Contacto agregado con exito') 
def mostrar_contactos():
    filtro = input('ingrese una parte del nombre del contacto o el nombre del contacto que desea buscar ').lower()
    for key,value in contactos:
        if filtro in key:
            print(f'{key}: {value}')
contactos = []
while True:
    fg.limpiar_p()
    try:
        menu = int(input("""   MENU
1.Agregar contacto
2.Buscar contacto
9.Salir
Ingrese un numero segun la opcion del menu que desea realizar """))
    except Exception:
        print('El menu solo permite ingresar numeros enteros')
    else:
        match menu:
            case 1:
                fg.limpiar_p()
                agregar_contactos()
                fg.pausar_p()
            case 2:
                fg.limpiar_p()
                mostrar_contactos()
                fg.pausar_p()