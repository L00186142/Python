'''
Script: library2.py
By: NM
Purpose: Write functions to derive trigonometry values from first principles. Using the math library.
Date: 2OCT23
'''
from math import sqrt
#from math import sin, cos, radians
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))