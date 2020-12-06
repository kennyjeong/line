#!/usr/bin/python3
# The problem is coming from https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        max = 0;
        temp = 0;
        length = len(self.__elements)
        for i in range(0,length-1):
            for j in range(1,length):
                temp = abs(self.__elements[i] - self.__elements[j])
                if max <= temp:
                    max = temp
        self.maximumDifference = max
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
