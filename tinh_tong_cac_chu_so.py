for i in range(int(input())):
    s = list(input())
    s.sort(reverse=False)
    sum = 0
    for i in s:
        if(i >= '0' and i <= '9'): sum += int(i)
        else:
            print(i,end = "")
    print(sum)
         
    