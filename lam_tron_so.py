n = int(input())
while n > 0 :
    a = int(input())
    i = 1
    while a > 10 ** i:
        tmp = 10**i
        x = a%tmp
        if (x >= (tmp-x)):
            a += tmp-x
        else: a-= x
        i+=1
    n-=1
    print(a)