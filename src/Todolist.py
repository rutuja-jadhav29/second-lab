import os

class ToDoList:
    def __init__(self):
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                tasks = [task.strip() for task in tasks]
            return tasks
        return []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks to show!")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added!")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number!")
    
    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = f"[Completed] {task}"
            self.save_tasks()
            print(f"Task '{task}' marked as completed!")
        else:
            print("Invalid task number!")


def main():
    todo_list = ToDoList()
    
    while True:
        print("\nMenu:")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "4":
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == "5":
            print("Exiting the To-Do List App!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
