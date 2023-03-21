import math

def check(n):
    for i in range(2,int(math.sqrt(n))+1,1):
        if(n % i == 0):
            return False
    return n > 1
for i in range(int(input())):
    s = input()
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    print("YES" if check(sum) else "NO")