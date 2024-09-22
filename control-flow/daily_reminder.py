task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
       print(f"Reminder: '{task}' is a {priority} priority task")
    case "medium":
        print(f"'{task}' is a {priority} priority task.")
    case "low":
       print(f"Note: '{task}' is a {priority} priority task.")
    case _:
       print(f"'{task}' has an unspecified priority.")
if time_bound == "yes":
    print(f"that requires immediate attention today!")
else:
   print(f"Consider completing it when you have free time.")
