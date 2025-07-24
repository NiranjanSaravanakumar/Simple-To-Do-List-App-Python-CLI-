# Simple To-Do List App

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_done():
    view_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the task number to mark as done: "))
            if 1 <= task_index <= len(tasks):
                del tasks[task_index - 1]
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Enter a number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
