
def checktn(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
def doicoso(n,b):
    res = ""
    while n > 0:
        r = n % b
        if r < 10:
            res += str(r)
        n //= b
    return res[::-1]

a,b,m = map(int,input().split())
dem =0
for i in range(a,b+1):
    for k in range(2,m+1):
        if checktn(doicoso(i,k)):
            dem+=1
print(dem)