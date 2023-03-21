import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
b = dict.fromkeys(a)
for i in b:
    if(snt(i)):
        print(i, a.count(i))
    