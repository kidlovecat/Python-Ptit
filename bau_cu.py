n, m = input().split()
n = int(n)
m = int(m)
a = [int(i) for i in input().split()]
a.sort()
dct = {}
for i in a:
    if(i in dct.keys()):
        dct.update({i:dct.get(i)+1})
    else:
        dct.update({i:1})
# print(dct)
x = max(dct.values())
tmp = dct.copy()
for i in tmp.keys():
    if(tmp.get(i) == x):
        dct.pop(i)
if(len(dct) > 0):
    for i in dct.keys():
        if(dct.get(i) == max(dct.values())):
            print(i)
            break
else: print("NONE")
    
     

