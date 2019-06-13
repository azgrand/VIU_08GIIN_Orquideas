"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from simulacion import simular_lotes
from simulacion import simular_dias

# El modulo de SIMULAR para montar el pequeño menu que utilizamos para las llamadas. 

def load_simular(dicLotes, dicInvernaderos):
    os.system('cls')
    print("Modulo Simulación")
    print("")
    print("  1 - Simular Lotes")
    print("  2 - Simular Dias")
    print("")
    print("  0 - Salir")
    print("-----------------")
    menu = validar_entero("Opcion:")
    
    while(menu > 3): 
        print("El valor introducido no pertenece al pedido")
        menu = validar_entero("Opcion:")
         
    if menu == 1:
        simular_lotes(dicLotes, dicInvernaderos)
        load_simular(dicLotes, dicInvernaderos)
    elif menu == 2:
        # Pedimos los dias antes y lo enviamos en al funcion
        dias = validar_entero("Dias a simular:")
        dicLotes = simular_dias(dicLotes, dias)
        load_simular(dicLotes, dicInvernaderos)
    else:
         print("")