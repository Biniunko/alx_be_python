task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match ( priority, time_bound):
    case (x,y) if x =="high" and y =="yes":
        print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
    case (x,y) if x =="medium" and y =="yes":
        print(f"Reminder: {task} is a medium priority task that requires attention sonn")
    case (x,y) if x =="low" and y=="yes":
        print(f"Reminder: {task} is low priority task that don't require immediiate attention")
    case (x,y) if x=="low" and y=="no":
        print(f"note: {task} is a low priority task. Consider completing it when you have free time.") 
    case _:
        print("invalid input")
