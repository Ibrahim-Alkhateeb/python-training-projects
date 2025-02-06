# تستخدم الدالة open() لفتح ملف محدد.
# تعيد الدالة ()getcwd سلسلة نصية تحتوي على مجلد العمل الحالي.
# تغيّر الدالة ()chdir مجلد العمل الحالي إلى المجلد الممرر.
# تعيد الدالة ()home كائن مسار جديدًا يمثّل المسار الرئيسي للمستخدم.

from pathlib import Path
import os

print(os.getcwd())
# os.chdir(r'C:\Users\eyad3\Desktop\Projects\files')
print(Path.home())

# myFile = open(Path.home() / Path("Desktop", "New folder", "file_one.txt"), "r")
#
# print(str(Path.home() / Path("Desktop", "New folder", "file_one.txt")))
#
# print(myFile)
# print(myFile.name)
# print(myFile.mode)
#
# # print(myFile.read())
# # print(myFile.readlines())
#
# lines = myFile.readlines()
# print(lines[0:5])
#
# print("-" * 50)
# i = 0
# for line in lines:
#     print(line)
#     i+=1
#
#     if i == 5:
#        break

# myFile.close
