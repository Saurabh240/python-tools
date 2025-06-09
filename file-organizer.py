#Automatically organizes files in folders based on extension.
import os
import shutil

folder = '/path/to/folder'
for filename in os.listdir(folder):
    ext = filename.split('.')[-1]
    target = os.path.join(folder, ext)
    os.makedirs(target, exist_ok=True)
    shutil.move(os.path.join(folder, filename), os.path.join(target, filename))
