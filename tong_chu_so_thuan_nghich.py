for i in range(int(input())):
    s = input()
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    sum = str(sum)
    if(len(sum) < 2):
        print("NO")
        continue
    re = sum[::-1]
    if(sum == re): 
        print("YES")
    else: print("NO")