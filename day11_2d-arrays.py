# Day 11: 2D Arrays
# Task: Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Tried a couple of methods using map, only landed on this from the discussions forum:

#!/bin/python

import sys

a = [map(int, raw_input().strip().split(' ')) for _ in range(6)]
print(max([sum(a[j][i:i+3]+[a[j+1][i+1]]+a[j+2][i:i+3]) for i in range(4) for j in range(4)]))

# Proposed solution (This only works in Python 3!)

results = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        results.append(s)

print(max(results))

