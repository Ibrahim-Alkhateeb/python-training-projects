import sqlite3
import csv
from pathlib import Path

path= Path.home() / Path('PycharmProjects\PythonProjectApps\DB_SqlLite')
DB_Connection= sqlite3.connect(path / 'DataBase.db')
crsr= DB_Connection.cursor()
print('DB Connected')

# crsr.execute("select name,salary, employment_date  from emp where salary > 850")
crsr.execute('select max(id) from emp')
# print(crsr.fetchone())
# print(crsr.fetchall())
max_id= crsr.fetchone()
max_id = max_id[0]
print(max_id)
# print(crsr.fetchmany(2))

# fetch_data= crsr.fetchall()
# for i in fetch_data:
#     print(i)


if max_id == 'None':
    user_id = 1
else:
    user_id = max_id + 1
    print(user_id)

