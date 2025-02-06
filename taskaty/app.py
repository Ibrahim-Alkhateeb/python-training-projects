from argparse import ArgumentParser
from .task_controller import TaskController

def main():
    controller = TaskController('tasks.txt')

    parser = ArgumentParser(description='Simple CLI Task Manager')
    subparser = parser.add_subparsers(dest="command")

    add_task = subparser.add_parser('add', help='Add a task')
    add_task.add_argument('title', help='Title of the task', type=str)
    add_task.add_argument('-d', '--description', help='Short description', type=str, default=None)
    add_task.add_argument('-s', '--start', help='Start date', type=str, default=None)
    add_task.add_argument('-e', '--end', help='End date', type=str, default=None)
    add_task.add_argument('--done', help='Mark task as done', action='store_true')
    add_task.set_defaults(func=controller.add_task)

    list_task = subparser.add_parser('list', help='List unfinished tasks')
    list_task.add_argument('-a', '--all', help='List all tasks', action='store_true')
    list_task.set_defaults(func=controller.display)

    check_task = subparser.add_parser('check', help='Mark a task as done')
    check_task.add_argument('-t', '--task', help='Task number', type=int, required=True)
    check_task.set_defaults(func=controller.check_task)

    remove = subparser.add_parser('remove', help='Remove a task')
    remove.add_argument('-r', '--task', help='Task number to remove', type=int, required=True)
    remove.set_defaults(func=controller.remove_task)

    reset = subparser.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func=controller.rest)

    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
