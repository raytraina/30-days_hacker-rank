# Day 5: Loops
# Task: Given an integer, , print its first  multiples. Each multiple  (where ) should be printed on a new line in the form: N x i = result.

#!/bin/python

import sys


N = int(raw_input().strip())

for i in range(1,11):
    result = N * i
    print '%s x %s = %s' %(N, i, result)