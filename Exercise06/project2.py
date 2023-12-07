'''
Script: project2.py
By: NM
Purpose: Import a module from another module into the project then printing the results out
Date: 2OCT23
'''
import mylib.cube as mycube
import mylib.square as mysquare

print(mycube.cube_text, mycube.cube(3))
print(mysquare.square_text, mysquare.square(3))

print(f"This module is called {mycube.__name__}") 