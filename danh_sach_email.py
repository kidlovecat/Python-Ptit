res=set()
with open("CONTACT.in","r") as file:
    a = file.readline().strip()
    while(a!=''):
        res.add(a.lower())
        a= file.readline().strip()
lst = list(res)
lst.sort()
for i in lst:
    print(i)