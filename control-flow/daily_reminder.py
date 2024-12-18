#Ask the user to input a task description and save it into a task variable
task = input("Enter your task:")

# Prompt for the task’s priority (high/medium/loww)

priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time bound? (yes/no):").lower() #Get time sensitivity

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case"high":
        priority_message ="a high priority task that requires immediate attention today!"
    case"medium":
        priority_message = "a medium priority task you still have time to work on it"
    case _ :
         priority_message = "a low priority task consider completing it when you have free time "
#final reminder based on sensitivity
if time_bound == "yes":
     print(f"Reminder: '{task}' is {priority_message}!")

else:
     print(f"Note: '{task}' is  {priority_message}!")


         
       





