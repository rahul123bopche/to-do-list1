import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:\n1. Add Task\n2. View Tasks\n3. Mark as Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to mark done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            show_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()