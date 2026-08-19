"""
Program 77: Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.
"""

# Accept input from the user
input_sequence = input("Enter a sequence of whitespace-separated words: ")

# Split the input into words and convert it into a set to remove duplicates
words = set(input_sequence.split())

# Sort the unique words alphanumerically
sorted_words = sorted(words)

# Join the sorted words into a string with whitespace separation
result = ' '.join(sorted_words)

# Print the result
print("Result:", result)
