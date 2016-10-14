# Day 22: Binary Search Trees
# Task: Write a method to calculate the height of a tree.

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

##################

    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        
        # recursively grab root
        return 1 + max(self.getHeight(root.left),self.getHeight(root.right))

##################

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height     