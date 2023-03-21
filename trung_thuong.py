for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    maxx, res = a.count(a[0]), a[0]
    for i in range(len(a)):
        if a.count(a[i]) > maxx:
            maxx = a.count(a[i])
            res = a[i]
    print(res)
    