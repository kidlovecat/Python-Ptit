def check(n):
    if(len(n) < 2 or n != n[::-1]): return False
    return True

n, m = list(map(int, input().split()))
a = []
res = 0
for i in range(n):
    a.append([int(x) for x in input().split()])
    for x in a[i]:
        if check(str(x)): res = max(res, x)

if res == 0: print("NOT FOUND")
else: 
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res: print(f'Vi tri [{i}][{j}]')