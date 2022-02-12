#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    alt = 0
    cnt = 0 
    check = False
    for i in range(steps):
        if path[i] == 'D' and alt ==0:
            check = True
        if path[i] == 'U' and alt ==-1 and check == True:
            cnt+=1
            check = False
        if path[i] =='D':
            alt-=1
        else:
            alt+=1
    return cnt 
        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
