# Backup-System
## Juan Manuel Muñoz Arias (Sistemas Operativos)

Este proyecto consiste en una herramienta de línea de comandos escrita en Python que permite hacer backups de archivos de manera segura y eficiente.

La herramienta toma una carpeta de archivos como entrada y la separa en pedazos más pequeños para hacer backups. Para ello, se divide el archivo en partes de tamaño máximo de 512 MB, se comprimen en un archivo Tar y se encriptan usando la biblioteca de criptografía Fernet. Los nombres de los archivos divididos se almacenan como Hashes y se genera un archivo json llamado segments.json que indica el orden de los archivos y una llave llamada key.key para desencriptarlos.

### 1.Store
La carpeta de Store recibe como parámetros las carpetas de entrada y salida, comprime los archivos de entrada en un solo archivo Tar, lo divide en archivos más pequeños, los encripta y los almacena con nombres encriptados como Hashes. Además, se genera el archivo json segments.json que indica el orden de los archivos y el archivo key.key que es la llave para poder desencriptarlos.

### 2.Restore
La carpeta de Restore se encarga de restaurar los archivos divididos y encriptados. Recibe por parámetros la carpeta donde se encuentran los archivos encriptados junto con su archivo json de orden y su archivo key. Se desencripta archivo por archivo y se añade su contenido a un archivo Tar de restauración. Una vez completo el archivo Tar, se extrae en la carpeta de salida. Es importante destacar que si el json o la key cambian, no será posible hacer el backup.

### 3.Funcionamiento
#### 3.1. Entorno virtual
Antes de todo, es necesario crear un entorno virtual en la raíz del proyecto de python para ejecutar el código.
```
python -m venv venv
```
Acceder al entorno virtual (Para usuarios Ubuntu)
```
source venv/bin/activate
```
Instalar las librerás por medio de requirements.txt
```
pip install -r requirements.txt
```
Y eso sería todo


#### 3.2. Store
Para generar el backup, se debe acceder a la carpeta store, donde se encuentra el archivo main.py y ejecutar el siguiente comando:

```
python main.py [carpeta_de_entrada] [carpeta_de_salida]
```
Se debería ver algo como esto

![image](https://user-images.githubusercontent.com/69641274/228420922-812d85ba-ea52-4d77-9f75-e67771d6971b.png)
![image](https://user-images.githubusercontent.com/69641274/228421021-f95a81ea-84f0-407c-8df9-50d3aacc2f50.png)



#### 3.3. Restore
Para restaurar el backup, se debe acceder a la carpeta restore, donde se encuentra el archivo main.py y ejecutar el siguiente comando:

```
python main.py [carpeta_de_entrada] [carpeta_de_salida]
```
Se debería ver algo como esto

![image](https://user-images.githubusercontent.com/69641274/228420964-51606aae-7ba4-4d01-a47a-45a756d580f2.png)
![image](https://user-images.githubusercontent.com/69641274/228421079-ca8c15a7-d125-4537-bd6c-c5713e32dba9.png)

