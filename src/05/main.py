"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# To be evenly divisible by two the number must be an even one
current_number = 2

while True:
    for divisor in range(1, 21):
      if (current_number % divisor != 0):
        break
      elif (divisor == 20):
        print("Result:", current_number)
        exit()

    # To be evenly divisible by two the number must be an even one
    current_number += 2
