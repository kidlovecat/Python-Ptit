import math
t = int(input())
for i in range(t):
    n = int(input())
    print("1 * ", end = "")
    dem = 0
    while n % 2 == 0:
        n /= 2
        dem += 1
    if dem > 0 and n != 1:
        print("2^" + str(dem) + " * ", end = "")
    elif dem > 0 and n == 1:
        print("2^" + str(dem))
    dem = 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        dem = 0
        while n % i == 0:
            n /= i
            dem += 1
        if dem > 0:
            if n == 1:
                print(str(i) + "^" + str(dem))
            else:
                print(str(i) + "^" + str(dem) + " * ", end = "")
    if n > 1:
        print(str(int(n)) + "^" + "1")