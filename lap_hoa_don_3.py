class HD:
    def __init__(self,ma,ten,sl,dgia,ckhau):
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dgia = dgia
        self.ckhau = ckhau
        self.tong = dgia*sl-ckhau
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(self.sl)+' '+str(self.dgia)+' '+str(self.ckhau)+' '+str(self.tong)
    
ls = []
for t in range(int(input())):
    ls.append(HD(input(),input(),int(input()),int(input()),int(input())))
ls.sort(key= lambda x: -x.tong)
for i in ls :
    print(i)