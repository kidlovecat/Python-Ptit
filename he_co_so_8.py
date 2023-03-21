import math
def doicoso(s):
    sum = 0
    x = 2
    for i in range(len(s)):
        sum += int(s[i])*int(math.pow(2,x))
        x -= 1
    # print(s,sum,sep = ' ')
    return sum
    
s = input()
res = ""
while(len(s) % 3 != 0):
    s = '0' + s
for i in range(len(s)-1,-1,-3):
    tmp = s[i-2]+s[i-1]+s[i]
    res += str(doicoso(str(tmp)))
print(res[::-1]) 