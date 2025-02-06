import shutil
from pathlib import Path

path_home= Path.home()
file_path = path_home / 'PycharmProjects' / 'PythonProjectApps' / 'Files' / 'file_one.txt'
file_to_copy= path_home / input('please select the path want you copy file or folder (Note: use forward slash "/" in path): \n')

shutil.copy(file_path , file_to_copy)
# shutil.copytree(file_path , file_to_copy)
