"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt, ceil


def get_largest_possible_prime(number: int):
    # The largest prime factor must be the square root of the number, or lower than it
    largest_possible_prime = sqrt(original_num)
    # We floor up the number to an int 1 value higher
    largest_possible_prime = ceil(largest_possible_prime)

    # If its even it can't be prime so we lower it by one
    if (number % 2 == 0):
        largest_possible_prime -= 1

    return largest_possible_prime


def is_prime(number: int):
    for i in range(2, get_largest_possible_prime(number)):
        if (number % i) == 0:
            return True
        else:
            continue

    return False


# Number to be factorized
original_num = 600851475143

largest_possible_result = get_largest_possible_prime(original_num)

result = 0

# We know largest possible result is odd so we can lower the possible primes by 2 so we skip all even options
# (all evens are non prime)
for possible_prime in range(largest_possible_result, 2, -2):
    if is_prime(possible_prime) and original_num % possible_prime == 0:
        result = possible_prime
        break

print("Result:", result)
