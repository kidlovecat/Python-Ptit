t = int(input())
while(t > 0):
    t-=1
    s = input()
    cnt = 1
    res = ""
    for i in range(0,len(s)-1,1):
        if(s[i] == s[i+1]):
            cnt+=1
        else:
            res = res + str(cnt)+s[i]
            cnt=1
    cnt2 = 1
    for i in range(len(s)-1,-1,-1):
        if(s[i] == s[i-1]):
            cnt2+=1
        else:
            res = res + str(cnt2)+s[i]
            break
    if(cnt == len(s)): print(str(cnt)+s[0])
    else: print(res)
            