import os
import shutil
from tkinter import filedialog

try:
    root = filedialog.askdirectory()
    for path, _, files in os.walk(root):
        for file in files:
            extension = file.split('.')[1]
            path_ext = os.path.join(root, extension)
            os.makedirs(path_ext, exist_ok=True)
            path_file = os.path.join(path, file)
            shutil.move(path_file, path_ext)
except:
    print('Done!')
