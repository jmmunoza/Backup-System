import json
import os
from cryptography.fernet import Fernet
from createHash import createHash


"""
Esta función toma un argumento de entrada "output_path", que
es la ruta de la carpeta donde se guardaron los segmentos
divididos en el módulo "splitTarfile". Encripta cada segmento
utilizando la librería cryptography y una clave Fernet, y
reemplaza el archivo original con el archivo encriptado.
"""


def encryptSegments(output_path):
    print('Encrypting segments...')
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)

    with open(f'{output_path}key.key', 'wb') as key_file:
        key_file.write(fernet_key)

    with open(f'{output_path}segments.json', 'r') as segments_fie:
        segments_dict = json.load(segments_fie)
        print('segments.json opened')
        print(segments_dict)

    for key in sorted(segments_dict.keys(), key=lambda x: int(x)):
        segment_path = segments_dict[key]
        segment_hash_path = output_path + createHash(segment_path)
        with open(segment_hash_path, 'wb') as segment_encrypted:
            with open(segment_path, 'rb') as segment_file:
                content = segment_file.read()
                encrypted = fernet.encrypt(content)
                segment_encrypted.write(encrypted)
                segments_dict[key] = segment_encrypted.name
                print(segment_file.name, 'encrpyted as', segment_encrypted.name)
                os.remove(segment_path)

    with open(f'{output_path}segments.json', 'w') as segments_file:
        json.dump(segments_dict, segments_file, indent=4)
        print(segments_file.name, 'JSON updated!')
