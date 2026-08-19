"""
Program 123: Create a function that takes in two lists and returns True if the second list follows
the first list by one element, and False otherwise. In other words, determine if the second list is the first list shifted to the right by 1.
Examples:
simon_says([1, 2], [5, 1]) -> True
simon_says([1, 2], [5, 5]) -> False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) -> True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) -> False
"""

def simon_says(list1, list2):
    # Check if the second list is the first list shifted to the right by 1
    return list1[:-1] == list2[1:]

if __name__ == "__main__":
    print(simon_says([1, 2], [5, 1]))
    print(simon_says([1, 2], [5, 5]))
    print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
    print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))
