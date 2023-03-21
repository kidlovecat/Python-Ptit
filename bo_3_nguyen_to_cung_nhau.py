import math
s = input().split()
l, r = int(s[0]), int(s[1])
for i in range(l,r-1):
    for j in range(i+1,r):
        if math.gcd(i,j) == 1:
            for k in range(j+1, r+1):
                if math.gcd(i,k) == 1 and math.gcd(j,k) == 1:
                    print('(',i,', ',j,', ',k,')',sep='')