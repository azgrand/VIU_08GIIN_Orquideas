"""
@author: Jon Lebrero Catalina
"""

from fichero import save_file
# Solo realiza una llamada. Asi, si el furuto se hiceran modificaciones podrian controlarse mas sencillamente
# Se valida que el fichero tenga algun dato (podria darse el caso de que guarden sin crear informacion)
def save_data(strFileName, dic):
    if len(dic) == 0:
        return dic
    return save_file(strFileName, dic)