arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in range(int(input())):
    n, b = (int(i) for i in input().split())
    res = ""
    while(n > 1):
        tmp = n % b
        n /= b
        res += str(arr[int(tmp)])
    print(res[::-1])