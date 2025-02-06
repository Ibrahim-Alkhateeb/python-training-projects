# تستخدم الدالة ()move لنقل الملفات أو المجلدات.
# تستخدم الدالة ()rename لإعادة تسمية الملفات أو المجلدات.
import shutil
# import os
from pathlib import Path

path_home= Path.home()
file_path = path_home / 'PycharmProjects' / 'PythonProjectApps' / 'Files' / 'myfile.txt'
file_to_move= path_home / input('please select the path want you copy file or folder (Note: use forward slash "/" in path): \n')

shutil.move(file_path, file_to_move)