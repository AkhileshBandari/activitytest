"""
Program 40: Write a Python Program to Sort Words in Alphabetic Order.
"""

# Program to sort alphabetically the words from a string provided by the user
my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.capitalize() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words
print("The sorted words are:")
for word in words:
    print(word)
