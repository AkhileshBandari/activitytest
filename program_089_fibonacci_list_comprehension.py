"""
Program 89: The Fibonacci Sequence is computed based on recurrence relation.
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
"""

def fibonacci(n):
    sequence = [0, 1]  # Initializing the sequence with the first two Fibonacci numbers
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter a value for n: "))
        result = fibonacci(n)
        print(','.join(map(str, result)))
    except ValueError:
        print("Invalid input. Please enter a valid integer for n.")
