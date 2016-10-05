# Day 16: Exceptions - String to Integer
# Task: Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

#!/bin/python

import sys


S = raw_input().strip()

try:
    S = int(S)
    print S
except:
    print "Bad String"