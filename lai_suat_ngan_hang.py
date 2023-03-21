import math
t = int(input())
while t > 0:
    t-=1
    n, x, m = input().split(" ")
    n = float(n)
    x = float(x)
    m = float(m)
    x /= 100
    print(math.ceil(math.log10(m / n) / math.log10(1 + x)))