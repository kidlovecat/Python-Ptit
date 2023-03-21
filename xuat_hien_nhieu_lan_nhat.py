for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    maxx = 0
    tmp = 0
    for i in range(len(a)):
        if(a.count(a[i]) > maxx and a.count(a[i]) > n/2 or a.count(a[i]) == maxx and a.count(a[i]) > n/2 and a[i] < tmp):
            maxx = a.count(a[i])
            tmp = a[i]
    print(tmp if(tmp) else "NO")
    

