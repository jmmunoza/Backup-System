import json
import sys, os, tarfile

def main():
    input_path  = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.isdir(input_path) or not os.path.isdir(output_path):
        raise ValueError('one of the inputs is not a folder')
    
    
    with open(f'{input_path}parts.json', 'r') as f:
        parts_dict = json.load(f)
        

    with open(f'{output_path}restore.tar.gz', 'wb') as restoring_tar:
        for key in sorted(parts_dict.keys()):
            part_file = parts_dict[key]
            
            with open(part_file, 'rb') as f:
                contnet = f.read()
                restoring_tar.write(contnet)
                
    with tarfile.open(f'{output_path}restore.tar.gz', "r:*") as tar:
        tar.extractall(output_path)
        
    
                

    # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA RESTORE
    
    
def getFolderSize(folder_path: str):
    size = 0

    for ele in os.scandir(folder_path):
        size+=os.path.getsize(ele)
        
    return size
        
if __name__ == '__main__':
    main()
         
        

    #tar = tarfile.open(output_path + 'output.tar.gz')
    #tar.extractall('../data/restore/')
  


    #tar.close()