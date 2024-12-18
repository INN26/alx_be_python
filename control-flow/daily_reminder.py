#Ask the user to input a task description and save it into a task variable
task = input("Enter your task:")

# Prompt for the task’s priority (high/medium/loww)

priority = input("priority (high/medium/low):").lower()
time_bound = input("is it time bound? (yes/no):").lower() #Get time sensitivity

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case"high":
        priority_message ="a high priority task that requires immediate attention today!"
    case"medium":
        priority_message = "a medium priority task you still have time to work on it"
    case"low":
        priority_message = "a low priority task consider completing it when you have free time "
    case _ :
         priority_message = "unknown priority check your input"
if priority == time_bound:
    print(f"'{task}' is {priority_message}!")

else:
    reminder = (f"'{task}' is  {priority_message}!")
#print the final reminder
print(reminder)

         
       





