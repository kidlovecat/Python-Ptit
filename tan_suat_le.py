for t in range(int(input())):
    n = input()
    a = [int(i) for i in input().split()]
    for i in a:
        if(a.count(i) % 2 != 0):
            print(i)
            break