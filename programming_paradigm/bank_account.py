#define a class bank account
class BankAccount:

     #initialise an account balance
      def __init__(self, initial_balance = 0):
            
      #initialise the bank account   
            self.account_balance = initial_balance
      def deposit(self, amount):
      #deposit amount in the bank account
            if amount > 0:
                  self.account_balance += amount
            else:
                  print("deposit amount must be positve")
                  
      def withdraw(self, amount):
      #withdaraw amount in the bank account if funds are sufficient
            if amount > self.account_balance:
                 return False
            
            else:
                  self.account_balance -= amount
                  return True
                              
            
      def display_balance(self):  
      #print the current balance in a user-friendly format. 
            print(f"Current Balance: ${self.account_balance :.2f}")   


 




 
      
       