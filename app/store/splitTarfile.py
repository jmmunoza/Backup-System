import os
import json


"""
Esta función toma un argumento de entrada "tar_path", que es la
ruta del archivo tar que se va a dividir en segmentos. Divide
el archivo tar en segmentos de 512 MB y los guarda en la misma
carpeta que el archivo tar. También guarda un archivo JSON que
contiene los nombres de los segmentos y sus rutas en la carpeta.
Elimina el archivo tar original.
"""


def splitTarfile(tar_path):
    print('Spliting Tarfile...')

    segments_dict = {}
    tar_folder_path = os.path.dirname(tar_path)
    size = 512 * 1000000  # 512 mb

    with open(tar_path, 'rb') as tar_file:
        i = 0

        while True:
            content = tar_file.read(size)
            if not content:
                break

            
            with open(f'{tar_folder_path}/segment_{i+1}.tar.gz', 'wb') as segment_file:
                segment_file.write(content)
                segments_dict[i + 1] = segment_file.name
                print(segment_file.name, 'created!')
                
            i += 1

    with open(f'{tar_folder_path}/segments.json', 'w') as segments_file:
        json.dump(segments_dict, segments_file, indent=4)
        print(segments_file.name, 'JSON generated!')

    os.remove(tar_path)
    print(tar_path, 'removed...')
