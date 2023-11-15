'''
Script: scope4.py
By: NM
Purpose: Function to find if a number is even
Date: 15OCT23
'''
# Function to find if a number is even
def even_num(number_list):
    # Iterate through each element ('number') in 'number_list'.
    for number in number_list:
        if number % 2 == 0:
            return True
        else:
            return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = even_num(numbers)
print(result)