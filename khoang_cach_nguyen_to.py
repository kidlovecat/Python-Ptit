def sieve():
    a = [True]*(10000)
    for i in range(2,int(10000**0.5)+1):
        if(a[i]):
            for j in range(i*i,10000,i):
                a[j] = False
    primes = []
    for i in range(2,10000):
        if(a[i]): primes.append(i)
    return primes

n, x = input().split()
n = int(n)
x = int(x)
res = x
primes = sieve()
for i in range(n+1):
    print(res,end=" ")
    res += int(primes[i])
    
