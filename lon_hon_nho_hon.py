from math import *
from collections import deque
import cv2

n = int(int(input()))
vtri = dict()
d = dict()
st = set()
for i in range(n):
    s = input().split()
    st.add(s[0])
    st.add(s[2])
    if s[1] == ">":
        if vtri.get(s[0]) == None:
            vtri[s[0]] = list()

        vtri[s[0]].append(s[2])
        if d.get(s[2]) == None:
            d[s[2]] = 1
        else:
            d[s[2]] += 1
    else:
        if vtri.get(s[2]) == None:
            vtri[s[2]] = list()
        vtri[s[2]].append(s[0])
        if d.get(s[0]) == None:
            d[s[0]] = 1
        else:
            d[s[0]] += 1
Q = deque()
for x in st:
    if d.get(x) == None:
        Q.append(x)
cnt = 0
while len(Q) > 0:
    s = Q.popleft()
    cnt += 1
    if vtri.get(s) != None:
        for x in vtri[s]:
            if d.get(x) != None:
                d[x] -= 1
                if d[x] == 0:
                    Q.append(x)
print("impossible" if cnt != len(st) else "possible")

