# Day 12: Inheritance 
# Task: You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

####################

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores=[]):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores
        
    def calculate(self):
        score_sum = 0
        
        for score in self.scores:
            score_sum += score
            
        average = score_sum/(len(self.scores))
        
        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 70:
            return 'A'
        elif average >= 55: 
            return 'P'
        elif average >= 40:
            return 'D'
        elif average < 40:
            return 'T'
        else:
            return 'Error'

####################

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()