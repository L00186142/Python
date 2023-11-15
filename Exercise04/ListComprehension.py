'''
Script: ListComprehension.py
By: NM
Purpose: Creating a string with a list comprehension function
Date: 15OCT23
'''
my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)

print(my_list)

my_string = "Morning Folks!"
my_list = [letter for letter in my_string]
print(my_list)
# The comprehension takes an element, for an element, from a string or other iterable object.
my_list = [number for number in range(0,20)]
print(my_list)
# perform operations on variables
my_list = [number * 10 for number in range(0,20)]
print(my_list)
# adding an if statement to further filter the output
my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)
# list of depths in feet on a US Sonar log file and I want to convert them to meters, rounded to 2 decimal places.
conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)

# Exercise 
# I have an American air conditioner system returning temperatures, 
Kelvin_Temp = [323, 333, 343, 353, 363, 373, 400, 450, 500, 600]
# but I need the temperatures in standard units. 
# Create a list of 10 values in degrees Kelvin. 
# Write a code block to print these values in Celsius and Fahrenheit.

for K in Kelvin_Temp:
    # Kelvin to Celsius: C = K - 273 (C = K - 273.15 if you want to be more precise)
    C = K - 273.15
    # Kelvin to Fahrenheit: F = 9/5(K - 273) + 32 or F = 1.8(K - 273) + 32
    F = (9/5) * (K - 273) + 32
    # Print the results in Celsius and Fahrenheit and return them to the calling function. 
    # This will return the temperature values to 2 decimal places.
    print(f"{K} Kelvin is {C:.2f}C and {F:.2f}F")




