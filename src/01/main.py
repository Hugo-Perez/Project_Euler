"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

total = 0

for num in range(1, 1000):              # For all natural numbers under 1000
    if num % 3 == 0 or num % 5 == 0:    # If they are multiples of 3 or 5
        total += num                    # Add them to the total counter

print("Result:", total)    # 233168
