# Day 15: Linked List
# Task: Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

####################

    def insert(self,head,data): 
    #Complete this method
        if not head:
            return Node(data)

        elif not head.next:
            head.next = Node(data)

        else:
            self.insert(head.next, data)
            
        return head
        
####################

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);