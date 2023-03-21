import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0: return False
    return n>1
def check(n):
    n = str(n)
    sum = 0
    for i in range(0,len(n),1):
        sum += int(n[i])
    if snt(sum): return True
    return False
t = int(input())
while t > 0:
    t-=1
    a, b = (input().split(" "))
    a = int(a)
    b = int(b)
    if check(math.gcd(a,b)): print("YES")
    else: print("NO")    