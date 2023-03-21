for t in range(int(input())):
    n = input()
    a = sorted(input().split())
    b = sorted(input().split())
    check = 0
    for i in range(int(n)):
        if(a[i] > b[i]):
            check = 1
            print("NO")
            break
    if(check == 0):
        print("YES")