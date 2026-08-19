"""
Program 113: Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself.
Examples:
add_indexes([0, 0, 0, 0, 0]) -> [0, 1, 2, 3, 4]
add_indexes([1, 2, 3, 4, 5]) -> [1, 3, 5, 7, 9]
add_indexes([5, 4, 3, 2, 1]) -> [5, 5, 5, 5, 5]
"""

def add_indexes(lst):
    # Use list comprehension to add index to each element
    return [i + val for i, val in enumerate(lst)]

if __name__ == "__main__":
    print(add_indexes([0, 0, 0, 0, 0]))
    print(add_indexes([1, 2, 3, 4, 5]))
    print(add_indexes([5, 4, 3, 2, 1]))
