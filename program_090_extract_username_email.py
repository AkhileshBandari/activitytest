"""
Program 90: Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
"""

def extract_username(email):
    # Split the email address at '@' to separate the username and domain
    parts = email.split('@')
    
    # Check if the email address has the expected format
    if len(parts) == 2:
        return parts[0]  # The username is the first part
    else:
        return "Invalid email format"

if __name__ == "__main__":
    try:
        email = input("Enter an email address: ")
        username = extract_username(email)
        print(username)
    except ValueError:
        print("Invalid input. Please enter a valid email address.")
