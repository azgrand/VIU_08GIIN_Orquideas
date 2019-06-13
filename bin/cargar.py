"""
@author: Jon Lebrero Catalina
"""

from fichero import load_file
# Solo realiza una llamada. Asi, si el furuto se hiceran modificaciones podrian controlarse mas sencillamente.
def load_data(dic, strFileName):
    return load_file(strFileName)