from datetime import datetime
class Gamer:
    def __init__(self,ma,ten,bd,kt):
        self.ma = ma
        self.ten = ten
        self.bd = bd
        self.kt = kt
        self.thoiGian = (datetime.strptime(self.kt,'%H:%M')-datetime.strptime(self.bd,'%H:%M')).seconds/60
    
    def __str__(self) -> str:
        return self.ma+' '+self.ten+' '+str(int(self.thoiGian / 60))+ ' gio '+ str(int(self.thoiGian % 60))+ ' phut'
    
ls = []
for t in range(int(input())):
    ls.append(Gamer(input(),input(),input(),input()))
ls.sort(key= lambda x: x.thoiGian,reverse=True)
for i in ls:
    print(i)