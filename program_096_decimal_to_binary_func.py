"""
Program 96: Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.
Examples:
binary(1) -> "1"
binary(5) -> "101"
binary(10) -> "1010"
"""

def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"

if __name__ == "__main__":
    print(binary(1))
    print(binary(5))
    print(binary(10))
