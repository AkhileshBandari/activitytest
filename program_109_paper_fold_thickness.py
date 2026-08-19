"""
Program 109: Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times.
The paper starts off with a thickness of 0.5mm.
Examples:
num_layers(1) -> "0.001m"
num_layers(4) -> "0.008m"
num_layers(21) -> "1048.576m"
"""

def num_layers(n):
    initial_thickness_mm = 0.5  # Initial thickness in millimeters
    final_thickness_mm = initial_thickness_mm * (2 ** n)
    final_thickness_m = final_thickness_mm / 1000  # Convert millimeter to meter
    return f"{final_thickness_m:.3f}m"

if __name__ == "__main__":
    print(num_layers(1))
    print(num_layers(4))
    print(num_layers(21))
