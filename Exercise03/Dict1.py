'''
Script: Dict1.py
By: NM
Purpose: Creating a dictionary then storing it in a list
Date: 10SEPT23
'''
my_dictionary = {"name": "John", "age": 30}
print(my_dictionary)
print("Age of John " + str(my_dictionary["age"]))

my_dictionary = {"name": "John", "age": 30 , "Occupation": "Software Engineer"}

print(my_dictionary)        
print("Works as a " + my_dictionary["Occupation"])

my_dictionary = {"name": "John", "age": 30 , "Occupation": "Software Engineer"}
print(my_dictionary)
my_dictionary["Salary"] = "Try Harder"
print(my_dictionary)

# Create the initial dictionary
my_dictionary = {"name": "John", "surname": "Doe", "age": 30, "Occupation": "Software Developer"}
print(my_dictionary)
# Add a key: value pair to the dictionary
my_dictionary["Salary"] = "Try Harder"
print(my_dictionary)
# Edit one value in the dictionary
my_dictionary["Occupation"] = "Student"

print(my_dictionary)    

# Delete a key: value pair from the dictionary  
del my_dictionary["Occupation"]
print(my_dictionary)

# Print the keys of the dictionary
keys = my_dictionary.keys()
print(keys)

# Print the values of the dictionary
values = my_dictionary.values()
print(values)

# Print the items of the dictionary 
items = my_dictionary.items()
print(items)




