import re

s = ""
dct = {}

for t in range(int(input())):
    s += ' '+input().lower()
regex = '[a-z\s]+'
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

     print('{} {}'.format(i, dct[i]))