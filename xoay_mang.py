for t in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = [int(i) for i in input().split()]
    for i in range(k,n,1):
        print(a[i],end=" ")
    for i in range(0,k,1):
        print(a[i],end=" ")
    print()