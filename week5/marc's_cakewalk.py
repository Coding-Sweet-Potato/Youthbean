#https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    calorie = sorted(calorie,reverse=True)
    tot = 0
    for i in range(n):
        tot+=(2**i)*calorie[i]
    return tot
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
