Task = input("Enter your task: ")
Priority = input("Priority (high, medium, low): ")
Time_Bound = input("Is the task time-bound? (yes or no): ")

match Priority:
    case 'high': 
        reminder = f"'{Task}' is a {Priority} priority task "
    case 'medium': 
       reminder = f"'{Task}' is a {Priority} priority task "
    case 'low': 
       reminder = f"'{Task}' is a {Priority} priority task "
        
if Time_Bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "consider completing it when you have free time."

print(reminder)