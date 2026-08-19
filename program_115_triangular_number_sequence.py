"""
Program 115: This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
1, 3, 6, 10, 15...
Write a function that gives the number of dots with its corresponding triangle number of the sequence.
Examples:
triangle(1) -> 1
triangle(6) -> 21
triangle(215) -> 23220
"""

def triangle(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

if __name__ == "__main__":
    print(triangle(1))
    print(triangle(6))
    print(triangle(215))
