# Simple lambda addition example
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# lambda as a parameter to a filter method
# the lambda is the first parameter into the filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# lambda assigned to a boolean variable
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False

# lambda and map function example.
# lambda is the first parameter into the map function
# A map function is a built-in function that applies a given function to each item in an iterable
numbers = [1, 2, 3, 4, 5]
# double each number in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)
# Output: [2, 4, 6, 8, 10]




