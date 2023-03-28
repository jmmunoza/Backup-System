import json
import sys, os, tarfile
from cryptography.fernet import Fernet 
import hashlib


def generateTarfile(input_path, output_path):
    tar_path = output_path + 'temp_.tar.gz'
    
    tar = tarfile.open(tar_path, "w:gz")
    for input_file in os.scandir(input_path):
        tar.add(input_file.path)
    tar.close()
    
    print('Tarfile generated in', tar_path)
    
    return tar_path


def splitTarfile(tar_path):
    print('Spliting Tarfile...')
    
    with open(tar_path, 'rb') as file:
        content = file.read()
        
    segments_dict = {}
    tar_folder_path = os.path.dirname(tar_path)
    
    size = len(content) // 5
    segments = [content[i:i+size] for i in range(0, len(content), size)]
    
    for i, segment in enumerate(segments):
        with open(f'{tar_folder_path}/segment_{i+1}.tar.gz', 'wb') as segment_file:
            segment_file.write(segment)
            segments_dict[i + 1] = segment_file.name
            print(segment_file.name, 'created!')
            
    with open(f'{tar_folder_path}/segments.json', 'w') as segments_file:
        json.dump(segments_dict, segments_file, indent=4)
        print(segments_file.name, 'JSON generated!')
            
    os.remove(tar_path)
    print(tar_path, 'removed...')
    
    
def createHash(filename):
    hash_object = hashlib.md5(filename.encode())
    return hash_object.hexdigest()
    
    
def encryptSegments(output_path):
    print('Encrypting segments...')
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)
    
    with open(f'{output_path}key.key', 'wb') as key_file:
        key_file.write(fernet_key)

    
    with open(f'{output_path}segments.json', 'r') as segments_fie:
        segments_dict = json.load(segments_fie)
        print('segments.json opened')
        
    for key in sorted(segments_dict.keys()):
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



def main():
    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')
    
    print('Backup process started...')
    tar_path = generateTarfile(input_path, output_path)
    splitTarfile(tar_path)
    encryptSegments(output_path)

    
if __name__ == '__main__':
    main()