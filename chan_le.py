import math
def check(n):
    n = str(n)
    sum = 0
    for i in range(0,len(n)-1,1):
        sum += int(n[i])
        if(abs(int(n[i])-int(n[i+1]))!=2): return False
    sum += int(n[-1])
    if(sum % 10 != 0): return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    n = input()
    if(check(n)): print("YES")
    else: print("NO")
