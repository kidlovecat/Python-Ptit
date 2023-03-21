import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

for i in range(int(input())):
    s = input()
    print("YES" if(snt(int(s[0]+s[1]+s[2])) and snt(int(s[-3]+s[-2]+s[-1]))) else "NO")