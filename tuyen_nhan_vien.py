class ThiSinh:
    def __init__(self,ma,ten,lt,th):
        self.ma = 'TS0'+str(ma)
        self.ten = ten
        if lt > 10 : lt /= 10
        if th > 10 : th /= 10
        self.diem = (float(lt)+float(th))/2
    def xeploai(self):
        if(self.diem < 5.0):
            return 'TRUOT'
        elif(self.diem < 8.0):
            return 'CAN NHAC'
        elif(self.diem <= 9.5):
            return 'DAT'
        return 'XUAT SAC'
    def __str__(self) -> str:
        return self.ma + ' '+ self.ten + ' '+ '{:.2f}'.format(self.diem) +' '+ self.xeploai()

ls = []
for t in range(int(input())):
    ls.append(ThiSinh(int(t+1),input(),float(input()),float(input())))
ls.sort(key=lambda x: x.diem,reverse=True)
for i in ls:
    print(i)

