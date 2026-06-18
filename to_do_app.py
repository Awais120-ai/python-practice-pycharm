try:
    with open("tasks.txt, r") as file:
        task = file.read().splitlines()
except:
    tasks = []

while True:
    print("\n===== TO DO APP =====")
    print("1. Add Task")
    print("2. View Tasks") 
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for t in tasks:
                file.write(t + "\n")

        print("Task added ✅")

    # View Tasks
    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks found ❌")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    # Delete Task
    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

        try:
            num = int(input("Enter task number to delete: "))
            tasks.pop(num - 1)

            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(t + "\n")

            print("Task deleted 🗑️")
        except:
            print("Invalid input ❌")

    # Exit
    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice ❌")
