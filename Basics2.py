# A variable is only available from inside the region it is created
# Global scope = variables available from within any scope
# Local scope = variables created inside a function, can only be used inside that function

# global variables
var1 = 10
var2 = "code"

# a function with its local variables
def square(a):
    print(f"The square of {a} equals {a*a}")
    print()

# a function to check the scope of variables
def scope_check():
    var3 = "variable inside function"
    print(var1) # This function knows global variables "var1" and "var2"
    print(var2)
    print(var3) # it also knows its local variable "var3"
    # print(a) # But it doesn't know the variable "a", only the square function knows "a"
    print()
    
square(4)  

scope_check()


# User input
# input() is a built-in function provided by Python language itself
user_input = input("Hey user, enter a number of days and I will convert it to hours.\n") # \n asks our program to create a new line
print(f"{user_input} days are {int(user_input)*24} hours.")
print()

# Function with return values
def sum(a, b):
    return (f"{a} + {b} = {a + b}") 

# Now that our function returns some value, we can store this value in a new variable and print it out
var4 = sum(13, 11)
print(var4)
print()

# we can also ask the user to input two values he wants to add
# input() always returns a string, so we must convert to integers before using the sum function
user_input1 = input("Please enter the first number of your sum:\n")
a = int(user_input1) # convert a variable into another type is called "casting"
user_input2 = input("Please enter the second number of your sum:\n")
b = int(user_input2)
result = sum(a, b)
print() # just skip a line
print(result)
print()

