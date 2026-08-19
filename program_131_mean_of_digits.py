"""
Program 131: Create a function that returns the mean of all digits.
Examples:
mean(42) -> 3
mean(12345) -> 3
mean(666) -> 6
"""

def mean(n):
    # Convert the number to a string to iterate through its digits
    n_str = str(n)
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in n_str)
    
    # Calculate the mean by dividing the sum by the number of digits
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count
    
    return int(digit_mean)

if __name__ == "__main__":
    print(mean(42))
    print(mean(12345))
    print(mean(666))
