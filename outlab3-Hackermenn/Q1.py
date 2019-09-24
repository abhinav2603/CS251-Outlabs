import os
import tarfile
import sys
def tardir(path, tar_name):
    full_path=os.path.abspath(path)
    for root, dirs, files in os.walk(full_path):
        for file in files:
        	file_name=os.path.join(root, file)
        	file_name1=file_name.replace('/','-')
        	if not(file_name1 in tar_name.getnames()):
        	   tar_name.add(file_name,arcname=file_name1)

lst=[]

def allmissing(my_lst):
    for i in my_lst:
        if os.path.exists(i):
            return False
    return True

if len(sys.argv) < 2:
    print("Too few arguments")
elif allmissing(sys.argv[2:]):
    print("All file are missing")
else:
    tar_handle=tarfile.open(sys.argv[1], "w:gz")
    for path in sys.argv[2:]:
        if os.path.exists(path):
            if os.path.isfile(path):
                full_path=os.path.abspath(path)
                file_name1=full_path.replace('/','-')
                if not(file_name1 in tar_handle.getnames()):
                    tar_handle.add(full_path,arcname=file_name1)
            elif os.path.isdir(path):
                tardir(path,tar_handle)
        else:
            lst.append(path)
    tar_handle.close()
    print("Successfully compressed")
    if len(lst) > 0:
        for i in lst:
            print(i)
#tardir(os.getcwd(), tar_handle)
