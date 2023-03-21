def sumDigit(s):
    tong = 0
    for value in s:
        tong = tong + ord(value) - ord('0')
    return str(tong)

s = input()
cnt=0
while(len(s) > 1):
    s = sumDigit(s)
    cnt += 1
print(cnt)