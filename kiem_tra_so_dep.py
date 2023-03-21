t = int(input())
while(t > 0):
    t -= 1
    s = input()
    check = 0
    for i in range(0, len(s)-2, 1):
        if(s[i] == s[i+1] or s[i] != s[i+2]):
            print("NO")
            check = 1
            break
    if(check == 0): print("YES")
    