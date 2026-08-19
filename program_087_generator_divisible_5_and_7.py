"""
Program 87: Please write a program using generator to print the numbers which can be divisible
by 5 and 7 between 0 and n in comma separated form while n is input by console.
"""

def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

if __name__ == "__main__":
    try:
        n = int(input("Enter a value for n: "))
        result = divisible_by_5_and_7(n)
        print(','.join(map(str, result)))
    except ValueError:
        print("Invalid input. Please enter a valid integer for n.")
