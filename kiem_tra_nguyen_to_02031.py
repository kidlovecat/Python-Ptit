import math

def Check(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: 
            return 0
    return 1

ip = list(map(int, input().split()))
for i in range(ip[0]):
    line = list(map(int, input().split()))
    for j in line:
        print(Check(j), end=' ')
    print("")