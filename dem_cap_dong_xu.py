def acb(k, n):
    a = b = d = 1
    for i in range(1, k + 1) :
        a *= i
    for i in range(1, n + 1) :
        b *= i
    for i in range(1, (n - k) + 1) :
        d *= i
    result = b  / (a * d) 
    return result

n = int(input())
arr = []
for i in range(n):
    arr.append(input())
cnt = 0

for i in range(n):
    tmp = 0
    for j in range(n):
        if(arr[i][j] == 'C'):
            tmp += 1
    if(tmp > 1): cnt += acb(2,tmp)
print(cnt)
for i in range(n):
    tmp = 0
    for j in range(n):
        if(arr[j][i] == 'C'):
            tmp += 1
    if(tmp > 1):cnt += acb(2,tmp) 
print(int(cnt)) 

    
