def check(n):
    check = 0
    for i in n:
        if i == '6': check = 1
        elif i == '8' and check == 1: check = 2
        elif i == '8' and check == 2: check = 0
        else: return False
    return True

s = input()

print("YES" if check(s) else "NO")