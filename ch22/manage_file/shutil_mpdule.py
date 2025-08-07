import shutil
import os
path = "./ch22/manage_file"
src = f"{path}/file.txt"
dst= f"{path}/copiedfile.txt"





if not os.path.exists(dst):
    # shutil.copy(src,dst)
    shutil.copy2(src,dst)    