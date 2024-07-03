# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
To turn on the time module and call the sleep function. Make it
program to sleep for 5 seconds and then print “Time module imported”."""

import time

# Sleep for 5 seconds
time.sleep(5)

# After 5 seconds, print the message
print("Time module imported")

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Create a module named “calculation.py” that has only one
function inside it. This function should calculate a face of a rectangle.
The program must have two variables length and width. The function to be called
calc_area(length, width)."""

# calculation.py

def calc_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle.
        width (float): Width of the rectangle.

    Returns:
        float: Area of the rectangle.
    """
    return length * width

# This code will be save in a file named "calculation.py". 
# We can use this module in another Python program 
# to calculate the area of a rectangle using the calc_area function. 

# main.py

import calculation

# Define length and width of the rectangle
length = 5
width = 3

# Calculate the area using the calc_area function from the calculation module
area = calculation.calc_area(length, width)

# Print the result
print("Area of the rectangle:", area)


