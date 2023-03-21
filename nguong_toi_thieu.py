s = input()
k = int(input())
if(len(s) % 2 != 0):
    s = s[:-1]
res = {}
for i in range(0,len(s)-1,2):
    if(str(s[i]+s[i+1]) not in res.keys()):
        res.update({str(s[i]+s[i+1]):1})
    else:
        res.update({str(s[i]+s[i+1]):res.get(str(s[i]+s[i+1]))+1})
ans = list(res.keys())
ans.sort()
print(ans)
print(res)
check = 0
for i in ans:
    if(res.get(i) >= k):
        check = 1
        print(i,res.get(i),sep=' ')
if(check == 0):
    print("NOT FOUND")