import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1
t = int(input())
while t > 0 :
    cnt = 0
    n = int(input())
    for x in range(1,n):
        if math.gcd(x,n) == 1: cnt+=1
    if snt(cnt): print("YES") 
    else: print("NO")
    t-=1