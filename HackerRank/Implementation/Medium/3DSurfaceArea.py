# link
# https://www.hackerrank.com/challenges/3d-surface-area/problem


# python HackerRank/Implementation/Medium/3DSurfaceArea.py 

# Sample Input
# 3 3
# 1 3 4
# 2 2 3
# 1 2 4

# Sample Output
# 60

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    top = 0
    front = 0
    side = 0
    
    sideHeight = [0 for x in A[0]]
    for i in range(len(A)):
        frontHeight = 0
        
        for j in range(len(A[0])):
            top += 1 if A[i][j] > 0 else 0
            
            front += abs(A[i][j] - frontHeight)
            if j == len(A[0]) - 1: front += A[i][j]
            frontHeight = A[i][j]
            
            side += abs(A[i][j] - sideHeight[j])
            sideHeight[j] = A[i][j]
            
    top, front, side = top * 2, front, side + sum(sideHeight)
    return top + front + side

if __name__ == '__main__':

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(str(result) + '\n')
