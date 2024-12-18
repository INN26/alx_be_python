#Ask the user to input a number for which they want to see the multiplication table: 
number =int(input("Enter a number to see its multiplication table:"))


#Generate and print the multiplication table
#loop through numbers 1 to 10

for i in range (1,11):

# calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
 product = number * i
 print(f"{number} * {i} = {product}")
   
