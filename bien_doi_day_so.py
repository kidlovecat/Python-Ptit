
while(1):
    a = input().split()
    if(a.count(a[0]) == 4 and a[0] == '0'): 
        break
    cnt = 0
    while(1):
        if(a.count(a[0]) == 4):
            print(cnt)
            break
        else:
            tmp = [0]*4
            for i in range (len(a)-1):
                tmp[i] = abs(int(a[i])-int(a[i+1]))
            tmp[3] = abs(int(a[3])-int(a[0]))
            cnt += 1
            a = tmp
   