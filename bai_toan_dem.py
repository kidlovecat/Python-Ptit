n = int(input())
a = []
while(1):
    a.append([int(i) for i in input().split()])
    if(len(a) == n): 
        break
if n == a[-1]: print("Excellent!") 
else:
    count = 1
    while count < a[-1]:
        if count not in a: print(count)
        count += 1