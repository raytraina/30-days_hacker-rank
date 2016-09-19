# Day 9: Recursion
# Task: Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(N):
    if N <= 1:
        return 1
    
    return N * factorial(N-1)
    
print factorial(int(raw_input()))