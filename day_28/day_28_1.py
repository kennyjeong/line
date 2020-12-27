#!/usr/bin/python3
#Day 28 Problem solving, coming from https://www.hackerrank.com/challenges/sherlock-and-anagrams/

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_dict = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            current = str(sorted(s[j:j+i]))
            #print(current, anagram_dict)
            if (current not in anagram_dict):
                anagram_dict[current] = 1
            else:
                #print("Exist")
                count+= anagram_dict[current]
                anagram_dict[current] += 1
    return count

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)
 #       fptr.write(str(result) + '\n')

#    fptr.close()

