#arithmetic_operations.py 
def perform_operation(num1, num2, operation):
   if operation == 'add':
        return num1 + num2
   elif operation == 'subtract':
        return num1 - num2
   elif operation == 'multiply':
        return  num1 * num2
   elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return"Error: Cannot divide by zero."
        else: 
            return num1 / num2
    
           

    
