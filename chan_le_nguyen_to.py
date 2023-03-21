import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

def check(s):
    sum = 0
    for i in range(0,len(s),2):
        if(int(s[i]) % 2 != 0):
            return False
        else: sum += int(s[i])
    for i in range(1,len(s),2):
        if(int(s[i]) % 2 == 0):
            return False
        else: sum += int(s[i])
    if(not snt(sum)): return False
    return True

for i in range(int(input())):
    print("YES" if(check(input())) else "NO")
