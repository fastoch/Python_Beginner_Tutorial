# Let's improve our program by preventing the user to enter invalid values
# Validating user input is very important. We don't want to allow the user to break or exploit our program

name_of_unit = "hours"
conversion = 24

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * conversion} {name_of_unit}"


def validate_user_input():
    try: 
        
        num_of_days = int(user_input)
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
    user_input = input("Please enter a number of days and I will convert it to hours:\n")
    validate_user_input()
    print()

# 2:03:00

# This is a single line comment

"""This 
is
a 
multi-line
comment"""