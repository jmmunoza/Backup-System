import sys
import os
from restoreTarfile import restoreTarfile


"""
Se encarga de recibir dos argumentos por línea de comandos
y verifica que ambos sean rutas de directorios válidas.
Luego, llama a la función restoreTarfile() para restaurar
un archivo de respaldo a partir de los segmentos generados anteriormente.
"""


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')

    restoreTarfile(input_path, output_path)


if __name__ == '__main__':
    main()
