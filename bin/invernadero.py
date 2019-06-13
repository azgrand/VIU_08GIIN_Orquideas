"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from validador import validar_texto

def load_invernadero(dicInvernaderos):
    os.system('cls')
    print("Modulo Invernaderos")
    print("")
    # Guardamos el Invernadero y validamos si existe. El Invernadero tiene que ser UNICO
    strInvernadero = validar_texto("Invernadero:")
    while strInvernadero in dicInvernaderos:
        print("El Lote ya existe. Introduzca un nuevo invernadero")
        strInvernadero = validar_texto("dicInvernaderos:")
    # Pedimos el Clima, tiene que ser ANDES o COSTA. usamos Capitalize para convertir la primera en mayuscula  
    strClima = validar_texto("Clima(Andes o Costa):")
    while(strClima.capitalize() != 'Andes' and strClima.capitalize() != 'Costa'):
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_texto("Clima(Andes o Costa):")
    # Pedimos la capacidad del Invernadero    
    intCapacidad = validar_entero("Capacidad:")
    # Guardamos la infroamcion en Invernadero. Clima usamos lower y capitalize para formatearlo.
    dicInvernaderos[strInvernadero] = {
          'Clima':strClima.lower().capitalize(),
          'Capacidad':intCapacidad,
          'Lote:':""
    }     
    
    intContinuar = validar_entero("¿Introducir Invernadero adicional(1) o Salir(0)?:")
    while(intContinuar != 1 and intContinuar != 0): 
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_entero("¿Introducir Invernadero adicional(1) o Salir(0)?:")
    
    if intContinuar == 1 :
        load_invernadero(dicInvernaderos)
        
    return dicInvernaderos