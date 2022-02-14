#https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    ml = 0
    mn = min(a)
    sa = sorted(a)
    
    for i  in set(sa):
        ans = [j for j in a if (j==i or j==i+1)]
        if len(ans)>1 and len(ans)>ml:
            ml = len(ans)
    return ml
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()