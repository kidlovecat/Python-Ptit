n, k = int(input()), int(input())
arr = [int(i) for i in input().split()]
ok = [0] *n
a = [0] *n
check = 0
def tinh():
    tmp = arr[0]
    for i in range(1,len(arr),1):
        if a[i-1] == 1:
            tmp += arr[i]
        if a[i-1] == 2:
            tmp -= arr[i]
        if a[i-1] == 3:
            tmp *= arr[i]
    if tmp == k:
        check = 1
        print(arr[0],end='')
        for i in range(1,len(arr)):
            print(a[i-1],end='')
            if arr[i] < 0:
                print("({:d})".format(arr[i]),end='')
            else: print(arr[i],end='')
        print()
def solve(i):
    for j in range(1,n):
        a[i] = j
        if i == n-1: 
            tinh()
        else: solve(i+1)
solve(1)