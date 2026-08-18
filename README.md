Program 1
Write a Python program to print "Hello Python".
In [1]:
In [2]:
In [3]:
1
print("Hello Python")
Hello Python
Program 2
Write a Python program to do arithmetical operations addition and division.
1
2
3
4
5
# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")
Enter the first number for addition: 5
Enter the second number for addition: 6
sum: 5.0 + 6.0 = 11.0
1
2
3
4
5
6
7
8
# Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
print("Error: Division by zero is not allowed.")
else:
div_result = num3 / num4
print(f"Division: {num3} / {num4} = {div_result}")
Enter the dividend for division: 25
Enter the divisor for division: 5
Division: 25.0 / 5.0 = 5.0
Program 3
Write a Python program to find the area of a triangle.
In [4]:
1
2
3
4
5
6
7
# Input the base and height from the user
base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
area = 0.5 * base * height
# Display the result
print(f"The area of the triangle is: {area}")
Enter the length of the base of the triangle: 10
Enter the height of the triangle: 15
The area of the triangle is: 75.0
1/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
Program 4
Write a Python program to swap two variables.
In [5]:
In [6]:
1
2
3
4
5
6
7
8
9
10
11
# Input two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")
Enter the value of the first variable (a): 5
Enter the value of the second variable (b): 9
Original values: a = 5, b = 9
Swapped values: a = 9, b = 5
Program 5
Write a Python program to generate a random number.
1
2
import random
print(f"Random number: {random.randint(1, 100)}")
Random number: 89
Program 6
Write a Python program to convert kilometers to miles.
In [7]:
1
2
3
4
5
6
7
8
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")
Enter distance in kilometers: 100
100.0 kilometers is equal to 62.137100000000004 miles
Program 7
Write a Python program to convert Celsius to Fahrenheit.
2/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [8]:
In [9]:
1
2
3
4
5
6
celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahr
Enter temperature in Celsius: 37
37.0 degrees Celsius is equal to 98.6 degrees Fahrenheit
Program 8
Write a Python program to display calendar.
1
2
3
4
5
6
7
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)
Enter year: 2023
Enter month: 11
November 2023
Mo Tu We Th Fr Sa Su
1  2  3  4  5
6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30
Program 9
Write a Python program to solve quadratic equation.
The standard form of a quadratic equation is:
2
𝑥
𝑎 +𝑏𝑥+𝑐=0
where
a, b and c are real numbers and
𝑎 ≠ 0
The solutions of this quadratic equation is given by:
2
𝑏
(−𝑏 ± ( −4𝑎𝑐 )/(2𝑎)
)1/2
3/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [10]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
import math
# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
# Two real and distinct roots
root1 = (-b + math.sqrt(discriminant)) / (2*a)
root2 = (-b - math.sqrt(discriminant)) / (2*a)
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
elif discriminant == 0:
# One real root (repeated)
root = -b / (2*a)
print(f"Root: {root}")
else:
# Complex roots
real_part = -b / (2*a)
imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
print(f"Root 1: {real_part} + {imaginary_part}i")
print(f"Root 2: {real_part} - {imaginary_part}i")
Enter coefficient a: 1
Enter coefficient b: 4
Enter coefficient c: 8
Root 1: -2.0 + 2.0i
Root 2: -2.0 - 2.0i
Program 10
Write a Python program to swap two variables without temp variable.
In [11]:
1
2
3
4
5
6
7
8
9
10
11
a = 5
b = 10
# Swapping without a temporary variable
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
After swapping:
a = 10
b = 5
4/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
Program 11
Write a Python Program to Check if a Number is Positive, Negative or Zero.
In [12]:
In [13]:
1
2
3
4
5
6
7
num = float(input("Enter a number: "))
if num > 0:
print("Positive number")
elif num == 0:
print("Zero")
else:
print("Negative number")
Enter a number: 6.4
Positive number
Program 12
Write a Python Program to Check if a Number is Odd or Even.
1
2
3
4
5
6
num = int(input("Enter a number: "))
if num%2 == 0:
print("This is a even number")
else:
print("This is a odd number")
Enter a number: 3
This is a odd number
Program 13
Write a Python Program to Check Leap Year.
In [14]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
print("{0} is not a leap year".format(year))
Enter a year: 2024
2024 is a leap year
5/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
Program 14
Write a Python Program to Check Prime Number.
Prime Numbers:
A prime number is a whole number that cannot be evenly divided by any other number
except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
cannot be divided by any other positive integer except for 1 and their own value.
In [15]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 1:
print(f"{num}, is not a prime number")
elif num > 1:
# check for factors
for i in range(2, num):
if (num % i) == 0:
flag = True     
break
# if factor is found, set flag to True
# break out of loop
# check if flag is True
if flag:
print(f"{num}, is not a prime number")
else:
print(f"{num}, is a prime number")
Enter a number: 27
27, is not a prime number
Program 15 ¶
Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
6/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [20]:
In [21]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
# Python program to display all the prime numbers within an interval
lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
# all prime numbers are greater than 1
if num > 1:
for i in range(2, num):
if (num % i) == 0:
break
else:
print(num)
Prime numbers between 1 and 10 are:
2
3
5
7
Program 16
Write a Python Program to Find the Factorial of a Number.
1
2
3
4
5
6
7
8
9
10
num = int(input("Enter a number: "))
factorial = 1
if num <0:
print("Factirial does not exist for negative numbers")
elif num == 0:
print("Factorial of 0 is 1")
else:
for i in range(1, num+1):
factorial = factorial*i
print(f'The factorial of {num} is {factorial}')
Enter a number: 4
The factorial of 4 is 24
Program 17
Write a Python Program to Display the multiplication Table.
7/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [22]:
1
2
3
4
num = int(input("Display multiplication table of: "))
for i in range(1, 11):
print(f"{num} X {i} = {num*i}")
Display multiplication table of: 19
19 X 1 = 19
19 X 2 = 38
19 X 3 = 57
19 X 4 = 76
19 X 5 = 95
19 X 6 = 114
19 X 7 = 133
19 X 8 = 152
19 X 9 = 171
19 X 10 = 190
Program 18
Write a Python Program to Print the Fibonacci sequence.
Fibonacci sequence:
The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, typically starting with 0 and 1. So, the sequence begins with 0 and 1, and
the next number is obtained by adding the previous two numbers. This pattern continues
indefinitely, generating a sequence that looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Mathematically, the Fibonacci sequence can be defined using the following recurrence
relation:
𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛−1)+𝐹(𝑛−2)𝑓𝑜𝑟𝑛 > 1
8/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
In [23]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
print("Fibonacci sequence upto",nterms,":")
print(n1)
# generate fibonacci sequence
else:
print("Fibonacci sequence:")
while count < nterms:
print(n1)
nth = n1 + n2
# update values
n1 = n2
n2 = nth
count += 1
How many terms? 10
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
Program 19
Write a Python Program to Check Armstrong Number?
Armstrong Number:
It is a number that is equal to the sum of its own digits, each raised to a power equal to the
number of digits in the number.
For example, let's consider the number 153:
It has three digits (1, 5, and 3).
If we calculate 
3
1
 + 
3
5
3
+
3
, we get 
1 +125+27
, which is equal to 
153
.
So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
of the number of digits in the number.
Another example is 9474:
It has four digits (9, 4, 7, and 4).
9/95
localhost:8888/notebooks/Piush Kumar Sharma/Basic Python Program.ipynb
11/26/23, 4:53 AM
Basic Python Program - Jupyter Notebook
, which is also
If we calculate 
equal to 
9474
.
4
9
4
4
4
+ + +
7
4
4
, we get 
6561 + 256 +2401 +256
Therefore, 9474 is an Armstrong number as well.
In [25]:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
num = int(input("Enter a number: "))
# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)
# Initialize variables
sum_of_powers = 0
temp_num = num
# Calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
digit = temp_num % 10
sum_of_powers += digit ** num_digits
temp_num //= 10
# Check if it's an Armstrong number
if sum_of_powers == num:
print(f"{num} is an Armstrong number.")
else:
print(f"{num} is not an Armstrong number.")
Enter a number: 9474
9474 is an Armstrong number.
Program 20
Write a Python Program to Find Armstrong Number in an Interval.
