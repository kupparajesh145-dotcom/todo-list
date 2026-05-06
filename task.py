task = []

while True:
    print("1.add")
    print("2.view")
    print("3.remove")
    print("4.exit")
    choice = input("enter your choice:")

    if choice == "1":
        new_task = input("enter a task:")
        task.append(new_task)
        print("task added")

    elif choice == "2":
        if len(task) == 0:
            print("no task")
        else:
            print("your task")
            for i in range(len(task)):
                print(i+1, "-", task[i])

    elif choice == "3":
        num = int(input("enter task num:"))
        if num > 0 and num <= len(task):
            task.pop(num-1)
            print("task removed")
        else:
            print("invalid condition")

    elif choice == "4":
        print("good bye")
        break

    else:
        print("invalid choice")


