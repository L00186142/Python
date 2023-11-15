'''
Script: list1.py
By: NM
Purpose: Creating a list of numbers and characters then slice them

Revision History:
Alpha version:      10SEPT23

Notes:
Do not edit the values in this script, all fixed settings are maintained at .\settings\tcp.py
This script has no error handling, by design.
'''
my_list = [1,2,3,4,"A"]
a = len(my_list)
print(a)
sliced_list = my_list[1:3:1]
print(sliced_list)
my_char = my_list[-1]
print(my_char)