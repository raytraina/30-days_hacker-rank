# Day 10: Binary Numbers
# Task: Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

#!/bin/python

import sys


n = int(raw_input().strip())

bits = [(n >> bit) & 1 for bit in range(n - 1, -1, -1)]

consecutive = 0

for i in bits:
    if i == 1:
        consecutive += 1
        
print consecutive


##########


#!/bin/python

import sys


n = int(raw_input().strip())

for i in xrange(n):
    print bin(n)[2:]