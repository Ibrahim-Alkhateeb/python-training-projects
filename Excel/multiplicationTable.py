import openpyxl, sys
from pathlib import Path
from openpyxl.styles import Font

if len(sys.argv) == 2:
    try:
        number= int(sys.argv[1])
    except Exception as e:
        print(e)

    excel_file= openpyxl.Workbook()
    sheet = excel_file.active

    for row in range(number +1):
        for column in range(11):
            # Check if in header row or column
            isHeader = False

            if row == 0 and column == 0:
                isHeader= True
                value= ''

            elif row == 0:
                isHeader= True
                value = column

            elif column == 0:
                isHeader= True
                value = row

            else:
                value = row * column

            cell = sheet.cell(row=row + 1, column=column + 1)

            if isHeader:
                cell.font = Font(bold= True)

            cell.value = value

            save_file_in_path = str(Path.home() / Path('OneDrive', 'Desktop') / 'multiplication_table_') + str(number) + '.xlsx'

            excel_file.save(save_file_in_path)

            print(f'Saved as {save_file_in_path}')

else:
    print('please enter only the name tow args : 1- "multiplicationTable.py and number')
