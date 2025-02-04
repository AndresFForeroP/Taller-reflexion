'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se usa el insert para agregar cosas a las
listas en la posicion que queramos
'''
lenguajes = ['python','c','java']
while True:
    nuevoL = input('Ingrese el nuevo lenguaje de programacion ')
    if nuevoL.isalpha() == False:
        print('Ningun lengujae de programacion tiene numeros ')
    else:
        break
nuevoL.lower()
if lenguajes.count(nuevoL) == 1 :
    print('El lenguaje ya esta en la lista')
else:
    lenguajes.insert(1,nuevoL)
print(lenguajes)
for i in lenguajes:
    print(i, end=('\n'))