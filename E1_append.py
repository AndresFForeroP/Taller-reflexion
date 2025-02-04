'''
Autor: Andres Forero
Fecha: 03/02/2025
Descripcion: mostrar como se crean y se agregan datos a las listas
'''
import modules.Fgenerales as fg
def mostrarfrutas(frutas):
    for i in frutas:
        print(i,end=('\n'))
frutas = []
for i in range(0,3):
    while True:
        fg.limpiar_p
        print("""      🍇 🍈 🍉 🍊 🍍 🍏 🍐 🍒""")
        fruta = input(f'Ingrese la fruta # {i +1} para agregar a la lista ')
        if fruta.isalpha() == True:
            frutas.append(fruta)
            break
        else:
            print('ninguna fruta lleva un numeros')
print(frutas)
mostrarfrutas(frutas)