"""
@author: Jon Lebrero Catalina
"""

import os

from validador import validar_entero
from validador import validar_texto

def load_lote(dicLotes):
    os.system('cls')
    print("Modulo Lotes de Orquídeas")
    print("")
    # Pedimos el Lote, se valida si existe y se pide otro. Los Lotes son UNICOS
    strLote = validar_texto("Lote:")
    while strLote in dicLotes:
        print("El Lote ya existe. Introduzca un nuevo lote")
        strLote = validar_texto("Lote:")
    # Pedimos la cantidad de Plantas  
    intCantidadPlanta = validar_entero("Cantidad Planta:")
    # Pedimos el Clima, tiene que ser ANDES o COSTA. usamos Capitalize para convertir la primera en mayuscula  
    strClima = validar_texto("Clima(Andes o Costa):")
    while(strClima.capitalize() != 'Andes' and strClima.capitalize() != 'Costa'):
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_texto("Clima(Andes o Costa):")
    # Pedimos los dias en ANDES
    intDiasAndes = validar_entero("Dias Andes:")
    # Pedimos los dias en Costas
    intDiasCosta = validar_entero("Dias Costa:")
    # Guardamos la informacion en Lotes. Clima usamos lower y capitalize para formatearlo.
    dicLotes[strLote] = {
          'Cantidad Plantas':intCantidadPlanta,
          'Clima':strClima.lower().capitalize(),
          'Dias Andes':intDiasAndes,
          'Dias Costa':intDiasCosta
    }
    
    intContinuar = validar_entero("¿Introducir Lote adicional(1) o Salir(0)?:")
    while(intContinuar != 1 and intContinuar != 0): 
        print("El valor introducido no pertenece al pedido")
        intContinuar = validar_entero("¿Introducir Lote adicional(1) o Salir(0)?:")
    
    if intContinuar == 1 :
        load_lote(dicLotes)
        
    return dicLotes