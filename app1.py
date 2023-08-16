class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    app = ToDoListApp()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            app.add_task(task)
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()