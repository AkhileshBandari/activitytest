"""
Program 75: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,.., Y-1.
"""

# Input two digits, X and Y
X, Y = map(int, input("Enter two digits (X, Y): ").split(','))

# Initialize a 2D array filled with zeros
array = [[0 for j in range(Y)] for i in range(X)]

# Fill the array with values i * j
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j

# Print the 2D array
for row in array:
    print(row)
