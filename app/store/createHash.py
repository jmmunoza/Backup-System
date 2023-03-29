import hashlib

"""
Esta función toma un argumento de entrada "filename",
que es el nombre del archivo del que se va a generar un hash MD5.
Convierte el nombre del archivo en una cadena codificada y
genera el hash utilizando la función md5 de la librería hashlib.
Devuelve el valor hash en formato hexadecimal.
"""


def createHash(filename):
    hash_object = hashlib.md5(filename.encode())
    return hash_object.hexdigest()
