
def fibo():
    arr = [0,1,1]
    for i in range(3, 93, 1):
        arr.append(int(arr[i-1] + arr[i-2]))
    return arr

for t in range(int(input())):
    arr = fibo()
    a, b = input().split()
    a = int(a)
    b = int(b)
    for i in range(a,b+1,1):
        print(arr[i],end=" ")
    print()
