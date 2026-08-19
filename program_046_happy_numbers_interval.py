"""
Program 46: Write a Python program to print all happy numbers between 1 and 100.
"""

def is_happy_number(num):
    seen = set()
    
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
        
    return num == 1

if __name__ == "__main__":
    happy_numbers = []
    for num in range(1, 101):
        if is_happy_number(num):
            happy_numbers.append(num)

    print("Happy Numbers between 1 and 100:")
    print(happy_numbers)
