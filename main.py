from task_manager import TaskManager
from storage import save_tasks, load_tasks

#task manager
def main():
    manager = TaskManager()
    manager.tasks = load_tasks()
    print('hello task manager, bch nched n9ata3 cha3ri')
    print("wlh 3ib wmlllkdfklvkgehsnkughjrg")
    print("excellent")
    print("dalanda zidou 9ahwa")
    print(TaskManager.add_task)

    while True:
        print("\n=== Smart Task Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (Low/Medium/High): ")
            manager.add_task(title, priority)
            save_tasks(manager.tasks)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            manager.list_tasks()
            index = int(input("Task number to complete: ")) - 1
            manager.complete_task(index)
            save_tasks(manager.tasks)

        elif choice == "4":
            manager.list_tasks()
            index = int(input("Task number to delete: ")) - 1
            manager.delete_task(index)
            save_tasks(manager.tasks)

        elif choice == "5":
            save_tasks(manager.tasks)
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
