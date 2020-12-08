#!/usr/bin/python3
# 9th day Problem solving, coming https://www.hackerrank.com/challenges/30-more-exceptions/
#Write your code here
import math
class Calculator:
    def power(self, natural, prime):
        if natural > -1 and prime > -1:
            return int(math.pow(natural, prime))
        else:
            raise Exception("n and p should be non-negative")

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
