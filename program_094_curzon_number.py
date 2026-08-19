"""
Program 94: In this challenge, establish if a given integer num is a Curzon number.
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
Examples:
is_curzon(5) -> True (2^5 + 1 = 33, 2*5 + 1 = 11, 33 % 11 == 0)
is_curzon(10) -> False (2^10 + 1 = 1025, 2*10 + 1 = 21, 1025 % 21 != 0)
is_curzon(14) -> True (2^14 + 1 = 16385, 2*14 + 1 = 29, 16385 % 29 == 0)
"""

def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

if __name__ == "__main__":
    # Test cases
    print(is_curzon(5))
    print(is_curzon(10))
    print(is_curzon(14))
