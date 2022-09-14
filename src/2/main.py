"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

previous_number = 0
current_number = 1
total = 0

while current_number <= 4000000:     # Run until value exceeds 4 mill
    # Calculate new pair
    temp = current_number
    current_number += previous_number
    previous_number = temp

    # Add to total if even
    if current_number % 2 == 0:
        total += current_number

print("Result:", total)     # 4613732