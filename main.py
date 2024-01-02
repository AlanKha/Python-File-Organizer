import os
from pathlib import Path
import glob
import shutil

def move_files(src, dst):
    fileTypes = ('*.jpg', '*.png', '*.jpeg', '*.gif')
    imagePaths = [glob.glob(os.path.join(src, t)) for t in fileTypes]

    for path_list in imagePaths:
        for file_path in path_list:
            try:
                if os.path.isfile(file_path):
                    shutil.move(file_path, dst)
            except Exception as e:
                print(f"Error moving {file_path}: {e}")


if __name__ == '__main__':
    downloadsPath = str(Path.home() / "Downloads")
    targetPath = str(Path.home() / "Pics")

    if os.path.exists(targetPath) and os.path.exists(downloadsPath):
        move_files(downloadsPath, targetPath)
    elif os.path.exists(downloadsPath) and not os.path.exists(targetPath):
        os.mkdir(targetPath)
        move_files(downloadsPath, targetPath)
    else:
        print(f"Error: {downloadsPath} does not exist")


