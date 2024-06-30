task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high': 
        reminder = f"'{task}' is a {priority} priority task "

        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
        else:
            reminder += "consider completing it when you have free time."
       
    case 'medium': 
        reminder = f"'{task}' is a {priority} priority task "

        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
        else:
            reminder += "consider completing it when you have free time."

    case 'low': 
        reminder = f"'{task}' is a {priority} priority task "
        
        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
        else:
            reminder += "consider completing it when you have free time."
        
print("Reminder: ", reminder)