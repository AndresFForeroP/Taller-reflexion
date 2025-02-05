'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: uso de lower y de in en diccionarios 
'''
def agregar_contactos():
    nombre = input('ingrese el nombre del contacto ')
    while True:
        try:
            telefono = int(input(f'Ingrese el numero de telefono de {nombre} ')) 
        except Exception:
            print('ERROR,solo ingrese numeros')
        else:
            break
    nContacto = {nombre,telefono}
    contactos.append(nContacto)
    print(contactos)    
contactos = []
agregar_contactos()
print('hola')