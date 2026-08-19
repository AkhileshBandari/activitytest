"""
Program 80: Write a program to check the validity of password input by users against criteria:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length: 6, Maximum length: 12
"""
import re

# Function to check if a password is valid
def is_valid_password(password):
    # Check the length of the password
    if 6 <= len(password) <= 12:
        # Check if the password matches all criteria using regular expressions
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False

if __name__ == "__main__":
    # Accept input from the user as comma-separated passwords
    passwords = input("Enter passwords separated by commas: ").split(',')

    # Initialize a list to store valid passwords
    valid_passwords = []

    # Iterate through the passwords and check their validity
    for psw in passwords:
        if is_valid_password(psw):
            valid_passwords.append(psw)

    # Print the valid passwords separated by commas
    print(','.join(valid_passwords))
