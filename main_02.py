# Lesson 05 / Homework 02
# There is a list of integers filled with random numbers.
# Based on the data of this array, you need to:
# Create a list of integers containing only even numbers from the first list;
# Create a list of integers containing only odd numbers from the first list;
# Create a list of integers that contains only negative numbers from the first list;
# Create a list of integers containing only positive numbers from the first list.

import random

try:
    random_list = [random.randint(-20, 20) for _ in range(10)]

    even_numbers = [x for x in random_list if x % 2 == 0]
    odd_numbers = [x for x in random_list if x % 2 != 0]
    negative_numbers = [x for x in random_list if x < 0]
    positive_numbers = [x for x in random_list if x > 0]

    print("Random List:", random_list)
    print("List of even numbers:", even_numbers)
    print("List of odd numbers:", odd_numbers)
    print("List of negative numbers:", negative_numbers)
    print("List of positive numbers:", positive_numbers)

except Exception as error:
    print("Error:", error)
