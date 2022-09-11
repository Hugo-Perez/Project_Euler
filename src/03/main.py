"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(number: int):
    for i in range(2, number):
        if (number % i) == 0:
            return False
        else:
            continue

    return True


# Number to be factorized
original_num = 600851475143
possible_factor = 2
biggest_factor = 1

while possible_factor ** 2 < original_num:
    if (original_num % possible_factor == 0 and is_prime(possible_factor)):    
        biggest_factor = possible_factor
    possible_factor += 1
    
print("Result:", biggest_factor)
