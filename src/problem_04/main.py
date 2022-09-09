"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

MAX_THREE_DIGITS = 999
result = 0

for digit_1 in range(MAX_THREE_DIGITS, 100, -1):
  for digit_2 in range(MAX_THREE_DIGITS, 100, -1):
      product = digit_1 * digit_2
      reverse_product_str = str(product)[::-1]
      if str(product) == reverse_product_str and product > result:
        result = product
    
print(result)