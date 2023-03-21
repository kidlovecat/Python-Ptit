def check(n):
    n = str(n)
    if len(n) % 2 == 1: return False
    for i in n:
        if int(i) % 2 == 1:
            return False
    for i in range(0,int(len(n)/2)+1,1):
        if(n[i] != n[len(n)-i-1]): return False
    return True
t = int(input())
while t > 0:
    t-=1
    n = int(input())
    for i in range(22,n,2):
        if(check(i)): print(str(i),end = " ")
    print()