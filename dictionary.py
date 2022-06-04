# https://www.youtube.com/watch?v=t8pPdKYpowI&t=4548s
# 2:44:00

"""DICTIONARY DATA TYPE
- does not allow duplicate values
- used to store values in |key:value| pairs
"""

# The goal is to convert days to another unit of time

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * days_and_unit[0]} {days_and_unit[1]}"


def validate_user_input():
    try: 
        num_of_days = int(days_and_unit[0])
        if num_of_days > 0:                     # we want to convert only positive integers
            result = days_to_units(num_of_days)
            print(result)
        elif num_of_days == 0: 
            print("Please enter some number greater than zero.")
        else:
            print("You entered a negative value, which makes absolutely no sense.")    
    except ValueError:
        print("Your input is not valid, don't try to break my program.")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and a conversion unit:\n")
    days_and_unit = user_input.split(":") # we wait two inputs separated by a colon => number_of_days:conversion_unit
    print(days_and_unit)
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    
# 2:47:00