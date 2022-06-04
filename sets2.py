# https://www.youtube.com/watch?v=t8pPdKYpowI&t=4548s
# 2:32:00

""" 
Basic set operations:
- create a set
- access items only via a loop
- add an item to the set
- remove an item from the set
"""

"""
Set are not lists:
- sets do NOT allow DUPLICATE values
- items in a set do not have a defined order
- items cannot be referred to by index, we can only access them via a loop
- items cannot be changed, only added|removed
"""

my_set = {"Jan","Feb","Mar","Apr"}
for element in my_set:
    print(element)
print()
    
my_set.add("May")
print(my_set)
print()

my_set.remove("Jan")
print(my_set)
print()

# 2:36:00