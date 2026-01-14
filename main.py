from task import *

# list of tasks 
tasks = []

def show_mune():
    print('1 : add new task')
    print('2 : show all tasks')
    print('3 : delet task')
    print('4 : update task')


def add_task(title , description):
    # create a new task 
    new_task = Task(title=title,description=description)
    tasks.append(new_task)




