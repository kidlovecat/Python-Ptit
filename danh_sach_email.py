tap = set()
with open('CONTACT.in') as f:
    a = f.readline().strip()
    while a!="":
        tap.add(a.lower())
        a = f.readline().strip()
lst = list(tap)
lst.sort()
for i in lst:
    print(i)
