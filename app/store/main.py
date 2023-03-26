import json
import sys, os, tarfile
from cryptography.fernet import Fernet 

def main():
    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')
    
    # Tarfile
    tar = tarfile.open(output_path + 'temp_output.tar.gz', "w:gz")
    for input_file in os.scandir(input_path):
        tar.add(input_file.path)
    tar.close()
    
    # Spliting the Tarfile
    with open(output_path + 'temp_output.tar.gz', 'rb') as file:
        content = file.read()
        
    # Creating Dict to export as a Json
    parts_dict = {}
    
    size = len(content) // 5
    partes = [content[i:i+size] for i in range(0, len(content), size)]
    
    for i, parte in enumerate(partes):
        with open(f'{output_path}output{i+1}.tar.gz', 'wb') as new_file:
            new_file.write(parte)
            parts_dict[i + 1] = new_file.name
            
    with open(f'{output_path}parts.json', 'w') as f:
        json.dump(parts_dict, f, indent=4)
            
    os.remove(output_path + 'temp_output.tar.gz')
    
if __name__ == '__main__':
    main()