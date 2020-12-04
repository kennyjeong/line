#!/usr/bin/python3
# The problem is coming from https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNumber)

    def calculate(self):
        array_len = len(scores)
        ave = 0;
        sum = 0;
        for i in (scores):
            sum = sum + i
        avg = sum / array_len
        if avg >= 90:
            return ("O")
        elif avg >= 80:
            return ("E")
        elif avg >= 70:
            return ("A")
        elif avg >= 55:
            return("P")
        elif avg >= 40:
            return("D")
        elif avg < 40:
            return("T")


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
