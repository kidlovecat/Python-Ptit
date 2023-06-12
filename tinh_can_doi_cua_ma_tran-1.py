n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if(i +j < n-1):
            cnt1 += a[i][j]
        if(i + j >= n):
            cnt2 += a[i][j]
t = int(input())
print("YES" if(abs(cnt1 -cnt2) <= t) else "NO")
print(abs(cnt1-cnt2))