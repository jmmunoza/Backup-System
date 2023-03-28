import json
import sys, os, tarfile
from cryptography.fernet import Fernet


def decryptSegment(segment_path, fernet):
    print('Decrypting', segment_path)
    
    decrypt_path = os.path.dirname(segment_path) + '/decrypt' + os.path.basename(segment_path) + 'tar.gz'
    
    with open(segment_path, 'rb') as segment_file:
        with open(decrypt_path, 'wb') as decrypt_file:
            content = segment_file.read()
            decrypted = fernet.decrypt(content)
            decrypt_file.write(decrypted)
            
            print(segment_file.name, 'decrypted as', decrypt_file.name)
            
            return decrypt_path
    


def restoreTar(input_path, output_path):
    with open(f'{input_path}segments.json', 'r') as segments_file:
        segments_dict = json.load(segments_file)
        
    with open(f'{input_path}key.key', 'rb') as key_file:
        fernet_key = key_file.read()
        fernet = Fernet(fernet_key)

    with open(f'{output_path}restore.tar.gz', 'wb') as restoring_tar:
        for key in sorted(segments_dict.keys()):
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


def main():
    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')

    restoreTar(input_path, output_path)
    
        
if __name__ == '__main__':
    main()
    