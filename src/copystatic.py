import os
import shutil

def copy_content(source, destination):
    # copy content of folder source to destination
    if not os.path.exists(source):
        raise ValueError(f"source folder {source} does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            copy_content(s, d)
        else:
            shutil.copy2(s, d)