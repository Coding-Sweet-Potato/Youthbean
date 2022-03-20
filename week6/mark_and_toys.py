#https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    prices = sorted(prices)
    cnt = 0
    for i in prices:
        if k-i >=0:
            cnt+=1
            k-=i
        else:
            return cnt
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
