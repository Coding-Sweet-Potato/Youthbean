# https://www.hackerrank.com/challenges/correctness-invariant/problem?isFullScreen=true

n = int(input())
n_list = list(map(int,input().split()))

for i in range(1,n):
    for j in range(i):
        if n_list[j] > n_list[i]:
            a=n_list[j]
            n_list[j]=n_list[i]
            n_list[i]=a
for i in n_list:
    print(i,end=' ')    