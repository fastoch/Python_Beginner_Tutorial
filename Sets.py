# https://www.youtube.com/watch?v=t8pPdKYpowI&t=4548s
# 2:27:00

# Sets are another built-in data type of Python (along with Lists)
# As with Lists, sets are used to store multiple items of data, but they do NOT allow duplicate values

name_of_unit = "hours"
conversion = 24

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * conversion} {name_of_unit}"


def validate_user_input():
    try: 
        num_of_days = int(num_of_days_element)
        # we want to convert only positive integers
        if num_of_days > 0:  
            result = days_to_units(num_of_days)
            print(result)
        elif num_of_days == 0: 
            print("Please enter some number greater than zero.")
        else:
            print("You entered a negative value, which makes absolutely no sense.")    
    except ValueError:
        print("Your input is not a valid number of days, don't try to break my program.")
        
user_input = "" 
while user_input != "exit":
    user_input = input("Please enter various numbers of days as a comma-separated list and I will convert them to hours:\n")
    list_of_numbers = user_input.split(",")
    print()
    
    print(f"user input type is: {type(list_of_numbers)}")
    print("This is a List:")
    print(user_input.split(",")) # prints the entire user input
    for num_of_days_element in list_of_numbers: 
        validate_user_input()
    print()
    
    print(f"user input type is: {type(set(list_of_numbers))}")
    print("This is a Set:")
    print(set(list_of_numbers)) # filters duplicate values
    for num_of_days_element in set(list_of_numbers): # the set function will filter duplicate values
        validate_user_input()
    print()

        
    print() # skip a line between two iterations of my program
    
# 2:30:00