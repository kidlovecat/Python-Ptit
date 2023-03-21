for t in range(int(input())):
    n = input()
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    check = 0
    for i in a:
        if(i in b and i in c):
            print(i,end=" ")
            check = 1
    if(check == 0):
        print("NO",end="")
    print()
    
