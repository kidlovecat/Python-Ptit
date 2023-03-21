from datetime import datetime

class TS:
    def __init__(self,ten,dvi,tg):
        self.ten = ten
        self.dvi = dvi
        self.tg = tg
        a = self.dvi.split()
        b = self.ten.split()
        self.ma = a[0][0]+a[1][0]
        for i in b:
            self.ma += i[0]
        t = (datetime.strptime(self.tg,'%H:%M')-datetime.strptime('06:00','%H:%M')).seconds
        self.vt = (120000*3.6/t)
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+self.dvi+' '+str(round(self.vt))+' Km/h'

ls = []
for t in range(int(input())):
    ls.append(TS(input(),input(),input()))
ls.sort(key=lambda x: -x.vt)
for i in ls:
    print(i)