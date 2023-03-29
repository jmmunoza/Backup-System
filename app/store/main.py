import sys
import os
from encryptSegments import encryptSegments
from generateTarfile import generateTarfile
from splitTarfile import splitTarfile
 

"""
Esta función principal es la que se ejecuta cuando se inicia
el programa. Toma dos argumentos de entrada, "input_path"
y "output_path", que representan las rutas de la carpeta
de entrada y la carpeta de salida, respectivamente.
Comprueba si ambos son directorios y lanza un error si no
lo son. Luego, utiliza las funciones "generateTarfile",
"splitTarfile" y "encryptSegments" para generar un archivo
de respaldo de la carpeta de entrada.
"""


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')

    print('Backup process started...')
    tar_path = generateTarfile(input_path, output_path)
    splitTarfile(tar_path)
    encryptSegments(output_path)


if __name__ == '__main__':
    main()
