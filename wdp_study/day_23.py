#!/usr/bin/python3
#Day 23 Problem solving, coming from https://www.hackerrank.com/challenges/swap-nodes-algo

import os
import sys

#
# Complete the swapNodes function below.
#
sys.setrecursionlimit(2000)
class Node:
    def __init__(self, data, left, right):
        self.data = str(data)+' '
        self.left = None
        self.right = None

def inorderTraversal(root,s):
    if root:
        sl = inorderTraversal(root.left,s)
        sc = root.data
        sr = inorderTraversal(root.right,s)
        return sl+sc+sr
    else:
        return ''

def getDepth(root, depth):
    if root:
        dl = getDepth(root.left, depth+1)
        dr = getDepth(root.right, depth+1)
        depth = max(dl,dr)
    else:
        depth -= 1
    return depth

def swap(root, depth, height):
    if root:
        if depth == height:
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            swap(root.left, depth, height+1)
            swap(root.right, depth, height+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

