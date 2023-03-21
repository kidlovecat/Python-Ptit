while 1:
    n = int(input())
    if n == 0:  break
    dem = 1
    while n != 1:
        dem += 1
        if n % 2 == 0:  n /= 2
        else: n = n*3 + 1
    print(dem)