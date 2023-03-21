n, m = list(map(int, input().split()))
a = []
minn, maxx, check = 10001, 0, 0

for i in range(n):
    a.append([int(x) for x in input().split()])
    for x in a[i]:
        minn = min(minn, x)
        maxx = max(maxx, x)

distance = maxx - minn
for i in range(n):
    for j in range(m):
        if a[i][j] == distance: 
            if check == 0: print(distance)
            check = 1
            print(f'Vi tri [{i}][{j}]')

if check == 0: print("NOT FOUND")