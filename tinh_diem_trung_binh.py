n = int(input())
arr = [float(i) for i in input().split()]
check = [min(arr), max(arr)]
b = [x for x in arr if x not in check]
res = float(0)
for i in range(len(b)):
    res += b[i]
print("%.2f" % (res/float(len(b))))