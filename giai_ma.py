t = int(input())
while(t > 0):
    t-=1
    s = input()
    res = ""
    for i in range(1,len(s),2):
        res = res + str(s[i-1]*int(s[i]))
    print(res)