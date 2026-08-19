"""
Program 134: Create a Circle constructor that creates a circle with a radius provided by an argument.
The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r).
Examples:
circy = Circle(11)
circy.getArea() -> 380
circy.getPerimeter() -> 69
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        # Calculate and return the area of the circle rounded to nearest integer
        return round(math.pi * self.radius**2)

    def getPerimeter(self):
        # Calculate and return the perimeter (circumference) of the circle rounded to nearest integer
        return round(2 * math.pi * self.radius)

if __name__ == "__main__":
    circy = Circle(11)
    print(circy.getArea())
    print(circy.getPerimeter())

    circy = Circle(4.44)
    print(circy.getArea())
    print(circy.getPerimeter())
