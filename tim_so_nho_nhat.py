import re
for t in range(int(input())):
    s = input()
    s1 = re.findall(r'\d+', s) #tach tung so
    a = []
    for x in s1:
        a.append(int(x))

    print(min(a))