n, m = list(map(int, input().split()))
a = []

for i in range(n): a.append([int(x) for x in input().split()])

distance, cnt = abs(n - m), 0

if n < m:
    key = 2 * distance - 1
    for i in range(n):
        for j in range(m):
            if j % 2 != 0 and j <= key: continue
            print(a[i][j], end = ' ')
        print("")
else:
    key = 2 * distance - 2
    for i in range(n):
        if i % 2 == 0 and i <= key: continue
        for j in range(m):
            print(a[i][j], end = ' ')
        print("")