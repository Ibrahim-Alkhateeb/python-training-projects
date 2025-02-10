import sqlite3
from pathlib import Path

DB_path= Path.home() / Path('PycharmProjects\PythonProjectApps\DB_SqlLite')
sqlLite_Connection= sqlite3.connect(DB_path / 'DataBase.db')
crsr= sqlLite_Connection.cursor()
print('DB Connected')

create_std_table= """CREATE TABLE if not exists students(
firstName VARCHAR(20),
lastName VARCHAR(20),
age INTEGER)
"""

crsr.execute(create_std_table)
sqlLite_Connection.close()