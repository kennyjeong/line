#!/usr/bin/python3
#Day 15 Problem Solving, coming from https://www.hackerrank.com/challenges/fraudulent-activity-notifications

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    freq = {}
    notify=0
    def find(idx):
        total_count = 0
        for i in range(201):
            if i in freq:
                total_count = total_count + freq[i]
            if total_count >= idx:
                return i

    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]]+=1
        else:
            freq[expenditure[i]]=1
        if i>=d-1:
            if d%2 ==0:
                median = (find(d//2)+find(d//2+1))/2
            else:
                median = find(d/2)
            if expenditure[i+1]>= (median*2) :
                notify +=1
                print("notify: ",notify)
            freq[expenditure[i-d+1]]-=1

    return notify

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

