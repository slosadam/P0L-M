"""""
CONSOLA
"""""
import os
import sys


with open("texto.txt.txt", 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)

""""
def pedir_archivo()->None:
    nombre_archivo = "data_dir"
    archivo = open(nombre_archivo,"r")
    completo = archivo.read()
    print(completo)
    archivo.close()

print(pedir_archivo)
    
"""

