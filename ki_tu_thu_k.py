def solve(n,k):
    if k == 2**(n-1): return n
    if k > 2**(n-1): return solve(n-1,k-2**(n-1))
    return solve(n-1,k)

t = int(input())
for i in range(t):
    n, k = [int(i) for i in input().split()]
    print(chr(solve(n,k) + ord('A') - 1))