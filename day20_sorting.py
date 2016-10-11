# Day 20: Sorting
# Task: Implement bubble sort.

#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
numberOfSwaps = 0

for index in range(n):
    jindex = index + 1
    while jindex < range(len(a)):
        if a[jindex] > a[jindex + 1]:
            a[jindex], a[jindex + 1] = a[jindex+1], a[jindex]
            numberOfSwaps += 1

print "Array is sorted in %s swaps."  %(numberOfSwaps)
print "First Element: %s" %(a[0])
print "Last Element: %s" %(a[-1])