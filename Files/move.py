# تحذف الدالة ()unlink الملف المحدد.
# تحذف الدالة ()rmdir المجلد المحدد (المجلدات الفارغة فقط).
# تستخدم الدالة ()rmtree لحذف شجرة المجلد بالكامل.
# تستخدم الدالة ()send2trash لحذف الملفات أو المجلدات ووضعها في سلة المهملات، لتثبيت الحزمة:
import os
from pathlib import Path
import shutil
# import send2trash # there is third party module
import zipfile


path_home= Path.home()
# file_to_remove= path_home / input('please select the path want you copy file or folder (Note: use forward slash "/" in path): \n')
folder_to_remove= path_home / input('please select the path want you copy folder (Note: use forward slash "/" in path): \n')

# os.unlink(file_to_remove)
os.rmdir(folder_to_remove) # only delete empty folder , (remove also of recycle bin)

shutil.rmtree(folder_to_remove) # delete any folder , (remove also of recycle bin)