import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

for i in range(int(input())):
    s = input()
    n = int(s[-4]+s[-3]+s[-2]+s[-1])
    print("YES" if(snt(n)) else "NO")