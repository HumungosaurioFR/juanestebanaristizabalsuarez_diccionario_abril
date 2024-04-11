mi_diccionario = {}

import os

despacho = 0
sw = True
def fnt_limpiar():
    os.system('cls')
    print('NombrE: Juan Esteban Aristizábal Suárez')
    print('Sede: Universidad Católica Luis Amigó')
    print('Fecha: 09/04/2024')
    print('')

def fnt_agregar(diccionario, nombre, direccion, contacto, sexo, descripcion_hogar, no_producto, referencia, cantidad ):
    global despacho
    if nombre == '' and direccion == '' and contacto == '' and sexo == '' and descripcion_hogar == '' and no_producto == '' and referencia == '' and cantidad == '':
        print('No se puede registrar un despacho sin datos')
        enter = input('<ENTER>')
    else:
        diccionario[despacho] = nombre, direccion, contacto, sexo, descripcion_hogar, no_producto, referencia, cantidad, despacho
        despacho += 1
        print('Datos registrados correctamente')
        enter = input('<ENTER>')
    
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        nombre = input('Nombre: ')
        direccion = input('Direccion: ')
        contacto = input('Contacto: ')
        sexo = input('Sexo: ')
        descripcion_hogar = input('Descripcion del hogar: ')
        no_producto = input('Nombre del Producto: ')
        referencia = input('Referencia: ')
        cantidad = int(input('Cantidad: '))
        
        fnt_agregar(mi_diccionario, nombre, direccion, contacto, sexo, descripcion_hogar, no_producto, referencia, cantidad)
    if opcion == '2':
        fnt_limpiar()
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar')
    if opcion == '3':
        sw = False
            
while sw == True:
    fnt_limpiar()
    opcion = input(' <<< Menú de opciones >>>\n\n1. Registrar\n2. Mostrar\n3. Salir\n\n-> ')
    fnt_selector(opcion)