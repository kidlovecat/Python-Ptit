def chuyen(n, a, b): 
    print(a, "->", b, sep=" ")
def ThapHaNoi(n,a,b,c):
    if n == 1:
        chuyen(n,a,c)
    else:
        ThapHaNoi(n-1,a,c,b)
        chuyen(n,a,c)
        ThapHaNoi(n-1,b,a,c)


n = int(input())
ThapHaNoi(n,'A','B','C')