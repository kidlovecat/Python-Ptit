def check(s):
    for i in range(len(s)):
        if(s[i] != '0' and s[i] != '1' and s[i] != '2'):
            return False
    return True
for t in range(int(input())):
    print("YES" if check(input()) else "NO")
