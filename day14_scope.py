# Day 14: Scope
# Task: Calculate the absolute difference of a list of integers.

class Difference:
    def __init__(self, a):
        self.__elements = a

####################

    def computeDifference(self):
        maximumDifference = 0
        small = self.__elements[0]
        large = self.__elements[-1]
        
        for i in self.__elements:
            if i <= small:
                small = i
            if i >= large:
                large = i
                
        self.maximumDifference = large - small
                
        return self.maximumDifference

####################

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference