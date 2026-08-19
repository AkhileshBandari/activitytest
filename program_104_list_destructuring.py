"""
Program 104: With Python 3, you can assign variables from lists using destructuring assignment:
first, *middle, last = writeyourcodehere
"""

writeyourcodehere = [1, 2, 3, 4, 5, 6]

# Unpack the list into variables
first, *middle, last = writeyourcodehere

print(first)
print(middle)
print(last)
