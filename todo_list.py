import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["task"] = new_task
        else:
            print("Invalid task number")

    def mark_task_done(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["done"] = True
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("----------------------")
        todo_list.display_tasks()
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_task_done(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
