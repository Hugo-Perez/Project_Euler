"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_of_squares = 0
square_of_sum = 0

for one_to_hundred in range (1, 101):

  sum_of_squares += one_to_hundred ** 2
  square_of_sum += one_to_hundred

square_of_sum = square_of_sum ** 2

difference = square_of_sum - sum_of_squares

print(difference)
