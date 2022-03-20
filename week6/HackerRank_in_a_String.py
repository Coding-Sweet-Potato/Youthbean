#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys



def hackerrankInString(s):
    hck = list('hackerrank')
    s = list(s)
    
    for ss in s:
        if ss == hck[0]:
            hck = hck[1:]
        if len(hck)==0:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
