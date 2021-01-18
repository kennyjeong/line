#!/usr/bin/python3
#Day 16 Problem Solving, coming from https://www.hackerrank.com/challenges/ctci-merge-sort/

import math
import os
import random
import re
import sys

def mergesort2(A):
    global count
    if len(A) > 1:
        n = len(A)
        m = int(n/2)
        L = A[:m]
        R = A[m:n]

        mergesort2(L)
        mergesort2(R)

        i = 0
        j = 0
        k = 0
        n1 = m
        n2 = n-m

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
                k += 1
            else:
                A[k] = R[j]
                j += 1
                k += 1
                count += n1-i

        while i < n1:
            A[k] = L[i]
            i+=1
            k+=1
        while j < n2:
            A[k] = R[j]
            j+=1
            k+=1



# Complete the countInversions function below.
def countInversions(arr):
    global count
    count = 0
    mergesort2(arr)
    return count

# Complete the countInversions function below.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

