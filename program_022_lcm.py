"""
Program 22: Write a Python Program to Find LCM.
"""

# Python Program to find the L.C.M. of two input numbers
def compute_lcm(x, y):
    if x > y:  # choose the greater number
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

if __name__ == "__main__":
    num1 = int(input('Enter the number: '))
    num2 = int(input('Enter the number: '))
    print("The L.C.M. is", compute_lcm(num1, num2))
