"""
Program 52: Write a Python program to find largest number in a list.
"""

# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the minimum/maximum value, initially set to the first element
minimum = numbers[0]

# Iterate through the list and update the maximum value if a larger number is found
for i in numbers:
    if i > minimum:
        minimum = i

# Print the maximum value
print("The largest number in the list is:", minimum)
