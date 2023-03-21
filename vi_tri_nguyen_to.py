import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

def check(s):
    for i in range(len(s)):
        if(snt(i)):
            if(not snt(int(s[i]))):
                return False
        else: 
            if (snt(int(s[i]))):
                return False
    return True

for i in range(int(input())):
    s = input()
    print("YES" if(check(s)) else "NO")
