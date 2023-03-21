from datetime import datetime,date

class HD:
    def __init__(self,ma,ten,phong,ngaynhan,ngaytra,ps):
        self.ma = 'KH{:02d}'.format(ma)
        self.ten = ten
        self.tang = phong[0]
        self.phong = phong
        self.ps = ps
        
        a = [int(i) for i in ngaynhan.split('/')]
        b = [int(i) for i in ngaytra.split('/')]
        t1 = datetime(year = a[2], month = a[1], day = a[0])
        t2 = datetime(year = b[2], month = b[1], day = b[0])
        self.songay = str(t2-t1).split()[0]
        if self.songay == '0:00:00':
            self.songay = 1
        else:
            self.songay = int(self.songay) + 1
    def tong(self):
        if(self.tang == '1'):
            return 25*self.songay+self.ps
        elif(self.tang == '2'):
            return 34*self.songay+self.ps
        elif(self.tang == '3'):
            return 50*self.songay+self.ps
        else:
            return 80*self.songay+self.ps
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+ self.phong+' '+str(self.songay)+' '+str(self.tong())

ls = []
for t in range(int(input())):
    ls.append(HD(int(t+1),input(),input(),input(),input(),int(input())))
ls.sort(key= lambda x: x.tong(),reverse=True)
for i in ls:
    print(i)

        