"""
Program 97: Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
Examples:
evenly_divisible(1, 10, 20) -> 0
evenly_divisible(1, 10, 2) -> 30
evenly_divisible(1, 10, 3) -> 18
"""

def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b + 1):
        if num % c == 0:
            total += num
    return total

if __name__ == "__main__":
    print(evenly_divisible(1, 10, 20))
    print(evenly_divisible(1, 10, 2))
    print(evenly_divisible(1, 10, 3))
