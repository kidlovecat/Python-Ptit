class HocSinh:
    def __init__(self,ma,ten,diem):
        self.ma = 'HS{:02d}'.format(ma)
        self.ten = ten
        self.diem = sum(diem)/len(diem)
    def Loai(self):
        if self.diem>=9:
            return "XUAT SAC"
        if self.diem>=8:
            return "GIOI"
        if self.diem>=7:
            return "KHA"
        if self.diem>=5:
            return "TB"
        return "YEU"
    def __str__(self):
        return self.ma+' '+self.ten+' '+ str(round((self.diem*100+1)/100,1))+' '+self.Loai()
    
ls = []
x = 1
for t in range(int(input())):
    ten = input()
    diem = [float(i) for i in input().split()]
    diem.extend(diem[:2])
    ls.append(HocSinh(x,ten,diem))
    x+=1
ls.sort(key=lambda x: x.diem,reverse=True)
for i in ls:
    print(i)