import sqlite3
from pathlib import Path

message = """
"a" => Add New Task
"d" => Delete A Task
"s" => Show All Task
"u" => Update A Task
"q" => Quit The App
Please choose an option:
"""

user_id = int(input('enter user id: '))
user_input = input(message).strip().lower()
commands_list = ["a", "d", "s", "u", "q"]
try:
    path= Path.home() / Path('PycharmProjects/PythonProjectApps/ToDo_App')
    DB_Connection= sqlite3.connect(path / 'ToDoApp.db')
    crsr= DB_Connection.cursor()
    print('ToDoApp DB Connected')
except:
    print('connection error')

finally:
    if (DB_Connection):
        # create_table
        create_task_table= """create table if not exists tasks(
        id integer,
        task name varchar(20),
        description text)"""

        crsr.execute(create_task_table)
        def show_tasks():
            crsr.execute(f"SELECT * FROM tasks WHERE id = '{user_id}' ")
            result= crsr.fetchall()

            print(f"You have {len(result)} tasks")

            if len(result) > 0:
                for task in result:
                    print(f"Task Name: {task[1]} AND", end=" ")
                    print(f"Task Description: {task[2]}")

            DB_Connection.commit()


        def add_task():
            task_name= input('Write Task Name: ').strip()
            task_desc= input('Write the description of Task: ')

            # crsr.execute('SELECT MAX(id) FROM tasks')
            # max_id = crsr.fetchone()[0]
            # if max_id is None:
            #     user_id = 1
            # else:
            #     user_id = max_id + 1
            crsr.execute(f"insert into tasks (id, task, description) values ('{user_id}', '{task_name}','{task_desc}')")
            DB_Connection.commit()

        def delete_task():
            task_name= input('write the task name your want delete: ').strip()
            crsr.execute(f"delete from tasks where task= '{task_name}' ")
            DB_Connection.commit()

        def update_task():
            task_name = input("Write The Name Of The Task You Want Modify: ").strip()
            crsr.execute(f"SELECT * FROM tasks WHERE task = '{task_name}' AND id='{user_id}'")
            results = crsr.fetchall()

            if not results:
                print("There is no task with this name")

            else:
                new_desc = input("Write The New Task Description: ").strip()
                new_task_name = input("Write The New Task Name: ").strip()

                crsr.execute("UPDATE tasks SET description = ?, task = ? WHERE task = ?",
                             (new_desc, new_task_name, task_name))
                DB_Connection.commit()
                print("Task updated successfully!")

        def end_app():
            print('Program Closed!')
            exit()


        if user_input in commands_list:
            if user_input == "s":
                show_tasks()

            elif user_input == "a":
                add_task()

            elif user_input == "d":
                delete_task()

            elif user_input == "u":
                update_task()

            else:
                end_app()

        else:
            print("Sorry This Command Is Not Found")