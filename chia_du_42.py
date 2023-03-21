arr = input().split()
res = []
for i in arr:
    res.append(int(i) % 42)
print(len(set(res)))