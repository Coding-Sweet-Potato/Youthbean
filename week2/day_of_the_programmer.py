#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

import math
import os
import randoms
import re
import sys


def dayOfProgrammer(year):
    if year==1918:
        return '26.09.'+str(year)
    if year <1918:
        if year%4==0:
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
    else:
        if year%400==0 or (year%4==0 and year%100!=0):
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()