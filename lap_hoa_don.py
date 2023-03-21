class HoaDon:
    def __init__(self,ma,ten,socu,somoi):
        self.ma = 'KH{:02d}'.format(ma)
        self.ten = ten
        self.somoi = somoi
        self.socu = socu
    def tongtien(self):
        so = self.somoi - self.socu
        if(so <= 50):
            return (so*100)+(so*100)*0.02
        elif(so <= 100):
            return 50 * 100 + (so - 50) * 150 + (50 * 100 + (so - 50) * 150)*0.03
        else:
            return 50 * 100 + 50 * 150 + (so - 100) * 200 + (50 * 100 + 50 * 150 + (so - 100) * 200)*0.05
    def __str__(self):
        return self.ma+' '+self.ten+' '+str(round(self.tongtien()))
    
ls = []
i = 1
for t in range(int(input())):
    ls.append(HoaDon(i,input(),int(input()),int(input())))
    i += 1
ls.sort(key=lambda x: x.tongtien(),reverse=True)
for i in ls:
    print(i)