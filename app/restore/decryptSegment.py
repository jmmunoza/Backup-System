import os


"""
Esta función toma dos argumentos de entrada, "segment_path" y "fernet",
que representan la ruta del segmento encriptado y una clave Fernet para
desencriptar el segmento, respectivamente. Desencripta el segmento y
guarda el archivo desencriptado en la misma carpeta con un nombre
modificado. Devuelve la ruta del archivo desencriptado.
"""


def decryptSegment(segment_path, fernet):
    print('Decrypting', segment_path)

    decrypt_path = os.path.dirname(
        segment_path) + '/decrypt' + os.path.basename(segment_path) + 'tar.gz'

    with open(segment_path, 'rb') as segment_file:
        with open(decrypt_path, 'wb') as decrypt_file:
            content = segment_file.read()
            decrypted = fernet.decrypt(content)
            decrypt_file.write(decrypted)

            print(segment_file.name, 'decrypted as', decrypt_file.name)

            return decrypt_path
