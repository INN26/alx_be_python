# prompt the user to enter a positive integer that represents the size of the pattern 
size = int(input("Enter the size of the pattern:"))


#use a while loop to iterate through each row
current_row = 0
while current_row <  size:
       #use for loop to print asterisks for each row 
        for j in range(size):#Loop through each column in the row
                 print("*", end="") #Print without advancing to a new line
     
        print()  # Move to a new line after each row of asterisks
        current_row += 1 #increament in the while loop to avoid infinite loops