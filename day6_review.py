# Day 6: Let's Review
# Task: Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line.

# Enter your code here. Read input from STDIN. Print output to STDOUT

amt_tests = int(raw_input())

for i in range(1, amt_tests + 1):
    i = raw_input()
    print i[::2] + " " + i[1::2]