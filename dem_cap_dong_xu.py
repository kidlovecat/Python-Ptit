import math
n=int(input())
hang=[0]*n
cot=[0]*n
for i in range(n):
    s=input()
    for k in range(len(s)):
        if s[k]=='C':
            hang[i]+=1
            cot[k]+=1
sum=0
for i in hang+cot:
    if i>1: sum+=math.comb(i,2)
print(sum)