s = input()
if(len(s) % 2 != 0):
    s = s[:-1]
res = {}
for i in range(0,len(s)-1,2):
    if(str(s[i]+s[i+1]) not in res.keys()):
        res.update({str(s[i]+s[i+1]):1})
    else:
        res.update({str(s[i]+s[i+1]):res.get(str(s[i]+s[i+1]))+1})

for i in res:
    print(i,res.get(i),sep=' ')