"""
Program 135: Create a function that takes a list of strings and return a list, sorted from shortest to longest.
Examples:
sort_by_length(["Google", "Apple", "Microsoft"]) -> ["Apple", "Google", "Microsoft"]
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) -> ["Raphael", "Leonardo", "Donatello", "Michelangelo"]
sort_by_length(["Turing", "Einstein", "Jung"]) -> ["Jung", "Turing", "Einstein"]
"""

def sort_by_length(lst):
    return sorted(lst, key=len)

if __name__ == "__main__":
    print(sort_by_length(["Google", "Apple", "Microsoft"]))
    print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))
    print(sort_by_length(["Turing", "Einstein", "Jung"]))
