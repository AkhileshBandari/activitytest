"""
Program 58: Write a Python program to Cloning or Copying a list.
"""

# 1. Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list1 = original_list[:]
print(cloned_list1)

# 2. Using the list() constructor
cloned_list2 = list(original_list)
print(cloned_list2)

# 3. Using List Comprehension
cloned_list3 = [item for item in original_list]
print(cloned_list3)
