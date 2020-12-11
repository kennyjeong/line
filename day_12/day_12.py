#!/usr/bin/python3
# Day 12 problem solving, coming from https://www.hackerrank.com/challenges/30-sorting

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_count = 0
for i in range (n-1):
    for j in range (i,n):
        if a[i] > a[j]:
            temp = a[i]
            a[i], a[j] = a[j], a[i]
            swap_count += 1

print ("Array is sorted in",swap_count,"swaps.")
print ("First Element:",a[0])
print ("Last Element:",a[n-1])

