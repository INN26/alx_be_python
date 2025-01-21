class Calculator:

    # Class attribute
     calculation_type = "Arithmetic Operations"

    #static decorator return the sum
     @staticmethod 
     def add(a, b):
        return a + b
    
 # Class method: Takes the class as its first parameter (cls)
     @classmethod
     def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

