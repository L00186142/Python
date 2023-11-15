'''
Script: Tuples.py
By: NM
Purpose: Creating a tuple of numbers and getting the type of the tuple
Date: 10SEPT23
'''
my_list = ["One", "Two", "Three", "Four"]
my_tuple = ("One", "Two", "Three", "Four")
print(type(my_list))
print(type(my_tuple))
print("\n")

my_tuple = ["One", "Two", "Three","One"]
# How many times does "one" appear in the tuple?
print(my_tuple.count("One"))
# At what position in the tuple can I first find "One"?
print(my_tuple.index("One"))

# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Convert the tuple to a list to make changes
my_list = list(my_tuple)

# Change the value at a specific index
index_to_change = 2
new_value = 10
my_list[index_to_change] = new_value

# Convert the list back to a tuple (if necessary)
my_tuple = tuple(my_list)

# Verify that the tuple has changed
print(my_tuple)
