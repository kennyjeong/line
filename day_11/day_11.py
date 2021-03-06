#!/usr/bin/python3
# The problem is coming from https://www.hackerrank.com/challenges/30-interfaces
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.sum = 0
    def divisorSum(self, n):
        for i in range(1, n+1):
            if n % i == 0:
                self.sum+=i
        return self.sum

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
