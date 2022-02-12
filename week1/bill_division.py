#https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    real = int((sum(bill)-bill[k])/2)
    if real - b == 0:
        print("Bon Appetit")
    else:
        print(b-real)
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
