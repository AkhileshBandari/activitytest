"""
Program 74: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D) / H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example: 100,150,180 -> 18,22,24
"""
import math

# Fixed values
C = 50
H = 30

# Function to calculate Q
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))

if __name__ == "__main__":
    # Input comma-separated sequence of D values
    input_sequence = input("Enter comma-separated values of D: ")
    D_values = input_sequence.split(',')

    # Calculate and print Q for each D value
    result = [calculate_Q(int(D)) for D in D_values]
    print(','.join(map(str, result)))
