import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(0,n-6,1):
        if(snt(i) and snt(i+2) and snt(i+6) or snt(i) and snt(i+4) and snt(i+6)):
            cnt += 1
    print(cnt)    