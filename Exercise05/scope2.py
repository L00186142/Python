'''
Script: scope2.py
By: NM
Purpose: Function to get the modules of 2 numbers
Date: 15OCT23
'''
# Function to get the modules of 2 numbers
def divisible(numerator: int, denominator: int) -> bool:
    # return true
    print(numerator % denominator)
    return ((numerator % denominator) == 0)

print(divisible(30, 4))

def divisible(numerator: int, denominator: int) -> bool:
    # return True
    print(numerator % denominator)
    if 2:
      print("2 is the remainder")
      return False
    else:
      print("0 is the remainder")
      return True
    
    # return a true value
    


print(divisible(30, 6))

