#!/usr/bin/python3
# 10th day Problem solving that is coming from the https://www.hackerrank.com/challenges/30-queues-stacks/

import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=list()

    def pushCharacter(self,one_char):
        self.stack.append(one_char)
        return True

    def popCharacter(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return False

    def enqueueCharacter(self, one_char):
        self.queue.insert(0, one_char)
        return True

    def dequeueCharacter(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return False

# read the string s
s=input()
#Create the Solution class object
obj=Solution()
l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
