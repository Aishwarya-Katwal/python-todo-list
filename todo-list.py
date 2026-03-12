print("---To do list---")
def show_menu():
    print("---To do list---")
    print("1. Add task ")
    print("2. View task")
    print("3. delete task")
    print("4. Exit \n")

def add_task():
    task=input("Enter your task:")
    with open("todo1.txt","a") as f:
        f.write(f"{task} \n")
        print("Task Added")




def view_task():
    try:
        with open("todo1.txt","r") as f:
            tasks=f.readlines()
            for i,task in enumerate(tasks,1):
                print(f"{i}.{task.strip()}")
        print("\n")
    except FileNotFoundError:
        print("File not found.Try Adding one...\n")

        

def del_task():
    try:
        with open("todo1.txt","r") as f:
            tasks=f.readlines()
            if not tasks:
                print("No tasks in the file. Try adding one..")
            for i,task in enumerate(tasks,1):
                print(f"{i}.{task.strip()}")
            while True:
                num_len=int(input("Enter the task no. you want to delete:"))
                if 1<=num_len<=len(tasks):
                    del tasks[num_len-1]
                    break
                else:
                    print("Invalid number entered...")
            with open("todo1.txt","w") as f:
                 f.writelines(tasks)
            print(f"task no.{num_len} deleted")
    except FileNotFoundError:
        print("tasks not found.Try Adding one\n")


            



while True:
    show_menu()
    choice=int(input("Enter your choice:"))
    if (choice==1):
        add_task()
    elif (choice==2):
        view_task()
    elif (choice==3):
        del_task()
    else:
        print("You are exiting...")
        break
