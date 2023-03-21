def maxx(s1,s2,n,m):
    s1 = str(s1)
    s1 = s1.replace(str(min(n,m)),str(max(n,m)))
    s2 = str(s2)
    s2 = s2.replace(str(min(n,m)),str(max(n,m)))
    return int(s1) + int(s2)

def minn(s1,s2,n,m):
    s1 = str(s1)
    s1 = s1.replace(str(max(n,m)),str(min(n,m)))
    s2 = str(s2)
    s2 = s2.replace(str(max(n,m)),str(min(n,m)))
    return int(s1) + int(s2)

for i in range(int(input())):
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = input().split()
    if len(arr) == 1:
        s1 = arr[0]
        s2 = input()
    else:
        s1, s2 = arr
    print(minn(s1,s2,n,m), maxx(s1,s2,n,m),sep=" ")
