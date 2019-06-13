"""
@author: Jon Lebrero Catalina
"""

def load_muestra_lote(dic):
    print("")
    print_muestra(dic)
    print("")   
    
def load_muestra_invernadero(dic):
    print("")
    print_muestra(dic)
    print("")  

# Recibimos un diccionario e imprimimos formateada toda la informacion que contiene de forma mas presentable.
def print_muestra(dic):
    for key, line in dic.items():
        print("\t", "-", key)
        for attribute, value in line.items():
            print("\t", "\t", "--", '{} : {}'.format(attribute, value))