import sqlite3
import csv
from pathlib import Path

path= Path.home() / Path('PycharmProjects\PythonProjectApps\DB_SqlLite')
DB_Connection= sqlite3.connect(path / 'DataBase.db')
crsr= DB_Connection.cursor()
print('DB Connected')


#create table
create_emp_table_command= """
CREATE TABLE if not exists emp(
id INTEGER,
name VARCHAR(20),
salary INTEGER,
employment_date TEXT
)
"""

crsr.execute(create_emp_table_command)

open_csvfile= open(path / 'employees_1.csv')
store_csv_data= csv.reader(open_csvfile)

crsr.executemany("""INSERT INTO emp VALUES (?, ?, ?, ?)""", store_csv_data)

DB_Connection.commit()
DB_Connection.close()
