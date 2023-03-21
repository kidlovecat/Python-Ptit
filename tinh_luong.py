class NV:
    def __init__(self, ma, ten, luong, songay):
        self.ma = ma
        self.ten = ten
        self.phong = dict[ma[3:]]

        a, nam = ma[0:1], int(ma[1:3])
        if a == "A":
            if nam <= 3:
                self.hs = 10
            elif nam <= 8:
                self.hs = 12
            elif nam <= 15:
                self.hs = 14
            else:
                self.hs = 20
        if a == "B":
            if nam <= 3:
                self.hs = 10
            elif nam <= 8:
                self.hs = 11
            elif nam <= 15:
                self.hs = 13
            else:
                self.hs = 16
        if a == "C":
            if nam <= 3:
                self.hs = 9
            elif nam <= 8:
                self.hs = 10
            elif nam <= 15:
                self.hs = 12
            else:
                self.hs = 14
        if a == "D":
            if nam <= 3:
                self.hs = 8
            elif nam <= 8:
                self.hs = 9
            elif nam <= 15:
                self.hs = 11
            else:
                self.hs = 13
        self.tong = luong * self.hs * songay * 1000

    def toString(self):
        return f'{self.ma} {self.ten} {self.phong} {self.tong}'


ls, dict = [], {}
for i in range(int(input())):
    s = input().split(' ', 1)
    dict[s[0]] = s[1]

for i in range(int(input())):
    ls.append(NV(input(), input(), int(input()), int(input())))

for x in ls: print(x.toString())