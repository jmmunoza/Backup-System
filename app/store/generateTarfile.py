import os
import tarfile

"""
Se encarga de generar un archivo
.tar.gz a partir de los archivos que se encuentran en
un directorio de entrada. Este archivo es guardado en
la ruta de salida especificada.
"""

def generateTarfile(input_path, output_path):
    tar_path = output_path + 'temp_.tar.gz'

    tar = tarfile.open(tar_path, "w:gz")
    for input_file in os.scandir(input_path):
        tar.add(input_file.path)
    tar.close()

    print('Tarfile generated in', tar_path)

    return tar_path
