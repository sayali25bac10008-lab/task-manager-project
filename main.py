from task_manager import TaskManager

tm = TaskManager()

def menu():
    print("""
========== TASK MANAGER ==========
1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. View Tasks by Priority
6. Edit Task
7. Delete Task
8. Mark Task as Completed
9. Exit
""")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due Date (DD/MM/YYYY): ")
        priority = input("Priority (High/Medium/Low): ")
        tm.add_task(title, description, due_date, priority)

    elif choice == "2":
        tm.view_all_tasks()

    elif choice == "3":
        tm.view_pending_tasks()

    elif choice == "4":
        tm.view_completed_tasks()

    elif choice == "5":
        priority = input("Enter Priority (High/Medium/Low): ")
        tm.view_by_priority(priority)

    elif choice == "6":
        task_id = input("Enter Task ID: ")
        print("Leave any field blank to skip editing.")
        title = input("New Title: ")
        description = input("New Description: ")
        due_date = input("New Due Date: ")
        priority = input("New Priority: ")
        tm.edit_task(task_id, title, description, due_date, priority)

    elif choice == "7":
        task_id = input("Enter Task ID: ")
        tm.delete_task(task_id)

    elif choice == "8":
        task_id = input("Enter Task ID: ")
        tm.mark_completed(task_id)

    elif choice == "9":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again!")
