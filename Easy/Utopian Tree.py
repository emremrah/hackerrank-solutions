# https://www.hackerrank.com/challenges/utopian-tree/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height = 1;
    spring = True
    
    for x in range(0, n):
        if (spring):
            height = height * 2
            spring = False
            
        elif (not spring):
            height = height + 1
            spring = True
    
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
