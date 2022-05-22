# https://www.youtube.com/watch?v=t8pPdKYpowI&t=4548s
# 2:03:00

# Data Types so far: Float, String, Integer, Boolean 
# New data type = List
# Lists are used to store multiple items in a single variable

# The goal is to convert days to hours
name_of_unit = "hours"
conversion = 24

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * conversion} {name_of_unit}"


def validate_user_input():
    try: 
        num_of_days = int(num_of_days_element)
        if num_of_days > 0:  
            result = days_to_units(num_of_days)
            print(result)
        elif num_of_days == 0: 
            print("Please enter some number greater than zero.")
        else:
            print("You entered a negative value, which makes absolutely no sense.")    
    except ValueError:
        print("Your input is not a valid number of days, don't try to break my program.")


List = [10, -2, 0, 3, 5] # Example of a list


# Let's use a list as an input for our previous program
user_input = "" # variable initialization
while user_input != "exit":
    user_input = input("Please enter various numbers of days as a comma-separated list and I will convert them to hours:\n")
    # as user_input is a string, we use the split() function to make it a list
    for num_of_days_element in user_input.split(","): # we expect a list of comma-separated values 
        validate_user_input()
    
# 2:13:00