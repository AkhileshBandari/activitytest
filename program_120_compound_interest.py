"""
Program 120: Create a function that accepts the principal p, the term in years t, the interest rate r,
and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.
Formula: a = p * (1 + (r / n)) ** (n * t)
Examples:
compound_interest(10000, 10, 0.06, 12) -> 18193.97
compound_interest(100, 1, 0.05, 1) -> 105.0
compound_interest(3500, 15, 0.1, 4) -> 15399.26
compound_interest(100000, 20, 0.15, 365) -> 2007316.26
"""

def compound_interest(p, t, r, n):
    # Calculate the compound interest using the formula
    a = p * (1 + (r / n)) ** (n * t)
    # Round the result to the nearest cent
    return round(a, 2)

if __name__ == "__main__":
    print(compound_interest(10000, 10, 0.06, 12))
    print(compound_interest(100, 1, 0.05, 1))
    print(compound_interest(3500, 15, 0.1, 4))
    print(compound_interest(100000, 20, 0.15, 365))
