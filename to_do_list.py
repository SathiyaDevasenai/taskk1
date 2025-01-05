import json

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. [{status}] {task['title']} (Due: {task['due_date']})")
        if task["description"]:
            print(f"   Description: {task['description']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description (optional): ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")

# Mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()