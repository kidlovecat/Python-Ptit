import math

def snt(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0): return False
    return n > 1

for i in range(int(input())):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if(snt(int(s[i]))): 
            cnt += 1
    print("YES" if(snt(len(s)) and cnt > int(len(s)/2)) else "NO")