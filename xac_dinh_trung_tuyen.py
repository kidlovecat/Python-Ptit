UT = [0,2,1.5,1,0]
class GV:
    def __init__(self,i,ten,m,tin,cmon):
        self.ten = ten
        self.ma = 'GV{:02d}'.format(i)
        if(m[0] == 'A'):
            self.m = 'TOAN'
        elif(m[0] == 'B'):
            self.m = 'LY'
        else:
            self.m = 'HOA'
        diem = (tin*2 + cmon)
        self.diem = diem + UT[int(m[1])]
        if(self.diem >= 18):
            self.xet = 'TRUNG TUYEN'
        else: self.xet = 'LOAI'
    
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+self.m+' '+str(self.diem)+' '+self.xet

ls = []
for t in range(int(input())):
    ls.append(GV(t+1,input(),input(),float(input()),float(input())))
ls.sort(key= lambda x: -x.diem)
for i in ls:
    print(i)