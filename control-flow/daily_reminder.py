Task = input("Enter your task: ")
Priority = input("Please enter the task's priority (high, medium, low): ")
Time_Bound = input("Is the task time-bound? (yes or no): ")

match Priority:
    case 'high': 
       reminder = f"'{task}' is a {priority} priority task "
    case 'medium': 
       reminder = f"'{task}' is a {priority} priority task "
    case 'low': 
       reminder = f"'{task}' is a {priority} priority task "
        
if Time_Bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completing it when you have free time."

print(reminder)