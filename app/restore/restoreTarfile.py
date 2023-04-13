import json
import os
import tarfile
from cryptography.fernet import Fernet
from decryptSegment import decryptSegment


"""
Esta función toma dos argumentos de entrada, "input_path" y "output_path",
que representan las rutas de la carpeta de entrada donde se guardaron los
segmentos encriptados y la carpeta de salida donde se restaurará el archivo
original, respectivamente. Lee el archivo JSON que contiene los nombres de
los segmentos y sus rutas, y utiliza la librería cryptography para desencriptar
los segmentos. Luego, junta los segmentos en un archivo tar y lo
guarda en la carpeta de salida.
"""


def restoreTarfile(input_path, output_path):
    with open(f'{input_path}segments.json', 'r') as segments_file:
        segments_dict = json.load(segments_file)

    with open(f'{input_path}key.key', 'rb') as key_file:
        fernet_key = key_file.read()
        fernet = Fernet(fernet_key)

    with open(f'{output_path}restore.tar.gz', 'wb') as restoring_tar:
        for key in sorted(segments_dict.keys(), key=lambda x: int(x)):
            segment_path = segments_dict[key]
            decrypted_path = decryptSegment(segment_path, fernet)

            with open(decrypted_path, 'rb') as decrypted_file:
                content = decrypted_file.read()
                restoring_tar.write(content)
                os.remove(decrypted_path)

    with tarfile.open(f'{output_path}restore.tar.gz', "r:*") as tar:
        tar.extractall(output_path)

    os.remove(f'{output_path}restore.tar.gz')

    print('Backup completed successfully!')
