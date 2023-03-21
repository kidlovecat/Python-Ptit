import math
def nto(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if n % i == 0:
            return 0
    return n > 1  
for i in range(int(input())):
    s = input()
    s1 = s[-4] + s[-3] + s[-2] + s[-1]
    n = int(s1)
    print("YES" if nto(n) else "NO")
   