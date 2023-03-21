import re
for t in range(int(input())):
    s1 = re.findall(r'\d+', input()) #tach tung so
    a = []
    for x in s1:
        a.append(int(x))
    print(max(a))