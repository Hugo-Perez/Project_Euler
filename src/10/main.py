"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(number: int): 
  x = 2
  while x**2 < number:
    if (number % x == 0):
      return False
    x += 1
  return True


sum_of_primes = 0

for possible_prime in range(2_000_000, 1, -1):
  if (is_prime(possible_prime)):
    sum_of_primes += possible_prime
  
print("Result:", sum_of_primes)