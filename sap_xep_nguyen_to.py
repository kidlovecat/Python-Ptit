import math
prime = []
def isprime():
    prime.append(0)
    prime.append(0)
    for i in range(2 , 1001): prime.append(1)
    for i in range(2 , int(math.sqrt(1001) + 1)):
        if prime[i]:
            for j in range(i*i , 1001 , i):
                prime[j] = 0

isprime()
n = int(input())
a = list(map(int, input().split()))[:n]
b = []
for i in a:
    if prime[i]: b.append(i)
b.sort()
k = 0
for i in a:
    if prime[i]:
        print(b[k], end=' ')
        k += 1
    else: print(i, end=' ')