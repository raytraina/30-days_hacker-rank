# Day 7: Arrays
# Task: Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
    
for i in arr[-1::-1]:
    print i,
