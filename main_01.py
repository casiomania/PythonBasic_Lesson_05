# Lesson 05 / Homework 01
# Given a list of integers filled with random numbers, calculate:
# The sum of negative numbers;
# The sum of even numbers;
# Sum of odd numbers;
# The product of elements with multiple indices of 3;
# The product of elements between the minimum and the maximum element;
# The sum of the elements between the first and last positive elements.

import random

try:
    my_list = [random.randint(-20, 20) for _ in range(10)]

    sum_negative = sum(x for x in my_list if x < 0)
    sum_even = sum(x for x in my_list if x % 2 == 0)
    sum_odd = sum(x for x in my_list if x % 2 != 0)

    product_index3 = 1
    for i in range(len(my_list)):
        if i % 3 == 0:
            product_index3 *= my_list[i]

    product_between_min_max = 1
    if my_list:
        min_element = min(my_list)
        max_element = max(my_list)

        min_index = my_list.index(min_element)
        max_index = my_list.index(max_element)
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        product_between_min_max = 1
        for i in range(min_index + 1, max_index):
            product_between_min_max *= my_list[i]

    first_positive_index = None
    for i in range(len(my_list)):
        if my_list[i] > 0:
            first_positive_index = i
            break

    last_positive_index = None
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] > 0:
            last_positive_index = i
            break

    sum_between_positive = 0
    if first_positive_index is not None and last_positive_index is not None:
        sum_between_positive = sum(my_list[first_positive_index + 1:last_positive_index + 1])

    print("Random List:", my_list)
    print("Sum of negative numbers:", sum_negative)
    print("Sum of even numbers:", sum_even)
    print("Sum of odd numbers:", sum_odd)
    print("Product of elements with indices divisible by 3:", product_index3)
    print("Product of elements between the minimum and maximum element:", product_between_min_max)
    print("Sum of elements between the first and last positive elements:", sum_between_positive)

except Exception as error:
    print("Error:", error)
