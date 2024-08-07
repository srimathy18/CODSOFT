import json
import os

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{i + 1}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            todo_list.view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.view_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.complete_task(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
