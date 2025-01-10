"""Define Global Conversion Factors"""
FAHRENHEIT_TO_CELSIUS_FACTOR =5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

#Implement Conversion Functions
#convert Fahrenheit to celcius
def convert_to_celsius(fahrenheit):
        return(fahrenheit -32) * 5/9

#convert Celcius to Fahrenheit
def convert_to_fahrenheit(celsius):
        return(celsius * 9/5) + 32

# function for User interaction
def main():
     temp = float(input("Enter the temperature to convert:"))
     unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
     if unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is equivalent to {converted:.2f}°F.")
     elif unit == 'F':
          converted = convert_to_celsius(temp)
          print(f"{temp}°F is equivalent to {converted:.2f}°C.")
     else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
     #Run the program
if __name__ == "__main__":
    main()

