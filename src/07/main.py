"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(possible_prime: int):
  possible_divisor = 2
  while possible_divisor ** 2 <= possible_prime:
    if possible_prime % possible_divisor == 0:
      return False
    else:
      possible_divisor += 1

  return True
  

current_number = 2
prime_count = 0

while prime_count != 10001:
  if is_prime(current_number):
    prime_count += 1
  
  current_number += 1

current_number -= 1
print("Result:", current_number)
