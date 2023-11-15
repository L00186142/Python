'''
Script: scope.py
By: NM
Purpose: Define a function called 'divisible' that takes two integer arguments: numerator and denominator.
Date: 15OCT23
'''
# my_string = "global"

# def my_function():
#     my_string = "enclosing"
#     def nested_function():
#         my_string = "local"
#         print(my_string)
#     nested_function()
#     return my_string

# # Print the variable my_string
# print(my_string)
# # Print the output of the function, my_function
# print(my_function())





# Define a function called 'divisible' that takes two integer arguments: numerator and denominator.
# It returns a boolean value indicating whether the numerator is evenly divisible by the denominator.

def divisible(numerator: int, denominator: int) -> bool:
    # Check if the remainder of the division of 'numerator' by 'denominator' is equal to 0.
    # If it is, return True, indicating that 'numerator' is divisible by 'denominator'.
    return numerator % denominator == 0

# Call the 'divisible' function with 'numerator' set to 30 and 'denominator' set to 4.
# This will check if 30 is evenly divisible by 4 and print the result, which is True.
print(divisible(30, 4))