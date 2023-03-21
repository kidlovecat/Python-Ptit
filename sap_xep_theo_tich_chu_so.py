def sum(n):
    s = 1
    for i in range(n):
        s *= int(n[i])
    return s
for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort()
    b = sorted(a,key=sum)
    print(*b,sep=" ")
