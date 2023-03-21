def check(s):
    if(len(s) < 3):
        return False
    i = 0
    while(i < len(s)-1 and s[i] < s[i+1]): i+=1
    while(i < len(s)-1 and s[i] > s[i+1]): i+=1
    return i == len(s)-1

for t in range(int(input())):
    print("YES" if check(input()) else "NO")