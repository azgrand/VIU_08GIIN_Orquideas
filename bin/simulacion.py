"""
@author: Jon Lebrero Catalina
"""

from muestra_informacion import print_muestra

# Simula el STOCK de con los Lotes e Invernaderos que le pasamos, contabiliza las plantas y segun el clima crea un Stock de Lotes anidados
# Luego se imprimen formateados con la funcion que esta descrita en muestra_informacion
def simular_lotes(dicLotes, dicInvernaderos):
    dicStock = {}
    for key in dicInvernaderos:
        dicStock[key] = {}
        dicStock[key]['Lotes'] = []
        dicStock[key]['Clima'] = ""
        dicStock[key]['Total Plantas'] = 0
        for LoteKey in dicLotes:
          if dicLotes[LoteKey]['Clima'] == dicInvernaderos[key]['Clima']:
              if dicInvernaderos[key]['Capacidad'] > dicStock[key]['Total Plantas'] + dicLotes[LoteKey]['Cantidad Plantas']:
                dicStock[key]['Lotes'].append(LoteKey)
                dicStock[key]['Total Plantas'] += dicLotes[LoteKey]['Cantidad Plantas']
                dicStock[key]['Clima'] = dicLotes[LoteKey]['Clima']             
    print_muestra(dicStock)

# Modifica los datos de Lotes, restando acorde al clima un valor que luego mantenemos, de tal forma que podemos simularlo con pocos dias y luego mostrar la informacio.
# Luego se imprimen formateados con la funcion que esta descrita en muestra_informacion
def simular_dias(dicLotes, dias):
    print("Simular paso de los dias")
    print("")
    print("\t  -------------")
    for d in range(dias):
        print("\t Dia:", d+1)
        for Lote in dicLotes:
            strClima = str(dicLotes[Lote]['Clima'])
            intDiasAndes = int(dicLotes[Lote]['Dias Andes'])
            intDiasCosta = int(dicLotes[Lote]['Dias Costa'])
            if intDiasAndes == 0 and intDiasCosta == 0:
              print("Lote ", Lote, " en estado optimo para ser vendido.")
            elif  strClima == 'Andes':
              if intDiasAndes > 0:
                intDiasAndes -= 1
              elif intDiasAndes == 0:
                print("Finalizado el crecimiento para " , Lote, " en ",  strClima)
            elif strClima == 'Costa':
              if intDiasCosta > 0:
                intDiasCosta -= 1
              elif intDiasCosta == 0:
                print("Finalizado el crecimiento para " , Lote, " en ",  intDiasCosta)
            dicLotes[Lote]['Dias Andes'] = intDiasAndes
            dicLotes[Lote]['Dias Costa'] = intDiasCosta
        print_muestra(dicLotes)
        print("\t  -------------")
    print("\t  -------------")
    return dicLotes