
a, k, n = [int (i) for i in input().split()]
if a <= k:
    b = k - a
else:
    b = (a // k + 1) * k - a
if a + b > n:
    print(-1)
else:
    for b in range(b, n - a + 1, k):
        print(b, end = " ")