import math

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += math.factorial(int(n[i]))
    return sum == n
for t in range(int(input())):
    n = input()
    print("Yes" if check(n) else "No")