# Image File Mover

This Python script moves image files from the Downloads folder to a specified destination folder.

## Description

The script searches for image files (with extensions: jpg, png, jpeg, gif) in the Downloads folder and moves them to a specified target folder. If the target folder doesn't exist, it creates one before moving the files.

## Usage

### Running the Script

By default, the downloads/pics path will be on the users path, but you can tweak the path in main.

1. Clone the repository or download the `main.py` script file.
2. Open a terminal or command prompt.
3. Navigate to the directory where `main.py` is located.
4. Run the script using Python:

    ```bash
    python main.py
    ```
    
### Creating an Executable

To create an executable file for the script:

1. Install PyInstaller if you haven't already:

    ```bash
    pip install pyinstaller
    ```

2. Open a terminal or command prompt.
3. Navigate to the directory where `main.py` is located.
4. Run PyInstaller to create the executable:

    ```bash
    pyinstaller --onefile main.py
    ```

The generated executable will be in the `dist` folder.


## Python Code

```python
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
