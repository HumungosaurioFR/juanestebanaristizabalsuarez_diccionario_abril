#una transportadora requiere el desarrollo de una app que permita llevar un registro de los despachos de sus vehiculos teniendo encuenta lo siguiente: placa de vehiculo, descripcion, nombre del conductor, contacto del conductor, ruta y descripcion de la carga; el númeor del despacho se crea de forma automática es decir, una variable que se genera de forma automática es decir, se auto incrementa. Dicha informacion debe quedar registrada en un diccionario.
#El sistema debe realizar: Registro de salidas y mostrar salida 

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

def fnt_agregar(diccionario, placa, descripcion, nombre, contacto, ruta, carga):
    global despacho
    if placa == '' and descripcion == '' and nombre == '' and contacto == '' and ruta == '' and carga == '':
        print('No se puede registrar un despacho sin datos')
        enter = input('<ENTER>')
    else:
        diccionario[despacho] = placa, descripcion, nombre, contacto, ruta, carga, despacho
        despacho += 1
        print('Datos registrados correctamente')
        enter = input('<ENTER>')
    
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
        global despacho
        placa = input('Placa del vehiculo: ')
        descripcion = input('Descripcion del vehiculo: ')
        nombre = input('Nombre del conductor: ')
        contacto = input('Contacto del conductor: ')
        ruta = input('Ruta: ')
        carga = input('Descripcion de la carga: \n')
        enter = input('<ENTER>')
        fnt_agregar(mi_diccionario, placa, descripcion, nombre, contacto, ruta, carga)
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
        