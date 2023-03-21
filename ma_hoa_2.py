P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    x = input()
    if(x == '0'): break
    n, s = x.split()
    n = int(n)
    res =""
    
    for i in range(0,len(s),1):
        res = res+ P[(P.index(s[i])+n)%28]  
    print(res[::-1])
    