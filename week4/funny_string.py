#https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def funnyString(s):
    ans_s = []
    ans_rev_s = []
    s = list(s)
    rev_s = reversed(s)
    
    ord_s = [ord(i) for i in s]
    rev_ord_s = [ord(i) for i in rev_s]
    
    for i in range(len(ord_s)-1):
        ans_s.append(abs(ord_s[i+1]-ord_s[i]))
        
    for i in range(len(rev_ord_s)-1):
        ans_rev_s.append(abs(rev_ord_s[i+1]-rev_ord_s[i]))
    
    if ans_s == ans_rev_s:
        return 'Funny'
    else:
        return 'Not Funny'
        
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
