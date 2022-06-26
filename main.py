__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, shutil, zipfile
# https://www.pythontutorial.net/python-basics/python-directory/

path = os.getcwd()

if os.path.exists(os.path.join(path, "files")):
    if os.path.isdir(os.path.join(path, "files")):
        path = os.path.join(path, "files")


def clean_cache():
    cache_path = os.path.join(path,"cache")
# https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder    
    if os.path.exists(cache_path):
        for filename in os.listdir(cache_path):
            file_path = os.path.join(cache_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    else:
        os.mkdir(cache_path)

def cache_zip(zip_file_path, cache_dir_path):
# https://stackoverflow.com/questions/3451111/unzipping-files-in-python    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)

def cached_files():
    file_list = []
    cache_path = os.path.join(path,"cache")
    if os.path.exists(cache_path):
        for filename in os.listdir(cache_path):

            file_list.append(os.path.abspath(
                # https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
                os.path.join(cache_path, filename)))
    return file_list



def find_password(file_list):   
    for file in file_list:
        text = open(file, "r")
        for line in text:
            if "password" in line.lower():
                text.close()
                return line[line.index(" ")+1:len(line)-1]
                # return line
        text.close()

print(find_password(cached_files()))