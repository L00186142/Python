'''
Script: lambda.py
By: NM
Purpose: Creating a lambda function that returns the area of a circle based on its radius
Date: 15OCT23
'''
# lambda arguments : expression
circumference = lambda radius : 2 * 3.142 * radius
area = lambda radius : 3.142 * radius * radius
radius = 5
print(circumference(radius), area(radius))