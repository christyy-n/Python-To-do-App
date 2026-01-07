list = dict()

def newTask():
    task = input("Enter your task: ")
    list.update({task: "Not completed"})

def showTasks():
    for task in list:
        print(task + ": " + list[task])

def greetings():
    print("Welcome to my first project by myself!")
    print("This program is to help the users to make a to-do list and keep track on tasks.")

def menu():
    print("-----To-do App-----")
    print("1.New task")
    print("2.Edit task")
    print("3.Remove task")
    print("4.Show tasks")
    print("5.Mark the task completed")
    print("6.Exit")
    print("\nList:")
    showTasks()

def main():
    greetings()
    choice = 0
    while(choice != 6):
        menu()
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                newTask()
            case 2:
                #editTask()
                break
            case 3:
                #removeTask()
                break
            case 4:
                #showTasks()
                break
            case 5:
                #completed()
                break
            case 6:
                break
        
main()