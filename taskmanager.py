tasks=[]
print("choose an option")
def print_tasks():
    print("Your Task List:")
    # for i in range(len(tasks)):
    #         print(str(i+1)+"."+tasks[i])
    for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
choice=0
while choice!="5":
    choice=input(" 1. Add Task \n 2. View Tasks \n 3. Remove Task\n 4. Mark Task Done \n 5. Exit")
    if choice=="1":
        task1=input("please enter your task")
        tasks.append(task1)
        print_tasks()
    elif choice=="2":
        print_tasks()

    elif choice=="3":
        try:
            t_no=int(input("enter the number of task u wish to remove"))
            if 1<t_no<=len(tasks):
                tasks.remove(tasks[t_no-1])
                print_tasks()
            else:
                print("Invalid task number")
        except:
            print("Please enter a valid number")
    elif choice=="4":
        t_no=int(input("enter the number of task u wish to mark done"))
        if(" -DONE" not in tasks[t_no-1]):
            tasks[t_no-1]=tasks[t_no-1]+" -DONE"
            print_tasks()
        else:
            print("Already marked done")
    elif choice=="5":
        print("You chose EXIT!Bye")
    else:
        print("Invalid Choice")
print("The end")