import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

tasks = []

def add_task(title, description):
    task = Task(title, description)
    tasks.append(task)
    return "Task added successfully."

def update_task(title, new_title, new_description):
    for task in tasks:
        if task.title == title:
            task.title = new_title
            task.description = new_description
            return "Task updated successfully."
    return "Task not found."

def complete_task(title):
    for task in tasks:
        if task.title == title:
            task.is_completed = True
            return "Task marked as completed."
    return "Task not found."

def list_tasks():
    return json.dumps([vars(task) for task in tasks], indent=4)

while True:
    print("\nOptions: add, update, complete, list, exit")
    option = input("Enter option: ")
    
    if option == 'add':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        print(add_task(title, description))
        
    elif option == 'update':
        title = input("Enter current task title: ")
        new_title = input("Enter new task title: ")
        new_description = input("Enter new task description: ")
        print(update_task(title, new_title, new_description))
        
    elif option == 'complete':
        title = input("Enter task title to mark as completed: ")
        print(complete_task(title))
        
    elif option == 'list':
        print(list_tasks())
        
    elif option == 'exit':
        break
        
    else:
        print("Invalid option.")
