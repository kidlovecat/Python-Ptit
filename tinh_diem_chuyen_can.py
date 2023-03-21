class SV:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
    
    def toString(self):
        return f'{self.ma} {self.ten} {self.lop}'
    
ls = []
n = int(input())
for i in range(n):
    ls.append(SV(input(), input(), input()))

dict = {}
for i in range(n):
    ma, s = input().split()
    diem = 10
    for x in s: 
        if x == 'm': diem -= 1
        if x == 'v': diem -= 2
    dict[ma] = (diem if diem > 0 else 0)

for x in ls: print(x.toString() + f' {dict[x.ma]}' if dict[x.ma] else x.toString() + f' {dict[x.ma]} KDDK')