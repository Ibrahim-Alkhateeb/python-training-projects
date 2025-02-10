import sqlite3
import csv
from pathlib import Path

path= Path.home() / Path('PycharmProjects\PythonProjectApps\DB_SqlLite')
DB_Connection= sqlite3.connect(path / 'DataBase.db')
crsr= DB_Connection.cursor()
print('DB Connected')

#update
crsr.execute("update emp set salary =600 where id = 4")

#delete
# crsr.execute("delete from emp where id = 4")


DB_Connection.commit()