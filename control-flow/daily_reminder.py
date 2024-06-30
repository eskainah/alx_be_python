task = input("Enter your task: ")
priority = input("Please enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

match priority:
    case 'high': 
       reminder = f"'{task}' is a {priority} priority task "
    case 'medium': 
       reminder = f"'{task}' is a {priority} priority task "
    case 'low': 
       reminder = f"'{task}' is a {priority} priority task "
        
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completing it when you have free time."

print(reminder)