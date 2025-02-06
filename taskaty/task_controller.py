from .task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace

class TaskController:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_task(self, args):
        start_date = args.start if args.start else date.today().isoformat()
        task = Task(args.title, args.description, start_date, args.end, args.done)
        with open(self.file_name, 'a') as file:
            file.write(str(task) + '\n')

    def list_task(self):
        unfinished_tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.strip().split(', ')
                end_date = None if end_date.strip().lower() in ['none', ''] else end_date
                done = done.lower() == 'true'
                if not done:
                    unfinished_tasks.append({'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date})
        return unfinished_tasks

    def list_all_tasks(self):
        tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.strip().split(', ')
                end_date = None if end_date.strip().lower() in ['none', ''] else end_date
                done = done.lower() == 'true'
                tasks.append({'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date, 'done': done})
        return tasks

    def due_date(self, start, end):
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        return f'{(end_date - start_date).days} days left'

    def print_table(self, tasks):
        formatted_tasks = []
        for number, task in enumerate(tasks, 1):
            due_date = self.due_date(task['start_date'], task['end_date']) if task['end_date'] else 'Open'
            formatted_tasks.append({'No.': number, **task, 'due_date': due_date})
        print(tabulate(formatted_tasks, headers='keys'))

    def display(self, args):
        all_tasks = self.list_all_tasks()
        unfinished_tasks = self.list_task()

        if not all_tasks:
            print('No tasks found. Use "add" to create a task.')
            return

        if args.all:
            self.print_table(all_tasks)
        else:
            if unfinished_tasks:
                self.print_table(unfinished_tasks)
            else:
                print('All tasks are completed!')

    def check_task(self, args):
        tasks = self.list_all_tasks()
        index = args.task

        if index <= 0 or index > len(tasks):
            print(f'Task number {index} does not exist!')
            return

        tasks[index - 1]['done'] = True
        self._save_tasks(tasks)

    def remove_task(self, args):
        tasks = self.list_all_tasks()
        index = args.task

        if index <= 0 or index > len(tasks):
            print(f'Task number {index} does not exist!')
            return

        tasks.pop(index - 1)
        self._save_tasks(tasks)

    def _save_tasks(self, tasks):
        with open(self.file_name, 'w') as file:
            for task in tasks:
                file.write(f"{task['title']}, {task['description']}, {task['start_date']}, {task['end_date']}, {task['done']}\n")

    def rest(self, args):
        with open(self.file_name, 'w') as file:
            file.write('')
        print('All tasks deleted!')
