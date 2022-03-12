#https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true

import math
import os
import random
import re
import sys
import itertools

def icecreamParlor(m, arr):
    result = []
    p = itertools.permutations(arr,2)
    for case in p:
        if sum(case) == m:
            if case[0] != case[1]:
                result.append(sorted([arr.index(case[0])+1,arr.index(case[1])+1]))
            else:
                tmp = list(filter(lambda x: arr[x] == case[0], range(len(arr))))
                result.append([tmp[0]+1,tmp[1]+1])
    result = list(set([tuple(ti) for ti in result]))
    result2 = []
    for i in result:
        result2.append(i[0])
        result2.append(i[1])
    return result2
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
