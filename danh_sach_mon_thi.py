class Mon:
    def __init__(self,ma,ten,hthuc):
        self.ma = ma
        self.ten = ten
        self.hthuc = hthuc
    def __str__(self):
        return self.ma+' '+ self.ten+' '+self.hthuc

ls = []    
for t in range(int(input())):
    ls.append(Mon(input(),input(),input()))
ls.sort(key=lambda x: x.ma)
for i in ls:
    print(i)