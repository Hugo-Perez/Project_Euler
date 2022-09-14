"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a^2 + b^2 = SOMETHING = c^2
"""

a = 0
b = 1
c = 999

result_found = 0

while not result_found:
  c -= 1
  b += 1

  temp_b = b
  for i in range(1, b + 1):
    temp_b -= 1
    a = i
    
    if (a**2 + temp_b**2 == c**2):
      if (a * temp_b * c > result_found):
        result_found = a * temp_b * c
      

print ("Result:", result_found)
