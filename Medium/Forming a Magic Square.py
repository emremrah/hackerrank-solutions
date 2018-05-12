# https://www.hackerrank.com/challenges/magic-square-forming/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magic_constant = 15
    cost = 0
    d = 0   # diagonal sum
    occupied = []   # occupied numbers my the matrix
    sums = [[0 for i in range(2)] for j in range(3)]
    
    # set occupied values, rows', columns' and diagonal sums
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            sums[i][0]+=s[i][j]
            sums[j][1]+=s[i][j]
            if s[i][j] not in occupied:
                occupied.append(s[i][j])
            if i==j:
                d+=s[i][j]
    
    for i in range(len(s)):
        difference = sums[i][0] - 15
        for j in range(len(s)):
            if (s[i][j] - difference not in occupied):
                s[i][j] = s[i][j] - difference
                cost += abs(s[i][j] - (s[i][j] - difference))
                occupied.append(s[i][j] - difference)
                break
        
    return cost
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
