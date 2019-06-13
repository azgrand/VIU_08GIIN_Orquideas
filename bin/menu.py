"""
@author: Jon Lebrero Catalina
"""

import os

from lote import load_lote
from validador import validar_entero
from cargar import load_data
from guardar import save_data
from invernadero import load_invernadero
from informacion import load_informacion
from simular import load_simular

# Creamos los nombres de los ficheros, de tal forma que siempre sabemos cuales son los correctos.
strFileNameLote = "file_lote"
strFileNameInvernadero = "file_invernadero"

# El modulo de MENU es el mas completo de todos y el mas simple. Su funcion es realizar las llamadas necesarias y mantener
# los diccionarios acumulados en todo momento, de tal forma, que hasta que no salgamos, Lotes e Invernadero estaran accesibles.

def load_menu(dicLotes, dicInvernaderos):
    os.system('cls')
    print("--- Orquideas ---")
    print("")
    print("  1 - Lotes de Orquídeas")
    print("  2 - Invernaderos")
    print("  3 - Simulación")
    print("  4 - Información del sistema")
    print("  5 - Cargar datos")
    print("  6 - Guardar datos")
    print("")
    print("  0 - Salir")
    print("-----------------")
    menu = validar_entero("Opcion:")

    while(menu > 6): 
        print("El valor introducido no pertenece al pedido")
        menu = validar_entero("Opcion:")
         
    if menu == 1:
        # Carga de Lotes
        dicLotes = load_lote(dicLotes)
        load_menu(dicLotes, dicInvernaderos)
    elif menu == 2:
        # Carga de Invernaderos
         dicInvernaderos = load_invernadero(dicInvernaderos)
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 3:
        # Carga de Simulacion
         load_simular(dicLotes, dicInvernaderos)
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 4:
        # Carga de Informacion
         load_informacion(dicLotes, dicInvernaderos)
         load_menu(dicLotes, dicInvernaderos)
    elif menu == 5:
        # Carga de Carga Fichero
        dicLotes = load_data(dicLotes, strFileNameLote)
        dicInvernaderos = load_data(dicInvernaderos, strFileNameInvernadero)
        load_menu(dicLotes, dicInvernaderos)
    elif menu == 6:
        # Carga de Guardar Fichero
        dicLotes = save_data(strFileNameLote, dicLotes)
        dicInvernaderos = save_data(strFileNameInvernadero, dicInvernaderos)
        load_menu(dicLotes, dicInvernaderos)
    else:
         print("Gracias por usar Orquideas")