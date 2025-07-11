#To do List
from datetime import datetime

def task_list():
    try:
        with open("tasks.txt", "r") as file:
            content = file.readlines()
            if content:
                for index, task in enumerate(content, start=1):
                    print(f"{index}. {task}")
            else:
                print("Task list is empty")
    except FileNotFoundError:
        print("Task file doesn't exist")
        
password = ''
while password != 'octrin':
    password = input("Enter the password: ")
while True:
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    user_input = input("1. See task list\n2. Add Task\n3. Remove all tasks\n4. Exit\nEnter your last preference in integer: ")
    if user_input == '1':
        task_list()
    elif user_input == '2':
        add_task = input("Write: ")
        with open("tasks.txt", "a") as file:
            file.write(f"{add_task} [{current_time}]\n")
        print("Task added sucessfully")
    elif user_input == '3':
        open("tasks.txt", "w").close()
        print("All of the tasks are removed")
    elif user_input == '4':
        print("Visit Again")
        break
    else:
        print("Invalid User Input")