tasks = []

def add_tasks():
    task = input("Add a task:")
    tasks.append(task)
    print("Task added!")
    print(f"\n The updated tasks is {tasks}")
    
def view_task():
    if len(tasks) == 0:
        print("No tasks yet")
    else:
        print("YOUR TASKS:")
        for numbers, task in enumerate(tasks, start=1):
            print(f"{numbers}.{task}")

def remove_task():
    print(f"The task is: {tasks}")
    print()
    remove = input("Enter task to be removed: ")
    if remove in tasks:
        tasks.remove(remove)
        print("Task removed")
        print(f"\ The Updated tasks is {tasks}")
    else:
        print("Task not found in tasks")
    

while True:
    print("\n 1. Add tasks")
    print("\n 2. View tasks")
    print("\n 3. Remove tasks")
    print("\n 4. Exit")

    choice = int(input("Choose 1 or 2 or 3 or 4: "))

    if choice == 1:
        add_tasks()
    elif choice == 2:
        view_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("INVALID INPUT")
