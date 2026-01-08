tasks = list()
completionState = list()

def newTask():
    task = input("Enter your task: ")
    tasks.append(task)
    completionState.append("Not completed")
    print(task + ": " + completionState[tasks.index(task)])

def showTasks():
    print("\n----------Tasks---------")
    for task in tasks:
        pos = tasks.index(task)
        print(task + ": " + completionState[pos])
    print("")
        

def editTask():
    showTasks()
    task = input("Choose task to edit: ")
    if task in tasks:
        changedTask = input("Change task: ")
        for i in tasks:
            if i == task:
                tasks[tasks.index(i)] = changedTask 
    else:
        print("There's no such task")
        editTask()
            
def removeTask():
    showTasks()
    task = input("Choose task to remove: ")
    if task in tasks:
        pos = tasks.index(task)
        tasks.remove(task)
        del completionState[pos]
    else:
        print("There's no such task.")
        removeTask()

def completed():
    task = input("Enter task name to mark completed: ")
    if task in tasks:
        pos = tasks.index(task)
        completionState[pos] = "Completed"
        print(task + ": " + completionState[pos])
    else:
        print("There's no such task.")
        completed()

def greetings():
    print("Welcome to my first project by myself!")
    print("This program is to help the users to make a to-do list and keep track on tasks.")

def menu():
    print("-----To-do App Menu-----")
    print("1.New task")
    print("2.Edit task")
    print("3.Remove task")
    print("4.Show tasks")
    print("5.Mark the task completed")
    print("6.Exit")

def main():
    greetings()
    choice = 0
    while(choice != 6):
        menu()
        print("")
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            match choice:
                case 1:
                    newTask()
                case 2:
                    editTask()
                case 3:
                    removeTask()
                case 4:
                    showTasks()
                case 5:
                    completed()
                case 6:
                    break
        else:
            print("Invalid input. Please enter a number.\n")
        
main()