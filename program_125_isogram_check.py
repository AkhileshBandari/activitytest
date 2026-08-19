"""
Program 125: An isogram is a word that has no duplicate letters.
Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples:
is_isogram("Algorism") -> True
is_isogram("PasSword") -> False
is_isogram("Consecutive") -> False
"""

def is_isogram(word):
    word = word.lower()
    
    # Create a set to store unique letters in the word
    unique_letters = set()
    
    for letter in word:
        # If the letter is already in the set, it's not an isogram
        if letter in unique_letters:
            return False
        # Otherwise, add it to the set
        unique_letters.add(letter)
        
    return True

if __name__ == "__main__":
    print(is_isogram("Algorism"))
    print(is_isogram("PasSword"))
    print(is_isogram("Consecutive"))
