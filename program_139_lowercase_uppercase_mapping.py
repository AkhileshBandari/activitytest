"""
Program 139: Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples:
mapping(["p", "s"]) -> {'p': 'P', 's': 'S'}
mapping(["a", "b", "c"]) -> {'a': 'A', 'b': 'B', 'c': 'C'}
mapping(["a", "v", "y", "z"]) -> {'a': 'A', 'v': 'V', 'y': 'Y', 'z': 'Z'}
"""

def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result

if __name__ == "__main__":
    print(mapping(["p", "s"]))
    print(mapping(["a", "b", "c"]))
    print(mapping(["a", "v", "y", "z"]))
