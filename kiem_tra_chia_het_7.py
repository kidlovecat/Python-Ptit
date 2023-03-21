
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    cnt = 1
    check = 1
    while(cnt <= 1000):
        cnt += 1
        if(int(n) % 7 == 0):
            print(n)
            check = 0
            break
        else:
            
            tmp = str(n)
            n += int(tmp[::-1])
    if(check == 1): print(-1)