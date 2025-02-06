# تستخدم الدالة ()write للكتابة في الملف.
# تستخدم الدالة ()writelines لكتابة سطر أو عدة أسطر مباشرةً في الملف.

from pathlib import Path

# myFile= open('file_one.txt', 'w')
file_path = Path.home() / 'PycharmProjects' / 'PythonProjectApps' / 'Files' / 'file_one.txt'
myFile= open(file_path , 'w')
# myFile.write('1. Hello how are you?')
myFile.writelines(['1. Hello how are you?\n','2. Hello how are you?'])

myFile= open('file_one.txt', 'r')
print(myFile.read())
#
# from pathlib import Path
#
# # Define the correct file path
# file_path = Path.home() / 'PycharmProjects' / 'PythonProjectApps' / 'Files' / 'myfile.txt'
#
# # Write to the file
# with open(file_path, 'w') as myFile:
#     myFile.write('1. Hello how are you?')
#
# # Read from the file
# with open(file_path, 'r') as myFile:
#     print(myFile.read())  # Read and print the file contents
