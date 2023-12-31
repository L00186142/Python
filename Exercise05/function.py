
'''
Script: function.py
By: NM
Purpose: Creating a function
Date: 15OCT23
'''
def name_of_function(first_name):
    """
    Simple test function
    """
    print(f"Yoo hoo, hello {first_name}!")

name_of_function("NM")

# TypeError: calculate_circumference() missing 1 required positional argument: 'radius'
# def calculate_circumference(radius = 1):
#     """
#     Calculate the circumference of a circle based on its radius
#     """
#     return 2 * 3.142 * radius 

# a = calculate_circumference(5)
# print("Circumference of a circle " + str(a))


def calculate_circumference(radius):
    """
    Calculate the circumference of a circle based on its radius

    """
    return 2 * 3.142 * radius 

# Get a radius value as a string
r = input("Provide a radius value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_circumference(r_float)
print(a)

# Add all the numbers together inside a function. Can use sum()
def auto_adder(*my_numbers):
    final_number = 0
    for number in my_numbers:
        final_number = final_number + number
    return final_number

print(auto_adder(12,34,23,66,8, 99))
