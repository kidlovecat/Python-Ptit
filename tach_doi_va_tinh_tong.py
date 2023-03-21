s = input()
while(len(s) > 1):
    x = int(len(s)/2)
    s1 = s[0:x]
    s2 = s[x:(len(s))]
    s = str(int(s1) + int(s2))
    print(s)
