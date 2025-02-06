# this code to change date patterns of files names from dd-mm-yyyy to mm-dd-yyyy
import re, shutil, os
from pathlib import Path
from datetime import datetime, timedelta

folder_path = Path.home() / "PycharmProjects" / "PythonProjectApps" / "Files" / "change_files_name_date_pattren"
# folder_path.mkdir(parents=True, exist_ok=True)  # Ensure the folder exists if not create folder
check_date_patterns= "^(.*?)((0|1|2|3)?\d)-((0|1)?\d)-((19|20)\d\d)(.*?)$"
files_list = os.listdir(folder_path)

for file in files_list:
    search = re.search(check_date_patterns, file)

    if search == None:
        continue

    before_part = search.group(1)
    days_part = search.group(2)
    month_part = search.group(4)
    year_part = search.group(6)
    after_part = search.group(8)

    new_file_name = before_part + month_part + '-' + days_part + '-' + year_part + after_part

    print(f'renaming file "{file}" to "{new_file_name}"')

    old_path= folder_path / file
    new_path= folder_path / new_file_name
    shutil.move(old_path, new_path)


# # Create files
# start_date = datetime.today()
# for i in range(5):
#     date_str = (start_date + timedelta(days=i)).strftime("%m-%d-%Y")  # Generate date in DD-MM-YYYY format
#     file_name = f"{date_str}.txt"  # Filename pattern
#     file_path = folder_path / file_name
#
#     # Write content into the file
#     with open(file_path, "w") as file:
#         file.write(f"This is a test file created on {date_str}\n")
#
#     print(f"File created: {file_path}")
# print("10 files successfully created!")

## this code to change date patterns of files names from dd-mm-yyyy to mm-dd-yyyy (enhancement by gpt)
# import re
# from pathlib import Path
#
# # Define the folder path
# folder_path = Path.home() / "PycharmProjects" / "PythonProjectApps" / "Files" / "change_files_name_date_pattren"
#
# # Regex pattern to match DD-MM-YYYY format in filenames
# date_pattern = re.compile(r"^(.*?)(\d{2})-(\d{2})-(\d{4})(.*?)$")
#
# # Iterate through files in the directory
# for file in folder_path.iterdir():
#     if not file.is_file():
#         continue  # Skip directories
#
#     match = date_pattern.match(file.name)
#     if not match:
#         continue  # Skip files without a date pattern
#
#     before, day, month, year, after = match.groups()
#     new_file_name = f"{before}{month}-{day}-{year}{after}"
#     new_file_path = folder_path / new_file_name
#
#     print(f'Renaming "{file.name}" to "{new_file_name}"')
#     file.rename(new_file_path)  # Rename file directly



