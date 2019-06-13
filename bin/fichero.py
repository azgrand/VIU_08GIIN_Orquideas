"""
@author: Jon Lebrero Catalina
"""

import json

# Esta funcion solo tiene la usabilidad de intentar abrir el fichero pero de NO EXISTIR nos lo crea evitando problemas en las funciones anteriores.
def create_file(strFileName):
    try:
        file = open(strFileName,"a")
        file.close()
    except ValueError:
        print(ValueError)

# Recibimos el nombre del fichero y lo abrimos para lectura usando la propiedad de JSON
def load_file(strFileName):
    try:
        create_file(strFileName)
        file = open(strFileName,"r")
        # Se usa JSON LOAD porque permite cargar texto plano previamente formateado de forma sencilla.
        dic = json.load(file)
        file.close()
        return dic
    except ValueError:
        print(ValueError)
        return {}
    
# Recibimos el nombre del fichero y el diccionario y guardamos la informacion usando propiedades de JSON
# Abrimos el fichero con la propiedad W que sobreescribe el contenido que tenia, de esta forma, cada fichero al guardar
# tiene la ultima informacion.
def save_file(strFileName, dic):
    try:
        create_file(strFileName)
        file = open(strFileName,"w")
        # Usamos JSON DUMPS para guardar el diccionario en texto plano.
        file.write(json.dumps(dic))
        file.close()
        return dic
    except ValueError:
        print(ValueError)
        return {}