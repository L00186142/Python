'''
Script: scope3.py
By: NM
Purpose: Function to check if a number is in a list
Date: 15OCT23
'''
# Function to check if a number is in a list
def find_num(number_list: list, number: int)->bool:
    # Iterate through each element ('iterate_number') in 'number_list'.
    for iterate_number in number_list:
        # Check iterated numnber is = to number
        if iterate_number == number:
            print(f"{number} is in the list")
            return True
        # else:
        #     print(f"{number} is not in the list")
        #     pass
    return False
# print(find_num([1,2,3,4,5,6,7], 3)) 
# Check if the number is inside the list so add a number that is in the list to be true
result = find_num([1,2,3,4,5,6,7,8], 3)
print(result)