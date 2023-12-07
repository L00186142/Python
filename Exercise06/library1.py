'''
Script: library1.py
By: NM
Purpose: write functions to derive trigonometry values from first principles.
Date: 2OCT23
'''

# Import the math library from the math module specified in the project
import math
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))