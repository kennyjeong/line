#!/usr/bin/python3
#Day 17 Problem Solving, coming from https://www.hackerrank.com/challenges/30-running-time-and-complexity/
import math

def isPrime(num):
    if num == 1:
        return "Not prime"
    elif num == 2 or num == 3:
        return "Prime"
    for i in range (2, math.ceil(math.sqrt(num))+1):
#    for i in range (2, num):
        if (num % i) == 0:
            return "Not prime"
    return "Prime"

T=int(input())
for i in range(T):
    data=int(input())
    print (isPrime(data))




