def Update(dct,n):
    n = str(n)
    for i in range(len(n)):
        dct[n[i]] += 1
    return dct    
for t in range(int(input())):
    dct = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    a,b = [int(i) for i in input().split()]
    for i in range(a,b+1,1):
        dct = Update(dct,i)
    for i in dct.values():
        print(i,end=' ')
    print()
    
