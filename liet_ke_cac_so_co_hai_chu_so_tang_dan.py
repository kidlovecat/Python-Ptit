s = input()
if(len(s) % 2 != 0):
    s = s[:-1]
res = set([])
for i in range(0,len(s)-1,2):
    res.add(str(s[i]+s[i+1]))
res2 = list(map(int,res))
res2.sort()
for i in res2:
    print(i,end=" ")