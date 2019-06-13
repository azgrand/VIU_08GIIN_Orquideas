"""
@author: Jon Lebrero Catalina
"""

import os
import sys
# Como no queremos mostrar los ficheros, los guardaremos todos en una carpeta BIN
sys.path.append('./bin')

from menu import load_menu

# Crearemos los Lotes e Invernaderos en el arranque y los enviaremos a las funciones.
# Idealmente, podria hacerse la carga del fichero automaticamente en el arranque para no tener que crear estos datos de esta manera.
dicLotes = {}
dicInvernaderos = {}

os.system('cls')
# Se llama a load_menu(dic, dic) y el crea la instancia que controla todo nuestro programa
load_menu(dicLotes, dicInvernaderos)