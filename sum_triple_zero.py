for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    res = 0
    for j in range(0,n-2):
        x = a[j]
        l = j+1
        r = n-1
        while l<r:
            if (x+a[l]+a[r]) == 0:
                res += 1
                l += 1
            elif (x+a[l]+a[r])>0:
                r -= 1
            else:
                l += 1
    print(res)