import re

s = ""
dct = {}
n, k = [int(i) for i in input().split()]
for t in range(n):
    s += ' '+input().lower()
regex = '[\w\s]+'
s = re.findall(regex, s)
for i in s:
    tmp = i.split()
    for j in tmp:
        if j in dct:
            dct[j] += 1
        else:
            dct[j] = 1
ls = list(dct.keys())
ls.sort(key = lambda x: (-dct[x], x))
for i in ls:
    if(dct[i] >= k):
     print('{} {}'.format(i, dct[i]))