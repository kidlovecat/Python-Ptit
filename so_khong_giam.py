t = int(input())
while(t > 0):
    t-=1
    s = input()
    check = 0
    for i in range(0,len(s)-1,1):
        if(s[i] > s[i+1]):
            check = 1
            print("NO")
            break
    if(check == 0): print("YES")