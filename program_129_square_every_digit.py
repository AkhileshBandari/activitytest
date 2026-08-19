"""
Program 129: Create a function that squares every digit of a number.
Examples:
square_digits(9119) -> 811181
square_digits(2483) -> 416649
square_digits(3212) -> 9414
"""

def square_digits(n):
    # Convert the number to a string to iterate through its digits
    num_str = str(n)
    
    # Initialize an empty string to store the squared digits
    result_str = ""
    
    # Iterate through the digits
    for digit in num_str:
        # Square the digit and convert it back to an integer
        squared_digit = int(digit) ** 2
        
        # Append the squared digit to the result string
        result_str += str(squared_digit)
        
    return int(result_str)

if __name__ == "__main__":
    print(square_digits(9119))
    print(square_digits(2483))
    print(square_digits(3212))
