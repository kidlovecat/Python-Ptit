import math

def nto(n):
    if len(str(n)) < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n, m = list(map(int, input().split()))
a, res, check = [], 0, 0

for i in range(n):
    a.append([int(x) for x in input().split()])
    for x in a[i]: 
        if nto(x): 
            check = 1
            res = max(res, x)

if check == 0: print("NOT FOUND")
else: 
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res: print(f'Vi tri [{i}][{j}]')