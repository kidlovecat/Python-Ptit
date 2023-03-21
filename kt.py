f = [0,1,1]
for i in range(3,1001,1):
    f.append(f[i-1]+f[i-2])

mod = 10**9+7
n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

for i in range(m):
    tmp = [int(i) for i in input().split()]
    if(len(tmp) == 4):
        for j in range(tmp[1]-1,tmp[2],1):
            a[j] += tmp[3]
    else:
        res = 0
        for j in range(tmp[1]-1,tmp[2],1):
            res += int(f[a[j]] % mod)
            res %= mod
            res = int(res)
        print(res)
        

        