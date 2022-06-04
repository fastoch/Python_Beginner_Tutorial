# https://www.youtube.com/watch?v=t8pPdKYpowI&t=4548s
# 2:44:00
# DICTIONARY DATA TYPE

# The goal is to convert days to hours
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


user_input = "" # variable initialization
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and conversion unit:\n")
    list_of_numbers = user_input.split(":") # we wait two inputs separated by a colon => number_of_days:conversion_unit
    for num_of_days_element in user_input.split(","): # we expect a list of comma-separated values 
        validate_user_input()
    
# 2:47:00