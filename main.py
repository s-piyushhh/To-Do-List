import os


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx + 1}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
        else:
            print("Invalid task number.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    to_do_list = ToDoList()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("======================")
        print("\n")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
            print("Task added Successfully \n")
        elif choice == "2":
            to_do_list.view_tasks()
            print("\n")
            input("Press Enter to continue...")
        elif choice == "3":
            task_number = int(
                input("Enter the task number to mark as complete: "))
            to_do_list.complete_task(task_number)
            input("Press Enter to continue...")
            print("\n")
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            to_do_list.delete_task(task_number)
            input("\n")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            input("\n")


if __name__ == "__main__":
    main()
