"""
Program 56: Write a Python program to print odd numbers in a List.
"""

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a list comprehension to filter odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the odd numbers
print("Odd numbers in the list:", odd_numbers)
