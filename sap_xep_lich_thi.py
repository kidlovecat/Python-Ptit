class mt:
    def __init__(self,ma,ten,ht):
        self.ma = ma
        self.ten = ten
        self.ht = ht
class ct:
    def __init__(self,ma,nt,gt,pt):
        self.ma = ma
        self.nt = nt
        self.gt = gt
        self.pt = pt
        self.d = int(nt[:2])
        self.mo = int(nt[3:5])
        self.y = int(nt[6:])
        self.h = int(gt[:2])
        self.m = int(gt[3:])
class lt:
    def __init__(self,ct,mt,mn,ssv):
        self.ct = ct
        self.mt = mt
        self.mn = mn
        self.ssv = ssv
    def __str__(self):
        return self.ct.nt+" "+ self.ct.gt+" "+self.ct.pt+" "+self.mt.ten+" "+self.mn+" "+self.ssv
        
f1 = open("MONTHI.in","r")
f2 = open("CATHI.in","r") 
f3 = open("LICHTHI.in","r")

ls1 = []
ls2 = []
ls3 = []

for i in range(int(f1.readline().strip())):
    ls1.append(mt(f1.readline().strip(),f1.readline().strip(),f1.readline().strip()))
for i in range(int(f2.readline().strip())):
    ls2.append(ct("C{:03d}".format(i+1),f2.readline().strip(),f2.readline().strip(),f2.readline().strip()))
for i in range(int(f3.readline().strip())):
    tmp = f3.readline().strip().split()
    for j in ls1:
        if tmp[1] == j.ma:
            for k in ls2:
                if tmp[0] == k.ma:
                    ls3.append(lt(k,j,tmp[2],tmp[3]))
ls3.sort(key=lambda x: (x.ct.y,x.ct.mo,x.ct.d,x.ct.h,x.ct.m,x.ct.ma))
for i in ls3:
    print(i)

f1.close()
f2.close()
f3.close()