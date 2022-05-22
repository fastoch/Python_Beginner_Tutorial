# DATA TYPES
print("whatever") # Here's a string
print(200) # An integer
print(29.99) # A float
print() # prints an empty line


# HOW MANY MINUTES IN X DAYS?
# Variables
# String concatenation
days = 20
minutes = days*24*60
sec = minutes*60
print("There are " + str(minutes) + " minutes in " + str(days) + " days.")
print()

# The following syntax only works for Python 3.6 and later versions
# f stands for format
print(f"There are {minutes} minutes in {days} days.")
print(f"There are {sec} seconds in {days} days.")
print()

# Python variables are dynamically typed, not statically typed
# We don't have to precise the variable type, only its name and value


# FUNCTIONS 
# To avoid duplicating the same code again and again, we define functions

# declaring variables
calculation = 24*60
unit_name = "minutes"

# defining the function
def days_to_units():
    print(f"20 days are {20*calculation} {unit_name}")
    print("All good!")
    print()
    
days_to_units() # calling the function


# FUNCTIONS WITH PARAMETERS
# parameters are also called arguments
def days_to_units2(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation} {unit_name}")
    print("All good!")
    print()

days_to_units2(10)
days_to_units2(20)    
days_to_units2(30)


def days_to_units3(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation} {unit_name}")
    print(custom_message)
    print()
    
days_to_units3(10, "Macron est une sous-merde")
days_to_units3(20, "Ses électeurs sont encore pire")