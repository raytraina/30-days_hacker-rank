# Day 18: Queues and Stacks
# Task: Make some helper methods related to queues and stacks.

import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []
        
    def pushCharacter(self, a):
        self.stack.append(a)
    def popCharacter(self):
        return self.stack.pop(0)
    def enqueueCharacter(self, a):
        self.queue.append(a)
    def dequeueCharacter(self):
        return self.queue.pop()

# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")  