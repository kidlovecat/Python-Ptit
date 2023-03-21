n = int(input())
a = [int(x) for x in input().split()]

a.sort()

res = []
res.append(a[0] * a[1] * a[2])
res.append(a[0] * a[1])
res.append(a[-1] * a[-2])
res.append(a[-1] * a[-2] * a[-3])
res.append(a[0] * a[1] * a[-1])

print(max(res))