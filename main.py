from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\nStudent Task Management System")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        manager.add_task(title)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        task_id = int(input("Enter task ID: "))
        manager.complete_task(task_id)

    elif choice == "4":
        task_id = int(input("Enter task ID: "))
        manager.delete_task(task_id)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
