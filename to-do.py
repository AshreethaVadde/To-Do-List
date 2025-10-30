import os
TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    
    with open(TODO_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks, new_task):
    tasks.append(f"[ ] {new_task.strip()}")
    save_tasks(tasks)
    print(f"✅ Added task: {new_task}")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty! 🎉")
        return

    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("------------------")

def complete_task(tasks, task_number):
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            if task.startswith("[ ]"):
                tasks[index] = task.replace("[ ]", "[x]", 1)
                save_tasks(tasks)
                print(f"🎉 Marked task {task_number} as COMPLETE.")
            else:
                print(f"Task {task_number} is already completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def delete_task(tasks, task_number):
    try:
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: {deleted_task}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def display_menu():
    print("\n--- To-Do Manager Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("--------------------------")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the task description: ")
            if new_task:
                add_task(tasks, new_task)
            else:
                print("Task cannot be empty.")
        elif choice == '3':
            view_tasks(tasks)
            task_num = input("Enter the number of the task to COMPLETE: ")
            if task_num:
                complete_task(tasks, task_num)
        elif choice == '4':
            view_tasks(tasks)
            task_num = input("Enter the number of the task to DELETE: ")
            if task_num:
                delete_task(tasks, task_num)
        elif choice == '5':
            print("Goodbye! Your to-do list has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()