#simlpe calculator using match case
# Ask  the user to enter two number
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

#Ask for the type of operation they’d like to perform
print("Choose the operation (+, -, *, /):")
operation = input("the type of operation you would like to perform:")

#Use match case to perform the operation 

match operation:
    case"+":
        result = num1 + num2
        print(f"The result is {result}.")
    case"-":
        result = num1 - num2
        print(f"The result is {result}.")
    case"*":
        result = num1 * num2
        print(f"The result is {result}.")
    case"/":
        if num2 == 0: # handle the division by zero case gracefully
            print("cannot divide by zero.")
    case"/":
        result = num1 / num2
        print(f"The result is {result}.")


