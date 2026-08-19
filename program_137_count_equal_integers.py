"""
Program 137: Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples:
equal(3, 4, 3) -> 2
equal(1, 1, 1) -> 3
equal(3, 4, 1) -> 0
"""

def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

if __name__ == "__main__":
    print(equal(3, 4, 3))
    print(equal(1, 1, 1))
    print(equal(3, 4, 1))
