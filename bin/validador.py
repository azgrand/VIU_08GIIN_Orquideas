"""
@author: Jon Lebrero Catalina
"""

# Este fichero contiene los validadores que usamos, creados asi para ahorrar tiempo a furuto

# Valida un ENTERO (INT)
def validar_entero(texto):
    correcto = False
    variable = 0
    while(not correcto):
        try:
            variable = int(input(texto))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return variable

# Valida un TEXTO(STR)
def validar_texto(texto):
    correcto = False
    variable = 0
    while(not correcto):
        try:
            variable = str(input(texto))
            correcto=True
        except ValueError:
            print('Error, introduce valor no nulo')
    return variable