task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f"Reminder: {task} is a {priority} priority task."
    case "medium":
        reminder = f"{task} is a {priority} priority task."
    case "low":
        reminder = f"note: {task} is a {priority} priority task."
    case _:
        reminder = f"{task} has an unspecified priority."

if time_bound == "yes":
    print(f"{reminder} This requires immediate attention today!")
else:
    print(f"{reminder} Consider completing it when you have free time.")
print(reminder)
