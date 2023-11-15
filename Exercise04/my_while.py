'''
Script: my_while.py
By: NM
Purpose: Creating a while loop to iterate over a list of numbers
Date: 15OCT23
'''
x = 0
while x < 10:
    print(f"X is = {x}")
    x = x + 1
else:
    print(f"As x is now = {x}, we are all finished")

# This code sets up an endless loop (while True) 
try:
    print("press [ctrl][c] to exit")
    while True:
        pass 
    # Exception handling. Print the message before exiting.
except KeyboardInterrupt:
    print("Loop ended with Ctrl+C")


