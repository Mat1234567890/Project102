import os
import shutil

from_dir = "/Users/m/Desktop/PythonBy/P102/Downloads"
to_dir = "/Users/m/Desktop/PythonBy/P102/Document_Files"

exts = ['.txt','.doc','.docx','.pdf']
list_of_files = os.listdir(from_dir)
#print(list_of_files)


for file in list_of_files:
    name, ext = os.path.splitext(file)
    if ext=="":
        continue
    if ext in exts:
        path1 = from_dir+"/"+file
        path2 = to_dir+"/Document_Files"
        path3 = path2+"/"+file
        if os.path.exists(path2):
            print("Moving "+file+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)