"""
Program 126: Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
Examples:
is_in_order("abc") -> True
is_in_order("edabit") -> False
is_in_order("123") -> True
is_in_order("xyzz") -> True
"""

def is_in_order(s):
    return s == ''.join(sorted(s))

if __name__ == "__main__":
    print(is_in_order("abc"))
    print(is_in_order("edabit"))
    print(is_in_order("123"))
    print(is_in_order("xyzz"))
