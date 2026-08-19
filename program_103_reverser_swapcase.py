"""
Program 103: The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
Examples:
reverse("Hello World") -> "DLROw OLLEh"
reverse("ReVeRsE") -> "eSrEvEr"
reverse("Radar") -> "RADAr"
"""

def reverse(input_str):
    # Reverse the string and swap the case of characters
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

if __name__ == "__main__":
    print(reverse("Hello World"))
    print(reverse("ReVeRsE"))
    print(reverse("Radar"))
