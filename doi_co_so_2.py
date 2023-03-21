for t in range(int(input())):
    n = int(input())
    s = input()
    x = int(s,2)
    if(n == 2):
        print(s)
    elif(n == 4):
        f = ""
        if len(s) % 2 != 0:
            s = "0" + s
        for i in range (0, len(s) - 1, 2):
            temp = int(s[i]) * 2 + int(s[i + 1])
            f += str(temp)
        print(int(f))
    elif(n == 8):
        tmp = oct(x)
        for i in range(2,len(tmp)):
            print(tmp[i],end="")
        print()
    else:
        tmp = hex(x)
        tmp = tmp.upper()
        for i in range(2,len(tmp)):
            print(tmp[i],end="")
        print()
