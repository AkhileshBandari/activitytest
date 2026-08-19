"""
Program 136: Create a function that validates whether three given integers form a Pythagorean triplet.
The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.
Examples:
is_triplet(3, 4, 5) -> True (3^2 + 4^2 = 25 == 5^2)
is_triplet(13, 5, 12) -> True (5^2 + 12^2 = 169 == 13^2)
is_triplet(1, 2, 3) -> False (1^2 + 2^2 = 5 != 3^2)
"""

def is_triplet(a, b, c):
    # Sort the numbers in ascending order
    sorted_numbers = sorted([a, b, c])
    # Check if the sum of squares of the two smaller numbers equals the square of the largest
    return sorted_numbers[0] ** 2 + sorted_numbers[1] ** 2 == sorted_numbers[2] ** 2

if __name__ == "__main__":
    print(is_triplet(3, 4, 5))
    print(is_triplet(13, 5, 12))
    print(is_triplet(1, 2, 3))
