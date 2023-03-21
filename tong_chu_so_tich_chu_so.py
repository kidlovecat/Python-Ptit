def tong(s):
    sum = 0
    for i in range(len(s)):
        if i%2 == 0:
            a = int(s[i])
            sum += a
    return sum 

def tich(s):
    mul = 1
    dem = 0
    for i in range(len(s)):
        if i%2 == 1:
            a = int(s[i])
            if a != 0:
                mul = mul * a
            else:
                dem = dem + 1
    if dem == int(len(s)/2):
        mul = 0
    return mul
                
t = int(input())
while t > 0:
    s = input()
    print("%d %d" % (tong(s), tich(s)))
           
    t -= 1