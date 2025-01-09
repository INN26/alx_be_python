#shopping_list_manager.py
shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

#Prompt the user for the item name and append it
def add_item():
    item =input("[\"]Enter the item to add: [\"]")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

#Ask the user for the item name and remove it 
def remove_item():
    item = input("Enter  item you want to remove:")
    if item in shopping_list:
       shopping_list.remove(item)
       print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

 #display options to view list
def view_list():
    if shopping_list:
        print("shopping list:") 
        for i, item in shopping_list:
         print(f"{i} . {item}")  
    else:
        print("The shopping list is empty.")  

 
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1': 
            add_item()# Prompt for and add an item
            pass
        elif choice == '2':
            remove_item() # Prompt for and remove an item
            pass
        elif choice == '3':
            view_list() # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    



