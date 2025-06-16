tasks=[]
print("choose an option")
choice=0
while choice!="5":
    choice=input(" 1. Add Task \n 2. View Tasks \n 3. Remove Task\n 4. Mark Task Done \n 5. Exit")
    if choice=="1":
        task1=input("please enter your task")
        tasks.append(task1)
        print("Your task List")
        for i in range(len(tasks)):
            print(str(i+1)+"."+tasks[i])
        print(tasks)
print("The end")